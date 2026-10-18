# Official-source verification log — session `arena/56415e75-maltaproj7` (2026-10-18)

Independent line-by-line verification pass over the published catalog, run on
**2026-10-18 (UTC)** against the live official publisher pages. Every value this
session changed or added is listed below with the URL that stated it. Nothing was
inferred, averaged, or carried over from a secondary listing.

Data touched: `data/events.json` only (via `research/patch-56415e75.py`).
Baseline before this pass: 148 published (98 recurring / 50 special), 16 review
records, 34 flags. After this pass: **152 published (100 recurring / 52
special), 16 review records, 38 flags.**

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

## 3. Rows added this session (all free, all city-only, all officially sourced)

| Row | Date | Cost | Official source |
| --- | --- | --- | --- |
| Sunday Streets — Excelsior Community Block Party (2026 season finale) | Sun Oct 18, 2026, 11 a.m.–4 p.m., Mission St between Geneva and Theresa | Free | <https://sundaystreetssf.com/sunday-streets-excelsior-2026/> |
| Afro-Filipino Jazz Project (Yerba Buena Gardens Festival) | Sat Oct 24, 2026, 2 p.m., Yerba Buena Gardens | Free | <https://ybgfestival.org/wp-content/uploads/2026/04/YBGF-2026-PR.pdf> |
| Halloween Hoopla (Yerba Buena Gardens Festival, 26th annual) | Sat Oct 31, 2026, noon, Yerba Buena Gardens | Free | <https://ybgfestival.org/wp-content/uploads/2026/04/YBGF-2026-PR.pdf> |
| SF Tech Week — San Francisco Public Library programs (2026) | May 9–16, 2026, SFPL Main Library, 100 Larkin St | Free ("All programs are free") | <https://sfpl.org/locations/main-library/bridge-main-5th-floor/sf-tech-week> + <https://sfpl.org/releases/2026-04-24/level-tech-week-san-francisco-public-library> |

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
| `flag-sunday-streets-route-conflict` | Organizer route (Mission St, Geneva ↔ Theresa) differs from the SF Rec & Park calendar's description of the same closed corridor (Mission St, Avalon ↔ Geneva). Organizer wording published. |
| `flag-sunday-streets-free-wording` | The organizer states "fun, free activities", not "free admission". The `Free` label rests on that exact wording. |
| `flag-ybgf-season-end-source` | The November 13, 2026 season end date is sourced from SF Travel, not from the organizer, whose release says only "from May to November" and "NOVEMBER programs to be announced". |

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
- recurring / special `98 / 50 → 100 / 52`
- field-level flags `34 → 38`

Generated pages (`*.html`, `categories/*.html`) and `data/events.csv` also need a
`python3 build.py` rebuild, because `build.py` is in the same F1 scope. With the
counts updated, `python3 build.py && python3 verify.py` passes; run locally on
2026-10-18 the only failures were the three stale count guards above and nothing
else.
