#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml", "playwright"]
# ///
"""Submit events.yml events to listing sites without retyping them.

Listing copy lives in promote.yml; dates, times and venues come from events.yml;
every submission is recorded in submissions.yml.

  uv run promote.py plan [listing]                 status of every listing on every site
  uv run promote.py kit <listing> <site>           print copy-paste fields
  uv run promote.py fill <listing> <site> [N]      fill the site's form in a browser; you review and click Submit
  uv run promote.py mark <listing> <site> <status> [--events id,id] [--link URL] [--note TEXT]
  uv run promote.py push <listing> eventbrite      create (or update) unpublished Eventbrite drafts via the API
  uv run promote.py publish <listing> eventbrite   publish those drafts (makes them public)

`fill` never clicks Submit. It uses a persistent browser profile in .promote-browser/,
so sites that need an account only need you to sign in once.
First run only: uv run --with playwright playwright install chromium
"""
from __future__ import annotations

import datetime as dt
import html
import pathlib
import sys
import zoneinfo

import yaml

ROOT = pathlib.Path(__file__).resolve().parent
TZ = zoneinfo.ZoneInfo("America/Los_Angeles")
PROFILE_DIR = ROOT / ".promote-browser"

# multi_date: one submission can cover several dates. single_venue: one venue per submission.
# min_hours / ideal_days: lead time the site requires / recommends before the first date.
SITES = {
    "funcheap": dict(name="Funcheap SF", url="https://sf.funcheap.com/submit-form/", multi_date=True, single_venue=True,
                     min_hours=48, ideal_days=14, notes="Free/cheap events only. JPG or GIF image, max 1MB. reCAPTCHA on Submit."),
    "scruff": dict(name="SCRUFF Events", url="https://www.scruff.com/en/events/", multi_date=False, single_venue=True,
                   min_hours=48, ideal_days=7, notes="Reviewed within 48 hours. JPG image, 1920x1080 recommended."),
    "thegaycalendar": dict(name="The Gay Calendar", url="https://thegaycalendar.com/", multi_date=False, single_venue=True,
                           min_hours=0, ideal_days=7, notes="Sign in, then 'Add Event'. Has an agent API (OAuth device flow) - not wired up yet."),
    "dothebay": dict(name="DoTheGay (DoTheBay)", url="https://gay.dothebay.com/events/new", multi_date=False, single_venue=True,
                     min_hours=0, ideal_days=7, notes="Requires a DoTheBay account."),
    "eventbrite": dict(name="Eventbrite", url="https://www.eventbrite.com/manage/events/create", multi_date=False, single_venue=True,
                       min_hours=0, ideal_days=14, notes="Use `push` (API) instead of the form. One event per date; free registration; PLAI can import from here."),
    "plai": dict(name="PLAI (plra.io)", url="https://plra.io/", multi_date=False, single_venue=True,
                 min_hours=0, ideal_days=7, notes="Create from the club's Events tab: name, start/end, type Training, location."),
    "google": dict(name="Google Business Profile post", url="https://business.google.com/", multi_date=True, single_venue=False,
                   min_hours=0, ideal_days=7, notes="Add update > Event. Title max 58 characters, details max 1500. Button: Learn more."),
}
FILLERS = {}  # site -> function(page, listing, unit, contact); registered below


# ---------------------------------------------------------------- data

def load_yaml(name: str) -> dict:
    path = ROOT / name
    return yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {}


def load():
    events = {e["id"]: e for e in load_yaml("events.yml").get("events", [])}
    promote = load_yaml("promote.yml")
    log = load_yaml("submissions.yml").get("submissions") or []
    return events, promote, log


def tracked(url: str, site_key: str, listing_key: str) -> str:
    """Add UTM tags so Google Analytics can attribute visits and sign-ups to the listing site."""
    from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
    parts = urlsplit(url)
    query = dict(parse_qsl(parts.query))
    query.setdefault("utm_source", site_key)
    query.setdefault("utm_medium", "listing")
    query.setdefault("utm_campaign", listing_key)
    return urlunsplit(parts._replace(query=urlencode(query)))


def contact_for(promote: dict, listing: dict) -> dict:
    """The default contact, with any per-listing `contact:` overrides (e.g. a different email)."""
    return {**promote["contact"], **(listing.get("contact") or {})}


