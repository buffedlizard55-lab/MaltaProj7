# San Francisco Events — official-source catalog

A static GitHub Pages catalog of **publicly advertised events in the City and County of San Francisco**. It separates **regularly occurring** events (weekly, monthly, seasonal, and annual traditions) from **dated special events** and makes the audit boundary visible rather than presenting an unsupported “all events” claim.

## What is included

- **139 publishable city-only rows:** 94 regularly occurring and 45 special events, checked on **2026-10-18** and re-verified row-by-row against live official pages the same day (including union reconciliation of three parallel integration contributions, PRs #9–#14, plus the 2026-10-18 coverage-gap passes logged in `research/coverage-gap-646f6727.md` and `research/review-5e333a6e.md`).
- **A source link on every published row.** Sources are labeled as official organizer, government source, official venue/federal trust, or trusted civic source.
- **Eight category pages** alongside dashboard, recurring, special, all-events, method, and clearly labeled **Flagged for Review** pages.
- **Sixteen review records** kept out of normal results because they are multi-city, cancelled, outside city limits, or could not be reconfirmed from a live official source (including former catalog rows demoted during re-verification).
- **25 field-level flags** (published on Flagged for Review with source links) recording applied date/source corrections, dead or hijacked organizer domains, conflicting official date windows, and values that could not be re-confirmed.

The catalog is a reproducible snapshot of official-source evidence, **not** a claim to list every private, unlisted, or newly announced event in San Francisco. Dates and operational details can change; check the linked source before attending.

## Data and audit trail

- `data/events.json` — source of truth; includes catalog metadata, publishable records, source authority, review statuses, and the field-level `flags` register.
- `research/integration-patch-2026-10-18.py` — reproducible patch script used to apply the integration corrections and additions.
- `research/coverage-patch-646f6727.py` and `research/coverage-gap-646f6727.md` — coverage-gap additions with row-level official-source evidence.
- `research/patch-5e333a6e.py` and `research/review-5e333a6e.md` — second coverage-gap pass (Moscone Center conventions, SFMTA-documented neighborhood events, FAMSF free days, SF Open Studios, Pride-week 2026 marches) and repo review notes.
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
