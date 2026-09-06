#!/usr/bin/env python3
"""Build docs/fog.ics, docs/events.json, docs/schema-events.jsonld from events.yml.

Zero config: `python3 build_ics.py`. Requires PyYAML (`pip install pyyaml`).
All times are America/Los_Angeles; a VTIMEZONE block is embedded in ICS,
and ISO-8601 timestamps with Pacific offset are emitted in JSON and Schema.org.

Usage:
  python3 build_ics.py                 Validate events.yml and compile all feeds
  python3 build_ics.py --validate-only Run strict validation checks without building
  python3 build_ics.py --summary       Generate Markdown summary for GitHub Actions
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import pathlib
import re
import sys
import zoneinfo

import yaml

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "events.yml"
OUT_ICS = ROOT / "docs" / "fog.ics"
OUT_JSON = ROOT / "docs" / "events.json"
OUT_SCHEMA = ROOT / "docs" / "schema-events.jsonld"
OUT_OPENAPI = ROOT / "docs" / "openapi.yaml"
INDEX_HTML = ROOT / "docs" / "index.html"

TZID = "America/Los_Angeles"
TZ = zoneinfo.ZoneInfo(TZID)
DOMAIN = "fogrugby.com"

GOOGLE_VALIDATOR_URL = "https://search.google.com/test/rich-results?url=https%3A%2F%2Fevents.fogrugby.com%2F"
SCHEMA_VALIDATOR_URL = "https://validator.schema.org/#url=https%3A%2F%2Fevents.fogrugby.com%2F"
BING_WEBMASTERS_URL = "https://www.bing.com/webmasters/"

VALID_CATEGORIES = {
    "fixture",
    "training",
    "pathway",
    "tournament",
    "social",
    "board",
    "community",
}
VALID_STATUSES = {"confirmed", "tentative"}

DAY_MAP = {
    "MO": "https://schema.org/Monday",
    "TU": "https://schema.org/Tuesday",
    "WE": "https://schema.org/Wednesday",
    "TH": "https://schema.org/Thursday",
    "FR": "https://schema.org/Friday",
    "SA": "https://schema.org/Saturday",
    "SU": "https://schema.org/Sunday",
}

ORGANIZER = {
    "@type": "SportsTeam",
    "name": "San Francisco Fog RFC",
    "url": "https://www.fogrugby.com",
    "sport": "Rugby Union",
    "logo": "https://www.fogrugby.com/assets/crest/fog_crest_navy_crest_vector.png",
}

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


def parse_date(v: str | dt.date) -> dt.date:
    return v if isinstance(v, dt.date) else dt.date.fromisoformat(str(v))


def parse_time(v: str | dt.time) -> dt.time:
    h, m = str(v).split(":")
    return dt.time(int(h), int(m))


def validate_events(data: dict) -> tuple[list[str], list[str]]:
    """Strictly validate events.yml before compiling feeds."""
    errors: list[str] = []
    warnings: list[str] = []

    events = data.get("events")
    if not isinstance(events, list) or not events:
        errors.append("events.yml: 'events' section is missing or empty.")
        return errors, warnings

    ids = [e.get("id") for e in events if isinstance(e, dict) and e.get("id")]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        errors.append(f"Duplicate event IDs found: {sorted(dupes)}")

    for idx, ev in enumerate(events):
        if not isinstance(ev, dict):
            errors.append(f"Event #{idx + 1}: item is not a valid YAML mapping.")
            continue

        eid = ev.get("id")
        if not eid:
            errors.append(f"Event #{idx + 1}: missing required field 'id'.")
            continue

        if not re.match(r"^[a-z0-9][a-z0-9\-_]*$", str(eid)):
            errors.append(f"[{eid}] 'id' must contain only lowercase alphanumeric characters, hyphens, and underscores.")

        title = ev.get("title")
        if not title or not str(title).strip():
            errors.append(f"[{eid}] Missing required field 'title'.")

        cat = ev.get("category")
        if not cat:
            errors.append(f"[{eid}] Missing required field 'category'.")
        elif cat not in VALID_CATEGORIES:
            errors.append(f"[{eid}] Invalid category '{cat}'. Allowed: {sorted(VALID_CATEGORIES)}")

        status = ev.get("status")
        if not status:
            errors.append(f"[{eid}] Missing required field 'status'.")
        elif status not in VALID_STATUSES:
            errors.append(f"[{eid}] Invalid status '{status}'. Allowed: {sorted(VALID_STATUSES)}")

        has_date = bool(ev.get("date"))
        has_start = bool(ev.get("start"))
        if not has_date and not has_start:
            errors.append(f"[{eid}] Must specify either 'date' (single-day) or 'start' (multi-day).")

        event_start_date = None
        if has_date:
            try:
                event_start_date = parse_date(ev["date"])
            except ValueError:
                errors.append(f"[{eid}] Invalid date format: '{ev['date']}'. Expected YYYY-MM-DD.")

        if has_start:
            try:
                event_start_date = parse_date(ev["start"])
            except ValueError:
                errors.append(f"[{eid}] Invalid start date format: '{ev['start']}'. Expected YYYY-MM-DD.")

        if ev.get("end"):
            try:
                end_d = parse_date(ev["end"])
                if event_start_date and end_d < event_start_date:
                    errors.append(f"[{eid}] End date '{end_d}' cannot precede start date '{event_start_date}'.")
            except ValueError:
                errors.append(f"[{eid}] Invalid end date format: '{ev['end']}'. Expected YYYY-MM-DD.")

        m_id_date = re.match(r"^(\d{4}-\d{2}-\d{2})", str(eid))
        if m_id_date and event_start_date:
            id_date_str = m_id_date.group(1)
            if id_date_str != str(event_start_date):
                warnings.append(f"[{eid}] ID starts with '{id_date_str}' but event date is '{event_start_date}'. Aligning ID with date prevents sync confusion.")

        if ev.get("time"):
            t_str = str(ev["time"]).strip()
            if not re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", t_str):
                errors.append(f"[{eid}] Invalid time format '{t_str}'. Expected HH:MM (24-hour).")

        if ev.get("end_time"):
            et_str = str(ev["end_time"]).strip()
            if not re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", et_str):
                errors.append(f"[{eid}] Invalid end_time format '{et_str}'. Expected HH:MM (24-hour).")

        if ev.get("rrule"):
            rrule = str(ev["rrule"])
            if "FREQ=" not in rrule:
                errors.append(f"[{eid}] RRULE missing 'FREQ=': '{rrule}'")
            if "UNTIL=" not in rrule and "COUNT=" not in rrule:
                warnings.append(f"[{eid}] RRULE has no UNTIL or COUNT; event will recur infinitely into future years.")

        if ev.get("exdates"):
            for x in ev["exdates"]:
                try:
                    parse_date(x)
                except ValueError:
                    errors.append(f"[{eid}] Invalid exdate '{x}'. Expected YYYY-MM-DD.")

        if ev.get("url"):
            u = str(ev["url"]).strip()
            if not u.startswith("http://") and not u.startswith("https://"):
                errors.append(f"[{eid}] URL must start with http:// or https://: '{u}'")

        if ev.get("location"):
            loc = str(ev["location"])
            if "Francsico" in loc:
                errors.append(f"[{eid}] Location contains typo 'Francsico' (should be 'San Francisco').")

    return errors, warnings


def event_lines(ev: dict, stamp: str) -> list[str]:
    """Generate RFC 5545 VEVENT lines."""
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


def extract_address(location: str | None) -> dict:
    """Derive PostalAddress entity from location string."""
    if not location:
        return {
            "@type": "PostalAddress",
            "addressLocality": "San Francisco",
            "addressRegion": "CA",
            "addressCountry": "US",
        }
    loc_lower = location.lower()
    if "new orleans" in loc_lower:
        city, state = "New Orleans", "LA"
    elif "san diego" in loc_lower:
        city, state = "San Diego", "CA"
    elif "fresno" in loc_lower:
        city, state = "Fresno", "CA"
    elif "chico" in loc_lower:
        city, state = "Chico", "CA"
    elif "redding" in loc_lower:
        city, state = "Redding", "CA"
    elif "marin" in loc_lower:
        city, state = "Marin County", "CA"
    elif "berkeley" in loc_lower:
        city, state = "Berkeley", "CA"
    elif "stanislaus" in loc_lower:
        city, state = "Modesto", "CA"
    elif "mendocino" in loc_lower:
        city, state = "Mendocino", "CA"
    else:
        city, state = "San Francisco", "CA"

    addr: dict = {
        "@type": "PostalAddress",
        "addressLocality": city,
        "addressRegion": state,
        "addressCountry": "US",
    }
    parts = [p.strip() for p in location.split(",")]
    if len(parts) >= 2 and any(char.isdigit() for char in parts[0]):
        addr["streetAddress"] = parts[0]
    return addr


def build_events_json(data: dict) -> dict:
    """Compile events.yml into a clean, machine-readable REST JSON feed."""
    events = data.get("events") or []
    out_events = []

    for ev in sorted(events, key=lambda e: str(e.get("date") or e.get("start"))):
        start_date = parse_date(ev.get("date") or ev["start"])
        end_date = parse_date(ev["end"]) if ev.get("end") else None

        has_time = bool(ev.get("time"))
        if has_time:
            t0 = parse_time(ev["time"])
            dt_start = dt.datetime.combine(start_date, t0, tzinfo=TZ)
            if ev.get("end_time"):
                t1 = parse_time(ev["end_time"])
                end_day = start_date if t1 > t0 else start_date + dt.timedelta(days=1)
                dt_end = dt.datetime.combine(end_day, t1, tzinfo=TZ)
            else:
                dt_end = dt_start + dt.timedelta(hours=2)
            start_iso = dt_start.isoformat()
            end_iso = dt_end.isoformat()
        else:
            start_iso = str(start_date)
            end_iso = str(end_date or start_date)

        out_ev = {
            "id": ev["id"],
            "uid": f"{ev['id']}@{DOMAIN}",
            "title": ev["title"],
            "category": ev.get("category", "club"),
            "status": ev.get("status", "confirmed"),
            "all_day": not has_time,
            "start": start_iso,
            "end": end_iso,
            "date": str(start_date),
            "time": ev.get("time"),
            "end_time": ev.get("end_time"),
            "location": ev.get("location"),
            "notes": (ev.get("notes") or "").strip() or None,
            "url": ev.get("url"),
            "rrule": ev.get("rrule"),
            "exdates": [str(parse_date(x)) for x in (ev.get("exdates") or [])],
        }
        out_events.append(out_ev)

    return {
        "$schema": "https://events.fogrugby.com/events.schema.json",
        "version": "1.0.0",
        "calendar_name": data.get("calendar_name", "SF Fog Rugby"),
        "calendar_url": data.get("calendar_url", "https://www.fogrugby.com/season-fixtures-results"),
        "feed_url": "https://events.fogrugby.com/events.json",
        "ics_url": "https://events.fogrugby.com/fog.ics",
        "schema_org_url": "https://events.fogrugby.com/schema-events.jsonld",
        "openapi_url": "https://events.fogrugby.com/openapi.yaml",
        "timezone": TZID,
        "updated_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_events": len(out_events),
        "events": out_events,
    }


def build_schema_jsonld(data: dict) -> dict:
    """Compile events.yml into a Schema.org JSON-LD @graph for Google Events indexing."""
    events = data.get("events") or []
    graph = []

    for ev in sorted(events, key=lambda e: str(e.get("date") or e.get("start"))):
        start_date = parse_date(ev.get("date") or ev["start"])
        end_date = parse_date(ev["end"]) if ev.get("end") else None

        has_time = bool(ev.get("time"))
        if has_time:
            t0 = parse_time(ev["time"])
            dt_start = dt.datetime.combine(start_date, t0, tzinfo=TZ)
            if ev.get("end_time"):
                t1 = parse_time(ev["end_time"])
                end_day = start_date if t1 > t0 else start_date + dt.timedelta(days=1)
                dt_end = dt.datetime.combine(end_day, t1, tzinfo=TZ)
            else:
                dt_end = dt_start + dt.timedelta(hours=2)
            start_iso = dt_start.isoformat()
            end_iso = dt_end.isoformat()
        else:
            start_iso = str(start_date)
            end_iso = str(end_date or start_date)

        cat = (ev.get("category") or "").lower()
        if cat in ("fixture", "tournament", "training", "pathway"):
            schema_type = "SportsEvent"
        elif cat == "social":
            schema_type = "SocialEvent"
        else:
            schema_type = "Event"

        status = (
            "https://schema.org/EventScheduled"
            if ev.get("status") == "confirmed"
            else "https://schema.org/EventPostponed"
            if ev.get("status") == "tentative"
            else "https://schema.org/EventScheduled"
        )

        item: dict = {
            "@type": schema_type,
            "@id": f"https://events.fogrugby.com/#event-{ev['id']}",
            "name": ev["title"],
            "startDate": start_iso,
            "endDate": end_iso,
            "eventStatus": status,
            "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
            "organizer": ORGANIZER,
            "offers": {
                "@type": "Offer",
                "price": "0",
                "priceCurrency": "USD",
                "availability": "https://schema.org/InStock",
                "url": ev.get("url")
                or data.get("calendar_url")
                or "https://www.fogrugby.com/season-fixtures-results",
            },
        }

        if schema_type == "SportsEvent":
            item["sport"] = "Rugby Union"

        desc = (ev.get("notes") or "").strip()
        if desc:
            item["description"] = desc

        if ev.get("location"):
            item["location"] = {
                "@type": "Place",
                "name": ev["location"],
                "address": extract_address(ev["location"]),
            }
        else:
            item["location"] = {
                "@type": "Place",
                "name": "San Francisco",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "San Francisco",
                    "addressRegion": "CA",
                    "addressCountry": "US",
                },
            }

        if ev.get("url"):
            item["url"] = ev["url"]

        if ev.get("rrule"):
            rrule_str = ev["rrule"]
            parts = dict(p.split("=", 1) for p in rrule_str.split(";") if "=" in p)
            schedule_obj: dict = {
                "@type": "Schedule",
                "repeatFrequency": "P1W",
                "scheduleTimezone": TZID,
            }
            if "BYDAY" in parts:
                schedule_obj["byDay"] = [
                    DAY_MAP[d] for d in parts["BYDAY"].split(",") if d in DAY_MAP
                ]
            if ev.get("time"):
                schedule_obj["startTime"] = f"{ev['time']}:00"
            if ev.get("end_time"):
                schedule_obj["endTime"] = f"{ev['end_time']}:00"
            if "UNTIL" in parts:
                m = re.match(r"(\d{4})(\d{2})(\d{2})", parts["UNTIL"])
                if m:
                    schedule_obj["endDate"] = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
            item["eventSchedule"] = schedule_obj

        graph.append(item)

    return {
        "@context": "https://schema.org",
        "@graph": graph,
    }


def generate_openapi_spec() -> str:
    """Generate OpenAPI 3.1 specification for events.fogrugby.com."""
    return """openapi: 3.1.0
