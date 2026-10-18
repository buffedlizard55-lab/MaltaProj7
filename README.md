# San Francisco Events — official-source catalog

A static GitHub Pages catalog of **publicly advertised events in the City and County of San Francisco**. It separates **regularly occurring** events (weekly, seasonal, and annual traditions) from **dated special events** and makes the audit boundary visible rather than presenting an unsupported “all events” claim.

## What is included

- **72 publishable city-only rows:** 55 regularly occurring and 17 special events, checked on **2026-10-18** (every source URL re-fetched from its official publisher page during final integration).
- **A source link on every published row.** Sources are labeled as official organizer, government source, official venue/federal trust, or trusted civic source.
- **Eight category pages** alongside dashboard, recurring, special, all-events, method, and clearly labeled **Flagged for Review** pages.
- **Five review records** kept out of normal results because they are multi-city, cancelled, outside city limits, or lack essential direct-source evidence.
- **13 field-level flags** (also on Flagged for Review) recording applied date/source corrections, dead or hijacked organizer domains, conflicting official date windows, and values that could not be re-confirmed — each with source links for manual review.

The catalog is a reproducible snapshot of official-source evidence, **not** a claim to list every private, unlisted, or newly announced event in San Francisco. Dates and operational details can change; check the linked source before attending.

## Data and audit trail

- `data/events.json` — source of truth; includes catalog metadata, publishable records, source authority, review statuses, and the field-level `flags` register.
- `data/events.csv` — generated export of every data record, including review-only rows.
- `research/official-source-audit.md` — row-level source matrix, review register, final-integration re-verification results, and material scope decisions.
- `research/integration-patch-2026-10-18.py` — reproducible patch script used to apply the final-integration corrections and additions.
- `COORDINATION.md` — work ledger, handoff notes, and deployment/verification record.

For a published row, `name`, cadence/date, San Francisco location, organizer, and source URL are required. Optional time and admission fields stay blank when the source did not state them. A record with an essential gap is never promoted to the normal tables; it is documented on **Flagged for Review**.

## Build and validate

No package installation is required.

```bash
python3 build.py
python3 verify.py
```

`build.py` regenerates the site pages, category pages, stylesheet, and CSV export from `data/events.json`. `verify.py` checks the data shape, source-link coverage, row separation, generated page counts, category pages, and local navigation. It deliberately does not live-crawl external organizer sites from the sandbox; those source links remain the final authority.
