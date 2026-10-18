# Verification log — coverage-gap closure (arena/2e5715f9-maltaproj7, 2026-10-18)

Scope (claimed in COORDINATION.md as W1–W4): discover **new** free San Francisco events from
official sources, prioritizing the standing `flag-free-gaming-coverage-gap` and
`flag-free-ai-coverage-gap`, plus free music and the thin Nov 2026–Feb 2027 window. Every value in
`research/patch-2e5715f9.py` is quoted from the official page fetched on 2026-10-18 below. Nothing
is inferred; where an official page states no cost, `admission` stays blank and a flag records the
gap. Values that could not be confirmed from an official source are **not** published as verified
rows (see §3 Rejected candidates). Peer session `arena/04813d69-maltaproj7` owns the whole-catalog
re-verification (V1); this log covers only rows discovered or re-checked by this session.

## 1. Published additions (quoted source text)

### 1.1 MAPP — December 5, 2026 edition (Mission Arts Performance Project) — free, music/arts
- **Source (official organizer):** https://mappsf.com/events — fetched 2026-10-18.
- **Quotes:** "December 5th MAPP … Saturday, December 5 @ 12:00PM … Mission District of San
  Francisco , San Francisco … MAPP is a familia, a community and a series of arts, music and
  activist events that has been taking place in the Mission for over 20 years. MAPP is always the
  first Saturday of the month every two months. **MAPP is always free.** … including **free live
  music**, Spoken word, Performance art, Film screenings, BBQ's, garage sales, unorthodox
  conversations and happenings."
