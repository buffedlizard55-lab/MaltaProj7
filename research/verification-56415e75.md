# Official-source verification log — session `arena/56415e75-maltaproj7` (2026-10-18)

Independent line-by-line verification pass over the published catalog, run on
**2026-10-18 (UTC)** against the live official publisher pages. Every value this
session changed or added is listed below with the URL that stated it. Nothing was
inferred, averaged, or carried over from a secondary listing.

Data touched: `data/events.json` only (via `research/patch-56415e75.py`).
Baseline (`origin/main`, `a9f96b6`): 148 published (98 recurring / 50 special), 16
review records, 35 flags. Applied to that baseline this pass yields **152
published (101 recurring / 51 special), 16 review records, 38 flags**; the patch is
idempotent and skips anything a concurrent session has already published, so the
same script re-applied after merging `arena/8c40d1c6-maltaproj7` adds only the rows
and flags that are still missing.

## 1. Method

1. Enumerated every published row from `data/events.json` and grouped it by
   source host (125 unique source URLs across 76 hosts).
2. Re-fetched the official publisher page for the focus categories named in the
   brief (free gaming, free music, AI/technology) and for every row dated on or
   after 2026-10-18, using the live page text as the only authority.
3. Compared the row's `date_text` / `start_date` / `end_date`, `time_text`,
   `location`, `admission` and cadence against that text.
4. Where the official text confirmed the row, the row was left untouched and the
   confirmation is recorded below. Where the official text was more specific than
   the row, the row was narrowed. Where the official text did **not** state a
   value, the value was left blank and an irregularity was filed instead.
5. Cost labels follow the existing house rule: a value is only `Free` when the
   linked official page says so; "no price published" is left blank and listed on
   Flagged for Review, never shown as free.

External fetching from this sandbox goes through the hosted page reader; direct
`curl` to organizer hosts is blocked by the sandbox network policy, so each
confirmation below is a page-read result, not a raw HTTP check.

## 2. Rows re-verified this session (live official pages)

| Row | What was checked | Official source read on 2026-10-18 | Result |
| --- | --- | --- | --- |
| Hardly Strictly Bluegrass | Oct 2–4, 2026; free, no tickets; Hellman Hollow / Lindley / Marx meadows | <https://hardlystrictlybluegrass.com/info-faq-2026/> | Confirmed. Row unchanged. |
| Fillmore Jazz Festival (2026) | July 4–5, 2026; free | <https://www.fillmorejazzfest.com/> | Confirmed (organizer "Thank you for an amazing 2026!" recap). Row unchanged. |
| Fillmore Jazz Festival (2027) | July 3–4, 2027; free | <https://fillmorejazzfest.com/> | Confirmed — organizer homepage states "Saturday & Sunday, July 3 & 4, 2027" and "keep the festival free and accessible to everyone". Row unchanged. |
| Lit Crawl SF | Date, hours, cost | <https://www.litquake.org/litcrawl> and <https://litcrawlsf2026.sched.com/> | Date confirmed (Oct 24, 2026). **Hours corrected** to 5:00–9:00 p.m. with the 6:30–7:30 p.m. per-program window; **cost** confirmed free and "no RSVPs are necessary". New flag for the suggested-donation wording. |
| Scaregrove | Oct 30, 2026, 3–9 p.m., Sigmund Stern Grove, free | <https://sfrecpark.org/Calendar.aspx> | Confirmed verbatim ("Free Halloween fun for the entire family!"). Row unchanged. |
| GDC Festival of Gaming 2027 | Dates, venue, pass prices | <https://gdconf.com/passes-pricing/> | March 1–5, 2027 at Moscone Center confirmed. **Admission text refreshed** to the currently advertised Early Rate window (deadline Fri Dec 11, 2026); the Super Early window quoted in the old text closed Oct 9, 2026, i.e. before today. Full five-tier rate table recorded in the row notes. |
| Day of the Devs — SF Edition 2026 | Date, hours, venue, cost | <https://www.dayofthedevs.org/events/day-of-the-devs-san-francisco-edition-2026> and <https://www.dayofthedevs.org/events> | Confirmed: "8 Mar 2026 • 3pm to 8pm", The Midway, 900 Marin Street; "Admission is always free, for developers and players alike, and open to all ages." **Time filled** (was blank). |
| San Francisco Pride 2027 | June 26–27, 2027 (57th annual) | <https://sfpride.org/> | Confirmed — organizer banner "June 26-27, 2027 • 57th Annual Celebration & Parade". Row unchanged. |
| San Francisco Chinese New Year Parade 2027 | Feb 20, 2027, 5:15 p.m., free to attend, bleachers ticketed | <https://chineseparade.com/faq/> | Confirmed verbatim, including "It is a free event for all to attend but tickets must be purchased to sit in the bleacher sections." Row unchanged. |
| San Francisco Italian Heritage Parade 2027 | Sunday, October 10, 2027 | <https://sfitalianheritage.org/> and <https://sfitalianheritage.org/explorers/> | Confirmed ("High Mass & Italian Heritage Parade – Sunday, October 10, 2027"). Row unchanged. |
| Bay to Breakers 2027 | Sunday, May 16, 2027 | <https://www.baytobreakers.com/> | Confirmed ("Join the legendary Bay to Breakers in San Francisco on May 16, 2027!"). Row unchanged. |
| Northern California Cherry Blossom Festival 2027 | April 10–11 and 17–18, 2027; Grand Parade April 18 | <https://sfcherryblossom.org/> | Confirmed verbatim on the organizer homepage ("60th Anniversary Celebration! April 10-11 and 17-18, 2027 / Grand Parade (April 18)"). Row unchanged. |
| Sunday Streets SF — 2026 season | Excelsior finale Oct 18, 2026 | <https://sundaystreetssf.com/sunday-streets-excelsior-2026/> and <https://sfrecpark.org/Calendar.aspx> | Confirmed by organizer and by the city calendar. **Cost label set to Free** on the stated wording basis; two flags filed (free wording, route discrepancy). |
| YBG Festival (Yerba Buena Gardens Festival) 2026 | Free season, May opening, October programmes | <https://ybgfestival.org/wp-content/uploads/2026/04/YBGF-2026-PR.pdf> | Organizer's own press release confirms the 26th free season ("Over 100+ Free Performances from May to November") and the May 9 opener. **Notes updated** to cite the organizer directly; the November 13 end date remains sourced only from SF Travel and is now flagged. |
| SF Sketchfest 2027 | January 14–31, 2027 | <https://sfsketchfest.com/> | Confirmed — organizer homepage: "returns to celebrate our 24th year January 14 - 31, 2027!". Row unchanged. |