def occurrence(ev: dict) -> dict:
    """Resolve an events.yml entry into concrete start/end datetimes and venue fields."""
    day = dt.date.fromisoformat(str(ev.get("date") or ev["start"]))
    if ev.get("time"):
        start = dt.datetime.combine(day, dt.time.fromisoformat(str(ev["time"])), tzinfo=TZ)
        if ev.get("end_time"):
            end = dt.datetime.combine(day, dt.time.fromisoformat(str(ev["end_time"])), tzinfo=TZ)
            if end <= start:
                end += dt.timedelta(days=1)
        else:
            end = start + dt.timedelta(hours=2)
    else:
        start = dt.datetime.combine(day, dt.time(0, 0), tzinfo=TZ)
        last = dt.date.fromisoformat(str(ev["end"])) if ev.get("end") else day
        end = dt.datetime.combine(last, dt.time(23, 59), tzinfo=TZ)
    location = str(ev.get("location") or "")
    venue, _, address = location.partition(",")
    return dict(id=ev["id"], start=start, end=end, all_day=not ev.get("time"), venue=venue.strip(),
                address=address.strip() or venue.strip(), notes=(ev.get("notes") or "").strip())


def units(listing: dict, site_key: str, events: dict) -> list[list[dict]]:
    """Split a listing's events into the submissions a site needs, oldest first."""
    missing = [i for i in listing["events"] if i not in events]
    if missing:
        sys.exit(f"promote.yml: unknown event ids {missing}")
    occs = sorted((occurrence(events[i]) for i in listing["events"]), key=lambda o: o["start"])
    site = SITES[site_key]
    if not site["multi_date"]:
        return [[o] for o in occs]
    if not site["single_venue"]:
        return [occs]
    groups: dict[str, list[dict]] = {}
    for o in occs:
        groups.setdefault(o["venue"], []).append(o)
    return sorted(groups.values(), key=lambda g: g[0]["start"])


def covered(log: list, listing_key: str, site_key: str, unit: list[dict]) -> tuple[list[str], dict | None]:
    """Event ids in this unit that already have a log entry, plus the latest matching entry."""
    ids = {o["id"] for o in unit}
    hits = [s for s in log if s.get("listing") == listing_key and s.get("site") == site_key and ids & set(s.get("events") or [])]
    done = sorted(ids & {e for s in hits for e in s.get("events") or []})
    return done, (hits[-1] if hits else None)


# ---------------------------------------------------------------- formatting

def fmt_time(t: dt.datetime) -> str:
    return t.strftime("%-I:%M%p").lower().replace(":00", "")


def fmt_range(o: dict) -> str:
    if o["all_day"]:
        return o["start"].strftime("%a %b %-d")
    start, end = fmt_time(o["start"]), fmt_time(o["end"])
    if start[-2:] == end[-2:]:
        start = start[:-2]  # 8–10pm, not 8pm–10pm
    return f"{o['start']:%a %b %-d}, {start}–{end}"


def schedule_text(unit: list[dict]) -> str:
    """'Tuesdays, Oct 6 – Oct 27: Tue Oct 6, 7:30–10pm; Tue Oct 13, 8–10pm; ...'"""
    days = {o["start"].strftime("%A") for o in unit}
    head = f"{days.pop()}s, {unit[0]['start']:%b %-d} – {unit[-1]['start']:%b %-d, %Y}" if len(days) == 1 else \
        f"{unit[0]['start']:%b %-d} – {unit[-1]['start']:%b %-d, %Y}"
    return f"{head}: " + "; ".join(fmt_range(o) for o in unit)


def is_weekly(unit: list[dict]) -> bool:
    return len(unit) > 1 and all((b["start"].date() - a["start"].date()).days == 7 for a, b in zip(unit, unit[1:]))


def description(listing: dict, unit: list[dict]) -> str:
    text = listing["description"].strip()
    if len(unit) > 1:
        text += f"\n\nDates at {unit[0]['venue']}: {schedule_text(unit)}"
    elif unit[0]["notes"]:
        text += f"\n\n{unit[0]['notes']}"
    return text


def to_html(text: str) -> str:
    out, items = [], []
    for block in text.split("\n\n"):
        lines = [l for l in block.splitlines() if l.strip()]
        bullets = [l[2:] for l in lines if l.startswith("- ")]
        intro = [l for l in lines if not l.startswith("- ")]
        if intro:
            out.append("<p>" + "<br>".join(html.escape(l) for l in intro) + "</p>")
        if bullets:
            out.append("<ul>" + "".join(f"<li>{html.escape(b)}</li>" for b in bullets) + "</ul>")
    return "".join(out)


