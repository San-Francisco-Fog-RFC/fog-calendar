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
- Cancelled? Delete the entry. Subscribers' copies disappear on next refresh.
- Repeating events (training) use `rrule:` + `exdates:` — see the training entry for the pattern.

## One-time setup

1. Create the repo (public) and push these files.
2. **Settings → Pages → Source: Deploy from a branch → `main` / `/docs`.**
3. **Settings → Actions → General → Workflow permissions: Read and write.**
4. Push once (or run the workflow manually) to generate the first `fog.ics`.
5. Optional: put the subscribe page behind `events.fogrugby.com` via a CNAME in `docs/` and a DNS record.

## Local build

```bash
pip install pyyaml
python3 build_ics.py
```

## Where this fits

This repo is the interim source of truth for dates while the club's CiviCRM event system comes online. When that lands, `events.yml` can be generated from Civi's API and this repo becomes a publishing step rather than a place people type.