## 3. Rows added this session (all free, all city-only, all officially sourced)

| Row | Date | Cost | Official source |
| --- | --- | --- | --- |
| Afro-Filipino Jazz Project (Yerba Buena Gardens Festival) | Sat Oct 24, 2026, 2 p.m., Yerba Buena Gardens | Free | <https://ybgfestival.org/wp-content/uploads/2026/04/YBGF-2026-PR.pdf> |
| Halloween Hoopla (Yerba Buena Gardens Festival, 26th annual) | Sat Oct 31, 2026, noon, Yerba Buena Gardens | Free | <https://ybgfestival.org/wp-content/uploads/2026/04/YBGF-2026-PR.pdf> |
| SF Tech Week — San Francisco Public Library programs (2026) | May 9–16, 2026, SFPL Main Library, 100 Larkin St | Free ("All programs are free") | <https://sfpl.org/locations/main-library/bridge-main-5th-floor/sf-tech-week> + <https://sfpl.org/releases/2026-04-24/level-tech-week-san-francisco-public-library> |
| From the E: Harvest Night Market (Excelsior) | Fri Nov 20, 2026, Ocean Ave & Mission St | Free ("FREE COMMUNITY FUN!") | <https://www.fromtheesf.com/> |

Plus one **cost fill** on an existing row: `from-the-e-night-market-2026-10-23` was published with a
blank admission and "Organizer not named in source" because it was built from the SFMTA travel update.
The organizer's own site states the programme "means free community fun" and lists the October 23
edition as "✨️ FREE COMMUNITY FUN! ✨️", so the row now carries `admission: Free` with
`admission_source_url: https://www.fromtheesf.com/` and the organizer name; SFMTA remains the source
for the date, hours and street footprint.

**Deduplicated against a concurrent session.** This session also prepared a dated row for the Sunday
Streets Excelsior finale (Oct 18, 2026). `arena/8c40d1c6-maltaproj7` published the same event as
`sunday-streets-excelsior-2026` from the same organizer page, so this session's duplicate row is not
added; the patch skips it by name. The same applies to the Sunday Streets "free wording" flag, which
that session filed as `flag-sundaystreets-free-wording`.

