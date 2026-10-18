# Independent line-by-line verification log — session `arena/e969f4df-maltaproj7`

**Audit date:** 2026-10-18 (UTC). **Auditor:** session `arena/e969f4df-maltaproj7` (task V1/V2).
**Method:** every cited source URL below was fetched directly from the publisher (official organizer, official
venue, government source, or explicitly labeled trusted civic source) during this session, and the row's
published fields were compared with the wording actually present in the fetched page. Quoted evidence is
copied from the fetched text. Nothing is marked PASS without an inspected page.
**Scope discipline:** this session is read-only on `data/events.json`, `build.py`, `verify.py` and the generated
pages, because concurrent sessions `arena/5e333a6e-maltaproj7` and `arena/646f6727-maltaproj7` claimed those
files at 2026-10-18T05:47Z. Corrections found here are handed to the integration owners as source-linked
requests in `COORDINATION.md` instead of being applied to shared files.

Verdicts: **PASS** = published fields match the live official source. **PASS·GAP** = fields match, but the live
source now states an optional value the row leaves blank (or the row's note is stale). **FAIL** = a published
value contradicts the live official source and must be corrected or blanked.

---

## Part 1 — upcoming / ongoing published rows (the rows a reader can still attend)

These are the 22 published rows whose ISO end date is on or after 2026-10-18, checked first because they carry
the most user-facing risk.

### 1. Sunday Streets SF — 2026 season (`sunday-streets-2026`) — **PASS**
- Source fetched: https://sundaystreetssf.com/ (Official organizer)
- Evidence: “**Sunday Streets 2026** … Sunday Streets SF is preparing for its 18th season!” and “#### 2026 Events —
  Tenderloin • June 14th … Mission • July 19th … Bayview • August 23rd … Excelsior • October 18th”.
- Row: `date_text` = “Tenderloin Jun 14; Mission Jul 19; Bayview Aug 23; Excelsior Oct 18, 2026”; ISO
  2026-06-14 → 2026-10-18; `location` = “Tenderloin, Mission, Bayview, and Excelsior, San Francisco”.
- Optional fields: the page states no hours and no admission, so the row's blank `time_text`/`admission` are correct.

### 2. Cloudflare Connect (`cloudflare-connect-2026`) — **PASS·GAP**
- Source fetched: https://www.cloudflare.com/connect/ (Official organizer)
- Evidence: “Connect2026 — **Oct 19-21 · Moscone West, SF**”; “Conference Pass **$595**”; “Cloudflare University
  **+$495** … Sold out”; “Group and team passes **$495** … Per pass for groups of 5-9. Groups of 10+ get 50% off.”
- Row: dates, venue and all three admission figures match the live page exactly.
- GAP: the row leaves `time_text` blank and its `notes` say “session times were not stated in captured text”, but
  the live page now publishes an “Agenda at-a-glance” with times (Day 1 Registration 8AM–7PM, Welcome Reception
  5PM–7PM; Day 2 Registration 7AM–6PM, Opening General Session 8:30AM–10:15AM, Expo Hall 8AM–5PM; Day 3
  Registration 7AM–5:30PM, General Session 9AM–10:15AM). Request: fill `time_text` from that agenda and drop the
  stale note; also note Cloudflare University is sold out.

### 3. Lit Crawl SF (`lit-crawl-sf-2026`) — **PASS·GAP**
- Source fetched: https://www.litquake.org/litcrawl (Official organizer, Litquake)
- Evidence: “# **OCTOBER 24, 2026** … a massive, one-night literary pub crawl through San Francisco's **Mission
  District** that caps off our annual Litquake Festival … the world's largest **free** pop-up literary event …
  **all programs from 6:30—7:30 PM**”.
- Row: date, Mission District location and `admission` = “Free” all match.
- GAP: `time_text` = “Programs include 6:30pm–7:30pm; **see full schedule**”. The second clause is a pointer, not a
  sourced value, and the official wording is stronger than “include”: all programs run 6:30–7:30pm. Request:
  `time_text` = “All programs 6:30pm–7:30pm”. (The organizer also lists three post-print venue changes — Blondie's
  Bar, Latin American Club, Et al — which do not affect the published row.)

### 4. San Francisco Dance Film Festival (`sf-dance-film-festival-2026`) — **PASS·GAP**
- Source fetched: https://sfdancefilmfest.org/fall-festival-2026/ (Official organizer)
- Evidence: “returns this fall for its **seventeenth year** … **Eighteen in-person screenings take place October
  23-November 8** at venues throughout San Francisco … the **Online Festival runs November 9-30**.” Schedule
  at-a-glance names Lucasfilm Premier Theater (Fri Oct 23, 7:00PM), Delancey Street Theater (Oct 28–30),
  Catharine Clark Gallery (Wed Nov 4, 7:00PM), **SHACK15 (Thu Nov 5, 7:00PM)**, Brava Theater (Nov 6–8), and marks
  the Nov 7 10:30AM Filmmaking Masterclass “(free!)”.
- Row: `date_text` “October 23–November 8, 2026 (in-person); November 9–30 online”, venue list and the SHACK15
  Marin-County caveat all match the live page; keeping admission blank is correct because ticketing is
  per-program.
- GAP: per-screening times ARE published (7:00PM opening night, 6:30PM/8:00PM Oct 28, etc.), so `time_text` could
  carry “Screening times vary by program; opening night Oct 23 at 7:00pm” only if the integration owner wants a
  partial value — otherwise leave blank. No correction required.

### 5. INFORMS Annual Meeting (`informs-annual-meeting-2026`) — **PASS**
- Source fetched: https://meetings.informs.org/wordpress/annual/ (Official organizer)
- Evidence: “Welcome to the **2026 INFORMS Annual Meeting in San Francisco** … **November 1-4, 2026  San
  Francisco, CA** … Join us at the **Moscone Center South & Marriott Marquis San Francisco**”.
- Row: dates, both venues, organizer match. `time_text`/`admission` blank — the page states no schedule times and
  no registration price, so blanking is correct (no inference).

### 6. San Francisco Transgender Film Festival (`sf-transgender-film-festival-2026`) — **PASS**
- Source fetched: https://sftff.org/festival/2026-festival-schedule/ (Official organizer)
- Evidence: “Program 1: Comedy — **November 12, 2026 at 7pm**”; “Program 2: Documentary — November 12, 2026 at
  9pm”; “Program 3: Horror — November 13, 2026 at 7pm”; “Program 4: Grab Bag — November 13, 2026 at 9pm”;
  “Program 5: Speculative Fiction — November 14, 2026 at 7pm”; “Program 6: Adult (18+) — November 14, 2026 at
  9pm”; “GETTING TO THE **ROXie THEATER**”.
- Row: `date_text` “November 12–14, 2026”, `time_text` “7pm and 9pm programs”, `location` “Roxie Theater, San
  Francisco” all match. `admission` blank is correct — the page links to ticketing but states no price.

### 7. Castro Farmers' Market (`castro-farmers-market-2026`) — **PASS**
- Source fetched: https://www.pcfma.org/market/castro-farmers-market (Official organizer, PCFMA)
- Evidence: “Castro Farmers' Market — **270 Noe St., San Francisco, California** — **Wednesdays — 3:00 pm - 7:00
  pm — April 1st 2026 - November 18th 2026**”.
- Row: season dates, weekday, hours and street address match exactly. `admission` blank is correct (PCFMA states
  no entry fee on this page).

### 8. Foodwise Black Holiday Market (`foodwise-black-holiday-market-2026`) — **PASS**
- Source fetched: https://foodwise.org/events/pop-ups-on-the-plaza-black-holiday-market/ (Official organizer)
- Evidence: “**Saturday, December 12, 2026, 9:00 am - 2:00 pm** … The **south arcade of the Ferry Building** will be
  transformed for a special holiday market … **Entry is free and open to the public, with products available for
  purchase.**”
- Row: date, hours, location and `admission` = “Free entry (products available for purchase)” all match verbatim.

### 9. Day of the Dead (Día de los Muertos) Procession (`day-of-the-dead-procession-2026`) — **PASS·FLAG**
- Cited source fetched: https://www.sftravel.com/article/san-francisco-festivals-events-november (Trusted civic source)
- Evidence: “**Day of the Dead Procession — Mission District** … Day of the Dead processions and the Festival of
  Altars are annual community events celebrating the traditions of Dia de los Muertos in the Mission District.
  **November 2, 2026.**” (page also carries the disclaimer “All dates and locations are subject to change and
  should be confirmed with sponsors before making travel plans.”)
- Organizer also fetched: https://www.dayofthedeadsf.org/ — as of 2026-10-18 the organizer (Day of the Dead SF /
  the Marigold Project) still shows “**November 2nd, 2025 @ 8 AM**” and “**Stay tuned for our community
  collaborations!**”; it publishes **no 2026 date, route or time**.
