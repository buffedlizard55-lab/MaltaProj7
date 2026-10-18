# Official-source re-verification — session arena/3977d9cb-maltaproj7

**Date of every check below: 2026-10-18 (UTC).**
**Rule applied:** a value is written into `data/events.json` only when the linked official page states it. Where the
official page is silent, the field stays blank and a flag records the gap. Secondary aggregators (Funcheap, JamBase,
Music Festival Wizard, AllEvents, GarysGuide, Luma discovery pages, press coverage) were used **only** to find
candidate official pages — never as the source of a published value.

Baseline at the start of this pass: `origin/main` at `68a0516`, 148 published rows (98 recurring + 50 special),
16 review records, 34 field-level flags, `python3 build.py && python3 verify.py` clean.

---

## 1. Rows re-fetched this session, with the quoted official text

| # | Row in the catalog | Official page fetched (2026-10-18) | What the page states | Result |
| --- | --- | --- | --- | --- |
| 1 | Lower Polk Live — `lower-polk-live-2026-10-23` | <https://www.sfmta.com/travel-updates/lower-polk-live-friday-october-23-2026> | "Lower Polk Live will be held on **Friday, October 23, from 4 to 9 p.m.**"; closures "**Polk** between Bush and Sutter", "**Fern** between Van Ness and Larkin" | Date, time and street footprint in the row **match the source**. The page states **no admission charge**, so `admission` stays blank and the row remains on the cost-not-stated register. No change. |
| 2 | From the E Excelsior Night Market — `from-the-e-night-market-2026-10-23` | <https://www.sfmta.com/travel-updates/e-night-market-friday-october-23-2026> | "a night of food, fun, unique crafts, entertainment and live music taking place on Ocean Avenue this **Friday, October 23, from 4:30 to 8:30 p.m.**"; "**Ocean Avenue** between Mission Street and Persia Avenue will be **closed from 12 p.m. to 11:59 p.m.**" | Date, time and footprint **match**. No admission stated → `admission` stays blank. No change. |
| 3 | Sunday Streets SF — 2026 season — `sunday-streets-2026` | <https://sundaystreetssf.com/> | "2026 Events": "Tenderloin • June 14th", "Mission • July 19th", "Bayview • August 23rd", "Excelsior • October 18th"; "preparing for its **18th season**" | All four dates in the row's `date_text` **match the official season page exactly**. No admission stated on the season page → `admission` stays blank. No change. |
| 4 | Sunday Streets Excelsior (today's edition of row 3) | <https://sundaystreetssf.com/sunday-streets-excelsior-2026/> | "Excelsior Community Block Party … **Sunday, October 18, 2026 ‧ 11 AM – 4 PM** … **Mission Street between Geneva Avenue and Theresa Street**"; a separate paid/registered "Excelsior 5k Walktober (9:30am @ Cayuga Playground)" with its own registration link | Confirms the season row's final 2026 date. The page states **no admission price** for the block party and mixes in a separately registered 5K, so no "free" value was written — the season row keeps a blank cost. No change. |
| 5 | Sunday Streets — cost question | <https://sundaystreetssf.com/about> | "Event routes are 1-4 miles in length, with fun, **free activities** provided by local nonprofits, community groups and small businesses"; "Exhibitor spaces start at **$35** and are free for organizations and businesses on the route" | The About page says the *activities* are free but publishes **no admission statement**, and it names an exhibitor fee. Writing "Free" here would be an inference, so the cost stays blank and the wording is recorded in this log instead. |
| 6 | Día de los Muertos and Halloween at Mission Community Market — `dia-de-los-muertos-halloween-mission-market-2026` | <https://foodwise.org/events/dia-de-los-muertos-and-halloween-at-mission-community-market/> | "**Thursday, October 29, 2026, 3:00 pm - 7:00 pm**"; "Market Happening", "Mission"; "**Enjoy music with DJ Lamont** (5-7 pm) at the Little Mission Studio stage"; "the orange Foodwise Seasonal Spotlight tent for **free samples**, recipes, and cooking tips"; "22nd Street between Mission and Valencia" | Date, time, stage times and location in the row **match**. The page states free *samples*, not free admission, so `admission` correctly stays blank. No change. |
| 7 | Foodwise market pages generally | <https://foodwise.org/farmers-markets/> (redirects to <https://foodwise.org/articles/farmers-markets-are-essential/>) | Lists "Ferry Plaza Farmers Market … Saturdays (8 am to 2 pm) and Tuesdays and Thursdays (10 am to 2 pm), year round" and "Mission Community Market … Thursdays (3 to 7 pm), March-November"; no admission statement | Confirms the market cadence used by the weekly Foodwise rows. **No cost published**, so the nine Foodwise/farmers-market rows keep blank costs. Redirect noted (the `/farmers-markets/` path now serves an article). |
| 8 | Lit Crawl SF — `lit-crawl-sf-2026` | <https://www.litquake.org/litcrawl> | "**OCTOBER 24, 2026**"; "the world's largest **free** pop-up literary event"; "**all programs from 6:30—7:30 PM**"; "a massive, one-night literary pub crawl through San Francisco's Mission District" | Date, `time_text` ("6:30pm–7:30pm (all programs)"), Mission District location and `admission: Free` all **match the official page**. Row confirmed as a free upcoming event. No change. |
| 9 | Hardly Strictly Bluegrass — `hardly-strictly-bluegrass-2026` | <https://hardlystrictlybluegrass.com/> | Home page still presents the 2026 edition (HSB app, "HSB at 25" book, merch store "open October 13 – 27", "Scenes from HSB 2025"); **no 2027 dates or lineup published** | The row's 2026 dates and `Free; no tickets needed` admission are unchanged. **No 2027 row was added**, because the only 2027 dates found (October 8–10, 2027) come from non-official aggregators — recorded as `flag-hsb-2027-dates-unconfirmed` with all three links. |
| 10 | Day of the Devs — San Francisco Edition — `day-of-the-devs-sf-2026` | <https://www.dayofthedevs.org/> | "Day of the Devs is a non-profit organization … **Our programs are provided entirely for free.**"; "We want Day of the Devs to always remain **FREE** to everyone"; "Our next showcase: **Day of the Devs The Game Awards Digital Showcase** — Join us **online** the day before the Game Awards" | Confirms the free classification of the existing SF row (a completed edition, March 8, 2026). The next announced program is **online**, not a San Francisco in-person event, and no new SF edition is announced → recorded as `flag-free-gaming-coverage-gap` with the official links. No row added. |
| 11 | City calendar context | <https://sf.gov/events/upcoming> | Live citywide calendar (e.g. "Monday, October 19" committee meetings, "September 14 to Friday, November 20" ZSFG flu clinic) | Confirms the city's own calendar is live as of the check date and that the SF.gov directory link on the Method page resolves. Added to the Method page's directory list. No rows taken from it this pass (individual listings are meetings, not public events). |
| 12 | Free-gaming candidate venue | <https://thedetoursf.com/> and <https://www.thedetoursf.com/> | **Fetch failed both times** (page could not be retrieved) | The aggregator-reported "Free Play Tuesday" arcade night was **not added**: no official page could be retrieved, so nothing was verified. Recorded here so the gap is visible. |

## 2. Rows added this session (all values quoted from the linked official page)

### 2.1 Hunters Point Shipyard Fall Open Studios — `hunters-point-shipyard-fall-open-studios-2026`

* **Official source used:** Shipyard Trust for the Arts' own event listing —
  <https://www.eventbrite.com/e/shipyard-open-studios-fall-2026-registration-1992234233221>
  ("By **Shipyard Trust for the Arts**", "Organized by Shipyard Trust for the Arts").
* **Quoted values:** "**October 17–18, 2026 · 11 AM–6 PM**"; "**Hunters Point Shipyard & Islais Creek Studios**";
  "**Free admission & parking** — reserve your free ticket below"; "**Twice a year**, one of San Francisco's most
  fascinating hidden landmarks throws open its doors"; "Main Shipyard Site: **451 Galvez Ave, San Francisco**",
  "Satellite Studios at Islais Creek: **1 Rankin St, San Francisco**"; "you'll see an optional **Supporter Ticket** —
  chip in if you can. Every dollar goes directly to keeping this weekend free and open to all."
* **Corroborating official page:** The Point — <https://www.thepointart.com/hunters-point-shipyard>:
  "**Fall Open Studio 2026 • Saturday & Sunday, October 17 & 18, 2026** … Twice a year – in the spring and in the
  fall – over 100 artists open their studio doors to the public. **Free admission and free parking.**"
* **Fields written:** `date_text` "October 17–18, 2026", `start_date` 2026-10-17, `end_date` 2026-10-18,
  `time_text` "11:00 a.m.–6:00 p.m.", location as quoted, `admission` "Free admission & parking (optional supporter
  ticket)" → cost class **free**, `bucket` recurring / `cadence` seasonal (the source's own "Twice a year … in the
  spring and in the fall"), category "Community & culture", authority "Official organizer".