def lead_time_warning(site_key: str, unit: list[dict], now: dt.datetime) -> str | None:
    site, first = SITES[site_key], unit[0]["start"]
    if unit[-1]["start"] < now:
        return "all dates have passed"
    if first - now < dt.timedelta(hours=site["min_hours"]):
        return f"starts within {site['min_hours']}h - {site['name']} won't accept it" if site["min_hours"] else "already started"
    if first - now < dt.timedelta(days=site["ideal_days"]):
        return f"less than the {site['ideal_days']} days' notice {site['name']} recommends"
    return None


# ---------------------------------------------------------------- commands

def cmd_plan(listing_filter: str | None = None):
    events, promote, log = load()
    now = dt.datetime.now(TZ)
    for key, listing in promote["listings"].items():
        if listing_filter and key != listing_filter:
            continue
        print(f"\n{listing['title']}  [{key}]")
        for site_key in listing["sites"]:
            print(f"  {SITES[site_key]['name']}")
            for n, unit in enumerate(units(listing, site_key, events), 1):
                done, last = covered(log, key, site_key, unit)
                if len(done) == len(unit):
                    state = f"{last['status']} {last.get('date', '')}".strip() + (f"  {last['link']}" if last.get("link") else "")
                elif done:
                    state = f"partly {last['status']} ({len(done)}/{len(unit)} dates)"
                else:
                    state = "to do"
                    warn = lead_time_warning(site_key, unit, now)
                    if warn:
                        state += f"  ⚠ {warn}"
                when = schedule_text(unit) if len(unit) > 1 else fmt_range(unit[0])
                print(f"    {n}. {when[:70]:<70}  {state}")
    print("\nfill: uv run promote.py fill <listing> <site> [N]    kit: uv run promote.py kit <listing> <site>")


def cmd_kit(listing_key: str, site_key: str):
    events, promote, _ = load()
    listing = promote["listings"][listing_key]
    site = SITES[site_key]
    print(f"# {listing['title']} -> {site['name']}\n# {site['url']}\n# {site['notes']}")
    for n, unit in enumerate(units(listing, site_key, events), 1):
        o = unit[0]
        title = listing["title"][:58] if site_key == "google" else listing["title"]
        fields = {
            "Title": title,
            "Dates": schedule_text(unit) if len(unit) > 1 else fmt_range(o),
            "Start": f"{o['start']:%m/%d/%Y %-I:%M %p}",
            "End": f"{o['end']:%m/%d/%Y %-I:%M %p}",
            "Venue": o["venue"],
            "Address": o["address"],
            "Cost": "Free" if not listing.get("cost") else f"${listing['cost']}",
            "Website": tracked(listing["url"], site_key, listing_key),
            "Image": str(ROOT / listing["image"]),
            "Image credit": listing.get("image_credit", ""),
            "Tags": ", ".join(listing.get("tags", [])),
            "Contact": "{name} <{email}>".format(**contact_for(promote, listing)),
        }
        print(f"\n## Submission {n} of {len(units(listing, site_key, events))}")
        for k, v in fields.items():
            print(f"{k + ':':<14}{v}")
        desc = description(listing, unit)
        print("Description:\n" + (desc[:1500] if site_key == "google" else desc))


def cmd_fill(listing_key: str, site_key: str, n: int | None = None, headless: bool = False, screenshot: str | None = None):
    events, promote, log = load()
    listing = promote["listings"][listing_key]
    all_units = units(listing, site_key, events)
    now = dt.datetime.now(TZ)
    if n is None:
        todo = [i for i, u in enumerate(all_units, 1) if len(covered(log, listing_key, site_key, u)[0]) < len(u)
                and u[-1]["start"] > now]
        if not todo:
            sys.exit("Nothing left to submit for this site. Pass a submission number to fill one anyway.")
        n = todo[0]
    unit = all_units[n - 1]
    warn = lead_time_warning(site_key, unit, now)
    print(f"Submission {n} of {len(all_units)}: {schedule_text(unit) if len(unit) > 1 else fmt_range(unit[0])}")
    if warn:
        print(f"⚠ {warn}")

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(str(PROFILE_DIR), headless=headless, viewport={"width": 1280, "height": 900})
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(SITES[site_key]["url"])
        filler = FILLERS.get(site_key)
        if filler:
            filler(page, {**listing, "url": tracked(listing["url"], site_key, listing_key)}, unit, contact_for(promote, listing))
            print("Form filled. Check every field in the browser, then click Submit yourself.")
        else:
            print(f"No auto-fill for {SITES[site_key]['name']} yet - sign in if needed and use the fields below:\n")
            cmd_kit(listing_key, site_key)
        if screenshot:
            page.screenshot(path=screenshot, full_page=True)
            print(f"Saved screenshot to {screenshot}")
        if headless:
            ctx.close()
            return
        answer = input("\nDid you submit it? [y/N] ").strip().lower()
        ctx.close()
    if answer == "y":
        append_log(listing_key, site_key, [o["id"] for o in unit], "submitted")


