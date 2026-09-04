# fog-calendar

The San Francisco Fog RFC club calendar, published as a subscribable `.ics` feed.

**Subscribe:** `https://justinmelbourne.github.io/fog-calendar/fog.ics` (or `https://calendar.fogrugby.com/fog.ics`)
**Landing page:** `https://justinmelbourne.github.io/fog-calendar/` (or `https://calendar.fogrugby.com/`)

## How it works

```
events.yml  ──(push to main)──►  GitHub Action runs build_ics.py  ──►  docs/fog.ics  ──►  GitHub Pages
```

- **`events.yml`** is the only file humans edit. One entry per event.
- **`build_ics.py`** turns it into a valid RFC 5545 calendar with an embedded Pacific timezone.
- **`docs/fog.ics`** is generated — never edit it by hand.
- **`docs/index.html`** is the subscribe page.

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
5. Optional: put the subscribe page behind `calendar.fogrugby.com` via a CNAME in `docs/` and a DNS record.

## Local build

```bash
pip install pyyaml
python3 build_ics.py
```

## Where this fits

This repo is the interim source of truth for dates while the club's CiviCRM event system comes online. When that lands, `events.yml` can be generated from Civi's API and this repo becomes a publishing step rather than a place people type.
