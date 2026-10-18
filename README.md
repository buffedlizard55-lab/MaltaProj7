# San Francisco Events — official-source catalog

A static GitHub Pages catalog of **publicly advertised events in the City and County of San Francisco**. It separates **regularly occurring** events (weekly, seasonal, and annual traditions) from **dated special events** and makes the audit boundary visible rather than presenting an unsupported “all events” claim.

## What is included

- **54 publishable city-only rows:** 46 regularly occurring and 8 special events, checked on **2026-10-18**.
- **A source link on every published row.** Sources are labeled as official organizer, government source, official venue/federal trust, or trusted civic source.
- **Eight category pages** alongside dashboard, recurring, special, all-events, method, and clearly labeled **Flagged for Review** pages.
- **Five review records** kept out of normal results because they are multi-city, cancelled, outside city limits, or lack essential direct-source evidence.

The catalog is a reproducible snapshot of official-source evidence, **not** a claim to list every private, unlisted, or newly announced event in San Francisco. Dates and operational details can change; check the linked source before attending.

## Data and audit trail

- `data/events.json` — source of truth; includes catalog metadata, publishable records, source authority, and review statuses.
- `data/events.csv` — generated export of every data record, including review-only rows.
- `research/official-source-audit.md` — row-level source matrix, review register, and material scope decisions.
- `COORDINATION.md` — work ledger, handoff notes, and deployment/verification record.

For a published row, `name`, cadence/date, San Francisco location, organizer, and source URL are required. Optional time and admission fields stay blank when the source did not state them. A record with an essential gap is never promoted to the normal tables; it is documented on **Flagged for Review**.

## Build and validate

No package installation is required.

```bash
python3 build.py
python3 verify.py
```

`build.py` regenerates the site pages, category pages, stylesheet, and CSV export from `data/events.json`. `verify.py` checks the data shape, source-link coverage, row separation, generated page counts, category pages, and local navigation — and, after mutation testing, also rejects example/local source hosts, locations without a San Francisco indicator, unknown status/cadence/authority values, malformed or inverted ISO dates, date-text years that disagree with ISO dates, duplicate name+date records, and placeholder time/admission text. It deliberately does not live-crawl external organizer sites from the sandbox; those source links remain the final authority. The stable row counts in `verify.py` must only change together with an entry in `research/official-source-audit.md`.