- Verdict: the published November 2, 2026 date is supported by the cited source, but only by that source.
  **FLAG (request):** add a field-level flag stating the organizer page has not confirmed a 2026 edition; keep
  `time_text`/`admission` blank (do not carry the organizer's stale “8 AM” 2025 time forward).

### 10. Illuminate SF Festival of Light (`illuminate-sf-2026`) — **PASS**
- Source fetched: https://www.sftravel.com/article/san-francisco-festivals-events-november
- Evidence: “**Illuminate SF Festival of Light — Citywide** … More than 60 permanent and temporary eco-friendly
  light art installations transform San Francisco nights into a citywide gallery of light … **Begins November 27,
  2026.**”
- Row: `date_text` “Begins November 27, 2026”, `location` “Citywide, San Francisco”, blank end date and blank
  time/admission all match; the row's note that illuminatesf.com errored at the last re-check is consistent with
  the fact that no organizer page could be reached this session either (not re-attempted — see coverage table).

### 11. San Francisco Italian Heritage Parade 2027 (`italian-heritage-parade-2027`) — **PASS**
- Source fetched: https://sfitalianheritage.org/parade/ (Official organizer)
- Evidence: “**Sunday, October 10th, 2027** … Admission to the parade including the Bank of America Concorso
  Italiano Auto Show is **FREE!** … The Parade begins at **12:30 pm** at the foot of **Jefferson and Powell Streets
  in Fisherman's Wharf**, proceeds south through North Beach on **Columbus Avenue** and ends in **Washington
  Square** in front of Saints Peter and Paul Church.”
- Row: date, weekday, 12:30pm step-off, free admission and the full route match the official page word for word.

### 12. Italian Heritage Parade 2026 (`italian-heritage-parade-2026`) — **PASS**
- Source fetched: https://sfitalianheritage.org/san-francisco-italian-heritage-parade-celebrates-158-years-with-grand-marshal-joe-mantegna/ (Official organizer release, dated October 12, 2026)
- Evidence: “**SAN FRANCISCO, October 12, 2026** — The San Francisco Italian Heritage Parade celebrated its
  **158th year on Sunday, October 11, 2026** … the longest-running annual Italian heritage parade in the United
  States … led by Grand Marshal Joe Mantegna.”
- Row: “Sunday, October 11, 2026 (158th annual)” matches. The release also states the parade “precedes **Italian
  Heritage Day**, celebrated in San Francisco on the **second Monday in October**” — a separate city event that is
  **not** in the catalog (coverage gap, handed to the coverage-gap owners below).

### 13. Fillmore Jazz Festival 2027 (`fillmore-jazz-festival-2027`) — **PASS**
- Source fetched: https://www.fillmorejazzfest.com/ (Official organizer)
- Evidence: “Stay tuned for artist announcements and more, as we begin planning for 2027. **Saturday & Sunday,
  July 3 & 4, 2027** – **The Fillmore Jazz Festival Preservation Fund & the Fillmore Merchants Association** …
  The Fillmore Jazz Festival is one of San Francisco's largest **free** music events.”
- Row: dates, weekday pair, both organizer names and `admission` = “Free” all match.

### 14. Fillmore Jazz Festival 2026 (`fillmore-jazz-festival-2026`) — **FAIL (source no longer states the value)**
- Source cited by the row: https://www.fillmorejazzfest.com/ — fetched 2026-10-18.
- Evidence on the live page: “Thank you for an amazing 2026! … Stay tuned for artist announcements and more, as we
  begin planning for 2027. **Saturday & Sunday, July 3 & 4, 2027**”. The live homepage **no longer states any 2026
  date**; the only dated text is the 2027 edition. The row publishes “July 4–5, 2026 (July Fourth weekend)” and
  its own note admits “the exact July 4–5 dates a[re] …” supported by press posts, not by the cited URL.
- **Request:** either cite an edition-specific official page that still states July 4–5, 2026 (organizer 2026
  press post / photo gallery page, or the SFMTA advisory already used elsewhere in this dataset), or move the 2026
  row to Flagged for Review as “date not re-confirmable from the cited live source”. Do not keep a published date
  whose cited source no longer states it.
- Hygiene: the 2026 row cites `https://www.fillmorejazzfest.com/` and the 2027 row cites `https://fillmorejazzfest.com/`
  — same site, two spellings. Canonicalise to one.

### 15. International Ocean Film Festival 2027 (`international-ocean-film-festival-2027`) — **PASS**
- Source fetched: https://intloceanfilmfest.org/about (Official organizer)
- Evidence: “Volunteer, donate, sponsor, or participate in the **24th Annual IOFF, taking place on April 16-18,
  2027 at Fort Mason Center for Arts & Culture in San Francisco**”.
- Row: dates, venue and “24th annual” note all match.

### 16. International Ocean Film Festival 2026 (`international-ocean-film-festival-2026`) — **PASS·FAIL (one field)**
- Source cited: https://fortmason.org/event/international-ocean-film-festival-2026/2026-04-12/ (Official venue)
- Evidence: “The **23rd Annual** International Ocean Film Festival (IOFF) 2026 at Fort Mason Center for Arts &
  Culture … three days of … screenings … **April 10 to 12** film programs at the Cowell … **Location** Cowell
  Theater, Pier 2 and BATS Improv's Bayfront Theatre, Building B, Third Floor, Fort Mason Center for Arts &
  Culture, **2 Marina Boulevard, San Francisco**”; prices “The film screening programs only are **$20 to $25** …
  2026 day passes … **$40 to $200** … The **$450** All-Access Three-Day Pass … Friday Opening Night Party (Cowell
  Theater, **9:00 p.m.**)”.
- Dates, 23rd-annual note, venue list and `admission` “$20–$450” all match → PASS.
- **FAIL on `time_text`:** the row prints “Fri 4:00–11:00 p.m.; **Sat 10:00 a.m.–11:00 a.m. (as posted)**; Sun
  10:00 a.m.–6:00 p.m.” The cited venue page states no such Saturday one-hour window (the organizer's own schedule
  puts the Saturday **Surf Party at 9:00–11:00 p.m.** and Sunday Program 7 at 10:00 a.m.), and the parenthetical
  “(as posted)” is a hedge, not a sourced value. **Request:** restate only times the cited page actually prints
  (e.g. Friday Opening Night Party 9:00 p.m.) or blank `time_text` and flag it.

### 17. San Francisco Chinese New Year Parade 2027 (`chinese-new-year-parade-2027`) — **PASS**
- Source fetched: https://chineseparade.com/faq/ (Official organizer, Chinese Chamber of Commerce)
- Evidence: “The San Francisco Chinese New Year Parade, celebrating the **Year of the Ram**, will be on **Saturday,
  February 20, 2027** and **starts at 5:15 PM from 2nd and Market St**. It is a **free event** for all to attend but
  **tickets must be purchased to sit in the bleacher sections** … The parade starts off at 2nd and Market Streets,
  goes around Union Square and ends at **Kearny Street & Columbus Ave**.”
- Row: date, weekday, 5:15pm, “Free to watch; bleacher seating is ticketed”, and the route string all match.
- Stale note: the row's note still says only “The source says the date shifts with the Lunar Calendar”; the live
  FAQ now states the concrete 2027 date and Year of the Ram (optional note update).

### 18. San Francisco Pride Celebration & Parade 2027 (`sf-pride-2027`) — **PASS**
- Official source checked: https://sfpride.org/ and https://sfpride.org/about/ (Official organizer)
- Evidence: site-wide banner “**June 26-27, 2027 • 57th Annual Celebration & Parade**” and About page “Our Pride
  Celebration takes place in **Civic Center Plaza** in downtown San Francisco during the last full weekend of June.”
- Row: “June 26–27, 2027”, Civic Center, 57th annual note all match. `time_text` correctly blank — the 10:30 a.m.
  parade time published on sfpride.org belongs to the **2026** parade (June 28, 2026), not 2027; carrying it over
  would be inference.

### 19. Northern California Cherry Blossom Festival 2027 (`cherry-blossom-2027`) — **PASS**
- Official source checked: https://sfcherryblossom.org/ (Official organizer)
- Evidence: “**Join us in 2027 for our big 60th Anniversary Celebration!** … **April 10-11 and 17-18, 2027** …
  **Grand Parade (April 18)**”.
- Row: two-weekend dates and Grand Parade date match exactly. Optional: the official site now states 2027 is the
  **60th anniversary** (row does not say so). Note also that the organizer's `/grand-parade/` subpage still shows
  the 2026 parade (“Sunday, April 19th – 1pm to 3pm”) — a stale subpage; the homepage carries the 2027 dates.

### 20. Bay to Breakers 2027 (`bay-to-breakers-2027`) — **PASS·GAP**
- Official source checked: https://www.baytobreakers.com/ and https://www.baytobreakers.com/15k (Official organizer)
- Evidence: “Join the legendary Bay to Breakers in San Francisco on **May 16, 2027**! This iconic **12K & 15K** race
  has been a city tradition **since 1912**”; 15K page: “All race distances start at the intersection of **Howard
  Street and Fremont Street** in downtown San Francisco. The **first wave will take off at 8:00am and the last wave
  at 8:45am**. Finish Line: **1000 Great Highway San Francisco, CA 94121**”.
- Row date and “annual … since 1912” note match → PASS.
- **GAP/requests:** (a) the organizer now publishes start times, so `time_text` can be “Waves start 8:00am–8:45am”
  instead of blank; (b) `location` currently reads “San Francisco streets; **official route information is published
  by the organizer**” — the second clause is a pointer, not a location, and the organizer does publish start
  (Howard & Fremont Streets) and finish (1000 Great Highway, 94121); (c) `admission` “Registration required” is
  consistent with the official registration flow.

### 21. SF Sketchfest 2027 (`sf-sketchfest-2027`) — **PASS**
- Official source checked: https://sfsketchfest.com/ and https://sfsketchfest.com/get-involved/ (Official organizer)
- Evidence: “SF Sketchfest, the San Francisco Comedy Festival, returns to celebrate our **24th year January 14 -
  31, 2027**!”; Get Involved page: “**Festival dates: January 14 – 31, 2027**”.
- Row: dates match; venue left as “San Francisco” is correct because the organizer has not published the 2027
  venue list yet. Optional: “24th year” is now stated officially.

### 22. Microsoft Ignite (`microsoft-ignite-2026`) — **PASS·GAP**
- Official sources checked: https://ignite.microsoft.com/en-US/home, https://www.microsoft.com/en-us/events,
  https://partner.microsoft.com/en-us/blog/article/ignite-2026-overview (Official organizer) and the venue's own
  listing https://www.moscone.com/events/microsoft-ignite-2026 (Official venue)
- Evidence: “**November 17–20, 2026**, Microsoft Ignite delivers keynotes …”; “November 17–20, 2026 | **San
  Francisco**”; “at the **Moscone Center in San Francisco** and online”; venue listing “**November 17 - November 20,
  2026 — Moscone North, South, and West — 747 Howard Street, San Francisco, CA 94103**”.
- Row: dates and “Moscone Center, 747 Howard Street, San Francisco” match; `admission` “Registration required” is
  supported. **GAP:** Microsoft's own registration flow now lists prices (Conference pass $2,325; Hub-only $1,625;
  digital pass free; optional pre-day Nov 16), so `admission` could carry official figures instead of the generic
  phrase, and the pre-day date is published.