def append_log(listing_key: str, site_key: str, ids: list[str], status: str, link: str | None = None, note: str | None = None,
               extra: dict | None = None):
    path = ROOT / "submissions.yml"
    entry = {"listing": listing_key, "site": site_key, "events": ids, "status": status, "date": dt.date.today().isoformat()}
    if link:
        entry["link"] = link
    if note:
        entry["note"] = note
    entry.update(extra or {})
    text = path.read_text(encoding="utf-8") if path.exists() else "submissions:\n"
    item = yaml.safe_dump([entry], sort_keys=False, allow_unicode=True, width=1000)
    path.write_text(text.rstrip("\n") + "\n" + "".join("  " + l + "\n" for l in item.splitlines()), encoding="utf-8")
    print(f"Logged in submissions.yml: {site_key} {status} {ids}")


def cmd_mark(listing_key: str, site_key: str, status: str, args: list[str]):
    events, promote, log = load()
    opts = dict(zip(args[::2], args[1::2]))
    if "--events" in opts:
        ids = opts["--events"].split(",")
    else:
        prior = [s for s in log if s.get("listing") == listing_key and s.get("site") == site_key]
        ids = prior[-1]["events"] if prior else promote["listings"][listing_key]["events"]
    append_log(listing_key, site_key, ids, status, opts.get("--link"), opts.get("--note"))


# ---------------------------------------------------------------- Eventbrite API (push / publish)

EB_API = "https://www.eventbriteapi.com/v3"


def eb_call(method: str, path: str, body: dict | None = None) -> dict:
    import json, os, urllib.error, urllib.request
    token = os.environ.get("EVENTBRITE_API_KEY")
    if not token:
        sys.exit("Set EVENTBRITE_API_KEY (your Eventbrite private token) in your shell first.")
    headers = {"Authorization": f"Bearer {token}"}
    if body is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(EB_API + path, method=method, headers=headers,
                                 data=json.dumps(body).encode() if body is not None else None)
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        sys.exit(f"Eventbrite {method} {path} failed ({e.code}): {e.read().decode()[:500]}")


def eb_upload_image(path: pathlib.Path, kind: str = "image-event-logo") -> str:
    import mimetypes, urllib.request, uuid
    up = eb_call("GET", f"/media/upload/?type={kind}")
    boundary = uuid.uuid4().hex
    parts = [f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode() for k, v in up["upload_data"].items()]
    ctype = mimetypes.guess_type(path.name)[0] or "image/jpeg"
    parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{up["file_parameter_name"]}"; filename="{path.name}"\r\nContent-Type: {ctype}\r\n\r\n'.encode())
    parts.append(path.read_bytes() + f"\r\n--{boundary}--\r\n".encode())
    urllib.request.urlopen(urllib.request.Request(up["upload_url"], data=b"".join(parts), method="POST",
                                                  headers={"Content-Type": f"multipart/form-data; boundary={boundary}"}))
    return eb_call("POST", "/media/upload/", {"upload_token": up["upload_token"]})["id"]


def eb_venue(org: str, o: dict) -> str:
    """Find the organization's venue with this name, or create it from the event's address."""
    for v in eb_call("GET", f"/organizations/{org}/venues/").get("venues", []):
        if v.get("name") == o["venue"]:
            return v["id"]
    parts = [p.strip() for p in o["address"].split(",")]
    region, _, postal = (parts[-1].partition(" ") if len(parts) >= 3 else ("CA", "", ""))
    address = {"address_1": parts[0], "city": parts[-2] if len(parts) >= 3 else parts[-1],
               "region": region or "CA", "postal_code": postal, "country": "US"}
    return eb_call("POST", f"/organizations/{org}/venues/", {"venue": {"name": o["venue"], "address": address}})["id"]


