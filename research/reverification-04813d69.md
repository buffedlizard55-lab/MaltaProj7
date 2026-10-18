# Official-source re-verification — session arena/04813d69-maltaproj7

**Date of checks: 2026-10-18 (UTC).** Baseline: `origin/main` at `0fb0c33` (merge of PR #37), 162 published rows (102 recurring, 60 special), 17 review records, 51 field-level flags, 9 categories. `python3 -m unittest discover -s tests -v && python3 build.py && python3 verify.py` passes cleanly on the untouched baseline.

**Verification rule reused from all prior sessions:** a value is written only when the linked official page states it. Where the official page is silent, the field stays blank (rendered as em dash or "Not stated") and a flag records the gap. No inference, no invented dates or prices.

**Honest verification boundary:** this pass is a full structural and local-link re-verification of every published row plus targeted live fetches where the sandbox permits. It is **not** a claim to have re-fetched all 162 official publisher pages in one session. For rows not live-fetched below, the factual evidence remains the quoted official-source text in `research/verification-8c40d1c6.md`, `research/verification-56415e75.md`, `research/reverification-3977d9cb.md` and `research/review-55c5243c.md`. External event details can change; the linked publisher remains the final authority.

---

## 1. Structural re-verification of all 179 records (179 = 162 verified + 17 review)

Performed locally without external fetching:

| Check | Method | Result |
| --- | --- | --- |
| Every published row has an HTTPS `source_url` | `python3 verify.py` + manual iteration over `data/events.json` | **Pass:** 162/162 verified rows have `https://` source; 17 review rows also have `https://` (including the legacy `sffringe.org` flagged as Unverified legacy URL) |
| Every published row has required fields `id, name, bucket, cadence, category, date_text, location, organizer, source_url, source_label, source_authority, status` | `verify.py` required_published set | **Pass:** no missing-field errors |
| No duplicate IDs | `verify.py` set check | **Pass:** 179 unique IDs |
| Verified bucket rule | `status==verified` implies bucket in `{recurring,special}`; otherwise `review` + `review_reason` | **Pass:** 102 recurring / 60 special / 17 review as expected |
| City-only scope: location contains San Francisco indicator | Python scan: every verified `location` contains "San Francisco" | **Pass:** 162/162 contain "San Francisco"; multi-city, outside-city and Bay Area–wide programs are correctly held in review (17 records including `open-source-ai-week-2026` Bay Area–wide, `litquake-2026` multi-city, `bay-area-aloha-festival` outside city, `sffilm-festival-2026` multi-city, `frameline-2026` etc.) |
| Admission cost separation: free main list vs paid/mixed vs not-stated | `build.cost_class` on every `admission` + page identity-set checks in `verify.py` | **Pass:** `free_upcoming`=20 dated free upcoming rows; `paid_rows`=16; `mixed`=12; `not-stated`=78; free list verified to contain exactly the 20 `(name, date-rank)` identities, paid/mixed pages contain exactly their sets, no leakage |
| Date-first ordering: upcoming before undated before completed; chronological inside each group | `build.sort_key` + `verify.py` per-table `data-daterank` monotonicity checks + focus-block checks | **Pass:** all generated pages keep upcoming first, then soonest date; Gaming→Music→AI→Everything else order preserved; per-focus-block upcoming-first invariant holds |
| Every table row has a source link | `source_link_count` guards in `verify.py` (free, paid, review, category pages) | **Pass:** all rendered rows carry `class="source-link"` to the official publisher |
| No inferred optional values | Scan for placeholder fragments (`TBD`, `See organizer`, `To be announced`) + blank admission handling | **Pass:** 73 published rows have blank `admission` rendered as "Not stated"; flagged on Flagged for Review with "Cost not established" table; no placeholder text |
| Local navigation and fragments | `verify.check_internal_links` now validates same-page/cross-page `#fragment` (including percent-encoded), directory index, escape, duplicate IDs, ARIA labels | **Pass:** 11 regression tests + live crawl of all 18 HTML pages pass; no broken local links or missing fragment targets |
| Category and cadence integrity | Counts vs `verify.py` stable guards | **Pass:** 9 categories; recurring cadences 14 weekly, 4 monthly, 10 seasonal, 74 annual |

Counts confirmed by `verify.py` stable guards: `published=162, recurring=102, special=60, review=17, flags=51, categories=9` with authority distribution `Official organizer 105, Government source 22, Official venue 19, Official venue / federal trust 13, Trusted civic source 3`.

---

## 2. Live official-source fetches performed this session

Network policy allows reliable fetches only to a subset of hosts; each fetch below is via the hosted page reader. Failures are recorded, never represented as success.

| # | Publisher URL fetched | Row it supports | Observed text (quoted verbatim) | Disposition |
| --- | --- | --- | --- | --- |
| 1 | https://www.fromtheesf.com/ | `from-the-e-night-market-2026-10-23`, `from-the-e-harvest-night-market-2026-11-20`, `from-the-e-holiday-night-market-2026-12-11` | "Fri, Oct 23 · Excelsior Night Market · Ocean Ave & Mission St"; "Fri, Nov 20 · Harvest Night Market"; "Fri, Dec 11 · Holiday Night Market"; each card/footer says "FREE COMMUNITY FUN!" | Confirms organizer lists three 2026 free night-market editions on Ocean Ave & Mission St. Year not stated on homepage date chip; row years come from event pages. No change. |
| 2 | https://www.fromtheesf.com/events/from-the-e-holiday-night-market | `from-the-e-holiday-night-market-2026-12-11` | "Dec 11, 2026, 4:30 PM – 8:30 PM"; "Ocean Ave & Mission St, San Francisco, CA 94112, USA"; "FREE COMMUNITY FUN!"; "Registration closes Dec 11, 2026 at 7:00 PM" | Confirms date, hours (4:30–8:30 pm), city and free admission for the Holiday edition. Registration close ≠ event end; row keeps 4:30–8:30 pm. No change. |
| 3 | https://sundaystreetssf.com/sunday-streets-excelsior-2026/ (attempt) | `sunday-streets-excelsior-2026`, `sunday-streets-2026` | *Fetch not completed in this pass* — page reader returned no body; prior session `arena/3977d9cb` recorded "Sunday, October 18, 2026 · 11 AM – 4 PM · Mission Street between Geneva Avenue and Theresa Street" from same URL | No independent re-fetch; rely on peer evidence in `research/reverification-3977d9cb.md` and existing `flag-sunday-streets-route-conflict`. No change. |
| 4 | https://ybgfestival.org/wp-content/uploads/2026/04/YBGF-2026-PR.pdf (attempt) | `ybg-festival-2026`, `ybgf-afro-filipino-jazz-project-2026`, `ybgf-halloween-hoopla-2026` | *Not fetched in this pass* — PDF host not in allowlist; peer sessions `arena/56415e75` and `arena/8c40d1c6` recorded "Over 100+ Free Performances from May to November", May 9 opener, and Oct 24 / Oct 31 programs | No independent re-fetch; preserve peer evidence. Row kept as Trusted civic/organizer press release per audit. |

All other free upcoming rows rely on inherited peer evidence documented in `research/verification-8c40d1c6.md` (Sunday Streets season, Foodwise demos, Diplo price wording, etc.), `research/verification-56415e75.md` (YBG Festival, SF Tech Week, From the E) and `research/reverification-3977d9cb.md` (Hunters Point Shipyard, Open Source AI Week, Lower Polk Live). None were altered without a fresh source.

---

## 3. Free upcoming set verified (20 rows = the entire free main catalog as of 2026-10-18)

Every row below has `cost_class == free` and `event_status == upcoming` against `catalog.as_of = 2026-10-18`. All 20 are rendered on `index.html` (dashboard + executive summary + Gaming/Music/AI/Everything else focus blocks), `upcoming.html` (chronological) and `free.html` (by focus). Paid (16), mixed (12) and not-stated (78) rows are **excluded** from those three pages and appear only on `paid.html` or `flagged.html`.

| Row | Date(s) | Cost wording in data | Source host |
| --- | --- | --- | --- |
| `sunday-streets-excelsior-2026` | 2026-10-18 | Free (organizer "fun, free activities") | sundaystreetssf.com |
| `sunday-streets-2026` | 2026-06-14 → 2026-10-18 (season) | Free (same organizer sentence) | sundaystreetssf.com |
| `ybg-festival-2026` | 2026-05-09 → 2026-11-13 (season) | Free | SF Travel trusted civic + YBG press release |
| `from-the-e-night-market-2026-10-23` | 2026-10-23 | Free | sfmta.com + fromtheesf.com evidence link |
| `ybgf-afro-filipino-jazz-project-2026` | 2026-10-24 | Free | ybgfestival.org PDF |
| `lit-crawl-sf-2026` | 2026-10-24 | Free; no RSVP required | litquake.org |
| `scaregrove-2026` | 2026-10-30 | Free | sfrecpark.org |
| `foodwise-demo-sofia-jimenez-2026-10-31` | 2026-10-31 | Free | foodwise.org |
| `ybgf-halloween-hoopla-2026` | 2026-10-31 | Free | ybgfestival.org PDF |
| `hunters-point-shipyard-fall-open-studios-2026` | 2026-10-17 → 2026-10-18 (ends today, so upcoming) | Free admission & parking (optional supporter ticket) | eventbrite.com (Shipyard Trust for the Arts) |
| `bhangra-beats-night-market-2026` | 2026-11-13 | Free | bhangraandbeats.com |
| `from-the-e-harvest-night-market-2026-11-20` | 2026-11-20 | Free | fromtheesf.com |
| `foodwise-demo-ann-evans-brennan-2026-11-21` | 2026-11-21 | Free | foodwise.org |
| `foodwise-demo-anna-voloshyna-2026-12-05` | 2026-12-05 | Free | foodwise.org |
| `from-the-e-holiday-night-market-2026-12-11` | 2026-12-11 | Free | fromtheesf.com |
| `foodwise-black-holiday-market-2026` | 2026-12-12 | Free entry (products available for purchase) | foodwise.org |
| `foodwise-demo-florencia-ramirez-2026-12-19` | 2026-12-19 | Free | foodwise.org |
| `italian-heritage-parade-2027` | 2027-10-10 | Free | sfitalianheritage.org |
| `fillmore-jazz-festival-2027` | 2027-07-03 → 2027-07-04 | Free | fillmorejazzfest.com |
| `cherry-blossom-2027` | 2027-04-10 → 2027-04-18 (parade Apr 18) | Free | sfcherryblossom.org |

Focus grouping for these 20 (per `build.focus_group`): **Gaming 0, Music 4, AI 0, Everything else 16** — rendered honestly as "No dated, free upcoming event in this focus area is confirmed" for Gaming and AI, with coverage-gap flags on Flagged for Review. No paid conference is presented as free.

---

## 4. No data changes in this pass

No `admission`, `date_text`, `time_text`, `location`, `organizer` or `cadence` was altered. Existing flags remain accurate:

- Free gaming gap (`flag-free-gaming-coverage-gap` → `day-of-the-devs-sf-2026` is completed, next announced showcase is online)
- Free AI gap (`flag-free-ai-coverage-gap` → 19 Technology, AI & gaming rows are paid or not-stated)
- From the E cadence inconsistency (`flag-from-the-e-cadence-inconsistency` — three editions carry three different cadence labels)
- Sunday Streets route conflict, Shipyard source interstitial, HSB 2027 dates unconfirmed, Open Source AI cost/time gaps, etc. (all 51 flags preserved)

An idempotent patch is **not needed** for this pass (no rows added). If a future integration needs to replay this verification, the dataset is already at the verified state.

---

## 5. Post-verification gate

```
python3 -m unittest discover -s tests -v  → 11 passed
python3 build.py                           → Built 162 published events: 102 recurring, 60 special, 9 categories; 17 review records; 67 upcoming; 68 free or partly free.
python3 verify.py                          → ALL LOCAL CATALOG, SOURCE-LINK, AND NAVIGATION CHECKS PASSED
```

All generated pages retain: upcoming-first ordering, free-only executive summary, cost badges on every row, Gaming→Music→AI→Everything else focus order, recurring vs special separation, mobile stacked cards, fragment-valid local navigation, and Flagged for Review with review records + field-level flags + cost-not-stated table.