### 23. AGU26 Annual Meeting (`agu-annual-meeting-2026`) — **PASS**
- Official sources checked: https://www.agu.org/annual-meeting, https://www.agu.org/meetings (Official organizer)
  and https://news.agu.org/press-release/press-registration-open-for-2026-agu-annual-meeting/ (organizer newsroom)
- Evidence: “Join us for **AGU26 in San Francisco, CA 7-11 December 2026**”; newsroom: “AGU Annual Meeting **7 – 11
  December 2026 — George R. Moscone Convention Center, 747 Howard St., San Francisco, CA 94103**”.
- Row: dates and Moscone venue/address match. This resolves the gap described in the row's own note (agu.org once
  printed only “San Francisco, CA”): the organizer's newsroom now states the venue explicitly, so the published
  venue is officially sourced. `admission` “Registration required” matches “Early registration for AGU26 is open!”.

### 24. Scaregrove (`scaregrove-2026`) — **PASS**
- Official sources checked: https://sfrecpark.org/calendar.aspx?view=month&year=2026&month=10 (Government source)
  and the department's own program site https://sfchildrennature.org/organizer/san-francisco-recreation-parks/
  (organizer `sameAs` https://sfrecpark.org/)
- Evidence: Rec & Park October 2026 calendar lists “**Volunteer at Scaregrove** — When: **3:00 PM - 9:00 PM** —
  Location: **Sigmund Stern Grove**”; the department's event record states “**Scaregrove — Fri October 30 | 3:00 PM
  - 9:00 PM — Stern Grove Park, 19th Avenue & Sloat Blvd, San Francisco** … a **free** Halloween celebration at
  Sigmund Stern Grove” with structured data `startDate 2026-10-30T15:00`, `endDate 2026-10-30T21:00`.
- Row: “Friday, October 30, 2026”, 3pm–9pm, Free, “Sigmund Stern Grove (19th Avenue & Sloat Boulevard)” all match.
  (The department's free-accessible-shuttle and Vale Avenue entrance details are extra, not required.)

### 25. Downtown First Thursdays (`downtown-first-thursdays`) — **PASS**
- Official source checked: https://www.dftsf.com/ and https://www.dftsf.com/street-party (Official organizer)
- Evidence: “A **FREE**, all-ages monthly party taking place the **first Thursday of every month from 5-10pm** in
  the streets of Downtown San Francisco. **Next UP: NOV 5, 2026 — Free w/ RSVP — 📍2nd St. between Market and
  Howard in SF | 5-10PM | RAIN OR SHINE**”; organizer blog: DFT renewed “for a 12-month season running from
  **January to December 2026** … every first Thursday of the month from 5 to 10 p.m.”
- Row: cadence, “next listed November 5, 2026”, 5pm–10pm, “Free with RSVP”, Second Street between Market and
  Howard all match exactly.

### 26. YBG Festival (Yerba Buena Gardens Festival) 2026 (`ybg-festival-2026`) — **FAIL (season end date not confirmable)**
- Cited source: an SF Travel press release (Trusted civic source). Organizer pages checked this session:
  https://ybgfestival.org/ and the organizer's own 2026 press release
  https://ybgfestival.org/wp-content/uploads/2026/04/YBGF-2026-PR.pdf
- Organizer evidence: homepage — “**Free.** More than **75** performing arts programs in downtown San Francisco,
  **May–Oct**”, with the latest listed 2026 events **Joe Bataan Oct 17**, **Afro-Filipino Jazz Project Oct 24**,
  **Halloween Hoopla Oct 31** (Children's Garden, 12:00–3:00pm). Organizer 2026 press release — “Yerba Buena
  Gardens Festival announces the programming for its **26th season** of free outdoor music, theater, circus, dance,
  poetry and children's programs … The Festival's 26th season **opens on Saturday, May 9, at 2:00pm**”.
- Row publishes “**May 9–November 13, 2026**”. The May 9 opening and “Free” are officially confirmed; **the
  November 13 end date is not stated anywhere on the organizer's live pages** (they say May–Oct and list Oct 31 as
  the final posted event). Third-party guides (SFCV, RIFF) do say “May 9 – Nov 13”, which is exactly the kind of
  value the brief says must not be published without an official source.
- **Request:** either (a) cite an organizer page that states the November 13 close, (b) restate as the officially
  published span “Opens Saturday, May 9, 2026; 2026 programs posted through October 31, 2026”, or (c) blank the end
  date and add a flag. Also switch `source_url` to the organizer's own press release/homepage (upgrades the row from
  “Trusted civic source” to “Official organizer”) and reconcile the program count (organizer says 75+, not 100+).

### 27. Alemany Farmers Market (`alemany-farmers-market`) — **PASS**
- Source: https://www.sf.gov/location--alemany-farmers-market (Government source)
- Evidence: “Buy fresh fruits and vegetables from local farmers **every Saturday, 7am - 2pm** … **Alemany Farmers
  Market, 100 Alemany Boulevard, San Francisco, CA 94110** … operated by **Foodwise**.”
- Row: weekday, 7am–2pm, address and Foodwise attribution all match.

### 28. Ferry Plaza Farmers Market (`ferry-plaza-farmers-market`) — **PASS**
- Source: https://foodwise.org/markets/ferry-plaza-farmers-market/ (Official organizer)
- Evidence: “**Ferry Building, Embarcadero and Market Streets, San Francisco** — **Saturday (8 am – 2 pm) and
  Tuesday & Thursday (10 am – 2 pm), year round**”.
- Row: three market days, both hour windows, “year-round” and the Ferry Building location match.

### 29. Heart of the City Farmers Market (`heart-of-the-city-farmers-market`) — **PASS (source is internally inconsistent)**
- Source: https://hotcfarmersmarket.org/ + /about + /find-us (Official organizer)
- Evidence: “/find-us — located year round at **Fulton Plaza** in San Francisco's Civic Center between the San
  Francisco Public Library and the Asian Art Museum **every Wednesday and Sunday from 7am to 4pm**, rain or shine.
  Our Information Tent is near the intersection of **Fulton Street and Larkin Street**”; “/about — … **relocated by
  the City & County of San Francisco in 2024 to Fulton Plaza**”; “/donate — In July 2023, our Wednesday and Sunday
  markets **reduced their hours to 7am to 4pm**”.
- Row: “Sunday and Wednesday”, 7am–4pm, “Civic Center, Fulton Street and Larkin Street” match the current official
  pages. **Irregularity in the source, not the row:** the organizer homepage's own embedded description still says
  “Sundays 7:00am - 5:00pm and Wednesdays 7:00am - 5:30pm” (pre-2023 hours) and still says “United Nations Plaza”.
  Recorded here so a future auditor does not “correct” the row back to the stale homepage text.

### 30. Mission Community Market (`mission-community-market`) — **PASS·GAP**
- Source: https://foodwise.org/markets/mission-community-market/ (+ /visitor-info, + the organizer's first/last-day
  event pages) (Official organizer); corroborated by the State's certified-market list
  https://www.cdfa.ca.gov/is/docs/CurrentMrktsCounty.pdf (Government source)
