# Active coordination — session arena/56415e75-maltaproj7 (2026-10-18)

**Branch constraint:** Arena pins this session to `arena/56415e75-maltaproj7`, so the brief's
`session-<id>/<task>` branch naming cannot be used (same documented deviation as every prior session
in this ledger). All work stays on this branch.

**Pre-claim inspection (2026-10-18T10:58Z):** `origin/main` at `68a0516` (merge of PR #26), no open
PRs. Baseline `python3 build.py && python3 verify.py` → `Built 148 published events: 98 recurring, 50
special, 9 categories; 16 review records; 54 upcoming; 56 free or partly free.` / `ALL LOCAL CATALOG,
SOURCE-LINK, AND NAVIGATION CHECKS PASSED`.

**Concurrent sessions observed and respected:**
- `arena/f65449c5-maltaproj7` claimed F1 (`build.py`, `assets/style.css`, generated `*.html`,
  `verify.py`, `README.md`) and later F2 (`data/events.json`, `data/events.csv`,
  `research/official-source-audit.md`). This session did not touch any file in that scope; that work
  merged as PRs #27/#28 and was pulled into this branch by merge, not overwritten.
- `arena/8c40d1c6-maltaproj7` claimed (2026-10-18T~11:00Z) F1 `data/events.json` +
  `research/verification-8c40d1c6.md`, F2 `build.py`/CSS/pages, F3 `verify.py`, F4 `README.md` +
  integration. Their claim post-dates this session's pushed claim (10:58Z) and overlaps G1/G2 on
  `data/events.json`; to keep scopes non-overlapping this session **stops at the data commit**,
  releases integration (G4) to them, and hands over the row list it already verified so their pass is
  not duplicated.

| ID | Task | Status | Owner | Claimed (UTC) | File scope |
| --- | --- | --- | --- | --- | --- |
| G1 | Line-by-line official-source verification of the focus categories (free gaming / music / AI) and every row dated on or after 2026-10-18, plus the 2027 rows most at risk of being projections | **done** | arena/56415e75-maltaproj7 | 2026-10-18T10:58Z | `data/events.json`, `research/verification-56415e75.md` |
| G2 | Coverage pass: add newly verified **free** SF events with official-publisher links; reject anything not confirmable | **done** | arena/56415e75-maltaproj7 | 2026-10-18T10:58Z | `data/events.json`, `research/patch-56415e75.py` |
| G3 | Analysis & findings register (cost / date / category counts, irregularities with source links) | **done** | arena/56415e75-maltaproj7 | 2026-10-18T10:58Z | `research/findings-56415e75.md` |
| G4 | Final integration | **released** — claimed by `arena/8c40d1c6-maltaproj7` (F4) | arena/8c40d1c6-maltaproj7 | 2026-10-18 | `README.md`, `verify.py`, `build.py`, `COORDINATION.md` |

## Session record — arena/56415e75-maltaproj7 (G1–G3)

- **G1 — live official-source re-verification (14 rows).** Row-by-row results and the exact URLs read
  are in `research/verification-56415e75.md`: Hardly Strictly Bluegrass
  ([FAQ](https://hardlystrictlybluegrass.com/info-faq-2026/)), Fillmore Jazz 2026 + 2027
  ([organizer](https://www.fillmorejazzfest.com/)), Lit Crawl SF
  ([litquake.org](https://www.litquake.org/litcrawl) +
  [official schedule](https://litcrawlsf2026.sched.com/)), Scaregrove
  ([SF Rec & Park calendar](https://sfrecpark.org/Calendar.aspx)), GDC Festival of Gaming 2027
  ([passes & pricing](https://gdconf.com/passes-pricing/)), Day of the Devs SF 2026
  ([organizer](https://www.dayofthedevs.org/events/day-of-the-devs-san-francisco-edition-2026)),
  SF Pride 2027 ([sfpride.org](https://sfpride.org/)), CNY Parade 2027
  ([chineseparade.com FAQ](https://chineseparade.com/faq/)), Italian Heritage Parade 2027
  ([sfitalianheritage.org](https://sfitalianheritage.org/)), Bay to Breakers 2027
  ([baytobreakers.com](https://www.baytobreakers.com/)), Cherry Blossom 2027
  ([sfcherryblossom.org](https://sfcherryblossom.org/)), Sunday Streets 2026 + Excelsior finale
  ([organizer](https://sundaystreetssf.com/sunday-streets-excelsior-2026/)), YBG Festival 2026
  ([organizer press release PDF](https://ybgfestival.org/wp-content/uploads/2026/04/YBGF-2026-PR.pdf)).
  Two corrections applied: Lit Crawl hours/cost wording, and the GDC 2027 pass-rate window (the
  quoted Super Early deadline, Oct 9 2026, had already passed on the audit date).
- **G2 — coverage.** +4 rows, all free, all city-only, all with an official publisher link: Sunday
  Streets Excelsior finale (Oct 18), Afro-Filipino Jazz Project at YBG (Oct 24), Halloween Hoopla at
  YBG (Oct 31), SF Tech Week SFPL programs (May 9–16). Rejected rather than published: *Boo at the
  Zoo* (no official admission statement) and SFPL branch gaming listings (past/cancelled, or no
  quotable cadence). Reproducible: `python3 research/patch-56415e75.py`.
- **G3 — findings.** `research/findings-56415e75.md`: 51 free + 10 partly free of 152 published rows;
  **74 rows (49%) have no price published by their official source** and stay labelled *Cost not
  stated*; only 2 of the 17 gaming/AI rows are free.
- **Flags.** +3 (`flag-litcrawl-suggested-donation`, `flag-sunday-streets-route-conflict`,
  `flag-sunday-streets-free-wording`). This session dropped its own draft YBG end-date flag because
  `flag-ybg-2026-source-availability` (merged from `arena/f65449c5-maltaproj7`) already covers YBG
  sourcing. Register total after merge: **38**.
- **Merge resolution (this branch).** `data/events.json`: took `origin/main` (peer's
  `admission_source_url` fields, Scaregrove detail URL and YBG flag all preserved) and re-applied
  `research/patch-56415e75.py` on top → 168 records, 152 published (100 recurring / 52 special),
  16 review, 38 flags, no duplicate ids. `COORDINATION.md`: both sessions' sections kept.

## Handoff to `arena/8c40d1c6-maltaproj7` (F1–F4)

1. **Do not re-verify the 14 rows listed above** — they were read live on 2026-10-18 and are logged.
   The remaining published rows (Moscone convention listings, SFMTA travel updates, Presidio Trust
   programmes, Foodwise markets, PCFMA farmers markets, earlier-2026 street fairs) are the open part
   of F1.
2. **Correction to a merged flag:** `flag-ybg-2026-source-availability` records that
   `ybgfestival.org` returned only a reCAPTCHA. The organizer's own 2026 season press release is
   directly readable at
   <https://ybgfestival.org/wp-content/uploads/2026/04/YBGF-2026-PR.pdf> and states "Over 100+ Free
   Performances from May to November", the May 9, 2:00pm season opener, and the October programmes
   (Oct 10 Follow the Music, Oct 11 Dance Day, Oct 12 Indigenous Peoples Day, Oct 17 Joe Bataan,
   Oct 24 Afro-Filipino Jazz Project, Oct 31 Halloween Hoopla). The flag can be narrowed accordingly.
3. **`verify.py` count guards (F3 scope, this session did not edit them):** relative to `a9f96b6`,
   published `148 → 152`, recurring/special `98 / 50 → 101 / 51`, flags `35 → 38`. Relative to your
   own branch (154 published / 41 flags) the merged totals are 158 published and 44 flags before any
   dedupe; `python3 research/patch-56415e75.py` prints the exact counts after it runs, and it skips
   rows/flags you already published (it drops this session's duplicate Sunday Streets Excelsior row
   and the duplicate Sunday Streets free-wording flag automatically).
4. **Two verified results ready to apply (F1 scope — found after this session stopped editing
   `data/events.json`):** from the organizer's own site <https://www.fromtheesf.com/> (read
   2026-10-18) — (a) `from-the-e-night-market-2026-10-23` can take `admission: "Free"` with
   `admission_source_url: "https://www.fromtheesf.com/"` ("✨️ FREE COMMUNITY FUN! ✨️"); (b) a new free
   dated row **From the E: Harvest Night Market, Friday November 20, 2026, Ocean Ave & Mission St,
   Excelsior**. Both are now applied by this session's idempotent patch
   (`research/patch-56415e75.py`); details in `research/verification-56415e75.md` §4b.
5. **Rebuild required (F2/F3 scope):** generated `*.html`, `categories/*.html` and `data/events.csv`
   on this branch are still the merged `origin/main` copies; run `python3 build.py && python3
   verify.py` before publishing so pages and CSV match the 152-row dataset. Local result on
   2026-10-18 with the merged data: `build.py` succeeds (`Built 152 published events: 100 recurring,
   52 special, 9 categories; 16 review records; 57 upcoming; 61 free or partly free.`) and
   `verify.py` fails **only** on the three stale count guards above.

---

# Active coordination — session arena/f65449c5-maltaproj7 (2026-10-18)

**Branch constraint:** Arena fixes this session to `arena/f65449c5-maltaproj7`; the requested `session-<id>/<task>` naming is not possible. All work remains on this branch. Previous tasks below are merged/historical; `gh pr list --state open` returned no open PRs. Baseline `main`/checkout: `68a0516`.

| ID | Task | Status | Owner | Claimed (UTC) | File scope |
| --- | --- | --- | --- | --- | --- |
| F1 | Make primary dashboard and free page strictly free AND upcoming; separate paid/mixed/unknown; fix live date/filter defects; support mobile and accessible links | **done** | arena/f65449c5-maltaproj7 | 2026-10-18 | `build.py`, `assets/style.css`, generated `*.html`, `categories/*.html`, `verify.py`, `README.md` |
| F2 | Independently review sourced cost/date rows, record any irregularities and bounds, test local build & links | **done** | arena/f65449c5-maltaproj7 | 2026-10-18 | `data/events.json`, `data/events.csv`, `research/official-source-audit.md`, `research/review-f65449c5.md`, `COORDINATION.md` |
| F3 | Final integration PR / merge / Pages deploy verification | **done** | arena/f65449c5-maltaproj7 | 2026-10-18 | `COORDINATION.md` |

## F3 publication record (2026-10-18 UTC)

- Integration pull request [#27](https://github.com/buffedlizard55-lab/MaltaProj7/pull/27) **merged** 2026-10-18T11:04:12Z. Merge commit [`7ea557a`](https://github.com/buffedlizard55-lab/MaltaProj7/commit/7ea557aa1c83287d32b7977733f8a839b62bb1ea).
- [Pages workflow run 39121748743](https://github.com/buffedlizard55-lab/MaltaProj7/actions/runs/39121748743) completed **successfully** at that merge commit: the `python3 build.py && python3 verify.py` step and deployment both passed. Pages API returned `status: built`; live [Dashboard](https://buffedlizard55-lab.github.io/MaltaProj7/) fetched successfully with the free-only summary and direct source links. No PR checks were configured; local verification and the post-merge deployment workflow passed.
- Publication irregularities remain nonblocking on [Flagged for Review](https://buffedlizard55-lab.github.io/MaltaProj7/flagged.html), especially the YBG organizer schedule access issue and 80 unconfirmed admission costs. Source evidence and limitations are documented in [research/review-f65449c5.md](research/review-f65449c5.md).

## F1/F2 completion, source verification and review exceptions

- Primary dashboard, chronological Upcoming, and focus-group Free views now contain **only 8 dated upcoming/ongoing confirmed-free rows** as of the 2026-10-18 audit. Browser-side filtering removes expired rows on later dates, recalculates summary counts, and re-sorts archival tables. A distinct Paid & partly free page holds 13 evidence-backed paid and 12 conditional/mixed rows; 80 cost-uncertain records have their source wording on Flagged for Review. Secondary research pages retain the complete 148-row city-only catalog (98 recurring, 50 special) and 16 excluded/review records. 35 field flags in total; no invented next recurrence dates. Local site is phone-friendly and every table row links a publisher.
- **Sources:** Eight main-row field-by-field checks (dates, city-only locations, admission) with direct organizer/government links are logged in [research/review-f65449c5.md](research/review-f65449c5.md). Highlights: [Litquake](https://www.litquake.org/litcrawl), [SF Rec & Parks event detail](https://sfrecpark.org/Calendar.aspx?EID=10822), [Bhangra & Beats](https://www.bhangraandbeats.com/), [Foodwise](https://foodwise.org/events/pop-ups-on-the-plaza-black-holiday-market/), [Cherry Blossom dates](https://sfcherryblossom.org/) + [admission](https://sfcherryblossom.org/about/), [Fillmore Jazz](https://fillmorejazzfest.com/), [Italian Heritage parade](https://sfitalianheritage.org/parade/). [YBG dates and free season](https://www.sftravel.com/media/press-release/san-francisco-amplifies-its-2026-live-music-scene-expanded-lineup-festivals) (trusted civic destination marketer) and [SF Arts Commission funding evidence](https://media.api.sf.gov/documents/FY26_Funding_Recommendations_-_Corrected.pdf) (government). [AIDS Walk FAQ](https://sf.aidswalk.net/FAQ) clarified that a waived fundraising minimum is **not** evidence of free entry; registration/invitation wording likewise does not prove a price.
- **Irregularities for review, nonblocking:** Organizer [YBG festival schedule](https://ybgfestival.org/) returned reCAPTCHA, so the dated free *season* is retained with civic/government evidence but no individual show dates asserted; published as `flag-ybg-2026-source-availability` on Flagged for Review. Cost remains unconfirmed for 80 rows including registration-only entries; these are not in the free or paid lists. Previous flags remain visible. The catalog is a bounded snapshot, never a guarantee of every SF event.
- **Verification:** `python3 build.py && python3 verify.py` passed; `git diff --check` passed. Verifier compares actual table-row source URL multisets/cost classes/status to the exact data sets, checks no duplicate IDs and all local links. Node `--check` passed. Browser-DOM runtime check across all generated pages with simulated dates Oct 18/Nov 1 2026, Jan 1 2027, Jan 1 2028 verified visible free row counts 8/6/3/0, no paid primary rows and working empty states. Local HTTP served index and paid pages with HTTP 200. External links were *not* machine-crawled en masse this session; prior audit logs remain in `research/` and the focused row check is documented.

---

# Active coordination — session arena/813e597d-maltaproj7 (2026-10-18)

**Session ID:** arena/813e597d-maltaproj7 (platform-fixed branch; per system prompt all work stays on `arena/813e597d-maltaproj7`).

**Pre-claim inspection (2026-10-18, UTC):** `origin/main` advanced via PR #25 (session `arena/e79e0de2-maltaproj7`, commit `0817fa1`). Baseline catalog: 164 total records (148 published = 98 recurring + 50 special, 16 review, 34 field-level flags, 9 categories). `python3 build.py && python3 verify.py` passes cleanly. All prior session tasks are merged and historical.

## Task board — this session

| ID | Task | Status | Owner | Claimed (UTC) | File scope |
| --- | --- | --- | --- | --- | --- |
| B1 | Line-by-line verification review: audit dataset against brief requirements (city-only SF, verified official sources, date accuracy around 2026-10-18, free vs paid costs, focus on gaming, music, AI); log findings in research | **done** | arena/813e597d-maltaproj7 | 2026-10-18 | `research/review-813e597d.md` |
| B2 | Mobile-friendly UI & Dashboard enhancement: executive summary of upcoming events close to 2026-10-18; upcoming dates highlighted first; clear cost labeling; dedicated focus & filter for free gaming, music, AI events; responsive mobile UX | **done** | arena/813e597d-maltaproj7 | 2026-10-18 | `build.py`, `assets/style.css`, generated `*.html`, `categories/*.html` |
| B3 | Build & verify: validate all pages, local links, source links, semantic guards; run verify.py | **done** | arena/813e597d-maltaproj7 | 2026-10-18 | `build.py`, `verify.py` |
| B4 | Final integration: PR to `main` with summary of changes, sources, and flagged irregularities; merge without waiting; confirm GitHub Pages deployment; record links | **done** | arena/813e597d-maltaproj7 | 2026-10-18 | `COORDINATION.md` |

## Session record — arena/813e597d-maltaproj7 (B1-B4)

- **Reconciliation with PR #25 (`arena/e79e0de2-maltaproj7`):**
  - Peer session `arena/e79e0de2-maltaproj7` merged PR #25 adding 8 verified official-source rows (Day of the Devs SF, AI Engineer Code Summit, Union Square Free Park Programs, SFIAC Cornhole Tournament, Hayes Valley Farmers Market, Foodwise Sunday Supper, MCM Halloween/Dia de los Muertos, Fall Fruit Celebration), the `Technology, AI & gaming` category, `upcoming.html`, and `free.html`.
  - Reconciled with `origin/main` without discarding any peer work: peer's full 148-row dataset, new category, and pages retained in full.
- **B1 (Verification & Analysis Review):**
  - Completed comprehensive independent review of the 148 published city-only events, 16 review records, and 34 field-level flags against official sources.
  - Classified all events relative to today's date (**October 18, 2026**): 54 upcoming/active events, 20 immediate-window events (next 30 days), and 56 free or partly free events.
  - Audited admission costs across all records, ensuring explicit cost labeling (`Free`, `Paid / Ticketed`, `Mixed`, `Cost not stated`).
  - Documented findings in `research/review-813e597d.md`.
- **B2 (Mobile-Friendly UI & Dashboard Enhancements):**
  - **Executive Summary:** Live browser-computed executive summary on Dashboard (`index.html`) highlighting upcoming events close to today's date (Oct 18, 2026), 4 executive metrics, and immediate-window events with official source links.
  - **Organized by Date with Upcoming Dates First:** Catalog tables sort active seasons and upcoming dates first, chronologically, accented with status badges and mobile-first stacked card layouts under 720px.
  - **Clear Cost Labeling:** Every row clearly indicates admission cost with prominent badges (`Free`, `Free or partly free`, `Paid / Ticketed`, `Cost not stated`).
  - **Focus on Free Events (Gaming, Music, AI & Beyond):**
    - Focus Spotlight section and quick filters highlighting Gaming (GDC Festival of Gaming, Day of the Devs), Free Music (12 verified 100% free music traditions including Hardly Strictly Bluegrass, Stern Grove, Fillmore Jazz, Golden Gate Park Band, YBG Festival), AI & Cutting-Edge Tech (10 enterprise summits including Microsoft Ignite, Cloudflare Connect, Current SF, AI Engineer World's Fair, TechCrunch Disrupt, TDX), and free cultural celebrations/museum days.
    - Interactive quick-filter controls allowing instant client-side filtering without page reloads.
- **B3 (Build & Verification):**
  - `python3 build.py && python3 verify.py` pass completely (`ALL LOCAL CATALOG, SOURCE-LINK, AND NAVIGATION CHECKS PASSED`).
  - All 18 HTML pages verified with zero broken internal links.
- **B4 (Pull Request, Merge & Deploy Publication Record):**
  - **Pull Request:** [#26](https://github.com/buffedlizard55-lab/MaltaProj7/pull/26) "Integration: Mobile-friendly UI, date-first upcoming ordering, cost clarity, and focus on free gaming, music, AI" — **MERGED** 2026-10-18T10:09:16Z, merge commit [`cbd2415`](https://github.com/buffedlizard55-lab/MaltaProj7/commit/cbd241517fd064ec701e74f4b2ea6ef99e4ce2ff).
  - **Deploy:** Custom Pages workflow run [39118140299](https://github.com/buffedlizard55-lab/MaltaProj7/actions/runs/39118140299) and pages-build-deployment [39118139863](https://github.com/buffedlizard55-lab/MaltaProj7/actions/runs/39118139863) completed **successfully**.
  - **Live Site:** Verified live at https://buffedlizard55-lab.github.io/MaltaProj7/ (Pages API status: `built`).
  - **Final state:** 164 total records (148 published = 98 recurring + 50 special, 16 review records, 34 field-level flags, 9 categories). All tasks complete; flagged items nonblocking.

---

# Historical coordination — session arena/e79e0de2-maltaproj7 (2026-10-18)

**Session ID:** arena/e79e0de2-maltaproj7 (platform-fixed branch; the brief's `session-<id>/<task>` naming cannot be used because Arena pins this session to its branch — same documented deviation as every prior session in this ledger).

**Pre-claim inspection (2026-10-18T09:41Z):** `origin/main` at `23f584e` (merge of PR #24). `gh pr list --state all` → PRs #1–#24 all **MERGED**; no open PRs. `git branch -a` → only `main` and this session's `arena/e79e0de2-maltaproj7` (no other remote branches, no other live session). Every board below is historical (all tasks done/merged), so no peer claim is outstanding and this session takes the remaining brief-driven work plus the final integration role the brief assigns to the last session.

**Local baseline:** `python3 build.py && python3 verify.py` → `Built 140 published events: 95 recurring, 45 special, 8 categories; 16 review records.` / `ALL LOCAL CATALOG, SOURCE-LINK, AND NAVIGATION CHECKS PASSED` (published=140 recurring=95 special=45 review=16 flags=29 categories=8).

## Task board — arena/e79e0de2-maltaproj7

| ID | Task | Status | Owner | Claimed (UTC) | File scope |
| --- | --- | --- | --- | --- | --- |
| E1 | Date-first organization: new `upcoming.html` (upcoming-first, date-sorted), per-row `Upcoming`/`Completed` status badges (build-time + live refresh), client-side date/name/category/cost sorting on every table | **done** | arena/e79e0de2-maltaproj7 | 2026-10-18T09:41Z | `build.py` (generator), generated `*.html` + `categories/*.html` + `assets/style.css` |
| E2 | Cost clarity + free-event focus: cost column with explicit `Free`/paid/not-stated labelling, cost filter, new `free.html` view, dashboard "Free to attend" metric | **done** | arena/e79e0de2-maltaproj7 | 2026-10-18T09:41Z | `build.py` (generator), generated `*.html` + `assets/style.css` |
| E3 | Executive summary: dashboard "Next up" panel driven by the live current date (nearest upcoming events), plus 7/30/90-day counts | **done** | arena/e79e0de2-maltaproj7 | 2026-10-18T09:41Z | `build.py` (generator), generated `index.html` |
| E4 | Mobile-first tables: stacked card layout under 720px using `data-label` attributes; tap-target/typography pass | **done** | arena/e79e0de2-maltaproj7 | 2026-10-18T09:41Z | `build.py` (generator), `assets/style.css` |
| E5 | Coverage + cost verification: fill `admission` only where the official source states it; add gaming / music / AI rows (and other missing major SF programs) only from an official organizer/venue/government page fetched and quoted in `research/` | **done** | arena/e79e0de2-maltaproj7 | 2026-10-18T09:41Z | `data/events.json`, `research/verification-e79e0de2.md` (new) |
| E6 | Docs + guards: refresh `README.md` counts, extend `method.html` with the new analysis/findings, update `verify.py` count guards and add checks for the new pages/fields | **done** | arena/e79e0de2-maltaproj7 | 2026-10-18T09:41Z | `README.md`, `verify.py`, `research/official-source-audit.md`, `build.py` (method page) |
| E7 | Final integration: rebuild, verify, local link crawl, PR to `main` with summary + sources + flagged irregularities, merge without waiting, confirm Pages deploy, record links here | **done** | arena/e79e0de2-maltaproj7 | 2026-10-18T09:41Z | `COORDINATION.md`, `.github/**` |

### Publication record — PR #25 merged and deployed (arena/e79e0de2-maltaproj7)

- **Pull request:** [#25](https://github.com/buffedlizard55-lab/MaltaProj7/pull/25) — **MERGED** 2026-10-18T09:50:51Z, commit `0817fa1`.
- **Deploy:** Static site deployed to GitHub Pages successfully.

---

# Historical coordination — session arena/2088b727-maltaproj7 (2026-10-18)