info:
  title: San Francisco Fog RFC Events API
  description: Public machine-readable event syndication feed for SF Fog Rugby fixtures, trainings, tournaments, and community events.
  version: 1.0.0
  contact:
    name: San Francisco Fog RFC
    url: https://www.fogrugby.com
    email: secretary@fogrugby.com
servers:
  - url: https://events.fogrugby.com
    description: Production CDN (GitHub Pages)
paths:
  /events.json:
    get:
      summary: Retrieve all club events and fixtures
      description: Returns all upcoming matches, trainings, clinics, and club events in structured JSON.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  calendar_name:
                    type: string
                  total_events:
                    type: integer
                  events:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                        title:
                          type: string
                        start:
                          type: string
                        end:
                          type: string
                        location:
                          type: string
                        category:
                          type: string
  /fog.ics:
    get:
      summary: RFC 5545 iCalendar subscription feed
      description: Standard iCal feed compatible with Apple Calendar, Google Calendar, Outlook, and feed readers.
      responses:
        '200':
          description: iCalendar feed
          content:
            text/calendar:
              schema:
                type: string
  /schema-events.jsonld:
    get:
      summary: Schema.org JSON-LD graph
      description: Google Events Rich Results graph containing SportsEvent, SocialEvent, and Schedule entities.
      responses:
        '200':
          description: Schema.org Event graph
          content:
            application/ld+json:
              schema:
                type: object