- Evidence: “**22nd and Bartlett Streets, San Francisco** — **Thursday (3 pm – 7 pm), mid March – mid November**”;
  visitor-info: “takes place at **22nd Street between Mission and Valencia**”; “First Day of the Season —
  **Thursday, March 19, 2026, 3:00 pm - 7:00 pm**”; “Last Day of the Season — **Thursday, November 12, 2026** …
  We'll be back in March 2027”; CDFA list: “22nd & Bartlett Sts., San Francisco, 94110 — Thur — 3 - 7pm — Mar - Nov”.
- Row: weekday, seasonal window, hours and both street descriptions match (this also closes the older audit finding
  that the season boundary was omitted). **GAP:** the organizer publishes exact 2026 season boundaries, so
  `start_date` 2026-03-19 / `end_date` 2026-11-12 can be added without inference — that also makes the row visible
  as still-running (four market days remain as of 2026-10-18).

### 31. NightLife at the California Academy of Sciences (`calacademy-nightlife`) — **PASS**
- Source: https://www.calacademy.org/nightlife (Official venue/organizer)
- Evidence: “NightLife is **Thursdays\*** from **6–10 p.m.** Last entry into the building is 9 p.m. All guests must
  be **21+** … **Tickets are $26**. If you have an EBT card, you can purchase a discounted **$5** ticket at the
  ticket window (limit 1 per group per visit).”
