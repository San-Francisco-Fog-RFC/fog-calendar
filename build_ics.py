#!/usr/bin/env python3
"""Build docs/fog.ics, docs/events.json, docs/schema-events.jsonld from events.yml.

Zero config: `python3 build_ics.py`. Requires PyYAML (`pip install pyyaml`).
All times are America/Los_Angeles; a VTIMEZONE block is embedded in ICS,
and ISO-8601 timestamps with Pacific offset are emitted in JSON and Schema.org.
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

        # If recurring, enrich with eventSchedule
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
    """Inject Schema.org JSON-LD and syndication links into docs/index.html."""
    if not INDEX_HTML.exists():
        return
    content = INDEX_HTML.read_text(encoding="utf-8")

    # Format JSON-LD script
    json_ld_str = json.dumps(schema_ld, ensure_ascii=False, indent=2)
    script_block = f'<script type="application/ld+json" id="schema-events">\n{json_ld_str}\n</script>'

    # Replace existing script block or insert before </head>
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

    return 0


if __name__ == "__main__":
    sys.exit(main())
