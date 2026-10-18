# San Francisco Events — official-source catalog

A static GitHub Pages catalog of **publicly advertised events in the City and County of San Francisco**. It separates **regularly occurring** events (weekly, monthly, seasonal, and annual traditions) from **dated special events**, orders every list **by date with upcoming events first**, labels **what each event costs to attend**, and makes the audit boundary visible rather than presenting an unsupported “all events” claim.

Live site: <https://buffedlizard55-lab.github.io/MaltaProj7/>

## What is included

- **154 publishable city-only rows:** 98 regularly occurring and 56 special events, checked on **2026-10-18** and re-verified row-by-row against live official pages the same day (the latest pass is logged in `research/verification-8c40d1c6.md`; earlier passes are in `research/verification-e79e0de2.md`, `research/reverification-2088b727.md`, `research/verification-e969f4df.md` and `research/reverification-55c58947.md`).
- **Free events lead, ticketed events are separate.** The main list on **Upcoming by date** holds only rows whose official source states they are free (or partly free), ordered by date and opened on upcoming rows only. Ticketed events sit in their own **Paid / ticketed** section and page, and rows whose source published no price sit in a third, clearly labelled section — no row is dropped, and a blank cost is never presented as free.
- **A source link on every published row.** Sources are labeled as official organizer, official venue, government source, official venue/federal trust, or trusted civic source.
- **A clearly labeled cost on every row.** The sourced admission text is classified as *Free*, *Free or partly free*, *Paid / ticketed*, or *Not stated*. “Not stated” means the linked official page published no price — it is never treated as free, and every such row is listed with its source link on the Flagged for Review page.
- **Nine category pages** — including a dedicated **Technology, AI & gaming** category — alongside a dashboard with a live executive summary, an **Upcoming by date** page (free first), a **Free to attend** page, a **Paid / ticketed** page, recurring, special, all-events, method, and clearly labeled **Flagged for Review** pages.
- **Sixteen review records** kept out of normal results because they are multi-city, cancelled, outside city limits, or could not be reconfirmed from a live official source (including former catalog rows demoted during re-verification).
- **Forty-one field-level flags** (published on Flagged for Review with source links) recording applied date/source corrections, dead or hijacked organizer domains, conflicting official date windows, ticket requirements published without a price, and values that could not be re-confirmed.

The catalog is a reproducible snapshot of official-source evidence, **not** a claim to list every private, unlisted, or newly announced event in San Francisco. Dates and operational details can change; check the linked source before attending.

## Date-first ordering and the executive summary

- Every list is generated with **upcoming rows first**, ordered by start date; completed editions are pushed to the bottom and badged *Completed*, and multi-week programs that are still running are badged *Ongoing now*.
- A small inline script re-computes each row's status and “in N days” label against the **visitor's real current date**, so the page stays correct after the static build date. The same script powers the dashboard's **Executive summary — free & upcoming** panel (the free events closest to today), the **Next up** panel for events of any cost, the *starting in 7 / 30 / 90 days* counters, and the *Running now* count. A build-time list is included for readers without JavaScript.
- The main table on **Upcoming by date** opens filtered to **upcoming rows only** (the *When* dropdown switches to “All dates”), so the free list leads with what you can still attend. Ticketed rows follow in their own table and page, and rows whose source published no price follow in a third table.
- Tables are readable on a phone: under 760 px each row becomes a labelled card (`data-label`) instead of a wide scrolling grid.

## Data and audit trail

- `data/events.json` — source of truth; includes catalog metadata, publishable records, source authority, review statuses, and the field-level `flags` register.
- `data/events.csv` — generated export of every data record, including review-only rows.
- `research/verification-8c40d1c6.md` — the latest row-by-row official-source log (41 rows re-fetched on 2026-10-18), including the values filled, the rows added, the irregularities found, and the scope decisions taken.
- `research/patch-8c40d1c6.py` — reproducible patch script for that pass (new rows, cost and time fills, new flags); re-running it is a no-op except for field updates.
- `research/verification-e79e0de2.md` — the previous session's row-by-row official-source log.
- `research/patch-e79e0de2.py` — reproducible patch script that applies this session's data changes (new rows, cost/time fills, the category split, the new flags).
- `research/official-source-audit.md` — row-level source matrix, review register, and material scope decisions.
- `research/reverification-2088b727.md`, `research/verification-e969f4df.md`, `research/reverification-55c58947.md` — earlier full re-verification passes.
- `COORDINATION.md` — work ledger, handoff notes, and deployment/verification record.

For a published row, `name`, cadence/date, San Francisco location, organizer, and source URL are required. Optional time and admission fields stay blank when the source did not state them. A record with an essential gap is never promoted to the normal tables; it is documented on **Flagged for Review**.

## Build and validate

No package installation is required.

```bash
python3 build.py
python3 verify.py
```

`build.py` regenerates the site pages, category pages, stylesheet, and CSV export from `data/events.json`. `verify.py` checks the data shape, source-link coverage, row separation, generated page counts, category pages, date-first ordering (per table, now that the upcoming page is split by cost), the free/paid section split, cost-label coverage, duplicate element ids, and local navigation — and, after mutation testing, also rejects example/local source hosts, locations without a San Francisco indicator, unknown status/cadence/authority values, malformed or inverted ISO dates, date-text years that disagree with ISO dates, duplicate name+date records, and placeholder time/admission text. It deliberately does not live-crawl external organizer sites from the sandbox; those source links remain the final authority. The stable row counts in `verify.py` must only change together with an entry in `research/official-source-audit.md` and `research/verification-8c40d1c6.md`.

## Scope

City and County of San Francisco only. Look-alike events outside the city — the Great Dickens Christmas Fair at the Cow Palace (Daly City), SFO airport programs (San Mateo County), and the Top of the Hill Festival (Daly City) — are excluded and are not published in the city-only tables.