- Row: “Most Thursdays”, 6pm–10pm, “$26; $5 for EBT cardholders at the ticket window”, Music Concourse Drive address
  all match. (The asterisk covers the holiday hiatus the Academy announces, which is why “Most Thursdays” is right.)

### 32. Exploratorium After Dark (`exploratorium-after-dark`) — **PASS**
- Source: https://www.exploratorium.edu/visit/calendar/after-dark (Official venue/organizer)
- Evidence: “**After Dark Thursday Nights — Every Thursday Night • 6:00–10:00 pm** … **Adults Only (18+)** …
  **Location Pier 15 (Embarcadero at Green Street) San Francisco, CA 94111**”.
- Row: Thursday, 6pm–10pm, Pier 15 all match. `admission` blank is correct — this page states no general ticket
  price (the reduced-rates page states $5 for EBT/SNAP holders; adding only that would misrepresent general admission).

### 33. People in Plazas — Market Street Music Festival (`people-in-plazas`) — **PASS·GAP**
- Source: https://peopleinplazas.org/ and https://peopleinplazas.org/calendar/ (Official organizer)
- Evidence: “Each year the ‘People in Plazas’ (PiP) **free** summer music festival in San Francisco produces **more
  than 130 concerts in 15 different venues on or near Market Street from the Embarcadero to Fourth Street**”;
  the live 2026 calendar lists concerts at **12:00 pm - 1:00 pm** through **Wednesday, October 28, 2026**
  (e.g. “425 Market – Chelle and Friends (New Orleans)”).
