# SF Fog RFC Calendar Portal Design Specification

**Date:** 2026-09-05  
**Topic:** Club Calendar Viewer & Editor Web Portal  
**Target File:** `docs/portal.html`  
**Repository:** `san-francisco-fog-rfc/fog-calendar`

---

## 1. Overview & Objectives

The SF Fog RFC Calendar Portal provides a brand-aligned, zero-build web interface for viewing, filtering, and updating the club's event schedule. 

* **Public Viewing:** Allows players, coaches, and supporters to view upcoming fixtures, trainings, Pathway to Rugby sessions, tournaments, and social events in an interactive Month Grid and Chronological Agenda view without requiring login or app installation.
* **Administrative Editing:** Enables authorized club administrators to authenticate via GitHub Personal Access Token (PAT) to add, edit, or remove events in `events.yml`, validate entries against calendar constraints, manage repeating training dates/exdates, and commit updates directly to GitHub `main` to trigger automated RFC 5545 `.ics` generation.
* **Brand Fidelity:** Strictly adheres to the **Fog Rugby Design System** (`fog-rugby-design.skill`), using the 6 canonical colors, Futura PT typography, flat editorial surfaces, near-square corners, and stroke-drawn iconography.

---

## 2. Architecture & File Structure

The portal is implemented as a client-side single-page application hosted on GitHub Pages inside the `docs/` folder. It requires no Node.js compilation pipeline, runtime backend, or external database.

### File Layout
```text
docs/
├── assets/
│   ├── css/
│   │   └── portal.css               # Brand-compliant styles (Fog tokens, typography, grid, drawer)
│   ├── fonts/                       # FuturaPT-*.otf (already present in repository)
│   ├── img/
│   │   ├── fog-logo.png             # Official Fog shield crest
│   │   └── fog-coat-of-arms.png     # Official coat of arms
│   └── js/
│       └── js-yaml.min.js           # Vendored JS-YAML v4 for parsing and serializing events.yml
├── index.html                       # Existing subscribe page with link to portal
├── portal.html                      # Main calendar portal entry point (semantic HTML + controller)
└── fog.ics                          # Generated RFC 5545 feed (built by GitHub Action)
```

### Data Flow & GitHub Synchronization
1. **Fetch:** On load, the portal reads `events.yml`:
   * In production (GitHub Pages): Fetches `https://raw.githubusercontent.com/san-francisco-fog-rfc/fog-calendar/main/events.yml` or via GitHub Contents API.
   * In local development: Relative fetch from `../events.yml`.
2. **Parse & Render:** `js-yaml.min.js` parses the YAML document into structured JavaScript objects. The controller generates the active month calendar grid and chronological agenda list.
3. **Session Authentication:** Admins enter a GitHub PAT (classic `repo` or fine-grained `Contents: Read and write`). The token is stored in browser `sessionStorage` (or optional `localStorage`) and never transmitted anywhere other than `api.github.com`.
4. **Draft Mutations:** All edits, additions, and deletions are held in local memory. A persistent notification bar shows the count of unsaved changes.
5. **Commit to GitHub:** Admins review changes, input a commit message, and confirm. The portal performs a `PUT /repos/san-francisco-fog-rfc/fog-calendar/contents/events.yml` with the base64-encoded serialized YAML and the file's current `sha`.
6. **Action Pipeline:** Pushing to `main` triggers `.github/workflows/build.yml`, which executes `python3 build_ics.py`, validating IDs, building `docs/fog.ics`, and publishing the feed.
7. **Offline/Manual Fallback:** A "Download updated `events.yml`" button is available for users without a GitHub token or for offline testing.

---

## 3. Visual & Component Standards (Fog Rugby Design System)

All visual elements strictly follow the canonical rules defined in the Fog Rugby Brand System:

### Color Palette (Zero Invented Colors)
* `--fog-blue`: `#006EB6` (Primary headlines-2, links, primary buttons, crest blue)
* `--fog-light-blue`: `#24A0F1` (Accents, hovers, text accent on dark backgrounds)
* `--fog-dark-blue`: `#00243C` (Dark panel backgrounds, footers, default heading color)
* `--fog-gray`: `#DCDDDE` (Neutral panels, table shading, stat cards)
* `--fog-dark-gray`: `#141718` (Body text — near black, never pure black for text)
* `--fog-white`: `#FFFFFF`
* `--fog-black`: `#000000`
* `--fog-green`: `#157A38` (Confirmed badges)
* `--fog-red`: `#C4321F` (Delete/cancellation alerts)
* **Contrast Compliance:** Light Blue on dark backgrounds (5.60:1 AA); Fog Blue on white (5.38:1 AA). No Light Blue on white; no Fog Blue on dark.

### Typography
* **Font Family:** `"Futura PT", "Jost", Futura, Arial, Helvetica, sans-serif`
* **Headings / Display:** ALL CAPS, `letter-spacing: 0.05em`, `line-height: 1.05`.
* **Eyebrows:** `0.8rem`, Demi 600, uppercase, `letter-spacing: 0.18em`.
* **Body Copy:** Book 400, sentence case, no tracking, `line-height: 1.6`, color `#141718`.
* **UI Controls & Buttons:** Demi 600 or Bold 700, uppercase, `letter-spacing: 0.08em`.

### Layout & Surfaces
* **Spacing:** 8px grid scale (8px, 16px, 24px, 32px, 48px).
* **Corner Radius:** Strict 2px for buttons/tags, 4px for cards and containers.
* **Surface Aesthetic:** Flat editorial surfaces. No gradients, no frosted glass, no heavy box-shadows.
* **Icons:** Stroke-drawn SVG icons (`fill:none; stroke:currentColor; stroke-width:2`). No emoji-as-icons.

---

## 4. UI Specification & Views

### Top Bar & Navigation
* Flat Fog Dark (`#00243C`) header with the SF Fog shield crest (`assets/img/fog-logo.png`).
* Eyebrow: `SAN FRANCISCO FOG RFC` in Light Blue (`#24A0F1`).
* Title: `CLUB CALENDAR PORTAL` (Futura PT Bold, caps, white).
* Actions:
  * "Back to Subscribe" link.
  * "Admin Access" toggle button (White outline on dark).
  * Status indicator (*Browsing Public Schedule* or *Authenticated as [user]*).

### Filter & Controls Bar
* Background: Neutral Fog Gray (`#DCDDDE`).
* Category chips: `All`, `Fixtures`, `Training`, `Pathway`, `Tournaments`, `Socials`, `Board`, `Community`.
* Status chips: `All`, `Confirmed`, `Tentative`.
* View Switcher: Segmented toggle between **Month Grid** and **Agenda List**.
* Search bar: Real-time search by title, opponent, location, or notes.
* Month navigation: `< Prev`, `Today`, `Next >`, with active Month & Year heading (e.g. `OCTOBER 2026`).

### View A: Month Calendar Grid
* 7-column layout (Sun–Sat) with weekend accent styling.
* Day cells display date number, current day indicator, and event chips colored by category:
  * **Fixtures:** Fog Dark (`#00243C`) badge with white text.
  * **Training:** Fog Blue (`#006EB6`) badge with white text.
  * **Pathway:** Fog Blue outline badge.
  * **Tournaments:** High-contrast Fog Dark tag.
  * **Socials / Community:** Neutral gray tag with dark gray text.
  * **Tentative:** Tag with dashed border and small `?` indicator.
* Clicking an event opens the Event Details & Edit Drawer.
* In Admin Mode, hover states on empty days display a "+ Add Event" prompt.

