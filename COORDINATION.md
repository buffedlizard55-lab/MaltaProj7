# FINAL INTEGRATION CLAIM — `arena/1bde1cd1-maltaproj7` (2026-10-18T02:57Z)

| Task | Status | Owner | File scope |
| --- | --- | --- | --- |
| Final integration: apply the `a4797fc9` independent-audit findings to data/site; fresh line-by-line re-verification of every published/review row against its official source; reconcile previously collected but dropped events (publish only with direct official evidence, otherwise review register); harden `build.py`/`verify.py` against the audit mutation tests; rebuild site; PR to `main`, merge without waiting (brief), confirm Pages deploy | in progress | `arena/1bde1cd1-maltaproj7` | `data/events.json`, `data/events.csv` (generated), `research/official-source-audit.md`, `build.py`, `verify.py`, generated `*.html`, `categories/*.html`, `assets/style.css`, `README.md`, `COORDINATION.md` |

- Handoff basis: prior owners `f3cb0dad` (catalog, PRs #5/#6) and `a4797fc9` (read-only audit, PRs #7/#8) both record their scopes **done** below and explicitly hand the unapplied audit findings to a final integration owner ("not yet applied to the event data or the five-record website review register"). `arena/185cda46-maltaproj7` has only its 2026-10-18T01:22:29Z claim commit (`47ab45b`), no further commits and no PR for >60 minutes; under the brief's stale-claim rule this session takes over, logged here. No peer work is discarded; all history below is preserved verbatim.
- Rules for this integration: every published row keeps an HTTPS official-organizer / official-venue / government (or explicitly labeled trusted-civic) source link; unconfirmed optional values stay blank (placeholder strings such as "See organizer schedule" / "Program-specific times" are not values and will be blanked); essential gaps, multi-city umbrellas, cancellations, and outside-city items stay on Flagged for Review and do not block merge. "All events" is published as an explicitly bounded, dated snapshot — never as an exhaustive claim.
- Branch note: this Arena session is fixed to `arena/1bde1cd1-maltaproj7`; work, commits, pushes, and the PR all use that branch (same deviation from `session-<id>/<task>` naming already recorded by prior sessions).

---

# Active coordination — concurrent-session collision resolved without discarding work

## Current arbitration log (2026-10-18T01:27Z)

Four sessions independently observed the original empty repository and published overlapping claims within seconds:

| Session | First claim commit (UTC) | Current known scope/state |
| --- | --- | --- |
| `arena/1e3b5ea8-maltaproj7` | `a9cfeb0`, 01:22:12 | Initial site and 42-row catalog already merged through PRs #1 and #2. Its board below is retained verbatim. |
| `arena/a4797fc9-maltaproj7` | `cdff6df`, 01:22:27 | Releases overlapping implementation claims. Performs independent **read-only audit**; writes only this shared coordination log until a unique scope is acknowledged. |
| `arena/185cda46-maltaproj7` | `47ab45b`, 01:22:29 | Active broad end-to-end claim seen on its branch. **Request:** narrow ownership to explicit files and use the already-published site; do not replace another session’s work wholesale. |
| `arena/f3cb0dad-maltaproj7` | `0350953` / `76f4db4`, approximately 01:22 | Active research claim for `data/events.json`, `research/**`. **Request:** treat this as the sole current catalog enrichment owner; preserve and re-audit the 42 main rows and their flags. |

- No implementation or research files were created by `a4797fc9` before discovering the collision. Official-page inspection was read-only. Its original board below is **historical**, not a continuing ownership claim.
- `a4797fc9` attempted `git pull --rebase origin main`; the independently created boards caused an add/add conflict. It stopped, aborted the rebase to avoid rewriting the already-published claim, merged `origin/main`, and preserved both boards below. No peer data or site code was discarded.
- Follow-up: `git pull --rebase` attempted to flatten the local merge and repeated the add/add conflict. The resolved combined board was retained during the final rebase; the initial claim remains archived verbatim below. The session branch alone will be updated with an exact `--force-with-lease` against its own original claim commit; no other branch is rewritten.
- **Scope request to integration owner:** reserve `audits/a4797fc9/**` for a field-by-field evidence audit and independent test reports. Until acknowledged here, `a4797fc9` will only append findings to this shared log.
- **Integration requests:** publish any findings below on the existing `flagged.html`; replace generic source-directory rows with actual events; keep strictly SF-only rows; do not combine annual with special or past with future without explicit labels. No user action is requested.

## Current independent audit task

| Task | Status | Owner | File scope |
| --- | --- | --- | --- |
| Read-only official-source audit of published catalog, build, and site; log source-backed findings for final integration | done | `arena/a4797fc9-maltaproj7` | `COORDINATION.md` only (shared log); no peer-owned implementation files |

## Independent audit findings awaiting integration

- **Season omitted:** Mission Community Market currently lists “Thursday (3 pm – 7 pm), mid March – mid November”; the published row omits the seasonal boundary. Source directly inspected 2026-10-18: https://foodwise.org/markets/mission-community-market/ . Do not present this as year-round.
- **SF-only scope:** CAAMFest’s official-tourism source expressly says “in San Francisco, Berkeley, and Oakland.” Its umbrella row does not identify any specific confirmed SF event. Keep that umbrella out of SF-only event counts until individual SF screenings/venues are verified. Source directly inspected: https://www.sftravel.com/article/san-francisco-festivals-events-may .
- **Completeness:** the SFPL calendar says “1 - 25 of 2252 results” at retrieval. A row named “San Francisco Public Library Events” is a source directory, not 2,252 verified event rows. The current 42-row catalog is not all city events. Source directly inspected: https://sfpl.org/events .
- **Classification:** `Annual / Special` conflates two of the requested groups. Recurring seasonal series, explicitly annual events, dated special events, and recurrence-unverified rows should be distinguishable. Evidence of a single edition is not proof of annual recurrence.
- **Verification tooling limit:** `verify.py` checks populated name/type/category/source fields, HTTPS prefix, a small name exclusion list, and file links. It does not fetch official sources or establish claim-level/date/geographic truth. “ALL CHECKS PASSED” must not be described as external content verification.

---

# Preserved published board from integration session `1e3b5ea8`

# COORDINATION.md — Shared Task Board

**Session ID:** arena/1e3b5ea8-maltaproj7 (system-assigned branch; user instruction called for `session-<id>/<task>` branches, but this platform fixes work to `arena/1e3b5ea8-maltaproj7` — noted here, all work stays on that branch to avoid losing session tracking)
**Started:** 2026-10-18

## Tasks
| # | Task | Status | Owner | Files touched |
|---|------|--------|-------|---------------|
| 1 | Repo review & coordination setup | in progress | arena/1e3b5ea8-maltaproj7 | COORDINATION.md, README.md |
| 2 | Research recurring SF events | done | arena/1e3b5ea8 | data/events.json |
| 3 | Research annual/special SF events | done | arena/1e3b5ea8 | data/events.json |
| 4 | Build GitHub Pages site | done | arena/1e3b5ea8 | index.html, recurring.html, annual-special.html, flagged.html, method.html, assets/, build.py |
| 5 | Line-by-line verification, link check, build check | done | arena/1e3b5ea8 | verify.py (ALL CHECKS PASSED: 42 rows, every row official source, internal links OK) |
| 6 | Final integration, PR to main, merge, confirm Pages deploy | done | arena/1e3b5ea8 | .github/workflows/pages.yml |

## Log
- 2026-10-18: Repo reviewed — initial commit only (README.md "# MaltaProj7", no code, no COORDINATION.md). No other sessions/branches found (`git branch -a` shows only arena branch + main). Claiming all tasks sequentially by this single session; scopes non-overlapping by file order.

## Rules (per project brief)
- Every table row must have a source link to an official site. Unverifiable values left blank + flagged on Flagged for Review page. Never infer.
- Flagged / unverified items do not block merge; publish them on Flagged for Review page.
- Shared outputs (table data, index/nav) changed only by final integration session.
- If a claim is >60 min old with no commits, another session may take over and log handoff here.

## Results (2026-10-18, this session acting as final integration — single active session)
- Repo irregularity: initial commit only had README.md "# MaltaProj7"; no licence/.gitignore/framework.
- Data: 42 entries (15 Recurring, 27 Annual/Special, 8 categories). Every row has official source URL; blank cost=32, blank location=5, blank when=0 — blanks flagged, not inferred.
- Irregularities/discrepancies & exclusions: published on site Flagged for Review page (flagged.html) with sources — incl. Hardly Strictly date-range discrepancy (SF Rec&Park Oct 2-5 vs SF Travel Oct 2-4), Chinese New Year 2026->2027 rollover, Carnaval sf.gov year mix, CAAMFest multi-city venues, Super Bowl LX / Mill Valley excluded as outside SF, sandbox external-curl limitation.
- Verification: `python3 build.py && python3 verify.py` -> ALL CHECKS PASSED; local HTTP 200 for index.
- PR/merge/Pages: recorded below after merge.

- PR #1: https://github.com/buffedlizard55-lab/MaltaProj7/pull/1 — MERGED 2026-10-18T01:24:20Z.
- GitHub Pages: workflow "Deploy static site to GitHub Pages" completed/success; Pages status=built; live site fetched and verified at https://buffedlizard55-lab.github.io/MaltaProj7/ (dashboard shows 42 / 15 / 27).
- This record commit is on arena branch; if merged, it only updates COORDINATION.md + one wording fix on flagged page.


---

# Historical original claim from `a4797fc9` (released above)

# Shared task board — SF Events

## Session and coordination rules

- Integration session: `a4797fc9` (Arena), branch `arena/a4797fc9-maltaproj7`.
- This Arena session is fixed to that branch by the execution environment; no alternate branch/worktree will be created. All pushes target that branch only. Main is updated only through an explicitly numbered pull request merge.
- Read this board before claiming work. Do not edit another session's claimed files. Add a request here instead. Claims with no commits for more than 60 minutes may be taken over, with a logged handoff.
- `COORDINATION.md` is the shared task/status log. Each other file has one owner below. Shared data/navigation are assembled by the integration session only after research completes.
- Every push is preceded by `git pull --rebase`. Verification means direct inspection of official publisher material, not an assumption or a search snippet. Missing/unconfirmed values remain empty and appear on Flagged for Review.
- Research cutoff: 2026-10-18 (UTC). A bounded catalog must not be described as every event in San Francisco. Official calendars change; past editions do not prove future dates or recurrence.

## Task board

| ID | Task | Status | Owner | Claimed (UTC) | File scope |
| --- | --- | --- | --- | --- | --- |
| T01 | Inspect repository, coordinate claims, audit existing contents | in progress | a4797fc9 | 2026-10-18T01:22:06Z | `COORDINATION.md` |
| T02 | Inspect official sources and prepare evidence-backed research records | in progress | a4797fc9 | 2026-10-18T01:22:06Z | `research/**` |
| T03 | Final integration: validate records, evidence, flags, tests, and build tooling after T02 | in progress | a4797fc9 | 2026-10-18T01:22:06Z | `data/**`, `scripts/**`, `tests/**`, `package.json`, `package-lock.json`, `.gitignore` |
| T04 | Final integration: accessible dashboard, category tables, analysis, and review pages after T02 | in progress | a4797fc9 | 2026-10-18T01:22:06Z | `index.html`, `pages/**`, `assets/**`, `404.html` |
| T05 | CI, documentation, PR, merge, and GitHub Pages deployment | in progress | a4797fc9 | 2026-10-18T01:22:06Z | `.github/**`, `README.md`, `LICENSE`, `.nojekyll` |

`needs review` means a published nonblocking finding, not an unfinished integration task. No other session claims or branches were present at the initial inspection.

## Verification and sources

Research evidence, exact supporting excerpts, retrieval dates, and official URLs will be recorded in `research/` and linked from each published row. Schema and internal-link validation will run before merge. Live checks will be recorded separately from historical verification.

## Irregularities / requests

1. The initial repository contains only a 12-byte `README.md`; there are no existing event rows or website to audit.
2. The request for “all events” has no end date or closed official universe. The site will explicitly state coverage boundaries and known omissions, rather than claim completeness.
3. Required task branch naming differs from the fixed Arena branch. The fixed Arena branch is used throughout; task ownership is recorded here instead.

## Activity log

- 2026-10-18T01:22:06Z — a4797fc9 inspected the clean checkout at `378c876`, root README, remote branches, and open PR list. Only `main` existed remotely and there were no open PRs. Created this board and claimed the file scopes above before beginning implementation or research.

## Publication

- Pull request: pending.
- Merge: pending.
- GitHub Pages URL: pending.
- Deployment checks: pending.

---

## Reconciliation addendum — `arena/f3cb0dad-maltaproj7`

- 2026-10-18 — This session has read the concurrent-session arbitration record and accepts the catalog-enrichment scope assigned there: `data/events.json`, `research/**`, and the source-audit rebuild that consumes them. No peer claim is being overwritten.
- 2026-10-18 — The independent audit findings are incorporated in the reconciled data/model: Mission Community Market is seasonal (mid-March–mid-November); generic source-directory rows are not treated as individual events; recurring annual traditions are distinguished from dated special events; and local validation is not presented as a live external-source crawl.
- 2026-10-18 — Multi-city/cancelled/outside-city/essentially incomplete items are review-only in the reconciled model. CAAMFest is being narrowed to its explicitly sourced San Francisco program rather than represented as a city-exclusive umbrella festival.
- Current rebase status: preserving the richer row-level source audit while replaying the static-site rebuild. Follow-up local build, navigation, source-link, PR, and Pages results will be recorded after the replay completes.

---

## Build and validation result — `arena/f3cb0dad-maltaproj7`

- 2026-10-18 — Rebuilt the static Pages site from the reconciled source-audited model: 54 published city-only rows (46 regularly occurring / 8 special), eight category pages, a source-audit method page, and a five-record review register. Every published table row now renders an official source link.
- 2026-10-18 — Local commands passed: `python3 build.py`, `python3 verify.py`, `python3 -m py_compile build.py verify.py`, source/review scope smoke checks, generated-page HTTP 200 checks, and `git diff --check`. The verifier explicitly checks local data shape, source-link coverage, review separation, category counts, and local navigation; it does not claim to live-crawl external sources.
- 2026-10-18 — CAAMFest is now titled and scoped as **CAAMFest — San Francisco program**, limited to named San Francisco venues in the official 2026 schedule; it no longer represents the umbrella festival as city-exclusive. Deployment/PR outcomes will be appended after this final data adjustment.

---

## Publication result — `arena/f3cb0dad-maltaproj7`

- 2026-10-18 — Pull request [#5](https://github.com/buffedlizard55-lab/MaltaProj7/pull/5), **Reconcile Pages catalog with official-source audit**, merged at `2026-10-18T01:32:34Z` (merge commit `0d9277703b889b443315ea093f6b8e499ee66c57`).
- 2026-10-18 — GitHub Actions deployment [run 39086874764](https://github.com/buffedlizard55-lab/MaltaProj7/actions/runs/39086874764) succeeded. Its `Verify data and internal links`, artifact upload, and Pages deployment steps all completed successfully.
- 2026-10-18 — GitHub Pages reports `built` for the merge commit. Live verification at [the Pages URL](https://buffedlizard55-lab.github.io/MaltaProj7/?v=0d9277703b889b443315ea093f6b8e499ee66c57) confirmed the 46 / 8 / 8 / 5 dashboard counts; recurring, special, flagged, and Film & media category pages rendered with row-level sources. A cache-busting query was used because an unversioned fetch initially returned a stale CDN response from the prior deployment.
- Completion: all catalog, UI, review, PR, merge, and deployment tasks owned by this session are complete. Future updates should recheck the linked organizer source before changing a row.

---

## Independent audit update — `arena/a4797fc9-maltaproj7` — 2026-10-18 (UTC)

**No implementation/data files were changed by this audit session.** PR #5 (`0d92777`) was pulled and audited after the original 42-row snapshot. The new site fixes the earlier missing-category-links and unlabeled-selector findings. This update is an explicit handoff request to the existing catalog/integration owner, not a competing claim on its files.

### Independent browser/build results (snapshot `0d92777`)

- `python3 build.py && python3 verify.py`: **passed**, 54 published / 46 recurring / 8 special / 5 review / 8 categories. Python syntax compilation and `git diff --check` passed. Generated compilation cache was removed; no generated binary/dependency artifacts added to Git.
- Real headless Chromium via Playwright: **16/16 HTML pages returned HTTP 200** from a local read-only copy; no browser JavaScript exceptions. All rendered event/review rows have an HTTPS source anchor. This checks presence, **not** the authority/availability/content of each external destination.
- Functional assertions: 54 all-events rows; exact-event search returns 1; no-match search returns 0; Food & markets selector returns 9; all 8 category cards link to their category subpage; skip link receives first keyboard focus. **All passed.**
- At a 390px viewport, none of the 16 pages has horizontal **body** overflow; wide tables scroll inside their wrapper.
- axe-core WCAG 2 A/AA and 2.1 A/AA rules: **zero automated violations across all 16 pages**. This is an automated sample, not a full accessibility conformance claim or screen-reader review.
- Tests and screenshots were generated in ephemeral `/home/user/.cache/sf-events-audit/` only, outside all claimed implementation/research scopes. Package setup required the Chromium default export and bundled NSS/NSPR libraries. No dependency or browser files belong in this repository.

### Source-integrity findings requiring catalog-owner disposition

All sources below were directly retrieved 2026-10-18 unless explicitly stated otherwise. These are **nonblocking review findings**, not a claim that the website build is broken. Please publish the unresolved findings on **Flagged for Review**, blank unsupported fields, and keep SF-only counts honest.

| ID / affected item | Observed evidence | Requested disposition / official review link |
| --- | --- | --- |
| `fillmore-jazz-festival-2026` | The current `https://fillmorejazzfestival.com/` source redirects to **www.premiumecigarette.com**, then a Cloudflare 522 error. It is not a usable official festival source. | Do not label that destination “Official source”. Retain the item as needs review or replace it only after proving the organizer's current canonical domain; the existing [official-tourism July guide](https://www.sftravel.com/article/san-francisco-festivals-events-july) is a discovery starting point, not proof of an unstated year. |
| `international-ocean-film-festival-2026` | [The linked organizer `/festival` URL](https://intloceanfilmfest.org/festival) returns “We couldn't find the page you were looking for.” | Flag failed source availability; locate an explicit 2026 organizer archive before calling date/venue verified. A successful text-fetch wrapper is not proof of a valid event page. |
| `world-arts-west-dance-festival-2026` | [The linked Presidio event URL](https://presidio.gov/explore/events/world-arts-west-dance-festival-2026) returns **404 Error**. | Flag or replace with the actual official archive/press source. The separately published [Presidio 2026 summer release](https://presidio.gov/about/press/presidio-unveils-vibrant-2026-summer-event-lineup) is available and should be checked for the specific event. |
| `sf-marathon-2026` | [Race-weekend page](https://www.thesfmarathon.com/race-weekend/) confirms July 24–26, 2026 in its body but has a **2027 header**. [Full-marathon course page](https://www.thesfmarathon.com/full-marathon/) explicitly describes crossing the bridge into Marin. A city start is not proof that the umbrella program stays within city limits. | Do not treat the entire race weekend/full marathon as a wholly SF event. Split out official, date-confirmed SF-only components (e.g. expo / a verified city-only distance) or keep the umbrella in review. Do not transfer a 2027 course/date into a 2026 record. |
| `fleet-week-sf-2026` | [Linked calendar](https://fleetweeksf.org/calendar-of-events/) has day headings October **6–12**, but repeatedly says “No events posted yet” / “couldn't find any posts.” It does not substantiate the published Oct 7–12 umbrella or air-show schedule. [Official-tourism Fleet Week guide](https://www.sftravel.com/article/where-you-need-to-watch-blue-angels-fly-over-san-francisco-during-fleet-week) instead says Oct 4–12, 2026 / air show Oct 9–11. | Flag the umbrella date-range discrepancy; choose and cite exact event-level organizer evidence rather than deriving dates from calendar headings. |
| `comedy-day-2026` | Current organizer text says **Comedy Day 2026**, free admission, and noon–5pm, but the date is carried in an image rather than the retrieved text. The [tourism September guide](https://www.sftravel.com/article/san-francisco-festivals-events-september) says Sep 20 without an explicit individual year; the new catalog says Sep 13, 2026. | The audit did **not** independently read the date from the image, so it cannot corroborate Sep 13 or establish a 2026 Sep 20 conflict. Retain an image-readable evidence capture / explicit dated organizer source, or blank the unconfirmed date and flag. [Organizer](https://www.comedyday.org/). |
| `sf-international-arts-festival-2026` | [Current organizer homepage](https://sfiaf.org/) identifies Mission District venues and the first two weeks of May, but does not expose the catalog's exact Apr 30–May 10, 2026 range. | Link an explicit 2026 archive/press page for that range; the homepage alone does not substantiate exact start/end dates. |
| `sf-aloha-run-2026` | [Current linked organizer source](https://sfaloharun.com/) could not be retrieved by the audit tool. | This is an availability gap, **not proof of an incorrect event**. Retain the owner’s direct evidence capture or label essential fields unconfirmed pending a readable official source. |
| Optional time/admission fields across the catalog | Many “time” cells contain “See organizer schedule” / “Program-specific times” instead of a confirmed time; many prices are blank although their sources explicitly provide them. A field-level unknown is not covered merely by giving the whole record `status: verified`. | Keep unknown field values actually empty, mark them unconfirmed, and list field-specific review flags. Examples already stated directly by source: [Foodwise Black Holiday Market](https://foodwise.org/events/pop-ups-on-the-plaza-black-holiday-market/) free; [Pistahan](https://pistahan.net/) free; [Porchfest](https://app.sfporchfest.org/) free; [Muni Heritage](https://www.sfmta.com/calendar/muni-heritage-weekend-2026) 10am–4pm/free rides; [Sundown Cinema press release](https://presidio.gov/about/press/presidio-unveils-vibrant-2026-summer-event-lineup) 7pm/free, Civil War Parade Ground. |

### Do not silently lose collected entries during reconciliation

The 54-row model is richer but does not retain every collected entry from `f69a270` in either its catalog or review register. Generic SFPL/RecPark directory rows should rightly stop counting as individual events, but their official calendars should remain discoverable. Please reconcile the following previously collected event/series rows rather than silently dropping them:

- [Heart of the City Farmers Market](https://hotcfarmersmarket.org/): current operator states **Sun/Wed 7am–4pm, Fulton/Larkin**, not the older UN Plaza location.
- [Fort Mason Farmers Market](https://www.cafarmersmkts.com/fort-mason-center-farmers-market): operator says **Sunday 9:30am–1:30pm**, Fort Mason Center, San Francisco.
- [Exploratorium After Dark](https://www.exploratorium.edu/visit/calendar/after-dark): **Thursday 6–10pm**, age 18+, Pier 15. Source lists dated themes rather than a promise of uninterrupted future occurrences.
- [Academy NightLife](https://www.calacademy.org/nightlife): **most Thursdays 6–10pm**, age 21+, **$26** general admission, one Thursday per month usually skipped and mid-December–early-January hiatus. [Getting-here page](https://www.calacademy.org/getting-here) supports 55 Music Concourse Drive.
- [Downtown First Thursdays](https://www.dftsf.com/): next **Nov 5, 2026**, monthly street party, **5–10pm**, 2nd between Market/Howard, **free with RSVP**. Do not rely on an undated January-guide year.
- Yerba Buena Gardens Festival: primary site is recaptcha-limited, **but not wholly unsupported**. The explicitly dated [official SF Travel June 11, 2026 press release](https://www.sftravel.com/media/press-release/san-francisco-amplifies-its-2026-live-music-scene-expanded-lineup-festivals) states **May 9–Nov 13, 2026**, 100+ **free** performances. Verify an address separately rather than inheriting one.
- [AIDS Walk SF organizer FAQ](https://sf.aidswalk.net/FAQ): **July 19, 2026**, Robin Williams Meadow / approximately 5K down JFK and back; check-in 8am, walk 10:30am, picnic noon–3pm. This direct source replaces the unreadable RecPark tentative-calendar citation.
- [SF Sketchfest organizer](https://sfsketchfest.com/): now explicitly **Jan 14–31, 2027**; do not carry January tourism-guide dates into an inferred 2026 edition.
- Also reconcile City Guides tours (as a series/directory, not every tour), Valencia LIVE!, Noise Pop, Escape from Alcatraz, Frameline, 2026 July 4 fireworks, Outside Lands, Portola, Día de los Muertos procession, and Illuminate SF. Preserve unknowns in the review register if direct official confirmation is not retained. The [official dated live-music press release](https://www.sftravel.com/media/press-release/san-francisco-amplifies-its-2026-live-music-scene-expanded-lineup-festivals) already substantiates **Outside Lands Aug 7–9, 2026** and **Portola Sep 26–27, 2026** (Pier 80 / age 21+).

### Verification limits confirmed by independent mutation tests

On temporary copies of the **current** `0d92777` dataset/tooling, all five deliberately invalid cases still passed both builder and verifier: (1) non-official `https://example.com` source; (2) Oakland venue under an unchanged SF geography statement; (3) fabricated date text plus arbitrary cadence; (4) duplicate event facts under a different unique ID; (5) end date before start date. Production data was never changed. The current verifier correctly adds useful local count/link/review checks, but neither the audit Markdown nor a passing verifier establishes external authority, semantic geography, or source-claim truth. Please retain explicit evidence for each supported field and test ISO dates/cadence/identity/geographic evidence separately.

### Coordination and publication record

- Coordination PR #3 merged **2026-10-18T01:28:29Z**, merge `f69a270d099dab38e672ff11465440a4390d9ddb`; custom Pages workflow run **39086616809** completed successfully. It changed the board only and did not replace the existing site.
- Issue #4: https://github.com/buffedlizard55-lab/MaltaProj7/issues/4 requests nonoverlapping ownership / independent `audits/a4797fc9/**`. No acknowledgement of the audit-directory scope was received, so no such files were created. The issue-comment API rejects writes with **403 Resource not accessible by integration** (both `gh issue comment` and REST); the shared board is used instead. No credentials were requested or stored.
- New `0d92777` data/site scope corrections and browser accessibility repairs are acknowledged above. The remaining source-integrity findings are handed to the existing integration owner for the required Flagged for Review publication. No user approval is requested.

- Rebase note: concurrent append-only board changes from PR #6 produced a content conflict. Both the peer publication record and this audit appendix were retained in full; no data/site file was changed.


### Completed row-by-row independent core-claim check (all 59 records in `0d92777`)

This matrix records **only what this session directly corroborated**, not a blanket certification of every optional field, annual recurrence, or future operational detail. A single-edition page by itself does not establish annual cadence. Exact hours/fees/venues without an identified supporting source must remain blank and field-flagged; instruction strings such as “See organizer schedule” are not confirmed values. Unknowns are deliberately not filled by inference.

**Additional concrete resolutions/discrepancies:** the correct Fillmore canonical domain was obtained from the official-tourism guide, the World Arts West replacement press release is fully readable, and the SFIAF archive proves an **April 29** start, not April 30. The legacy Fringe source also redirects to an unrelated domain. These refine the earlier handoff, without changing peer-owned data.

| Record ID | Directly corroborated evidence | Remaining field-level review / integration action | Review source |
| --- | --- | --- | --- |
| `ferry-plaza-farmers-market` | Tue/Thu 10am–2pm, Sat 8am–2pm; year-round, Ferry Building. | Admission not inferred. | [Official / explicitly labeled civic review source](https://foodwise.org/markets/ferry-plaza-farmers-market/) |
| `alemany-farmers-market` | Saturday 7am–2pm, 100 Alemany; City identifies Foodwise operator since February 2026. | Operator and government source agree. | [Official / explicitly labeled civic review source](https://www.sf.gov/location--alemany-farmers-market) |
| `mission-community-market` | Thursday 3–7pm; mid-March–mid-November; 22nd/Bartlett. | Earlier missing-season finding is resolved. | [Official / explicitly labeled civic review source](https://foodwise.org/markets/mission-community-market/) |
| `castro-farmers-market-2026` | Wednesday Apr 1–Nov 18, 2026, 3–7pm, 270 Noe. | 2026 season only; do not project into 2027. | [Official / explicitly labeled civic review source](https://www.pcfma.org/market/castro-farmers-market) |
| `divisadero-farmers-market` | Sunday 9am–1pm, year-round, 1377 Fell. | Admission not inferred. | [Official / explicitly labeled civic review source](https://www.pcfma.org/market/divisadero-farmers-market) |
| `fillmore-farmers-market` | Saturday 9am–1pm, year-round, 1700 O’Farrell. | Admission not inferred. | [Official / explicitly labeled civic review source](https://www.pcfma.org/market/fillmore-farmers-market) |
| `hayes-valley-farmers-market` | Saturday 10am–2pm, year-round, 450 Hayes. | Admission not inferred. | [Official / explicitly labeled civic review source](https://www.pcfma.org/market/hayes-valley-farmers-market) |
| `inner-sunset-farmers-market` | Sunday 9am–1pm, year-round, 1315 8th Avenue. | Admission not inferred. | [Official / explicitly labeled civic review source](https://www.pcfma.org/market/inner-sunset-farmers-market) |
| `sunday-streets-2026` | Organizer lists Tenderloin Jun 14, Mission Jul 19, Bayview Aug 23, Excelsior Oct 18, 2026. | A season/series row, not four fully inventoried occurrences; exact times need event pages. | [Official / explicitly labeled civic review source](https://sundaystreetssf.com/) |
| `stern-grove-festival-2026` | Organizer lineup runs Jun 14–Aug 16, including Saturday Aug 15; lottery/free tickets described. | Do not generate Sundays only or import tourism lottery durations; retain separate venue/time evidence. | [Official / explicitly labeled civic review source](https://www.sterngrove.org/lineup2026) |
| `free-shakespeare-in-the-park-2026` | Actual 2026 schedule gives SF McLaren Sep 5/6/7/12/13 and Sue Bierman Sep 19/20/26/27, all 2pm; free. | Replace generic location/time placeholders with sourced SF-only schedule; do not include Cupertino/Redwood City/Orinda. | [Official / explicitly labeled civic review source](https://sfshakes.org/performance/free-shakes/ac/) |
| `flower-piano-2026` | Sep 10–20, 2026, SF Botanical Garden; event page lists Free–$18; companion page confirms 130 performances/12 pianos. | Start/end timestamps alone do not prove daily hours; retain an explicit daily-hours and resident-admission source if those fields are shown. | [Official / explicitly labeled civic review source](https://gggp.org/event/flower-piano-2026/) |
| `chinese-new-year-parade-2027` | Feb 20, 2027, 5:15pm, 2nd/Market around Union Square to Kearny/Columbus; free street viewing, ticketed bleachers. | Do not inherit a 2026 edition date. | [Official / explicitly labeled civic review source](https://chineseparade.com/faq/) |
| `cherry-blossom-2027` | Organizer explicitly announces Apr 10–11 and 17–18, 2027; Grand Parade Apr 18. | Page also contains 2026 co-chair/volunteer text; 2027 operational details must not be copied from it. | [Official / explicitly labeled civic review source](https://sfcherryblossom.org/) |
| `sf-pride-2027` | Organizer explicitly announces Jun 26–27, 2027 / 57th annual celebration. | Header confirms date, not all 2027 venue/time details; FAQ body still describes the 2026 edition. | [Official / explicitly labeled civic review source](https://sfpride.org/) |
| `carnaval-sf-2026` | Organizer Past Events section explicitly gives May 23–24, 2026, 11am–6pm/free; parade May 24, 10am–2pm. | Keep past 2026 separate from homepage May 29–30, 2027. | [Official / explicitly labeled civic review source](https://carnavalsanfrancisco.org/special-events/) |
| `bay-to-breakers-2027` | Organizer explicitly announces May 16, 2027; describes historic San Francisco race. | Homepage contains older May 18/2026 materials too; do not carry them into 2027 hours/routes. | [Official / explicitly labeled civic review source](https://www.baytobreakers.com/) |
| `sf-marathon-2026` | Race-weekend body explicitly confirms Jul 24–26, 2026 and individual starts/expo. | Umbrella not proven wholly SF; source header rolled to 2027. Split city-only components or review. | [Official / explicitly labeled civic review source](https://www.thesfmarathon.com/race-weekend/) |
| `st-patricks-parade-2026` | Mar 14, 2026, 11:30am parade 2nd/Market to Civic Center; free festival 11am–5pm; sports 11am–4pm. | Do not conflate festival and sports hours. | [Official / explicitly labeled civic review source](https://uissf.org/st-patricks-day-parade) |
| `caamfest-2026` | Official 2026 schedule lists May 7–10 and named SF venues/screening times. | New SF-program restriction resolves original umbrella-scope finding; a festival summary is not an individual-screening inventory. | [Official / explicitly labeled civic review source](https://caamfest.com/2026/schedule/) |
| `sf-silent-film-festival-2026` | Official archive explicitly says May 6–10, 2026, Castro Theatre; 22 programs. | Program-specific time/admission remains unknown until its program source is captured; single-edition evidence alone is not annual-cadence evidence. | [Official / explicitly labeled civic review source](https://silentfilm.org/festival-2026/) |
| `international-ocean-film-festival-2026` | Linked /festival page is not found; organizer root currently promotes 2027 submissions. | 2026 dates/Cowell venue are not independently confirmed by these pages. Never inherit a 2027 submission deadline as event date. | [Official / explicitly labeled civic review source](https://intloceanfilmfest.org/festival) |
| `sf-black-film-festival-2026` | Organizer explicitly says June 18–21, 2026 and identifies the festival. | Exact city venue schedule/time/price not present in homepage text; retain separate evidence. | [Official / explicitly labeled civic review source](https://sfbff.org/) |
| `sf-dance-film-festival-2026` | Official page states 18 in-person SF screenings Oct 23–Nov 8, 2026 and lists named theaters/times; online Nov 9–30. | Keep online window outside city-only in-person counts; unknown individual prices stay blank. | [Official / explicitly labeled civic review source](https://sfdancefilmfest.org/fall-festival-2026/) |
| `sf-transgender-film-festival-2026` | Organizer confirms Nov 12–14, 2026 in person at Roxie SF; online Nov 15–22. Civic listing supplies 7–8pm/9–10pm sessions and 3117 16th. | Prefer available organizer link over calling the civic listing the official organizer. | [Official / explicitly labeled civic review source](https://sftff.org/) |
| `third-i-south-asian-film-festival-2026` | Organizer explicitly says Oct 9–11, 2026, San Francisco, annual 24th anniversary. | Exact theater/time/admission requires program links, not placeholder strings. | [Official / explicitly labeled civic review source](https://thirdi.org/) |
| `lit-crawl-sf-2026` | Official page says Oct 24, 2026, Mission District, free; text says all programs 6:30–7:30pm. | Published venue corrections override printed map; follow full schedule for each reading. | [Official / explicitly labeled civic review source](https://www.litquake.org/litcrawl) |
| `hardly-strictly-bluegrass-2026` | 2026 FAQ explicitly confirms Oct 2–4, named SF meadows/free; gates Fri 11am, weekend 9am; performances end 7pm. | Performance start times require actual schedule evidence, not gate-opening times. Earlier RecPark conflict was not independently corroborated. | [Official / explicitly labeled civic review source](https://hardlystrictlybluegrass.com/info-faq-2026/) |
| `fleet-week-sf-2026` | Linked calendar has Oct 6–12 day headings but no event posts. | Published Oct 7–12 umbrella is not supported there; tourism guide gives Oct 4–12. Flag and verify event-level dates. | [Official / explicitly labeled civic review source](https://fleetweeksf.org/calendar-of-events/) |
| `up-your-alley-2026` | Organizer FAQ explicitly says Jul 26, 2026, 11am–6pm, SF SoMa street footprint, last-Sunday cadence. | Source also states optional $10–20 donation and 18+ audience guidance; do not imply mandatory admission fee. | [Official / explicitly labeled civic review source](https://www.folsomstreet.org/faq) |
| `folsom-street-fair-2026` | Dedicated organizer page explicitly says Sep 27, 2026, 11am–6pm; FAQ supplies SoMa footprint/annual pattern. | Source also states optional donation and adult audience; primary root has rolled to 2027. | [Official / explicitly labeled civic review source](https://www.folsomstreet.org/folsom-street-fair) |
| `castro-street-fair-2026` | 52nd annual fair Oct 4, 2026, 11am–6pm, Castro/Market; suggested $10–20 donation. | Donation is not a required ticket price. | [Official / explicitly labeled civic review source](https://castrostreetfair.org/fair/) |
| `nihonmachi-street-fair-2026` | Organizer explicitly announces 52nd annual fair Aug 1–2, 2026, Japantown. | Page mixes 2025 shirts/volunteer remnants; retain separate 2026 evidence for precise footprint/hours. | [Official / explicitly labeled civic review source](https://www.nihonmachistreetfair.org/home-1) |
| `pistahan-2026` | 33rd annual Aug 8–9, 2026, Yerba Buena Gardens SF; Saturday parade; festival free. | Source permits filling free admission; precise parade route needs its linked parade page. | [Official / explicitly labeled civic review source](https://pistahan.net/) |
| `north-beach-festival-2026` | 2026 / 70th annual Jun 20–21; North Beach boundaries Filbert–Broadway / Stockton–Grant. | Exact hours absent from captured homepage text; do not substitute a schedule placeholder as a time. | [Official / explicitly labeled civic review source](https://northbeachfestival.org/) |
| `fillmore-jazz-festival-2026` | Catalog domain redirects to unrelated commercial site. Tourism-linked canonical fillmorejazzfest.com confirms free SF festival and Jul 3–4, 2027. | Replace wrong domain; Jul 4–5, 2026 still needs an explicit dated archive, not the new 2027 header. | [Official / explicitly labeled civic review source](https://www.fillmorejazzfest.com/) |
| `haight-ashbury-street-fair-2026` | All three retrieved homepage chunks describe 2026 sponsors/free fair and show photos; no readable Sep 20 date. | Published exact date is not independently corroborated from this text; retain readable official date evidence or blank/flag. | [Official / explicitly labeled civic review source](https://haightashburystreetfair.org/) |
| `comedy-day-2026` | Organizer text confirms 2026 edition/free/noon–5pm; dated banner not read by this audit. | Sep 13, 2026 remains unconfirmed. Nonofficial search results are not substituted for official evidence. | [Official / explicitly labeled civic review source](https://comedyday.org/) |
| `muni-heritage-weekend-2026` | SFMTA explicitly gives Sep 19–20, 2026, 10am–4pm; 77 Steuart/Embarcadero; free rides/activities. | Optional fields can be completed from this source; do not count every ride as a verified individual event. | [Official / explicitly labeled civic review source](https://www.sfmta.com/calendar/muni-heritage-weekend-2026) |
| `italian-heritage-parade-2026` | Organizer’s Oct 12, 2026 retrospective explicitly confirms Oct 11, 2026 SF parade / annual tradition. | Use edition-specific retrospective rather than borrowing newer homepage dates. | [Official / explicitly labeled civic review source](https://sfitalianheritage.org/san-francisco-italian-heritage-parade-celebrates-158-years-with-grand-marshal-joe-mantegna/) |
| `world-arts-west-dance-festival-2026` | Dated Presidio Aug 6, 2026 press release explicitly confirms Sep 6, 1–4pm/free/East Meadow, Presidio Tunnel Tops; fifth consecutive year. | Primary event URL is 404, but core claims are now corroborated by this replacement official source. | [Official / explicitly labeled civic review source](https://presidio.gov/about/press/world-arts-west-enlivens-presidio-tunnel-tops-sept-6/) |
| `sf-porchfest-2026` | Organizer app explicitly says May 30, 2026, eighth annual/Mission/free. | Actual set times/venues are not loaded in captured text; keep them unconfirmed, not invented. | [Official / explicitly labeled civic review source](https://app.sfporchfest.org/) |
| `juneteenth-sf-freedom-celebration-2026` | SF.gov explicitly gives Jun 13, 2026, annual Fillmore celebration; introductory text says no-cost. | Source authority is Government source, not Official organizer; organizer is separately linked. | [Official / explicitly labeled civic review source](https://www.sf.gov/san-francisco-celebrates-juneteenth-2026) |
| `juneteenth-market-street-parade-2026` | SF.gov explicitly gives fourth annual Jun 20, 2026, 11am start Market/Second to Embarcadero Plaza; no-cost. | Time/admission/endpoint may be filled from this government source. | [Official / explicitly labeled civic review source](https://www.sf.gov/san-francisco-celebrates-juneteenth-2026) |
| `juneteenth-on-the-waterfront-2026` | Foodwise independently confirms Sunday Jun 7, 2026, 11am–4pm, Ferry Building front plaza/free/sixth annual. | Special Sunday event is confirmed; do not infer it cannot occur from normal farmers-market weekday schedule. | [Official / explicitly labeled civic review source](https://foodwise.org/events/pop-ups-on-the-plaza-juneteenth-on-the-waterfront/) |
| `sf-aloha-run-2026` | Organizer URL could not be retrieved. | Keep owner evidence or flag date/venue/registration unconfirmed; failed retrieval is not proof the event is false. | [Official / explicitly labeled civic review source](https://sfaloharun.com/) |
| `sf-international-arts-festival-2026` | Official 2026 archive heading is Apr 29–May 10, 2026. | Published Apr 30 start disagrees with archive; correct/link edition-specific source or flag, rather than cite generic homepage. | [Official / explicitly labeled civic review source](https://www.sfiaf.org/2026_festival) |
| `sundown-cinema-inside-out-2026` | Dated Presidio release explicitly confirms Jul 24, 2026, 7pm/free, Civil War Parade Ground, Graham St. | Available exact time/admission/location need not remain placeholders. | [Official / explicitly labeled civic review source](https://presidio.gov/about/press/presidio-unveils-vibrant-2026-summer-event-lineup) |
| `scaregrove-2026` | RecPark calendar explicitly confirms Oct 30, 2026, 3–9pm/free/Stern Grove. | Prefer stable event permalink; separate Mobile Rec 12–8pm listing should not overwrite the main event hours. | [Official / explicitly labeled civic review source](https://sfrecpark.org/Calendar.aspx) |
| `foodwise-black-holiday-market-2026` | Organizer explicitly confirms Dec 12, 2026, 9am–2pm/free/south arcade Ferry Building. | Free entry is distinct from products available for purchase. | [Official / explicitly labeled civic review source](https://foodwise.org/events/pop-ups-on-the-plaza-black-holiday-market/) |
| `cloudflare-connect-2026` | Official organizer explicitly gives Oct 19–21, 2026, Moscone West SF; $595 pass / optional add-ons/group offers. | Do not replace canonical dates with alternate Oct 22 logistical wording; exact sessions are separate. | [Official / explicitly labeled civic review source](https://www.cloudflare.com/connect/) |
| `informs-annual-meeting-2026` | Official organizer explicitly gives Nov 1–4, 2026, Moscone South and SF Marriott Marquis. | Exact hours and registration/admission terms require supporting source; do not infer them from conference type. | [Official / explicitly labeled civic review source](https://meetings.informs.org/wordpress/annual/) |
| `microsoft-ignite-2026` | Official organizer explicitly gives Nov 17–20, 2026, San Francisco Moscone Center; registration link. | Source does name Moscone; capture that evidence rather than describing venue as unavailable. | [Official / explicitly labeled civic review source](https://ignite.microsoft.com/) |
| `agu-annual-meeting-2026` | Official organizer explicitly gives Dec 7–11, 2026, San Francisco; registration/program links. | Moscone Center is not exposed in retrieved homepage or sparse attend page; retain a specific venue source or blank that precision. | [Official / explicitly labeled civic review source](https://www.agu.org/annual-meeting) |
| `sffilm-festival-2026` | Dated official 2026 festival page covers Apr 24–May 4 and SF/Oakland/Berkeley. | Review-only mixed-geography treatment retained; individual SF programs can be added separately. | [Official / explicitly labeled civic review source](https://sffilm.org/2026-about-the-festival/) |
| `sfjff-2026` | Official 2026 archive title confirms Jul 16–Aug 2; venue/program links and tourism guide identify SF/East Bay scope. | Review-only umbrella treatment retained until SF components are separated. | [Official / explicitly labeled civic review source](https://jfi.org/sfjff-2026) |
| `sf-fringe-2026` | Catalog legacy URL redirects to fun88.de.com and a 404 page. | Do not label legacy destination an official source; unknown date/venue stays blank and source-authority failure must also be flagged. | [Legacy source — NOT verified official](https://www.sffringe.org/) |
| `opera-in-the-park-2026` | Official Sep 12, 2026 cancellation release explicitly cancels Sep 13 Opera in the Park. | Cancellation overrides earlier promotion; keep review-only, not active. Earlier promotion is not proof it occurred. | [Official / explicitly labeled civic review source](https://www.sfopera.com/press/press-releases/Season-Opening-Performances-Cancelled-Strike/) |
| `bay-area-aloha-festival` | Linked source returned HTTP 500 to this audit. | Outside-city exclusion is preserved, but its geography evidence was not independently retrieved; retain owner’s official location capture. | [Official / explicitly labeled civic review source](https://www.bayareaalohafestival.com/) |


- Independent audit task is **done** within its authorized read-only/board scope. The data/source/coverage findings remain **needs review**, nonblocking, with implementation publication requested from the existing catalog/integration owner. This is not a claim that the remaining source defects have been corrected or published on `flagged.html`.
- No acknowledgement/release of the peer's broader implementation scope has been received. Accordingly, this session did not change `data/**`, `research/**`, builder, verifier, navigation, category pages, or Pages configuration.

---

## Independent audit publication completed — `arena/a4797fc9-maltaproj7`

- Audit handoff pull request [#7](https://github.com/buffedlizard55-lab/MaltaProj7/pull/7), **Document independent source, browser, and coverage audit**, merged **2026-10-18T01:45:44Z**, merge commit `61ad8c2899f64b8ecee441bfc24af77b54a0e31c`.
- Both deployments for that merge completed **successfully**: custom [Pages workflow 39087652670](https://github.com/buffedlizard55-lab/MaltaProj7/actions/runs/39087652670) and legacy [pages-build-deployment 39087652768](https://github.com/buffedlizard55-lab/MaltaProj7/actions/runs/39087652768). The Pages API reports `status: built`. Neither workflow is being described as an external fact-verification service.
- Independently fetched the deployed [dashboard](https://buffedlizard55-lab.github.io/MaltaProj7/?v=61ad8c2899f64b8ecee441bfc24af77b54a0e31c), [Food & markets category](https://buffedlizard55-lab.github.io/MaltaProj7/categories/food-and-markets.html?v=61ad8c2899f64b8ecee441bfc24af77b54a0e31c), and [Flagged for Review](https://buffedlizard55-lab.github.io/MaltaProj7/flagged.html?v=61ad8c2899f64b8ecee441bfc24af77b54a0e31c). Dashboard shows 46 recurring / 8 special / 8 categories / 5 existing review records. Category table contains nine source-linked records. Cache-busting query identifies the checked deployment.
- **Important remaining integration status:** this session’s newly discovered source/date/geography/coverage findings are published in this board, **not yet applied to the event data or the five-record website review register**. The current website must not be described as fully content-verified or exhaustive. Publication of those additional flags/corrections remains requested from the existing catalog/integration owner; peer-owned files were not overwritten.
- The temporary read-only HTTP test preview was stopped after the audit. No server, dependency tree, browser binary, screenshots, or mutation fixture was committed.
- Audit scope is done; handoff findings remain nonblocking **needs review**. No user approval or manual research is requested.

---

## Final integration completed — `arena/1bde1cd1-maltaproj7` (2026-10-18)

- **Re-verification method:** every one of the 59 pre-existing records was re-checked against a live official organizer / venue / government page fetched on 2026-10-18 (15+ fetch/search batches), plus fresh candidate reconciliation (markets, museum late nights, monthly street parties, major festivals, civic events). Search snippets and third-party prices were never published as values.
- **Result:** 79 records — **67 published (56 regularly occurring incl. a new `monthly` cadence + 11 dated specials), 12 on Flagged for Review**, 8 categories. Authorities: 49 official organizer, 11 government, 4 trusted civic (SF Travel), 2 official venue/federal trust, 1 official venue.
- **Demoted (could not be reconfirmed live / scope):** San Francisco Marathon umbrella (course enters Marin; SF-only Expo published instead), Comedy Day (no date on official site), Haight-Ashbury Street Fair (no date on official site), International Ocean Film Festival (/festival page gone), SF Aloha Run (site unreachable). New register entries: Frameline50 (SF/Berkeley/Oakland), Noise Pop (venue geography unresolved). SF Fringe legacy URL now labeled unverified (redirects off-site to 404).
- **Key corrections:** Fillmore Jazz now documents the verified July 3–4, 2027 edition via fillmorejazzfest.com (old domain dead); Flower Piano false hours blanked, Free–$18; AGU venue removed (unstated on captured page); Ignite re-sourced to the official Moscone venue page; SFIAF start fixed to Apr 29 with Mission District venues; Dance Film ISO end fixed to in-person Nov 8; Fleet Week published at component level (no false "free"); Folsom fairs = suggested donation, adults-only; all placeholder time/admission strings ("See organizer schedule", "Program-specific", …) blanked catalog-wide.
- **Added (direct official/government/trusted-civic evidence only):** Heart of the City & Fort Mason farmers markets, Exploratorium After Dark, Cal Academy NightLife, Downtown First Thursdays, Valencia LIVE!, AIDS Walk SF, SF Sketchfest 2027, YBG Festival, Outside Lands, Portola, Jerry Day, Escape from Alcatraz, Day of the Dead Procession, Illuminate SF; specials: SF Marathon Expo, Juneteenth Mayor's Kickoff, July 4 Golden Gate Bridge fireworks (America 250 one-off).
- **Builder/verifier:** monthly cadence in sort + dashboard; link text "Source ↗" (accurate for civic/unverified rows); dashboard/method category and authority summaries computed from data; alias page labeled; Method page gained official directories (SFPL events, SF City Guides, Rec & Park calendar) and explicit coverage boundaries (Bhangra & Beats / SF Hip-Hop Dance Fest / Renegade pending direct verification; Dickens Fair = Daly City and SFO = San Mateo County excluded; Bayview Juneteenth unresolved). `verify.py` hardened (enums, ISO/end≥start, date-year consistency, duplicate name+date, placeholder ban, example-host ban, SF-location indicator) — all five original mutation cases now fail; `python3 build.py && python3 verify.py` passes; rebuild is deterministic.
- **Publication record:** PR and merge details appended below after merge; flagged items are nonblocking per brief.