- Row: “15 venues on or near Market Street, from the Embarcadero to Fourth Street” and `admission` “Free” match the
  organizer word for word. **GAP:** `date_text` “Summer season” is vaguer than the official record — the organizer's
  calendar shows the 2026 season running July through **October 28, 2026**, and concert times are published
  (noon–1:00pm), so `time_text` need not stay blank.

### 34. Merola Opera Program Summer Festival (`merola-summer-festival`) — **FAIL (date not sourced; season concluded)**
- Source cited: https://merola.org/summerfestival/ (Official organizer)
- Evidence available on the official page: “**The 2026 Merola Summer Festival is underway**, showcasing the next
  generation of opera stars … Each summer, Merola Opera Program brings exceptional young artists … for intensive,
  tuition-free training.” The page states **no calendar dates** for the 2026 season.
- Row publishes `date_text` “**Summer 2026**”, `cadence` annual, blank times/admission, location “San Francisco”.
  “Summer 2026” is a season label, not a sourced date, the 2026 season has now ended (audit date 2026-10-18), and
  the location carries no venue. **Request:** move to Flagged for Review as “essential values (dates, venue) not
  stated by the official source”, or republish with the specific performance dates/venues the organizer lists for
  the next edition. Do not infer a date range from the word “summer”.

---

## Part 2 — structural / integrity audit (task V2, harness output)

Harness: `research/audit_checks_e969f4df.py` (read-only; run with `python3 research/audit_checks_e969f4df.py`).
Full machine output for the record: `ERROR: 0 · WARN: 3 · NOTES: 91` at commit time of this log.

**What passed (no exceptions found):**
- Every one of the 105 records has an HTTPS source URL on a real publisher host; no `example.com`/`localhost`/
  shortlink hosts; no placeholder strings (“TBA”, “See organizer”, “Varies”, …) in any populated field.
- Calendar logic: every weekday name printed in a `date_text` agrees with the ISO `start_date`/`end_date`
  (e.g. “Sunday, October 10, 2027”, “Saturday, February 20, 2027”, “Friday, October 30, 2026”,
  “Wednesday, April 1–November 18, 2026” all check out); no inverted ranges; no malformed ISO dates; no
  `date_text` year that disagrees with its ISO dates.
- Geography: every published row's `location` carries a San Francisco indicator (city name, 941xx ZIP, or a
  recognised SF neighborhood/venue); no row is located in Oakland, Berkeley, San Mateo, Daly City, Mill Valley, etc.
- Classification: all `bucket`, `status`, `category` and `source_authority` values are inside the controlled
  vocabularies; no published row cites an `Unverified legacy URL`; review records all sit in the `review` bucket
  with a `review_reason`.
- Page parity: `all-events.html` renders 93 rows/93 source links, `recurring.html` 74/74, `special.html` and
  `annual-special.html` 19/19 each, `flagged.html` 12 review records, the eight category pages render every row of
  their category (3/25/14/9/11/20/5/6), and `data/events.csv` has exactly 105 rows = the record count.
- Links: 16 HTML files, **197 internal references — all resolve** (no broken local links, none escaping the repo);
  345 external references over 72 hosts.
- Source inventory: 66 distinct source hosts, 18 records on `.gov` domains; most-used hosts `presidio.gov` (12),
  `carnavalsanfrancisco.org` (7), `www.sf.gov` (6), `www.pcfma.org` (5), `www.sfmta.com` (4), `foodwise.org` (4).

**Irregularities the harness raises (all need an owner of `data/events.json`/`build.py` to act — not this session):**

1. **Three annual traditions are published twice**, once as the completed 2026 edition and once as the announced
   2027 edition, which inflates the “list of all events” and mixes editions of one tradition:
   - `fillmore-jazz-festival-2026` (July 4–5, 2026) **and** `fillmore-jazz-festival-2027` (July 3–4, 2027)
   - `international-ocean-film-festival-2026` (April 10–12, 2026) **and** `international-ocean-film-festival-2027` (April 16–18, 2027)
   - `italian-heritage-parade-2026` (October 11, 2026) **and** `italian-heritage-parade-2027` (October 10, 2027)
   The roll-forward policy is applied **inconsistently** across the catalog: SF Pride, Chinese New Year Parade,
   Bay to Breakers and SF Sketchfest were rolled forward to their next edition (their 2026 editions were dropped),
   while these three keep both. Pick one policy. Recommended: one row per tradition carrying the next edition, with
   completed editions either dropped or grouped in an explicitly labelled “2026 editions already held” section.
2. **57 of 93 published rows are past-dated** (their ISO end date is before the audit date 2026-10-18), 22 are
   upcoming/ongoing and 14 are undated recurring programs — and **no generated page labels past rows as past**.
   A reader of `index.html`/`all-events.html` cannot tell an event that already happened from one they can still
   attend; the dashboard headline is a single “93 publishable city-only rows”. Recommended: add an
   upcoming/completed indicator (the ISO dates already support it) or split the tables, and state the split in the
   dashboard summary. This is a presentation change in `build.py` + `index.html`, i.e. integration-owner scope.
3. **Pointer text published as a value** in two rows: `bay-to-breakers-2027` `location` = “San Francisco streets;
   *official route information is published by the organizer*” and `lit-crawl-sf-2026` `time_text` = “Programs
   include 6:30pm–7:30pm; *see full schedule*”. The italicised clauses are not values. The harness's exact-match
   placeholder test does not catch embedded pointers, so `verify.py` passes them; recommend a substring test for
   “see …”, “published by the organizer”, “varies by …” in `location`/`time_text`/`admission`.
