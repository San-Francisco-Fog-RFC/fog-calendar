# fog-calendar

The San Francisco Fog RFC club calendar and syndication engine, published as subscribable calendar feeds, open REST JSON APIs, and Schema.org rich data for search engines.

- **Calendar Feed (iCal):** `https://events.fogrugby.com/fog.ics`
- **REST JSON API:** `https://events.fogrugby.com/events.json`
- **Schema.org JSON-LD:** `https://events.fogrugby.com/schema-events.jsonld`
- **OpenAPI 3.1 Spec:** `https://events.fogrugby.com/openapi.yaml`
- **Portal & Landing Page:** `https://events.fogrugby.com/`

## How it works

```
events.yml ──(push to main)──► GitHub Action runs build_ics.py ──► docs/fog.ics (iCal Feed)
                                                                 ├── docs/events.json (REST API)
                                                                 ├── docs/schema-events.jsonld (Schema.org)
                                                                 ├── docs/openapi.yaml (OpenAPI 3.1)
                                                                 └── docs/index.html (Web Portal)
```

- **`events.yml`** is the only file humans edit. One entry per event.
- **`build_ics.py`** compiles `events.yml` into all syndication formats automatically.
- **`docs/fog.ics`** is the RFC 5545 calendar feed with embedded Pacific timezone (`America/Los_Angeles`).
- **`docs/events.json`** is a machine-readable JSON REST API with ISO-8601 timestamps and venue metadata.
- **`docs/schema-events.jsonld`** is the Schema.org `@graph` for Google Events Rich Results and crawler indexing.
- **`docs/openapi.yaml`** is the OpenAPI 3.1 contract for developers and partner clubs.
- **`docs/index.html`** is the subscriber page with embedded Schema.org JSON-LD in the `<head>`.

## Editing the calendar

1. Open `events.yml` on GitHub → pencil icon → edit → *Commit changes* to `main`.
2. Wait ~1 minute. The Action regenerates `fog.ics` and commits it.
3. Subscribers pick it up on their next refresh (Apple ~hourly by default, Google 12–24 h).

Rules that keep the feed sane:

- **Never change an `id`** once published — it's the calendar UID. Change the title, date, anything else; not the id.
- Leave `time:` out for TBD-kickoff or all-day items. Add it when the kickoff is known.
- Use `status: tentative` for anything conditional (playoffs, unconfirmed friendlies).
- Cancelled? Set `status: cancelled` rather than deleting the entry. Calendars, bay.lgbt and Google then show it as cancelled instead of it silently vanishing.
- Repeating events (training) use `rrule:` + `exdates:` — see the training entry for the pattern.
- **Venues:** places are defined once under `venues:` and referenced with `venue: <key>`. Fix an address there and every event using it updates. Use free-text `location:` only for placeholders like "TBC - Fresno".
- **Series:** events that share details (e.g. Pathway to Rugby) set `series: <key>`. They inherit the series `defaults` (time, venue, image, link, category, status); anything set on the event itself wins. A series `listing:` holds the copy `promote.py` submits to listing sites.
- The build checks `events.yml` against [`schema/events-yml.schema.json`](schema/events-yml.schema.json) and stops on typos (e.g. `venu:`), unknown venues or series, or times like `7:30pm`. Editors such as VS Code use the same schema for autocomplete and inline errors.

## One-time setup

1. Create the repo (public) and push these files.
2. **Settings → Pages → Source: Deploy from a branch → `main` / `/docs`.**
3. **Settings → Actions → General → Workflow permissions: Read and write.**
4. Push once (or run the workflow manually) to generate the first `fog.ics`.
5. Optional: put the subscribe page behind `events.fogrugby.com` via a CNAME in `docs/` and a DNS record.

## Local build & validation

```bash
pip install pyyaml

# Strict validation check (halts with error code if any issue exists)
python3 build_ics.py --validate-only

# Compile all feeds (runs validation first; fails if errors exist)
python3 build_ics.py
```

## Promoting events on listing sites

`promote.py` submits events to sites like Funcheap and SCRUFF without retyping them. Listing copy (description, image, cost, tags, which sites) lives in each series' `listing:` in `events.yml`, along with its dates, times and venues; site settings (default contact, Eventbrite ids) live in `promote.yml`; every submission is recorded in `submissions.yml`.

```bash
uv run promote.py plan                                   # what's been submitted where, and what's due
uv run promote.py fill pathway-to-rugby-2026 funcheap    # fill the form in a browser; you review and click Submit
uv run promote.py kit pathway-to-rugby-2026 plai         # copy-paste fields for sites without auto-fill
uv run promote.py mark pathway-to-rugby-2026 funcheap published --link https://...
```

Links submitted to listing sites get UTM tags (`utm_source=<site>&utm_medium=listing&utm_campaign=<listing>`), so Google Analytics on fogrugby.com shows visits and sign-ups per site. Links inside `fog.ics` are left untagged, because bay.lgbt identifies events by their link.

`fill` never clicks Submit. It opens a real browser window with a saved profile in `.promote-browser/` (gitignored), so for sites that need an account you sign in once and stay signed in. Sites that take several dates in one submission (Funcheap, Eventbrite) get one per venue; the rest get one per date. First run only: `uv run --with playwright playwright install chromium`.

## Search engine & Schema.org verification links

After publishing or making schedule changes, verify that crawlers and aggregators detect all events cleanly:

- [**Google Rich Results Test**](https://search.google.com/test/rich-results?url=https%3A%2F%2Fevents.fogrugby.com%2F) — Simulates Googlebot crawl to verify interactive event cards and carousels.
- [**Schema.org Markup Validator**](https://validator.schema.org/#url=https%3A%2F%2Fevents.fogrugby.com%2F) — Official consortium validator across Google, Microsoft/Bing, and Yahoo.
- [**Bing Webmaster Tools**](https://www.bing.com/webmasters/) — Inspect URL markup and request Bing indexing.

## Where this fits

This repo is the interim source of truth for dates while the club's CiviCRM event system comes online. When that lands, `events.yml` can be generated from Civi's API and this repo becomes a publishing step rather than a place people type.