Candidates that were **rejected** rather than published: *Boo at the Zoo*
(SF Recreation and Park calendar, Oct 31) was not added because no official page
states an admission price and the event sits behind zoo entry; SFPL branch gaming
programmes (e.g. *Social: Game Night*) were not added because the individual
listings found were in the past or cancelled and the standing
[Gaming at The Mix](https://sfpl.org/teens/the-mix/gaming) page publishes no
schedule that could be quoted as a cadence.

## 4. Irregularities found and filed

| Flag | Finding |
| --- | --- |
| `flag-litcrawl-suggested-donation` | Litquake's festival listing labels Lit Crawl "FREE, $10-15 suggested donation" while the crawl's own pages present it as free with no RSVP. Cost label stays `Free`; the wording is documented. |
| `flag-sunday-streets-route-conflict` | Organizer route (Mission St, Geneva ↔ Theresa) differs from the SF Rec & Park calendar's description of the same closed corridor (Mission St, Avalon ↔ Geneva). Organizer wording published. Attaches to `sunday-streets-excelsior-2026`, so it only lands once that row exists in the merged data. |
| `flag-from-the-e-general-hours-mismatch` | The organizer's general "second Saturday, 5–10 p.m." wording contradicts the Friday dates and SFMTA's 4:30–8:30 p.m. hours for the 2026 editions; no hours are published for the November 20 edition. |
| `flag-sunday-streets-free-wording` | The organizer states "fun, free activities", not "free admission". Dropped automatically when a peer session's equivalent flag (`flag-sundaystreets-free-wording`) is present. |

## 4b. From the E — organizer-site evidence (applied)

Both results below come from the organizer's own site, <https://www.fromtheesf.com/>, read on
2026-10-18, and are applied by `research/patch-56415e75.py`:

1. **Cost fill — `from-the-e-night-market-2026-10-23`.** The row's admission was blank and its
   organizer read "Organizer not named in source" because the row was built from the SFMTA travel
   update. The organizer's site states the programme "means free community fun" and lists
   "From the E: Fall Festival Night Market — Fri, Oct 23 — Ocean Ave & Mission St — ✨️ FREE COMMUNITY
   FUN! ✨️". Suggested fill: `admission: "Free"`,
   `admission_source_url: "https://www.fromtheesf.com/"`, organizer "From the E Excelsior Night
   Market". SFMTA remains the source for the date, hours and street footprint.
2. **New free row — From the E: Harvest Night Market.** The same organizer page lists
   "From the E: Harvest Night Market — Fri, Nov 20 — Ocean Ave & Mission St — ✨️ FREE COMMUNITY
   FUN! ✨️". Added as a dated free row for **Friday, November 20, 2026** at Ocean Avenue & Mission
   Street, Excelsior. No hours are published for that edition, so `time_text` stays blank rather than
   borrowing the organizer's general monthly wording ("the second Saturday of the month from 5pm
   -10pm"), which does not match a Friday date — the mismatch is filed as
   `flag-from-the-e-general-hours-mismatch`.

## 5. Honest coverage statement — what this pass did **not** re-fetch

This session re-fetched official pages for the rows above (the brief's focus
categories plus every row dated on or after 2026-10-18, plus the future-dated
2027 rows most at risk of being projections). The remaining published rows —
principally the recurring Moscone Center convention listings, SFMTA travel
updates, Presidio Trust programmes, Foodwise market events, PCFMA farmers markets
and the annual street fairs dated earlier in 2026 — were **not** re-fetched in
this pass. Their last live re-verification is recorded in
`research/verification-e79e0de2.md`, `research/reverification-2088b727.md`,
`research/verification-e969f4df.md` and `research/reverification-55c58947.md`,
and their source links are unchanged. They are carried forward as previously
verified rather than presented as re-verified today.

## 6. Handoff note for the integration session

`verify.py` carries hard-coded audit counts and is inside the file scope claimed
by session `arena/f65449c5-maltaproj7` (task F1), so this session did not edit
it. The guards must be updated when this data lands:

- published rows `148 → 152`
- recurring / special `98 / 50 → 101 / 51`
- field-level flags `35 → 38`

Generated pages (`*.html`, `categories/*.html`) and `data/events.csv` also need a
`python3 build.py` rebuild, because `build.py` is in the same F1 scope. With the
counts updated, `python3 build.py && python3 verify.py` passes; run locally on
2026-10-18 the only failures were the three stale count guards above and nothing
else.
