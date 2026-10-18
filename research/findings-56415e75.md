# Findings & analysis register — session `arena/56415e75-maltaproj7` (2026-10-18)

Computed directly from the merged `data/events.json` (this session's
`research/patch-56415e75.py` applied on top of `origin/main` `81425ee`, merge of
PR #29) using `build.py`'s own `cost_class()` so the numbers match the published
site. Reference date: **2026-10-18**. A row is only `Free` when its linked
official page says so; "no price published" is never treated as free.

## 1. Catalog shape

| Measure | Count |
| --- | --- |
| Published city-only rows | **158** |
| — regularly occurring (weekly / monthly / seasonal / annual) | 101 |
| — dated special events | 57 |
| Review-only records (multi-city, cancelled, outside city, or unconfirmable) | 16 |
| Field-level flags published on Flagged for Review | 44 |
| Categories | 9 |
| Upcoming or still running on 2026-10-18 | 63 |

Cadence split: 74 annual, 35 single-date, 21 single-event, 14 weekly, 9 seasonal,
4 monthly, 1 dated-program.

Source authority: 101 official organizer, 22 government, 19 official venue,
13 official venue / federal trust, 3 trusted civic (SF Travel). **Every published
row carries an official or government source link; none relies on an aggregator.**

## 2. What it costs to attend — the central finding

| Cost label | Rows | Share |
| --- | --- | --- |
| Free | 54 | 34% |
| Free or partly free (mixed) | 12 | 8% |
| Paid / ticketed | 16 | 10% |
| **Cost not stated by the official source** | **76** | **48%** |

Almost **half the catalog has no published price**. That is a property of the
official sources, not a gap in this audit: the Moscone Center convention
listings, most SFMTA travel updates and the medical/industry association meetings
publish dates and venues but no admission figures. Those rows are labelled *Cost
not stated* and are listed with their source links on Flagged for Review; they are
never shown as free.

Practical consequence for the brief's free-first requirement: **66 rows (42%)**
are free or partly free, and 54 of them can be called free outright.

## 3. Free events near today (the executive-summary window)

| Window from 2026-10-18 | Events starting | of which free or partly free |
| --- | --- | --- |
| Next 7 days | 10 | 5 |
| Next 30 days | 26 | 10 |
| Next 90 days | 37 | 15 |

Free rows whose start date is on or after 2026-10-18 (16 rows), soonest first:

| Date | Event | Category |
| --- | --- | --- |
| 2026-10-18 | Sunday Streets Excelsior — 2026 season finale | Community & culture |
| 2026-10-23 | From the E Excelsior Night Market | Food & markets |
| 2026-10-24 | Lit Crawl SF | Books & ideas |
| 2026-10-24 | Afro-Filipino Jazz Project (YBG Festival) | Music & performing arts |
| 2026-10-30 | Scaregrove (SF Rec & Park, Sigmund Stern Grove) | Community & culture |
| 2026-10-31 | Foodwise cooking demo — Sofía Jiménez, Tutuli Mexican Bakery | Food & markets |
| 2026-10-31 | Halloween Hoopla (YBG Festival, 26th annual) | Community & culture |
| 2026-11-13 | Bhangra & Beats Night Market | Community & culture |
| 2026-11-20 | From the E: Harvest Night Market (Excelsior) | Food & markets |
| 2026-11-21 | Foodwise cooking demo — Ann M. Evans and Georgeanne Brennan | Food & markets |
| 2026-12-05 | Foodwise cooking demo — Anna Voloshyna, Ukraïne | Food & markets |
| 2026-12-12 | Foodwise Black Holiday Market | Food & markets |
| 2026-12-19 | Foodwise cooking demo — Florencia Ramirez, The Kitchen Activist | Food & markets |
| 2027-04-10 | Northern California Cherry Blossom Festival | Community & culture |
| 2027-07-03 | Fillmore Jazz Festival | Music & performing arts |
| 2027-10-10 | San Francisco Italian Heritage Parade | Community & culture |

Two more free programmes are running right now and are catalogued as seasons
rather than dated rows: **YBG Festival** (free outdoor performances through
November) and **Sunday Streets SF — 2026 season**. Two more free rows are
"free to watch, paid to sit" and therefore classed *mixed*: the San Francisco
Chinese New Year Parade 2027 and Renegade Craft Fair.

## 4. Focus categories named in the brief

**Gaming & AI/technology (17 rows).** Only **2 are free**: *Day of the Devs —
San Francisco Edition* (the organizer states "Admission is always free, for
developers and players alike, and open to all ages") and *SF Tech Week — SFPL
programs* ("All programs are free"). Of the other 15, 4 publish prices (Cloudflare
Connect, AI Engineer Code Summit, GDC Festival of Gaming, Microsoft Ignite) and 11
publish none. This is the clearest structural finding of the audit — **San
Francisco's large gaming and AI events are commercial; the city's free gaming/AI
programming is small and institutional (library workshops, nonprofit showcases),
not festival-scale.**

**Music (24 rows, 14 free or partly free).** Free music is the strongest area of
the catalog: Hardly Strictly Bluegrass, Stern Grove Festival, Fillmore Jazz
Festival (2026 and 2027), YBG Festival and its Afro-Filipino Jazz Project, Free
Shakespeare in the Park, SF Porchfest, Comedy Day, People in Plazas, Golden Gate
Park Band, World Arts West, Bay Area International Deaf Dance Festival, and Flower
Piano (free with paid add-ons).

**Everything else.** Free or partly free rows by category: Community & culture 28,
Music & performing arts 14, Food & markets 8, Fairs & nightlife 7, Books & ideas 3,
Film & media 2, Technology/AI/gaming 2, Sports & outdoors 1, Professional &
academic 1.

## 5. Recurring vs special — what the split shows

Regularly occurring programming (101 rows) is dominated by weekly farmers markets,
free museum days and open-streets events — dependable, free, and verifiable from a
city or institutional source. Dated special events (57 rows) carry nearly all of
the paid/ticketed inventory and nearly all of the *cost not stated* rows, because a
one-off conference or festival is the format that publishes dates without prices.

## 6. Irregularities carried to Flagged for Review

Three new flags were filed this session (`flag-litcrawl-suggested-donation`,
`flag-sunday-streets-route-conflict`, `flag-from-the-e-general-hours-mismatch`),
bringing the register to 44. All are nonblocking: each publishes what the official
sources actually say and records the disagreement instead of resolving it by
guesswork. A fourth (the Sunday Streets "free wording" nuance) was dropped because
`arena/8c40d1c6-maltaproj7` had already filed the same point as
`flag-sundaystreets-free-wording`.

Two corrections were applied where the official page was more current than the row:
Lit Crawl's hours and no-RSVP wording, and GDC 2027's pass-rate window, whose
"super early" deadline (Oct 9, 2026) had already passed on the audit date. One
organizer-domain observation is also worth a reviewer's eye: the Fillmore Jazz
Festival's two rows cite `www.fillmorejazzfest.com` and `fillmorejazzfest.com` —
the same official site with and without the `www` prefix, both live on 2026-10-18.