4. **Source-host canonicalisation:** `www.fillmorejazzfest.com` vs `fillmorejazzfest.com` for the same organizer
   (two rows), and `www.presidio.gov/about/press/presidio-unveils-vibrant-2026-summer-event-lineup` is the single
   cited source for **11** different Presidio events while `carnavalsanfrancisco.org/special-events/` is cited for
   **7** Carnaval rows and `sf.gov/san-francisco-celebrates-juneteenth-2026` for **4** Juneteenth rows. One shared
   umbrella URL per family is defensible (it is the page that states them) but it means a single page change
   invalidates up to 11 rows; recommend recording per-event anchors/deep links where the publisher has them.

---

## Part 3 — coverage gaps found while verifying (handoff to the coverage-gap owners)

These surfaced from official pages fetched during Part 1. This session does **not** add rows: `data/events.json` is
claimed by `arena/5e333a6e-maltaproj7` (S2) and `arena/646f6727-maltaproj7` (G1). Each item below lists the official
page that states it, and whether this session already inspected that page.

**City-only events with an official date already inspected this session (publishable as-is):**

| Event | Official evidence seen this session | Source |
| --- | --- | --- |
| Italian Heritage Day | “The parade precedes **Italian Heritage Day, celebrated in San Francisco on the second Monday in October**” (2026: Monday, October 12) | https://sfitalianheritage.org/san-francisco-italian-heritage-parade-celebrates-158-years-with-grand-marshal-joe-mantegna/ (fetched) |
| Día de los Muertos & Halloween at Mission Community Market | “Día de los Muertos and Halloween at Mission Community Market \| **October 29, 2026 \| 3:00 pm**” | https://foodwise.org/events/ (listed on the fetched Foodwise event page) |
| Foodwise Fall Fruit Celebration | “Fall Fruit Celebration \| **October 31, 2026 \| 11:00 am**” | https://foodwise.org/events/fall-fruit-celebration/ (listed on the fetched Foodwise event page) |
| Foodwise Sunday Supper | “Foodwise Sunday Supper \| **October 18, 2026 \| 4:30 pm**” | https://foodwise.org/events/foodwise-sunday-supper/ (listed on the fetched Foodwise event page) |
| YBG Halloween Hoopla | “Halloween Hoopla — **2026-10-31 12:00–15:00**, Children's Garden, Yerba Buena Gardens, San Francisco” (organizer structured data) | https://ybgfestival.org/ (official organizer) |
| Mission Community Market — first/last day of 2026 season | “**Thursday, March 19, 2026**” opening and “last day of the 2026 season will be **Thursday, November 12**” | https://foodwise.org/events/mission-community-market-first-day-of-the-season/ and /last-day-of-the-season/ |

**City-only events named by SF Travel's official November guide whose organizer pages this session did NOT inspect
(inspect before publishing — the guide itself warns “All dates and locations are subject to change and should be
confirmed with sponsors”):**

| Event | SF Travel text | Organizer to confirm |
| --- | --- | --- |
| Bhangra and Beats Night Market | “Clay and Battery streets … This **free** event takes place two Fridays in 2026 … **November 13, 4 - 9 p.m.**” | https://www.bhangraandbeats.com/ |
| San Francisco Hip-Hop Dance Festival | “**Palace of Fine Arts** … **November 14-15, 2026**” | https://www.sfhiphopdancefest.com/ |
| Renegade Craft Fair (San Francisco Winter) | “**Fort Mason** … **November 14-15, 2026; 11 a.m to 5 p.m.** both days” | https://www.renegadecraft.com/event/san-francisco-winter/ |
| Union Square Free Programs | “**every week** … free activities in the middle of Union Square … every second Saturday special cultural activities” | https://visitunionsquaresf.com/park-programs |

**Must NOT be added (scope guard):** SF Travel's San Francisco November guide also lists **The Great Dickens
Christmas Fair** at the **Cow Palace** — that venue is in Daly City, outside the City and County of San Francisco,
so it fails this catalog's geography rule even though an official civic source files it under “San Francisco”.
Likewise the Embarcadero Center, Union Square and Ghirardelli Square **tree-lighting ceremonies** are listed by SF
Travel as “**Date TBD**”: with no official date they cannot be published as dated rows and belong on Flagged for
Review if they are recorded at all.

---

## Part 4 — coverage of this audit, and its limits (stated plainly)

| Group | Records | Re-checked against a live official source **this session** | Method |
| --- | --- | --- | --- |
| Published rows with an ISO end date on/after 2026-10-18 (upcoming/ongoing) | 22 | **22 (100%)** | direct fetch of the cited source, or direct inspection of the official organizer/venue/government page |
| Duplicate-edition partners (2026 rows of the three twice-published traditions) | 3 | **3 (100%)** | direct fetch (Fillmore Jazz, Italian Heritage Parade) / official venue listing (IOFF at Fort Mason) |
| Undated or seasonal recurring programs | 14 | **8** (Alemany, Ferry Plaza, Heart of the City, Mission Community Market, Downtown First Thursdays, NightLife, Exploratorium After Dark, People in Plazas) | official organizer / government page |
| Published rows dated before 2026-10-18 (completed 2026 editions) | 54 remaining | 0 this session | structural harness only; field-level evidence for these rows is the direct-fetch log of the earlier integration sessions (`research/reverification-55c58947.md`, `research/official-source-audit.md`), which this session read but did not repeat |
| Review-only records (Flagged for Review) | 12 | 0 this session | structural harness (all 12 confirmed to sit in the `review` bucket with reasons and no promoted fields) |
| Field-level flags register | 16 | structural only | harness confirmed every flag has HTTPS sources and a disposition |

**Limits.** (1) The sandbox has no general outbound network, so URL liveness could not be tested with HTTP status
codes in bulk; every “fetched”/“inspected” claim above came through the platform's page-fetch/search tooling and is
quoted. (2) Rows marked “not re-checked this session” are **not** asserted to be wrong — they are asserted to be
unre-verified by this session, and their evidence trail is the earlier logs named above. (3) Nothing in this log was
inferred: where an official page did not state a value, the recommendation is to leave the field blank and flag it.