- **Fields:** date 2026-12-05 (start 12:00 PM; end time not stated on the listing), location
  "Mission District of San Francisco" (source wording; "several venues as well as public spaces,
  street corners, bart stations, cafes, bars, taquerias, homes"), admission "Free" ("MAPP is always
  free."), cadence bimonthly per the source ("the first Saturday of the month every two months").
  Category **Music & performing arts** on the source's own "arts, music and activist events" and
  "free live music" wording.

### 1.2 Noontime Concerts — weekly Tuesday series (free, classical music)
- **Source (official organizer):** https://noontimeconcerts.org/ — fetched 2026-10-18 (and
  https://noontimeconcerts.org/about/, https://noontimeconcerts.org/concerts/ in search capture).
- **Quotes:** "**Free Live Concert Every Tuesday** … Live Stream Starts at 12:30PM or attend in
  person at **Old St. Mary's Cathedral 660 California Street**"; "**Upcoming Concerts** …
  **11/10/2026** — Angela Lee, Cello and Marc Teicholz, Guitar"; concerts page: "Live weekly
  concerts happen every Tuesday at 12:30 pm at Old Saint Mary's Cathedral. … **Always on Tuesdays
  and always free.**"; About page: "Noontime Concerts are not ticketed but **suggested donations
  are solicited** to ensure all can enjoy performances regardless of ability to pay. … Currently,
  Noontime Concerts are presented **weekly on Tuesdays at 12:30** in historic Old Saint Mary's
  Cathedral **and on one Sunday each month from April through November at the historic San
  Francisco Mint**."
- **Fields:** series row = recurring weekly, dates blank (series publishes no season window);
  edition row `noontime-concerts-2026-11-10` = the next concert actually listed ("11/10/2026
  Angela Lee, Cello and Marc Teicholz, Guitar"). Admission wording "Free concerts; suggested
  donations solicited" — the word "ticketed" is deliberately avoided in the admission field (the
  source's full sentence "are not ticketed" is quoted in notes) so the cost classifier does not
  misread the negation as a ticketed program. Location 660 California Street (source wording).
  Organizer is the 501(c)(3) Noontime Concerts (founded 1988/1989; "now in its 34th year").

### 1.3 The Detour — Free Play Tuesday (free-with-purchase arcade night, gaming)
- **Source (official venue):** https://www.detoursf.com/event/free-play-tuesday/ — fetched
  2026-10-18. Title: "1st Tuesday of the Month Free Play All Day 21+ | The Detour | Restaurant and
  Arcade Bar in San Francisco, CA".
- **Quotes:** "**1st Tuesday of the Month Free Play All Day 21+** — On the 1st Tuesday of every
  month enjoy **all of our arcade games for free with a food or beverage purchase**. Get here
  early before it gets busy since it's the best night in town! **21+ event.**"
- **Fields:** monthly (first Tuesday); specific future dates are **not** published on the official
  page, so `start_date`/`end_date` stay blank per the no-invented-dates policy. Admission text
  carries the condition verbatim ("Free arcade game play with a food or beverage purchase (21+
  event)") and `flag-detour-free-play-condition` records that a reviewer may prefer the
  partly-free class. Street address is **not** published as a confirmed field: the official pages
  fetched name only the venue and city (2200A Market St appears in third-party listings and is
  recorded here, not in the row's location).

### 1.4 The Detour — Tuesday Board Game Night (gaming; cost not stated)
- **Source (official venue):** https://www.detoursf.com/happenings/ — fetched 2026-10-18.
- **Quotes:** "**WEEKLY & MONTHLY EVENTS** — Mondays Super Trashed Bros 7:00-10:00 · Mondays
  Killer Queen League Night Casual Play 7:30-12:00 · 1st Tuesday of the Month Free Play All Day 21+
  · **Tuesdays Board Game Night 7:30-10:00** · 3rd Tuesday --4Play-- Connect 4 Tournament ·
  Wednesdays Drag Bingo Tinsel Tease 7:30-10:00 · 1st WEDNESDAY FLIP' N FIERCE PINBALL TOURNAMENT ·
  Thursdays Trivia Night 7:30-10:00 · Fridays RuPaul's All Stars Viewing Party 7:00-10:00 ·
  Fridays Detour Disco 9:30-Late."
- **Fields:** the page states **no admission cost** for any listed program, so `admission` is
  blank and `flag-detour-weekly-cost-unstated` records the gap (per the brief: never infer).
  The other listed programs are documented in the row's notes rather than given invented costs.

### 1.5 Gaming at The Mix (San Francisco Public Library) — free gaming program
- **Source (government):** https://sfpl.org/teens/the-mix/gaming — fetched 2026-10-18.
- **Quotes:** "**Gaming at The Mix** — Come in and play video games or tabletop gaming with
  friends! Teens can check out controllers with their library card, and our staff will set them up
  with a console. If tabletop gaming is more your style, we offer sessions of D&D led by teen
  interns or professional DMs, along with a wide selection of traditional board games and new RPGs.
  **The Mix also hosts monthly gaming tournaments**, giving you the chance to compete against your
  friends and the librarians." Location from the same official site (https://sfpl.org/teens/the-mix):
  "The Mix at Main … 100 Larkin, 2nd Floor San Francisco, CA 94102 … youth ages 12-18."
- **Cost wording:** the page itself states no cost. SFPL's own events page states "All programs and
  events are free and open to the public" (https://sfpl.org/es/teens/events). That exact sentence
  was captured from the live search index of that SFPL URL on 2026-10-18; the rendered-page fetch
  of the same URL returned navigation-heavy extraction that did not surface the sentence in the
  extracted body text. The row therefore cites it via `admission_source_url` and
  `flag-sfpl-free-statement-capture` tells a human reviewer to re-check the sentence on the live
  page. If a stricter reading is preferred the label can be downgraded to "Not stated".

### 1.6 AI Engineering SF (Latent.Space) — free AI engineering meetup series
- **Source (official organizer registration calendar):** https://luma.com/aieng — fetched
  2026-10-18. Hosted by Latent.Space (swyx et al.) at AWS Builder Loft.
- **Quotes:** "AI Engineering SF: 2026 is the year of ____? … **Friday, January 23** 5:00 PM -
  8:00 PM PST … AWS Builder Loft 525 Market St, San Francisco, CA 94105, USA … **Past Event**
  (This event ended 268 days ago) … if you liked our previous meetup, you'll like this! **we are
  now THE definitive AI Engineering meetup in SF.** … **This is a free event, thanks to AWS for
  the lovely venue!**"
- **Fields:** recurring series; **next edition not posted** on the official page as of 2026-10-18,
  so dates stay blank (no invented occurrence). Admission "Free" from the source's own sentence.
  Location "San Francisco" is the only location that generalizes safely across editions; the
  January 2026 edition's venue is recorded in notes.

### 1.7 AI Tinkerers San Francisco — free-class unstated, high-cadence AI builder meetups
- **Source (official chapter site):** https://sf.aitinkerers.org/ — fetched 2026-10-18.
- **Quotes:** "AI Tinkerers San Francisco is a **hands-on AI builder meetup with live demos,
  technical discussion, and no-pitch networking.** … **Local cadence**: 25 events in the last 12
  months … Format: Live demos, technical Q&A, no sales pitches … Audience: Screened AI builders,
  founders, researchers, and engineers."
- **Fields:** no future edition is posted on the chapter page as of 2026-10-18 (newest posts are
  the September 12, 2026 global hackathon recap and August 26, 2026 demo night), so dates stay
  blank. **Cost stays blank**: some past editions' registration listings expose "$0" general
  admission in their structured data (e.g., luma.com/ai-tinkerers-workshop, ended 2025-07-24), but
  other editions are screened/invite ("You MUST apply here", "Capacity is limited to 80 accepted
  attendees", VIP dinners are "invitation-only"), and no series-level cost statement exists —
  `flag-ai-tinkerers-cost-unstated` records the gap. Adding the row closes none of the cost rules;
  it records a real, high-cadence SF AI program with its official source so the AI section is not
  empty of programs.

### 1.8 New Year's Eve Fireworks on the San Francisco waterfront (annual, free)
- **Source (government — Port of San Francisco):** https://www.sfport.com/blog/nye — captured
  2026-10-18. **Quotes:** "Celebrate New Year's Eve on the Waterfront … **The fireworks show
  begins at midnight and lasts approximately 15 minutes over the Bay.** … The best places to
  watch the show are the areas around the Ferry Building and the open area along the Promenade."
- **Cost wording (labeled trusted civic source, via `admission_source_url`):** Downtown SF
  Partnership — https://downtownsf.org/do/san-francisco-new-years-eve-fireworks-at-midnight:
  "Ring in 2026 with San Francisco's **annual FREE fireworks show over the Bay**." The Port page
  itself states no cost; the cost field therefore cites downtownsf.org and
  `flag-nye-fireworks-edition-unannounced` discloses both the cost-source class and the missing
  2026–27 edition date.
- **Dates:** the official Port page currently describes the December 31, 2025 → January 1, 2026
  edition. **No 2026–27 edition is posted as of 2026-10-18**, so `start_date`/`end_date` stay
  blank per policy (an undated annual tradition is not assigned an invented next occurrence).
  Location from the Port page (waterfront / Embarcadero viewing areas) plus the established launch
  area wording "over the Bay" — no launch-site coordinates published on the Port page.

### 1.9 Review record (not published as verified): Small Change Arcade grand opening
- **Official site:** https://www.smallchangearcade.com/ — fetched 2026-10-18: currently describes
  the mini-cabinet rental business ("$200/hr - 2.5hr min", "All games accept quarters only, no
  free play!") and lists **no storefront events**.
- **Press reports (not official):** Mission Local, 2026-09-25 — "The storefront at 4740 Mission
  Street at Leo … will be having its grand opening on Oct. 16 … A flyer shared via the arcade's
  Instagram … **Admission is free. No reservation or tickets are required.**"
  (https://missionlocal.org/2026/09/excelsior-buzz-the-comic-book-store-is-finally-open-coming-soon-an-arcade/);
  SF Examiner, 2026-10-11 — "Small Change Arcade grand opening (Friday) … Friday's grand opening
  will be held from noon to 3 p.m."
- **Disposition:** held as a `needs_review` record with blank cost and blank dates (the brief:
  values that cannot be confirmed from an official source are left blank and flagged). The event
  already passed (Oct 16, 2026). `flag-small-change-arcade-source` points to both press links and
  the silent organizer site. If the organizer publishes the event, promote with official values.

## 2. Coverage-gap flag dispositions updated (W3)

- `flag-free-gaming-coverage-gap` → **partially closed**. Verified free gaming *programs* are now
  catalogued with official sources (The Detour Free Play Tuesday — "all of our arcade games for
  free with a food or beverage purchase"; Gaming at The Mix at SFPL — free per SFPL's programs
  statement). Neither publishes dated future occurrences, so the dated-free-gaming count on the
  dashboard remains 0 and the honest "no dated, free upcoming event" notice stays. Day of the Devs
  2027 remains unannounced; GDC 2027 remains paid.
- `flag-free-ai-coverage-gap` → **partially closed**. A verified free AI program series (AI
  Engineering SF — "This is a free event") is now catalogued, and AI Tinkerers SF (high-cadence)
  is catalogued with cost unstated. Neither publishes a dated future edition as of 2026-10-18, so
  the dated-free-AI count remains 0 and the notice stays. The Open Source AI Week programs remain
  cost-unstated and stay out of the free section (flag-open-source-ai-cost unchanged).

## 3. Rejected candidates (checked and NOT added — with reasons)

| Candidate | Source checked | Reason rejected |
| --- | --- | --- |
| Akihabara Arcade "SF Mondays" (Street Fighter 3rd Strike "Free to Play") + "Losers Bracket" | akihabaraarcade.com/tournaments-special-events (fetched 2026-10-18) | **Out of city.** The event pages' own map/calendar links give "8901 Harlan Street, Westminster, CO, 80031". "SF Mondays" = Street Fighter Mondays, not San Francisco. Aggregator pages associate it with SF queries; the official page proves otherwise. `flag-akihabara-sf-mondays-out-of-city` records the rejection so no later pass re-adds it. |
| GobbleCon (free tabletop weekend) | gobblecon.com | Burlingame Hyatt Regency SFO — outside city (already cited in flag-free-gaming-coverage-gap). |
| KublaCon Fall 2026 | fancons listing | Burlingame — outside city. |
| California Extreme | caextreme.org | Classic arcade show; venue not in San Francisco (Silicon Valley hotel show). |
| GamesBeat NEXT (Nov 2–3, 2026, Convene SF) | events.gamesbeat.com | Ticketed B2B conference; not free. |
| "Secure Agents Buildathon" / "AIT x Google Cloud NOV 20" banners on sf.aitinkerers.org | sf.aitinkerers.org (fetched) | Both are **past** (buildathon ended December 6, 2025; the Nov 20 banner art belongs to the ended Nov 20, 2025 meetup whose page says "Event Ended"). Not upcoming. |
| AG-UI workshop with AI Tinkerers (Frontier Tower, 995 Market St) | luma.com/ai-tinkerers-workshop (fetched) | Past (July 24, 2025; "This event ended 451 days ago"). Price $0 belongs to that past edition only. |
| AI Tinkerers Humans-in-the-Loop Hackathon (Nov 2–3) | sf.aitinkerers.org post | Recaps/deadlines show 2024 dates ("Nov 3 … past"); not a future edition. |
| Cerebral Valley AI Summit (Nov 12, 2026) | gracker listing | Invite-only per its listing; no public official page stating free admission. |
| TechEquity AI Summit (Nov 3–6) | techequity-ai.org | Snowflake "Silicon Valley AI Hub" — not San Francisco city (and summit days are paid-tier). |
| The Detour weekly programs other than Board Game Night | detoursf.com/happenings/ | No cost stated on the official page; documented inside flag-detour-weekly-cost-unstated and the Board Game Night notes instead of being given invented rows/costs. |
| Emporium SF "Industry Night" 8 free tokens (Mondays) | funcheap snippet only | No official venue page fetched stating the offer; industry-gated; rejected as unverified. |
| "Third Thursdays on Treat" (Nov fair with games) | funcheap snippet only | No official organizer page found; the catalog's `third-thursdays-on-ellis` row is a different program and already needs_review. |
| NYE dinner/party cruises (Luxe, Gatsby, Speakeasy) | luxecruises.com etc. | Paid tickets ($135–$212); correctly belong in the paid section and were not added (the free waterfront show is the public event). |
| SFPL dated gaming events after 2026-10-18 | sfpl.org events search | The Gaming topic listing exists (sfpl.org/events?field_event_topic_target_id=553) but no individual dated post-Oct-18 gaming event page could be confirmed in this pass; each SFPL program is published as its own dated page and none was captured. The standing "Gaming at The Mix" program page is used instead. |
| Small Change Arcade grand opening | smallchangearcade.com (fetched), Mission Local, SF Examiner | Press-only evidence; official site silent (see §1.9) — review record only. |
| "Singing in the Park" Community Party (Nov 14, Mothers Meadow) | funcheap snippet only | No official organizer page found; rejected as unverified. |
| MAPP earlier 2026 editions (Aug 1 etc.) | mappsf.com/events "View previous events" | Past editions not enumerated in this pass; the December 5 listing is the only future edition posted. |
| Noontime Concerts Sunday series at the SF Mint | noontimeconcerts.org/about | "one Sunday each month from April through November" — no specific future Sunday listed on the fetched pages; covered in the series row's date_text/notes, not given an invented date. |

## 4. Machine checks run after the patch

- `python3 build.py` → rebuilt all pages from `data/events.json`.
- `python3 verify.py` → ALL LOCAL CATALOG, SOURCE-LINK, AND NAVIGATION CHECKS PASSED
  (170 published / 109 recurring / 61 special / 18 review / 58 flags) — count guards in
  `verify.py` updated for the new totals in the same commit.
- `python3 -m unittest tests.test_verifier` → offline regression tests pass (no count coupling).
- Row-identity guards (data-name/data-daterank multisets) rebuilt from the generated pages and
  compared against the expected free/paid sets; no leak of not-stated rows into the free main
  section (The Detour Free Play and the new free rows carry sourced "free" wording only;
  cost-unstated rows land on the cost-not-stated register on flagged.html).
