# San Francisco Events — official-source catalog, free events first

A static GitHub Pages catalog of **publicly advertised events in the City and County of San Francisco**, organised the
way the brief asks: **free events are the main section**, paid events are collected and organised in a **separate
section**, every list is ordered **by date with upcoming events first**, the requested focus areas (**gaming, music,
AI**) lead the free list and everything else follows, every row **labels what it costs to attend**, and every row
carries its own **official source link**. Regularly occurring events (weekly, monthly, seasonal, annual traditions)
are kept apart from dated special events.

Live site: <https://buffedlizard55-lab.github.io/MaltaProj7/>

## What is included

- **151 publishable city-only rows:** 99 regularly occurring and 52 special events, checked on **2026-10-18** and
  re-verified row-by-row against live official pages (this session's pass, with quoted source text, is in
  `research/reverification-3977d9cb.md`; earlier full passes are in `research/verification-e79e0de2.md`,
  `research/reverification-2088b727.md`, `research/verification-e969f4df.md` and
  `research/reverification-55c58947.md`).
- **57 free or partly free rows — 12 of them still upcoming** — published as the main list on `free.html`.
- **94 non-free rows** (13 priced/ticketed, 4 registration-or-invitation-only, 77 with no published price) collected
  and organised on a separate `paid.html` page, never mixed into the free list.
- **A source link on every published row.** Sources are labeled official organizer, official venue, government source,
  official venue/federal trust, or trusted civic source.
- **A clearly labeled cost on every row,** classified only from the admission text the linked source published:
  *Free*, *Free or partly free*, *Paid / ticketed*, *Registration / invitation — no price published*, or *Not stated*.
  “Not stated” means the official page published no price — it is never treated as free, and every such row is listed
  with its source link on the Flagged for Review page.
- **Nine category pages** — including **Technology, AI & gaming** — plus a dashboard with a live free-first executive
  summary, an Upcoming-by-date page, recurring, special, all-events, method, and clearly labeled **Flagged for
  Review** pages.
- **Seventeen review records** kept out of normal results because they are multi-city, cancelled, outside city limits,
  or could not be reconfirmed from a live official source.
- **Forty-two field-level flags** (published on Flagged for Review with source links, each deep-linkable by id)
  recording applied corrections, dead or bot-blocked organizer domains, conflicting official times, coverage gaps in
  the free gaming and free AI focus areas, aggregator-only dates, and values that could not be confirmed.

The catalog is a reproducible snapshot of official-source evidence, **not** a claim to list every private, unlisted,
or newly announced event in San Francisco. Dates and operational details can change; check the linked source before
attending.

## Free-first ordering, the executive summary, and the paid section

- **`free.html` is the main section.** It holds only rows whose official source states the event is free or free for
  part of the programme, ordered **gaming → music & performing arts → AI & technology → everything else**, and inside
  each focus area the nearest upcoming date leads with completed editions pushed to the bottom and badged
  *Completed*. A Focus control filters by area and a Sort control switches back to plain date, name, category or cost.
- **`paid.html` is the separate section.** Two clearly labelled tables — priced/ticketed/registration-only rows, then
  rows whose source published no price — both ordered with upcoming dates first.
- **The executive summary is free-first.** The dashboard's headline panel lists the free events closest to today, the
  counters count *free* events starting in 7 / 30 / 90 days and free programs running now, and a separate labelled
  panel shows the nearest paid or unpriced events. A small inline script recomputes all of it against the **visitor's
  real current date**, so the page stays correct after the static build date; `<noscript>` fallbacks are included.
- **Focus areas are generated from the data**, not from hand-written prose: each card lists real rows with their
  sourced cost and official link, and where a focus area has no verified free rows (gaming and AI as of 2026-10-18) the
  card says so and links to the coverage-gap finding instead of implying coverage.
- **Every list separates free from non-free.** `recurring.html`, `special.html`, `annual-special.html` and all nine
  category pages render their free rows first and their non-free rows in a second table. `upcoming.html` and
  `all-events.html` keep the complete date-ordered catalog with the cost visible on every row.
- **Repeating programs are honest about dates.** 18 rows are weekly/monthly/seasonal programs whose source states a
  schedule rather than one date (for example “Saturday (year-round)”, “First Tuesday of every month”). They badge
  *Repeating — no single date* and can be filtered; no next-occurrence date is computed, because that would publish an
  unsourced value.
- Tables are readable on a phone: under 760 px each row becomes a labelled card (`data-label`), the navigation becomes
  a horizontally scrollable pill row, and the focus grid collapses to one column.

## Data and audit trail

- `data/events.json` — source of truth; includes catalog metadata, publishable records, source authority, review
  statuses, and the field-level `flags` register.
- `data/events.csv` — generated export of every data record, including review-only rows and the derived `cost_class`.
- `research/reverification-3977d9cb.md` — this session's row-by-row official-source log: every page fetched, the
  quoted source text, the rows added, the values left blank, and the candidates rejected.
- `research/review-3977d9cb.md` — this session's repository review: 18 irregularities (R1–R18) with evidence,
  severity, and the action taken, plus the items left for manual review.
- `research/patch-3977d9cb.py` — reproducible, idempotent patch script that applies this session's data changes.
- `research/official-source-audit.md` — row-level source matrix, review register, and material scope decisions.
- `research/verification-e79e0de2.md`, `research/reverification-2088b727.md`, `research/verification-e969f4df.md`,
  `research/reverification-55c58947.md` — earlier full re-verification passes.
- `COORDINATION.md` — work ledger, handoff notes, and deployment/verification record.

For a published row, `name`, cadence/date, San Francisco location, organizer, and source URL are required. Optional
time and admission fields stay blank when the source did not state them. A record with an essential gap is never
promoted to the normal tables; it is documented on **Flagged for Review**.

## Build and validate

No package installation is required.

```bash
python3 build.py
python3 verify.py
```

`build.py` regenerates the site pages, category pages, stylesheet, and CSV export from `data/events.json`.
`verify.py` checks the data shape, source-link coverage, date-first ordering, local navigation, and — for the
free-first structure — proves that `free.html` renders **exactly** the source-stated free rows and that `paid.html`
renders **exactly** the non-free rows (compared by row identity, not by name, because two editions of Pride and of the
Italian Heritage Parade share a name), that the free list leads with the gaming/music/AI focus areas and keeps
upcoming dates first inside each focus block, that every page's navigation offers both sections, and that the
dashboard's executive summary is the free-first one. It also rejects example/local source hosts, locations without a
San Francisco indicator, unknown status/cadence/authority values, malformed or inverted ISO dates, date-text years
that disagree with ISO dates, duplicate name+date records, and placeholder time/admission text. It deliberately does
not live-crawl external organizer sites from the sandbox; those source links remain the final authority. The stable
row counts in `verify.py` must only change together with an entry in `research/official-source-audit.md` and the
current session's verification log.

## Scope

City and County of San Francisco only. Look-alike events outside the city — the Great Dickens Christmas Fair at the
Cow Palace (Daly City), SFO airport programs (San Mateo County), the Top of the Hill Festival (Daly City), and
GobbleCon (Burlingame) — are excluded and are not published in the city-only tables. Bay Area–wide programs such as
Open Source AI Week are held as review records, with their San Francisco flagship events catalogued individually.