* **Irregularity recorded:** `flag-shipyard-open-studios-source` — the lead organizer domain
  <https://www.shipyardartists.com/shipyard-open-studios/> returned an interstitial "Please wait …" page when fetched,
  so the row is sourced from the organizer's official listing plus The Point's official page.

### 2.2 Open Source AI Week — Open Weight Debate Night — `open-weight-debate-night-2026`

* **Official source:** <https://opensourceaiweek.com/the-debates/> (organizer: Open Source AI Week /
  Open Intelligence Foundation, hosted by GitHub and Microsoft Azure).
* **Quoted values:** "**Date:** Monday, October 19, 2026"; "**Time:** 5:00 PM – 9:00 PM"; "**Where:** GitHub Office —
  88 Colin P. Kelly Jr. Street, San Francisco, CA 94107"; "**Capacity:** Limited to 250 — reserve early"; confirmed
  debaters listed on the page (Ion Stoica, Percy Liang, Ben Brooks, Cheryl Cheng, Malo Bourgon, David Bellamy).
* **Fields written:** date/time/location/organizer as quoted; category "Technology, AI & gaming"; `bucket` special /
  `cadence` single-date (the page states no recurrence, so none was inferred); authority "Official organizer".
* **Cost:** **left blank.** Neither the event page nor the official registration listing
  (<https://luma.com/592fcwx2>, which shows "**Approval Required**" and "Request to Join") publishes a price.
  Recorded as `flag-open-source-ai-cost`. The row therefore appears in the separate non-free section, **not** in the
  free main list.

### 2.3 Open Source AI Awards Night — `open-source-ai-awards-night-2026`

* **Official source:** <https://opensourceaiweek.com/open-source-ai-awards/>.
* **Quoted values:** "**Date:** Friday, October 23, 2026 — awards night"; "**Time:** 5:00 PM – 9:00 PM";
  "**Where:** Founder's Inc — 2 Marina Blvd B300, San Francisco, CA 94123"; hosts "Founders Inc, OSS4AI,
  Open Intelligence Foundation".
* **Fields written:** date/time/location/organizer as quoted; category "Technology, AI & gaming"; `bucket` special /
  `cadence` single-date; authority "Official organizer".
* **Cost:** **left blank** — no price on the event page or on the official registration listing
  (<https://luma.com/7ebvz0oq>, "Approval Required"). Recorded as `flag-open-source-ai-cost`.
* **Irregularity recorded:** `flag-open-source-ai-awards-time` — the organizer's registration listing states
  "**5:00 PM - 10:00 PM PDT**" for the same event while the organizer's event page states "5:00 PM – 9:00 PM".
  The row keeps the event-page value and the conflict is flagged rather than averaged.

### 2.4 Review record: Open Source AI Week 2026 — `open-source-ai-week-2026`

* **Official source:** <https://opensourceaiweek.com/>.
* **Quoted values:** "Ten days · **October 16-25, 2026** · **San Francisco Bay Area**"; "**66** Events across the Bay
  Area"; "**200+** Participating organizations"; calendar entries outside the city (for example "MITAI Conference
  2026 … Computer History Museum, **Mountain View**").
* **Disposition:** held as `partial_sf_program` on **Flagged for Review** rather than published as a single city-only
  row, because the program is Bay Area–wide. Its two San Francisco flagship programs are catalogued individually
  (2.2 and 2.3). No cost is asserted for the week itself.

## 3. Cost-classification correction applied this session

Four published rows carry sourced wording that names a gate but **no price**:

| Row | Sourced admission text | Old class | New class |
| --- | --- | --- | --- |
| Microsoft Ignite (`microsoft-ignite-2026`) | "Registration required" | Paid / ticketed | Registration / invitation — no price published |
| AGU26 Annual Meeting (`agu-annual-meeting-2026`) | "Registration required" | Paid / ticketed | Registration / invitation — no price published |
| Bay to Breakers (`bay-to-breakers-2027`) | "Registration required" | Paid / ticketed | Registration / invitation — no price published |
| J.P. Morgan Healthcare Conference (`jpm-healthcare-conference-2027`) | "By invitation only (invitations not transferable)" | Paid / ticketed | Registration / invitation — no price published |

Calling these "Paid" was an inference the brief forbids. `build.py:cost_class` now returns a distinct `restricted`
class for registration/invitation wording with no price, and a `not-stated` default for text that names no cost at
all. No row's sourced `admission` text was altered, no row was moved into the free list, and the change is recorded
as `flag-registration-only-cost-class` with each row's official link.

Resulting split after this pass: **151 published rows → 57 free or partly free (12 of them upcoming),
13 priced/ticketed, 4 registration-or-invitation-only, 77 with no published price.**

## 4. Rows deliberately not added

| Candidate | Why it was not added |
| --- | --- |
| Hardly Strictly Bluegrass 2027 (aggregators list Oct 8–10, 2027) | Official festival site publishes no 2027 dates — `flag-hsb-2027-dates-unconfirmed`. |
| The Detour SF "Free Play Tuesday" arcade night | Official venue page could not be fetched (two attempts failed); the only descriptions found were on aggregators. |
| Emporium SF arcade "Industry Night" | Only aggregator descriptions found; no official page verified, and the offer is a token promotion rather than a dated public event. |
| GobbleCon (Thanksgiving weekend tabletop gaming, no admission fee) | Official site places it at the "Burlingame Hyatt Regency SFO" — outside the City and County of San Francisco. |
| Open Source AI Week community events outside SF (e.g. Mountain View) | Outside city limits; the umbrella program is a review record and only its SF flagships are published. |
| SF.gov citywide calendar listings checked on 2026-10-18 | The visible upcoming entries were board/committee meetings and an employee flu clinic, not public events. |

## 5. Reproducibility

* Data changes are applied by `research/patch-3977d9cb.py` (idempotent; safe to re-run).
* `python3 build.py && python3 verify.py` regenerates every page from `data/events.json` and re-checks the catalog,
  the free/paid separation, focus ordering, date-first ordering, source-link coverage and local navigation.
* Every new row and every new flag carries its own official source link on the generated pages, so each line can be
  re-checked by hand from the live site.