**Summary of verdicts:** 30 records re-verified this session → **26 PASS**, **4 PASS with a sourced gap**
(Cloudflare Connect times, Lit Crawl pointer text, Bay to Breakers times/location, People in Plazas season span;
plus optional enrichments for Cherry Blossom “60th anniversary”, Sketchfest “24th year”, Ignite pass prices,
Mission Community Market ISO dates), **2 FAIL** (Fillmore Jazz 2026 date no longer stated by its cited source;
Merola Summer Festival “Summer 2026” not a sourced date), **1 FAIL on one field** (IOFF 2026 `time_text` Saturday
window), **1 FAIL on one field** (YBG Festival 2026 season end “November 13”), **1 PASS·FLAG** (Day of the Dead
Procession — organizer has not published a 2026 edition), **1 PASS with a source-side inconsistency** (Heart of the
City Farmers Market homepage still prints pre-2023 hours).

---

## Part 5 — post-merge addendum (2026-10-18, after PRs #17–#21)

While this audit was in progress, sessions `arena/646f6727-maltaproj7` and `arena/5e333a6e-maltaproj7` completed their
coverage/integration tasks and merged (PRs #17–#21). The catalog is now **155 records: 139 published (94 recurring,
45 special), 16 review records, 25 field-level flags**. This session merged `main` (resolving the add/add
`COORDINATION.md` conflict by keeping both boards verbatim) and re-ran everything against the combined data:

- `python3 build.py && python3 verify.py` → ALL LOCAL CATALOG, SOURCE-LINK, AND NAVIGATION CHECKS PASSED
  (published=139, recurring=94, special=45, review=16, flags=25, categories=8).
- `python3 research/audit_checks_e969f4df.py` → **0 errors, 3 warnings, 105 notes**; 197 internal references, all
  resolved; 526 external references over 94 hosts; `data/events.csv` 155 rows = record count. The 3 warnings are
  the same three doubled traditions as Part 2 (Fillmore Jazz, International Ocean Film Festival, Italian Heritage
  Parade — 2026 + 2027 rows each), still unresolved in the merged data.
- All five FAIL findings from Part 1 are **still present verbatim** in the merged data (checked 2026-10-18):
  `fillmore-jazz-festival-2026` still publishes “July 4–5, 2026” citing the homepage that now announces 2027 only;
  `merola-summer-festival` still publishes “Summer 2026”; `ybg-festival-2026` still publishes “May 9–November 13,
  2026” from an SF Travel press release; `international-ocean-film-festival-2026` still prints the “Sat 10:00
  a.m.–11:00 a.m. (as posted)” window; `lit-crawl-sf-2026` and `bay-to-breakers-2027` still carry pointer clauses.
- New-taxonomy note: the merged catalog uses both `Official venue` (19 rows, mostly Moscone Center listings) and
  `Official venue / federal trust` (13 rows). Both are defensible, but one label or an explicit definition of the
  split should be chosen so readers are not left guessing why two near-identical authorities exist.

**Independent spot re-verification of peer-added upcoming rows (this session, official sources):**

| Row | Verdict | Official evidence |
| --- | --- | --- |
| Bhangra & Beats Night Market (`bhangra-beats-night-market-2026`) | **PASS** | Organizer: “Happening on two Fridays—**July 24 and November 13** (Diwali edition)—from **4pm–9pm**, this **FREE** event will transform **Yerba Buena Gardens, Jessie Square, and Yerba Buena Lane**” (bhangraandbeats.com). Note: SF Travel's November guide says “Clay and Battery streets” — stale; the row correctly follows the organizer. |
| San Francisco International Hip Hop DanceFest (`sf-hip-hop-dance-festival-2026`) | **PASS·GAP** | Organizer: “Micaya Presents The **28th Annual** San Francisco International Hip Hop DanceFest — **Saturday, November 14, 2026, 7:00 PM** … **Sunday, November 15, 2026, 12:00 PM** and **5:00 PM** — **Palace of Fine Arts Theatre**” (sfhiphopdancefest.com). Dates/edition/venue match; `time_text` is blank although 7pm / 12pm / 5pm are official. |
| Renegade Craft Fair — San Francisco Winter (`renegade-craft-fair-2026`) | **PASS** | Organizer: “**11/14/2026 11:00 am – 5:00 pm … 11/15/2026 11:00 am – 5:00 pm** … Fort Mason Center Festival Pavilion, **2 Marina Blvd., San Francisco, CA 94123**” and participation kit: “there is a **$5 suggested entry** at the door” (renegadecraft.com). Row matches, including the $5 suggested-entry wording. |
| San Francisco Ballet — Nutcracker (`sf-ballet-nutcracker-2026`) | **PASS** | Organizer: “**DEC 4–27** … Location **War Memorial Opera House** … **Fri Dec 04 7:00 pm**” (sfballet.org/productions/nutcracker). Row matches; dark days (Dec 7/14/21/25) exist but are not claimed. |
| Chinese New Year Flower Market Fair 2027 (`chinese-new-year-flower-market-fair-2027`) | **PASS** | Organizer: “The 2027 Flower Market Fair is scheduled for **Sat. & Sun. Jan. 30 & 31 @ Grant between Clay and Broadway**” (chineseparade.com/flowermarketfair). Row matches exactly. |

Moscone-Calendar-sourced conference rows added by peers (Current San Francisco, Winter FancyFaire, ASCO GI/GU,
SPIE Photonics West, ORS, TDX, AAD, AMCP, Atlassian Team '27, ASRS, GDC, RSA Conference 2027, Dreamforce 2027,
J.P. Morgan Healthcare Conference) were **not** re-fetched this session; their source is the venue's official events
calendar and their row text already discloses where the venue is not stated (“venue not stated on official page”,
“Listed on the Moscone Center events calendar”), which is the correct non-inferential treatment.