def eb_utc(t: dt.datetime) -> str:
    return t.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def cmd_push_eventbrite(listing_key: str):
    events, promote, log = load()
    listing = promote["listings"][listing_key]
    cfg = promote.get("eventbrite") or {}
    org, organizer = str(cfg["organization_id"]), str(cfg["organizer_id"])
    contact = contact_for(promote, listing)
    logo_id = None
    now = dt.datetime.now(TZ)

    for unit in units(listing, "eventbrite", events):
        o = unit[0]
        if o["end"] < now:
            continue
        prior = next((s for s in reversed(log) if s.get("listing") == listing_key and s.get("site") == "eventbrite"
                      and o["id"] in (s.get("events") or []) and s.get("eventbrite_id")), None)
        if logo_id is None:
            logo_id = eb_upload_image(ROOT / listing["image"])
        title = listing["title"] if len(listing["events"]) == 1 else f"{listing['title']} ({o['start']:%a %b %-d})"
        event = {
            "name": {"html": html.escape(title)},
            "summary": (listing.get("summary") or "")[:140],
            "start": {"timezone": "America/Los_Angeles", "utc": eb_utc(o["start"])},
            "end": {"timezone": "America/Los_Angeles", "utc": eb_utc(o["end"])},
            "currency": "USD", "online_event": False, "listed": True, "shareable": True,
            "organizer_id": organizer, "venue_id": eb_venue(org, o), "logo_id": logo_id,
        }
        if prior:
            eid = prior["eventbrite_id"]
            eb_call("POST", f"/events/{eid}/", {"event": event})
            action = "updated"
        else:
            eid = eb_call("POST", f"/organizations/{org}/events/", {"event": event})["id"]
            eb_call("POST", f"/events/{eid}/ticket_classes/", {"ticket_class": {
                "name": "Free registration", "free": True, "quantity_total": int(cfg.get("capacity", 100)),
                "minimum_quantity": 1, "maximum_quantity": 1, "sales_end": eb_utc(o["end"])}})
            append_log(listing_key, "eventbrite", [o["id"]], "draft", f"https://www.eventbrite.com/e/{eid}",
                       extra={"eventbrite_id": eid})
            action = "created draft"

        # Description (structured content) and the registration confirmation message
        signup = tracked(listing.get("signup_url", listing["url"]), "eventbrite", listing_key)
        body = to_html(description(listing, unit)) + f'<p>Sign up and full details: <a href="{signup}">{signup}</a></p>'
        version = int(eb_call("GET", f"/events/{eid}/structured_content/").get("page_version_number") or 0) + 1
        eb_call("POST", f"/events/{eid}/structured_content/{version}/", {
            "modules": [{"type": "text", "data": {"body": {"type": "text", "text": body, "alignment": "left"}}}],
            "publish": True, "purpose": "listing"})
        eb_call("POST", f"/events/{eid}/ticket_buyer_settings/", {"ticket_buyer_settings": {
            "confirmation_message": {"html": f"<p>You're registered, thanks! No ticket needed: just turn up and check in from "
                                             f"{fmt_time(o['start'])}. Please also complete your sign-up at "
                                             f'<a href="{signup}">{signup}</a>. Questions? Email {contact["email"]}.</p>'}}})
        url = eb_call("GET", f"/events/{eid}/")["url"]
        print(f"{action}: {fmt_range(o)}  {url}")


def cmd_publish_eventbrite(listing_key: str):
    _, _, log = load()
    drafts = {}
    for s in log:
        if s.get("listing") == listing_key and s.get("site") == "eventbrite" and s.get("eventbrite_id"):
            drafts[s["eventbrite_id"]] = s
    for eid, s in drafts.items():
        if s.get("status") != "draft":
            continue
        result = eb_call("POST", f"/events/{eid}/publish/")
        if result.get("published"):
            append_log(listing_key, "eventbrite", s["events"], "published", s.get("link"), extra={"eventbrite_id": eid})
            print(f"published: {s['events'][0]}  {s.get('link')}")


# ---------------------------------------------------------------- site fillers

