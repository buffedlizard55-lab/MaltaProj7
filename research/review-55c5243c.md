# Independent maintenance audit — 2026-10-18

Session: `arena/55c5243c-maltaproj7`. Baseline `4877da9` (PR #35).

## Scope and honest verification boundary

Reviewed the repository's coordination ledger, README, deployment workflow, generator/verifier interfaces and source-data structure. Rebuilt every generated page and ran the existing row-level structural checks on all 179 records (162 published, 17 review), including the 51 existing flags. This is **not** independent factual re-verification of all 162 published rows. Their source evidence remains in the existing research logs; no claim of a new full official-source crawl is made. No event values or verification statuses changed in this pass.

The requested exhaustive list cannot be certified: organizers publish and revise schedules independently, and private/unlisted events cannot be enumerated. Existing site caveats and published coverage-gap flags remain necessary. Gaming and AI still have no dated free upcoming entry confirmed in the current dataset; do not infer that no such events exist.

## Official sources actually fetched in this session

Fetched with the page retrieval tool on 2026-10-18:

| Official publisher URL | Observed source text | What this check supports |
| --- | --- | --- |
| https://www.fromtheesf.com/ | “Fri, Oct 23”; “Fri, Nov 20”; “Fri, Dec 11”; “Ocean Ave & Mission St”; each entry says “FREE COMMUNITY FUN!” | Organizer lists three free night-market editions. Homepage omits the year in the displayed date; no year inferred from this page alone. |
| https://www.fromtheesf.com/events/from-the-e-holiday-night-market | “Dec 11, 2026, 4:30 PM – 8:30 PM”; “Ocean Ave & Mission St, San Francisco, CA 94112, USA”; “FREE COMMUNITY FUN!” | Independently confirms existing Holiday row's date, hours, city and free admission. Registration closes at 7 PM, which is not the event end time. |

No new facts required data changes. Existing cadence inconsistency remains on Flagged for Review; neither page states weekly/monthly/annual recurrence for the series.

## Reproducible checks and findings

- `python3 -m unittest discover -s tests -v`: 11 tests passed.
- `python3 build.py && python3 verify.py`: passes for 162 published rows, 102 recurring, 60 special, 17 review, 51 flags and nine categories.
- Existing verifier checks free-only upcoming row identity sets, paid separation, focus order, source links, date ordering, blank optional-field policy and navigation.
- Found a structural verification gap: local `#fragment` links were skipped and cross-page fragments were not validated. Fixed this and added regression fixtures for valid/missing/encoded fragments, directory indexes, missing files, path escapes, duplicate IDs, ARIA references and external-link non-fetch behavior.
- All currently generated local links and HTML fragment targets pass the stronger check. External URL availability is not implied by this result.
- Pages workflow now runs regression tests before rebuilding, verifying and deploying; malformed internal anchors block deployment.
- Existing dashboard is preserved: dated free events first, free-only executive summary, separate paid section, all catalog categories, mobile stacked tables, and published review flags.