### View B: Chronological Agenda List
* Organized chronologically with sticky month headers (Futura PT Bold, Fog Blue, ALL CAPS).
* Event cards (4px radius, white background, 1px border):
  * **Date Column:** Month abbreviation, large day number, day of week, and kickoff/event time.
  * **Event Info:** Category pill, event title (H3), venue location with Google Maps search link, notes snippet, and external URL link.
  * **Status & Controls:** Confirmed/Tentative pill, and in Admin Mode: "Edit" and "Duplicate" action buttons.

---

## 5. Event Editor & Schema Enforcement

The Event Drawer provides a guided form ensuring compliance with `build_ics.py` and `events.yml` constraints:

| Field | Type / Rule | Validation / Behavior |
|---|---|---|
| `id` | Slug (string) | **Existing events:** Locked/Read-only with explanation.<br>**New events:** Auto-generated from date + title slug, editable once before creation. Must be unique. |
| `title` | Text | Required. Title shown on the calendar. |
| `date_type` | Choice | "Single Day" (`date`) or "Multi-Day" (`start` & `end`). |
| `date` / `start` & `end` | Date picker (`YYYY-MM-DD`) | Required. End date must be on or after start date. |
| `time_type` | Choice | "Timed Event" or "All-Day / TBD Kickoff". |
| `time` & `end_time` | Time inputs (`HH:MM`) | Optional. 24-hour format. Default duration is 2 hours if end time omitted. |
| `category` | Select | `fixture`, `training`, `pathway`, `tournament`, `social`, `board`, `community`. |
| `status` | Select | `confirmed` (standard) or `tentative` (playoffs, friendlies awaiting confirmation). |
| `location` | Text | Free text. Includes quick autofill suggestions (e.g., "Raymond Kimbell Playground", "Crocker Amazon", "Pilsner Inn"). |
| `notes` | Textarea | Event description, instructions, volunteer details. |
| `url` | URL string | Event link (e.g., match link, Partiful, Eventbrite). |

### Repeating Events & Exdate Manager (Training)
* For repeating events containing `rrule` (e.g. `2026-27-training`):
  * Displays RRULE string and visual summary ("Every Tuesday & Thursday until May 16, 2027").
  * **Exdates Manager:** Visual tag cloud of excluded holiday/break dates.
  * Admin can click an "×" on any exdate chip to remove it, or use a date picker to append new blackout dates (e.g., coach-confirmed holiday breaks or weather cancellations).

---

## 6. Security, Error Handling & Integrity

1. **Token Hygiene:** GitHub PAT is kept only in client `sessionStorage` or optional `localStorage`. No third-party servers, logging, or trackers.
2. **SHA Conflict Prevention:** Every GitHub update checks the remote file's latest `sha`. If a remote conflict occurs (someone else committed changes), the portal notifies the admin to reload or download a local diff.
3. **YAML Schema Validation:** Before sending to GitHub or downloading, the serialized YAML is verified:
   * Duplicate `id` check (guarantees `build_ics.py` won't fail).
   * Date and time format validation.
   * Category allowlist check.
4. **Voice & Tone:** All UI copy and error dialogs follow club voice: direct, respectful, addressing "you" and "your team".

---

## 7. Verification & Acceptance Criteria

* [ ] `docs/portal.html` loads cleanly in browser with zero console errors.
* [ ] Calendar Month Grid and Agenda List render all current 2026–2027 events accurately.
* [ ] Category filtering, status filtering, and text search work instantaneously.
* [ ] Responsive on both mobile screens (375px) and desktop screens (1200px+).
* [ ] Admin mode unlocks upon entering a valid GitHub PAT.
* [ ] Adding a new event generates a unique slug and validates required fields.
* [ ] Editing an event preserves its immutable `id`.
* [ ] Exdate manager allows adding and removing blackout dates for repeating training.
* [ ] Committing changes correctly calls the GitHub API and triggers `.github/workflows/build.yml`.
* [ ] Fallback download button exports valid, well-formatted `events.yml`.
* [ ] Contrast ratios meet WCAG AA standards (Light Blue on dark panels, Fog Blue on white).