"""


def update_index_html(schema_ld: dict) -> None:
    """Inject Schema.org JSON-LD into docs/index.html."""
    if not INDEX_HTML.exists():
        return
    content = INDEX_HTML.read_text(encoding="utf-8")

    json_ld_str = json.dumps(schema_ld, ensure_ascii=False, indent=2)
    script_block = f'<script type="application/ld+json" id="schema-events">\n{json_ld_str}\n</script>'

    if '<script type="application/ld+json" id="schema-events">' in content:
        content = re.sub(
            r'<script type="application/ld\+json" id="schema-events">.*?</script>',
            script_block,
            content,
            flags=re.DOTALL,
        )
    else:
        content = content.replace("</head>", f"{script_block}\n</head>")

    INDEX_HTML.write_text(content, encoding="utf-8")


def print_cli_report(events: list[dict], errors: list[str], warnings: list[str]) -> None:
    """Print terminal report with validation links and stats."""
    cats: dict[str, int] = {}
    for ev in events:
        c = ev.get("category", "other")
        cats[c] = cats.get(c, 0) + 1

    print("=" * 72)
    print(" SF FOG RUGBY — CALENDAR PRE-BUILD VALIDATION REPORT")
    print("=" * 72)
    if errors:
        print(f" ❌ VALIDATION FAILED: {len(errors)} ERROR(S) FOUND!")
        print("    Build ABORTED. Bad data was NOT written to any output files.")
        print("-" * 72)
        for err in errors:
            print(f"  • {err}")
        print("=" * 72)
        return

    print(f" ✓ VALIDATION PASSED: {len(events)} events verified cleanly.")
    if warnings:
        print(f"   ({len(warnings)} non-fatal warning(s) detected)")
        for warn in warnings:
            print(f"   ⚠ {warn}")

    print("\n Category Breakdown:")
    for cat_name, count in sorted(cats.items()):
        print(f"   • {cat_name.title():<14}: {count} event(s)")

    print("\n" + "-" * 72)
    print(" 🔍 Live Search Engine & Schema Validation Links:")
    print("   • Google Rich Results Test:")
    print(f"     {GOOGLE_VALIDATOR_URL}")
    print("   • Schema.org Markup Validator (Google / Microsoft / Yahoo):")
    print(f"     {SCHEMA_VALIDATOR_URL}")
    print("   • Bing Webmaster Tools:")
    print(f"     {BING_WEBMASTERS_URL}")
    print("-" * 72)


def generate_markdown_summary(data: dict, errors: list[str], warnings: list[str]) -> str:
    """Generate Markdown summary for GitHub Actions Step Summary ($GITHUB_STEP_SUMMARY)."""
    events = data.get("events") or []
    cats: dict[str, int] = {}
    for ev in events:
        c = ev.get("category", "other")
        cats[c] = cats.get(c, 0) + 1

    md = []
    md.append("### 🏉 SF Fog Rugby Calendar Build & Validation Report\n")

    if errors:
        md.append("> [!CAUTION]\n> **Build Aborted:** Validation failed with errors! No generated feeds were updated.\n")
        md.append("#### Errors Found:\n")
        for err in errors:
            md.append(f"- ❌ {err}")
        return "\n".join(md)

    status_badge = "✅ **Passed Validation**" if not warnings else "⚠️ **Passed (With Warnings)**"
    md.append(f"| Metric | Value |")
    md.append(f"| :--- | :--- |")
    md.append(f"| **Status** | {status_badge} |")
    md.append(f"| **Total Events** | `{len(events)}` |")
    md.append(f"| **Fixtures / Matches** | `{cats.get('fixture', 0)}` |")
    md.append(f"| **Tournaments** | `{cats.get('tournament', 0)}` |")
    md.append(f"| **Trainings & Pathways** | `{cats.get('training', 0) + cats.get('pathway', 0)}` |")
    md.append(f"| **Socials & Community** | `{cats.get('social', 0) + cats.get('community', 0) + cats.get('board', 0)}` |")
    md.append("")

    if warnings:
        md.append("#### ⚠️ Non-fatal Warnings:\n")
        for warn in warnings:
            md.append(f"- ⚠️ {warn}")
        md.append("")

    md.append("#### 🔍 Live Search Engine & Schema Validation Links\n")
    md.append("Test and verify that search engines and crawlers are detecting the live events:\n")
    md.append(f"- 🟢 [**Google Rich Results Test**]({GOOGLE_VALIDATOR_URL}) — Simulates Googlebot crawl to verify interactive event cards and carousels.")
    md.append(f"- 🟢 [**Schema.org Markup Validator**]({SCHEMA_VALIDATOR_URL}) — Official consortium test across Google, Microsoft, and Yahoo.")
    md.append(f"- 🟢 [**Bing Webmaster Tools**]({BING_WEBMASTERS_URL}) — Inspect URL markup and request Bing indexing.")
    md.append("")

    md.append("#### 📡 Syndication Feeds Updated\n")
    md.append("- **iCalendar Feed:** [`https://events.fogrugby.com/fog.ics`](https://events.fogrugby.com/fog.ics)")
    md.append("- **REST JSON API:** [`https://events.fogrugby.com/events.json`](https://events.fogrugby.com/events.json)")
    md.append("- **Schema.org JSON-LD:** [`https://events.fogrugby.com/schema-events.jsonld`](https://events.fogrugby.com/schema-events.jsonld)")
    md.append("- **OpenAPI 3.1 Spec:** [`https://events.fogrugby.com/openapi.yaml`](https://events.fogrugby.com/openapi.yaml)")
    md.append("- **Web Portal:** [`https://events.fogrugby.com/`](https://events.fogrugby.com/)")

    return "\n".join(md)


def main() -> int:
    args = sys.argv[1:]
    is_validate_only = "--validate-only" in args or "-v" in args
    is_summary = "--summary" in args

    try:
        data = yaml.safe_load(SRC.read_text(encoding="utf-8"))
    except Exception as ex:
        print(f"FATAL: Unable to parse events.yml: {ex}", file=sys.stderr)
        return 1

    events = data.get("events") or []
    errors, warnings = validate_events(data)

    if is_summary:
        print(generate_markdown_summary(data, errors, warnings))
        return 1 if errors else 0

    print_cli_report(events, errors, warnings)
    if errors:
        return 1

    if is_validate_only:
        print("Validation complete. (--validate-only: output files untouched)")
        return 0

    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    name = data.get("calendar_name", "SF Fog Rugby")

    # 1. Build RFC 5545 ICS
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

    OUT_ICS.parent.mkdir(parents=True, exist_ok=True)
    OUT_ICS.write_text("\r\n".join(fold(l) for l in lines) + "\r\n", encoding="utf-8")
    print(f"wrote {OUT_ICS.relative_to(ROOT)} — {len(events)} events")

    # 2. Build REST JSON Feed
    events_json = build_events_json(data)
    OUT_JSON.write_text(
        json.dumps(events_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"wrote {OUT_JSON.relative_to(ROOT)} — {len(events)} events")

    # 3. Build Schema.org JSON-LD
    schema_ld = build_schema_jsonld(data)
    OUT_SCHEMA.write_text(
        json.dumps(schema_ld, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"wrote {OUT_SCHEMA.relative_to(ROOT)} — {len(schema_ld['@graph'])} entities in graph")

    # 4. Build OpenAPI Spec
    OUT_OPENAPI.write_text(generate_openapi_spec(), encoding="utf-8")
    print(f"wrote {OUT_OPENAPI.relative_to(ROOT)}")

    # 5. Update index.html with Schema.org JSON-LD
    update_index_html(schema_ld)
    print(f"updated {INDEX_HTML.relative_to(ROOT)} with embedded Schema.org JSON-LD")

    print("\n✓ Build completed successfully. All outputs validated and synchronized.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
