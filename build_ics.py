#!/usr/bin/env python3
"""Build docs/fog.ics from events.yml.

Zero config: `python3 build_ics.py`. Requires PyYAML (`pip install pyyaml`).
All times are America/Los_Angeles; a VTIMEZONE block is embedded so every
client (Apple, Google, Outlook) gets DST right without trusting the host.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "events.yml"
OUT = ROOT / "docs" / "fog.ics"
TZID = "America/Los_Angeles"
DOMAIN = "fogrugby.com"

VTIMEZONE = """BEGIN:VTIMEZONE
TZID:America/Los_Angeles
X-LIC-LOCATION:America/Los_Angeles
BEGIN:DAYLIGHT
TZOFFSETFROM:-0800
TZOFFSETTO:-0700
TZNAME:PDT
DTSTART:19700308T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:-0700
TZOFFSETTO:-0800
TZNAME:PST
DTSTART:19701101T020000
RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU
END:STANDARD
END:VTIMEZONE"""


def esc(s: str) -> str:
    """Escape text per RFC 5545."""
    return (
        str(s)
        .replace("\\", "\\\\")
        .replace(";", "\\;")
        .replace(",", "\\,")
        .replace("\r\n", "\\n")
        .replace("\n", "\\n")
    )


def fold(line: str) -> str:
    """Fold lines longer than 75 octets (RFC 5545 §3.1)."""
    out, cur = [], ""
    for ch in line:
        if len((cur + ch).encode("utf-8")) > 74:
            out.append(cur)
            cur = " " + ch
        else:
            cur += ch
    out.append(cur)
    return "\r\n".join(out)


def parse_date(v) -> dt.date:
    return v if isinstance(v, dt.date) else dt.date.fromisoformat(str(v))


def parse_time(v) -> dt.time:
    h, m = str(v).split(":")
    return dt.time(int(h), int(m))


def event_lines(ev: dict, stamp: str) -> list[str]:
    uid = f"{ev['id']}@{DOMAIN}"
    lines = ["BEGIN:VEVENT", f"UID:{uid}", f"DTSTAMP:{stamp}"]

    start_date = parse_date(ev.get("date") or ev["start"])
    end_date = parse_date(ev["end"]) if ev.get("end") else None

    if ev.get("time"):
        t0 = parse_time(ev["time"])
        if ev.get("end_time"):
            t1 = parse_time(ev["end_time"])
            end_day = start_date if t1 > t0 else start_date + dt.timedelta(days=1)
        else:
            t1 = (dt.datetime.combine(start_date, t0) + dt.timedelta(hours=2)).time()
            end_day = start_date
        lines.append(f"DTSTART;TZID={TZID}:{start_date:%Y%m%d}T{t0:%H%M}00")
        lines.append(f"DTEND;TZID={TZID}:{end_day:%Y%m%d}T{t1:%H%M}00")
    else:
        # all-day; DTEND is exclusive
        last = end_date or start_date
        lines.append(f"DTSTART;VALUE=DATE:{start_date:%Y%m%d}")
        lines.append(f"DTEND;VALUE=DATE:{last + dt.timedelta(days=1):%Y%m%d}")

    if ev.get("rrule"):
        lines.append(f"RRULE:{ev['rrule']}")
    for x in ev.get("exdates", []) or []:
        xd = parse_date(x)
        if ev.get("time"):
            t0 = parse_time(ev["time"])
            lines.append(f"EXDATE;TZID={TZID}:{xd:%Y%m%d}T{t0:%H%M}00")
        else:
            lines.append(f"EXDATE;VALUE=DATE:{xd:%Y%m%d}")

    lines.append(f"SUMMARY:{esc(ev['title'])}")
    if ev.get("location"):
        lines.append(f"LOCATION:{esc(ev['location'])}")
    desc = (ev.get("notes") or "").strip()
    if ev.get("url"):
        lines.append(f"URL:{ev['url']}")
        desc = (desc + "\n\n" if desc else "") + ev["url"]
    if desc:
        lines.append(f"DESCRIPTION:{esc(desc)}")
    if ev.get("category"):
        lines.append(f"CATEGORIES:{esc(ev['category']).upper()}")
    lines.append("STATUS:" + ("TENTATIVE" if ev.get("status") == "tentative" else "CONFIRMED"))
    lines.append("TRANSP:TRANSPARENT" if not ev.get("time") else "TRANSP:OPAQUE")

    # SEQUENCE bumps whenever the entry's content changes → clients refresh it
    digest = hashlib.sha1(repr(sorted(ev.items())).encode()).hexdigest()
    lines.append(f"SEQUENCE:{int(digest[:6], 16) % 100000}")
    lines.append("END:VEVENT")
    return lines


def main() -> int:
    data = yaml.safe_load(SRC.read_text(encoding="utf-8"))
    events = data.get("events") or []
    ids = [e["id"] for e in events]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        print(f"ERROR duplicate ids: {sorted(dupes)}", file=sys.stderr)
        return 1

    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    name = data.get("calendar_name", "SF Fog Rugby")
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//San Francisco Fog RFC//fog-calendar//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        f"X-WR-CALNAME:{esc(name)}",
        f"X-WR-TIMEZONE:{TZID}",
        "X-WR-CALDESC:Fixtures\\, training\\, Pathway to Rugby\\, tournaments and club events.",
        "REFRESH-INTERVAL;VALUE=DURATION:PT6H",
        "X-PUBLISHED-TTL:PT6H",
    ]
    if data.get("calendar_url"):
        lines.append(f"URL:{data['calendar_url']}")
    lines += VTIMEZONE.split("\n")
    for ev in sorted(events, key=lambda e: str(e.get("date") or e.get("start"))):
        lines += event_lines(ev, stamp)
    lines.append("END:VCALENDAR")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\r\n".join(fold(l) for l in lines) + "\r\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} — {len(events)} events")
    return 0


if __name__ == "__main__":
    sys.exit(main())