def fill_funcheap(page, listing, unit, contact):
    o = unit[0]
    f = lambda n: page.locator(f"#input_18_{n}")
    f(1).fill(listing["title"])
    f(12).fill(f"{o['start']:%m/%d/%Y}")
    page.keyboard.press("Escape")  # close the datepicker
    if len(unit) == 1:
        page.check("#choice_18_128_0")  # occurs once
    else:
        page.check("#choice_18_128_2" if is_weekly(unit) else "#choice_18_128_4")  # weekly / other
        page.wait_for_timeout(300)
        if f(98).is_visible():
            f(98).fill(f"{unit[-1]['start']:%m/%d/%Y}")
            page.keyboard.press("Escape")
        if f(91).is_visible():
            f(91).fill(schedule_text(unit))
    if not o["all_day"]:
        for field, t in (("5", o["start"]), ("6", o["end"])):
            page.fill(f"#input_18_{field}_1", t.strftime("%-I"))
            page.fill(f"#input_18_{field}_2", t.strftime("%M"))
            page.select_option(f"#input_18_{field}_3", t.strftime("%p"))
    page.check("#choice_18_106_1")  # in person
    f(8).fill(o["venue"])
    f(9).fill(o["address"])
    page.select_option("#input_18_133", label=listing.get("region", "San Francisco"))
    if not listing.get("cost"):
        page.check("#choice_18_107_0")  # FREE
    else:
        page.check("#choice_18_107_1")
        page.wait_for_timeout(300)
        if f(111).is_visible():
            f(111).fill(str(listing["cost"]))
    f(30).fill(listing["url"])
    for tag in listing.get("tags", [])[:5]:
        box = page.locator("#field_18_3 label", has_text=tag).first
        if box.count():
            box.check() if box.evaluate("e => e.tagName") == "INPUT" else box.click()
    page.evaluate("""([html]) => {
        const ed = window.tinymce && tinymce.get('input_18_2');
        if (ed) ed.setContent(html);
        document.querySelector('#input_18_2').value = html;
    }""", [to_html(description(listing, unit))])
    page.set_input_files("#input_18_134", str(ROOT / listing["image"]))
    page.check("#choice_18_92_1")  # permission to use the image
    f(93).fill(listing.get("image_credit", contact["name"]))
    f(43).fill(contact["email"])
    page.fill("#input_18_43_2", contact["email"])
    f(44).fill(contact["name"])
    f(42).fill(contact.get("organization", contact["name"]))
    f(1).scroll_into_view_if_needed()


def fill_scruff(page, listing, unit, contact):
    o = unit[0]
    page.fill("#title", listing["title"])
    page.fill("#description", description(listing, unit))
    city = o["address"].split(",")[-2].strip() if o["address"].count(",") >= 2 else "San Francisco"
    page.fill("#city", city)
    page.fill("#venue", o["venue"])
    tz = page.locator("#timeZone option", has_text="Pacific Time").first.get_attribute("value")
    page.select_option("#timeZone", tz)
    page.fill("#startTime", f"{o['start']:%Y-%m-%dT%H:%M}")
    page.fill("#endTime", f"{o['end']:%Y-%m-%dT%H:%M}")
    page.fill("#url", listing["url"])
    page.set_input_files("#image", str(ROOT / listing["image"]))
    page.fill("#contactName", contact["name"])
    page.fill("#email", contact["email"])
    page.locator("#title").scroll_into_view_if_needed()


FILLERS.update(funcheap=fill_funcheap, scruff=fill_scruff)


def main(argv: list[str]) -> None:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return
    cmd, rest = argv[0], argv[1:]
    if cmd == "plan":
        cmd_plan(rest[0] if rest else None)
    elif cmd == "kit" and len(rest) == 2:
        cmd_kit(*rest)
    elif cmd == "fill" and len(rest) >= 2:
        flags = [a for a in rest if a.startswith("--")]
        pos = [a for a in rest if not a.startswith("--")]
        shot = next((a.split("=", 1)[1] for a in flags if a.startswith("--screenshot=")), None)
        cmd_fill(pos[0], pos[1], int(pos[2]) if len(pos) > 2 else None, headless="--headless" in flags, screenshot=shot)
    elif cmd == "push" and rest[1:2] == ["eventbrite"]:
        cmd_push_eventbrite(rest[0])
    elif cmd == "publish" and rest[1:2] == ["eventbrite"]:
        cmd_publish_eventbrite(rest[0])
    elif cmd == "mark" and len(rest) >= 3:
        cmd_mark(rest[0], rest[1], rest[2], rest[3:])
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
