# Repository review and irregularities — session arena/3977d9cb-maltaproj7

**Review date: 2026-10-18 (UTC).** Baseline reviewed: `origin/main` at `68a0516` (merge of PR #26), 164 data records
(148 published, 16 review, 34 flags), 18 generated HTML pages, `build.py` (1,034 lines), `verify.py` (405 lines),
`.github/workflows/pages.yml`, `README.md`, `COORDINATION.md`, `data/events.json`, `data/events.csv`,
`assets/style.css`, and the nine `research/` documents.

Method: read each file, re-ran the build and the verifier, re-derived every count from `data/events.json`, audited
every source host and every weak field, and re-fetched official pages for the near-term upcoming rows (log:
`research/reverification-3977d9cb.md`). Nothing below was accepted on the strength of a secondary listing.

---

## 1. What the review confirmed as sound

| Check | Result |
| --- | --- |
| `python3 build.py && python3 verify.py` on the untouched baseline | Passed cleanly: `Built 148 published events … ALL LOCAL CATALOG, SOURCE-LINK, AND NAVIGATION CHECKS PASSED`. |
| Every published row has an HTTPS source link | 148/148 at baseline, 151/151 after this session's additions. |
| Source-host audit (93 distinct hosts) | All hosts are organizer, venue, government (`sf.gov`, `sfmta.com`, `presidio.gov`, `sfrecpark.org`, `agu.org`) or the three labeled `sftravel.com` civic rows. No example/placeholder hosts, no dead-domain placeholders in `source_url`. |
| City-only scope | Every published `location` carries a San Francisco indicator; the three known look-alikes outside the city (Great Dickens Christmas Fair at the Cow Palace, SFO programs, Top of the Hill Festival) are excluded, and 17 records are held on Flagged for Review rather than deleted. |
| No inferred optional values | `time_text` and `admission` are blank wherever the captured source was silent; blanks are published as “Not stated”, never as “Free”. |
| Review/flag separation | Review records never render in the city-only tables; every flag row carries its own source links. |
| CI/CD | `.github/workflows/pages.yml` runs `python3 build.py && python3 verify.py` **before** uploading the artifact, so a broken catalog cannot deploy. Left unchanged. |
| Data/export sync | `data/events.csv` is regenerated from `data/events.json` by the build; no hand-edited divergence. |

## 2. Irregularities found, and what was done about each

| # | Irregularity (with evidence) | Severity | Action taken |
| --- | --- | --- | --- |
| R1 | **The dashboard mixed paid events into a section headed “Focus: Free events for Gaming, Music, AI & beyond.”** The generated cards listed Microsoft Ignite (`admission: "Registration required"`), TechCrunch Disrupt (no price published), AI Engineer World's Fair (no price published), Cloudflare Connect (`$595` pass), Current SF and TDX under a free-events heading, and described GDC Festival of Gaming as a gaming highlight while the catalog's own row records “Festival pass $549 early rate … 1-Day Career $125” from <https://gdconf.com/passes-pricing/>. | High — contradicts the brief's free/paid separation | Focus cards are now **generated from the verified dataset** (`build.py:focus_card`): each card lists only rows whose source states free admission, with the sourced cost and official link on every line, plus an explicit count of how many rows in that focus area are paid/registration-only/unpriced and a link to the separate section. No hand-written event claims remain on any page. |
| R2 | **Unverifiable hand-written counts in generated prose.** The dashboard asserted “12 verified 100% free music and performing arts traditions” and “10 enterprise summits”, and gave GDC dates (“March 1–5, 2027”) in prose rather than from the row. The dataset actually holds **13** free/partly-free music rows and **16** technology rows. | High — hallucination risk | All such numbers are removed. Counts on every page are now computed from the dataset at build time, and dates come from the row's own `date_text`. |
| R3 | **The cost classifier inferred a price from gate wording.** `cost_class` counted “registration required” and “invitation only” as `paid`, so Microsoft Ignite, AGU26, Bay to Breakers and the J.P. Morgan Healthcare Conference were labelled “Paid / ticketed” although no linked page states a price. | High — violates “never infer” | New `restricted` class: “Registration / invitation — no price published”, rendered with its own badge, kept out of the free list, and recorded as `flag-registration-only-cost-class` with all four official links. No `admission` text was changed. |
| R4 | **The brief's free-only main section did not exist.** `upcoming.html`, `recurring.html`, `special.html`, `all-events.html` and all nine category pages mixed free, paid and unpriced rows, and there was no paid section page at all. | High — core requirement | New information architecture (see §3): `free.html` is the free-only main list; new `paid.html` is the separate paid & ticketed section; `recurring.html`, `special.html`, `annual-special.html` and every category page now render free rows first and non-free rows in a second, clearly labelled table. |
| R5 | **The executive summary was not free-focused.** The dashboard's “Next up” panel listed the ten nearest events regardless of cost, so a $1,299 conference could headline the summary. | High — core requirement | The executive summary is now free-first: the headline panel lists only free/partly-free upcoming events, the counters count *free* events starting in 7/30/90 days and free programs running now, a separate clearly-labelled panel shows the nearest paid/registration-only/unpriced events, and both panels are recomputed in the browser against the visitor's real current date with `<noscript>` fallbacks. |
| R6 | **`verify.py` and `build.py` disagreed on what “cost not stated” means.** The verifier counted rows with a *blank* `admission` field (75) while the generator counted rows whose *cost class* was not-stated; the standalone fallback classifier inside `verify.py` was also an older copy that returned `paid` for anything not free. | Medium — a guard that could pass a wrong page | Verifier now derives both sets from the imported `cost_class`, the fallback classifier was synced to the new policy, and the two numbers are asserted against the generated pages. |
| R7 | **Row-absence guards were name-substring based and produced false positives.** Two editions share a name (“San Francisco Pride Celebration & Parade” 2026 and 2027), and “Italian Heritage Parade” is a substring of “San Francisco Italian Heritage Parade”, so a name test cannot tell whether a *row* leaked into the wrong section. | Medium — weak guard | Replaced with row-identity checks: every rendered row's `data-name` + `data-daterank` pair is compared as a multiset against the expected free/non-free sets, so `free.html` and `paid.html` are proven to contain exactly the right rows. |
| R8 | **No guard proved the free-first ordering.** Nothing asserted that the free list leads with the requested focus areas, or that each focus block keeps upcoming dates first. | Medium | New checks: `data-focusrank` must be non-decreasing on `free.html`, statuses must be non-decreasing inside each contiguous focus block, and every `paid.html` table must keep upcoming rows first. |
| R9 | **Focus-area coverage gaps were invisible.** The catalog's only free gaming row is a completed edition (Day of the Devs — San Francisco Edition, March 8, 2026), and **no** AI/technology row carries a source-stated free admission (16 rows: 13 priced/registration-gated, 3 unpriced). A reader of the old dashboard would have believed free gaming and AI events were covered. | Medium — honesty of the “free” promise | Two coverage-gap findings added with official links (`flag-free-gaming-coverage-gap`, `flag-free-ai-coverage-gap`), and the dashboard cards state the zero counts explicitly and link to those findings instead of implying coverage. |
| R10 | **Hardly Strictly Bluegrass 2027 dates exist only on aggregators.** Music Festival Wizard and JamBase both list October 8–10, 2027, while the official site fetched on 2026-10-18 still presents the 2026 edition and publishes no 2027 dates. | Medium | No 2027 row added; recorded as `flag-hsb-2027-dates-unconfirmed` with all three links so a human can decide when the official site catches up. |
| R11 | **Two editions of the same annual parade carry different cost evidence.** Italian Heritage Parade 2027 states admission FREE; the 2026 edition row (organizer retrospective) publishes no price — so one edition of the same parade lands in the free list and the other in the non-free section. Same pattern for SF Pride (2026 free/partly free, 2027 unpriced). | Low–Medium | Recorded as `flag-dual-edition-cost-evidence`; no cost was copied between editions because that would be an inference. |
| R12 | **A lead organizer domain would not serve content.** <https://www.shipyardartists.com/shipyard-open-studios/> returned an interstitial “Please wait …” page on 2026-10-18. | Low | The new Shipyard Open Studios row is sourced from the organizer's own official listing plus The Point's official page, and the access problem is recorded as `flag-shipyard-open-studios-source`. |
| R13 | **18 published rows carry no ISO date** (weekly farmers markets, de Young free days, Downtown First Thursdays, Exploratorium After Dark, People in Plazas, Golden Gate Park Band, Merola, Union Square programs). They badged “Date not published” and could not be filtered, even though each row's `date_text` carries the source's own schedule wording (e.g. “Saturday (year-round)”, “First Tuesday of every month”). | Low–Medium | Badge relabelled “Repeating — no single date”, a new **When** filter option isolates them, and their sourced schedule text stays visible in the row. **No next-occurrence date was computed**, because deriving one would put an unsourced value on the page. |
| R14 | **Inline `style="…"` attributes throughout the generated dashboard** (carried over from an earlier session) made the focus cards inconsistent on small screens and unthemeable. | Low | Replaced with real CSS classes (`.focus-grid`, `.focus-card`, `.button`, `.split-head`, `.cost-restricted`), including a mobile pass: the nav becomes a horizontally scrollable pill row under 760 px and the focus grid collapses to one column. |
| R15 | **`README.md` counts were stale** (148 published / 98 recurring / 50 special / 16 review / 34 flags) and it described the old page set. | Low | Rewritten for the new structure and counts (151 / 99 / 52 / 17 / 42). |
| R16 | **`COORDINATION.md` ends with an empty historical section header** — “# Historical coordination — session arena/2088b727-maltaproj7 (2026-10-18)” with no body, so that session's board is only recoverable from git history (PRs #23–#24). | Low — documentation | Noted here and left as-is: inventing or reconstructing another session's board entries would be fabrication. This session's board is prepended above it, with the earlier content untouched. |
| R17 | **Weak field values that are honest but thin**: 7 rows say the venue or hall was not stated by the source (e.g. “Listed on the Moscone Center events calendar, San Francisco (hall not stated)”, “San Francisco, CA (venue not stated on events index)”), and 4 rows carry `organizer: "Organizer not named in source"` (two SFMTA-sourced street events, Cole Valley Street Fair, Clement Street Art Fair). | Low | Left exactly as sourced — filling them would be inference. Listed here for manual review; all 7 vague-venue rows are conferences in the separate non-free section. |
| R18 | **Three published rows rest on SF Travel** (a labeled trusted civic source) rather than an organizer page: Day of the Dead Procession, Illuminate SF, YBG Festival. The Day of the Dead row already carries a flag because the organizer's own site still shows the 2025 edition. | Low | Unchanged and still labeled “Trusted civic source” in every row, per the catalog's stated source policy. |

## 3. Structure of the site after this pass

| Page | Role | Content rule |
| --- | --- | --- |
| `index.html` | Dashboard | Free-first executive summary (live, recomputed against the visitor's date), free-starting-soon panel, a clearly separated paid panel, four dataset-generated focus cards (gaming → music → AI → everything else), metrics, cost legend, findings. |
| `free.html` | **Main section** | Only rows whose source states free or partly free. Ordered gaming → music → AI → everything else, then upcoming dates first, completed editions last. Focus and cost filters. |
| `paid.html` | **Separate section** | Two labelled tables: priced/ticketed/registration-only rows, then rows whose source published no price. Upcoming first. |
| `upcoming.html` | Everything by date | All published rows in one date-ordered list, upcoming first; cost visible on every row; focus filter available. |
| `recurring.html` / `special.html` / `annual-special.html` | Regular patterns vs dated specials | Each page renders its free rows first and its non-free rows in a second table. |
| `categories/*.html` (9) | Subpages by category | Same free-first split, upcoming first, every row source-linked. |
| `all-events.html` | Full list | All 151 rows, searchable, filterable by focus/category/cost/date status, sortable five ways. |
| `flagged.html` | Flagged for Review | 17 review records, 42 field-level flags (each row deep-linkable by flag id), and the 77-row cost-not-stated register. |
| `method.html` | Method & sources | Publish rule, ordering rules, cost policy including the registration-only class, findings, directories, and links to every verification log. |

Post-change counts, all re-derived from `data/events.json`: **151 published rows (99 regularly occurring + 52 special)
across 9 categories; 57 free or partly free (12 of them upcoming); 13 priced/ticketed; 4 registration-or-invitation
only; 77 with no published price; 17 review records; 42 field-level flags; 57 rows still upcoming as of 2026-10-18.**

## 4. Items left for manual review (non-blocking, all published on the Flagged for Review page)

1. `flag-free-gaming-coverage-gap` — no upcoming in-person **free gaming** event in the city could be verified.
2. `flag-free-ai-coverage-gap` — no **free AI** row exists; the two nearest candidates publish no price.
3. `flag-hsb-2027-dates-unconfirmed` — 2027 Hardly Strictly Bluegrass dates are aggregator-only.
4. `flag-dual-edition-cost-evidence` — decide whether completed-edition rows should be retired once a 2027 edition is documented.
5. `flag-registration-only-cost-class` — confirm the new “Registration only” label reads correctly to you.
6. `flag-open-source-ai-cost`, `flag-open-source-ai-awards-time` — the two new AI rows' cost and the one-hour time conflict.
7. `flag-shipyard-open-studios-source` — re-point the source link when `shipyardartists.com` serves content again.
8. R17/R18 above — thin venue/organizer values and the three SF Travel–sourced rows.
