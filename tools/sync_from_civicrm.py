#!/usr/bin/env python3
"""Rebuild events.yml from the Clubhouse (CiviCRM).

CiviCRM at clubhouse.fogrugby.com is where events are edited now. This reads
its public export and rewrites events.yml, keeping the file's top-level
settings (calendar name, venues, series). build_ics.py then turns events.yml
into docs/fog.ics as before, so the subscribe URL and event UIDs stay the same.

Safety: if the export can't be fetched, isn't valid, or has suspiciously few
events, events.yml is left untouched and the script exits 0, so a Clubhouse
outage never empties anyone's calendar.

Usage: python3 tools/sync_from_civicrm.py [--source URL_OR_FILE] [--min-events N]
Exit 0 always on "nothing to do"; prints CHANGED when events.yml was rewritten.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
import urllib.request

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_YML = ROOT / "events.yml"
DEFAULT_SOURCE = "https://clubhouse.fogrugby.com/api/calendar/export.json"
KEY_ORDER = ["id", "series", "title", "date", "start", "end", "time", "end_time",
             "venue", "location", "category", "status", "notes", "url", "image", "rrule", "exdates"]
HEADER = (
    "# GENERATED FROM THE CLUBHOUSE (CiviCRM) - do not edit events here.\n"
    "# Add or change events at https://clubhouse.fogrugby.com/civicrm/event/manage\n"
    "# tools/sync_from_civicrm.py rewrites this file every 30 minutes; top-level\n"
    "# settings (calendar_name, venues, series) are kept as they are.\n"
)


def fetch(source: str) -> dict | None:
    try:
        if source.startswith("http"):
            req = urllib.request.Request(source, headers={"User-Agent": "fog-calendar-sync"})
            with urllib.request.urlopen(req, timeout=30) as r:
                if r.status != 200:
                    print(f"skip: export returned HTTP {r.status}")
                    return None
                return json.load(r)
        return json.loads(pathlib.Path(source).read_text())
    except Exception as e:  # network, JSON, file
        print(f"skip: couldn't read export ({e})")
        return None


class _Dumper(yaml.SafeDumper):
    pass


def _str(dumper, s):
    style = "|" if "\n" in s else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", s, style=style)


_Dumper.add_representer(str, _str)


def convert(export: dict, current: dict) -> list[dict]:
    venues = current.get("venues") or {}
    by_name = {v.get("name", "").strip().lower(): k for k, v in venues.items()}
    old_series = {e["id"]: e["series"] for e in current.get("events", []) if e.get("series")}

    out = []
    for e in export["events"]:
        row = {k: e[k] for k in ("id", "title", "date", "start", "end", "time", "end_time",
                                 "category", "status", "notes", "url", "image") if e.get(k)}
        if e["id"] in old_series:
            row["series"] = old_series[e["id"]]
        name = (e.get("venue_name") or "").strip()
        if name:
            key = by_name.get(name.lower())
            if key:
                row["venue"] = key
            else:
                row["location"] = name
        out.append({k: row[k] for k in KEY_ORDER if k in row})
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default=DEFAULT_SOURCE)
    ap.add_argument("--min-events", type=int, default=5,
                    help="refuse to write if the export has fewer events than this")
    ap.add_argument("--force", action="store_true",
                    help="write even if most existing events would disappear")
    args = ap.parse_args()

    export = fetch(args.source)
    if not export or not isinstance(export.get("events"), list):
        return 0
    if len(export["events"]) < args.min_events:
        print(f"skip: export has only {len(export['events'])} events (< {args.min_events})")
        return 0

    raw = EVENTS_YML.read_text()
    current = yaml.safe_load(raw) or {}
    events = convert(export, current)

    old_ids = {e["id"] for e in current.get("events", [])}
    kept = old_ids & {e["id"] for e in events}
    if old_ids and len(kept) < len(old_ids) / 2 and not args.force:
        # Recurring series are one entry before the first sync and one per date after,
        # so only count ids that are still recognisable (exact or "<series>-YYYYMMDD").
        kept |= {o for o in old_ids if any(e["id"].startswith(o + "-") for e in events)}
        if len(kept) < len(old_ids) / 2:
            print(f"skip: only {len(kept)} of {len(old_ids)} existing events are in the export; rerun with --force if intended")
            return 0

    doc = {k: v for k, v in current.items() if k != "events"}
    body = yaml.dump(doc, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=1000)
    body += yaml.dump({"events": events}, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=1000)
    new = HEADER + body

    if new == raw:
        print("unchanged")
        return 0
    EVENTS_YML.write_text(new)
    print(f"CHANGED: {len(events)} events from {export.get('source', args.source)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
