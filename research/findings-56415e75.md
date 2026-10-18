# Findings & analysis register — session `arena/56415e75-maltaproj7` (2026-10-18)

Computed directly from `data/events.json` after this session's pass
(`python3 research/patch-56415e75.py`). Reference date: **2026-10-18**.
Cost classes use the same house rule as `build.py`: a row is only `Free` when its
linked official page says so.

## 1. Catalog shape

| Measure | Count |
| --- | --- |
| Published city-only rows | **152** |
| — regularly occurring (weekly / monthly / seasonal / annual) | 100 |
| — dated special events | 52 |
| Review-only records (multi-city, cancelled, outside city, or unconfirmable) | 16 |
| Field-level flags published on Flagged for Review | 38 |
| Categories | 9 |

Cadence split of the published rows: 74 annual, 30 single-date, 21 single-event,
14 weekly, 9 seasonal, 3 monthly, 1 dated-program.

Source authority split: 96 official organizer, 21 government, 19 official venue,
13 official venue / federal trust, 3 trusted civic (SF Travel). **Every published
row carries an official or government source link; none relies on an aggregator.**

## 2. What it costs to attend — the central finding

| Cost label | Rows | Share |
| --- | --- | --- |
| Free | 51 | 34% |
| Free or partly free (mixed) | 10 | 7% |
| Paid / ticketed | 17 | 11% |
| **Cost not stated by the official source** | **74** | **49%** |

Roughly **half the catalog has no published price**. That is a property of the
official sources, not a gap in this audit: the Moscone Center convention
listings, most SFMTA travel updates and the medical/industry association
meetings publish dates and venues but no admission figures. Those rows are
labelled *Cost not stated* and are listed with their source links on Flagged for
Review; they are never shown as free.

Practical consequence for the brief's free-first requirement: **61 rows (40%)**
are free or partly free, and only 51 of them can be called free outright.

## 3. Free events near today (the executive-summary window)

| Window from 2026-10-18 | Events starting | of which free or partly free |
| --- | --- | --- |
| Next 7 days | 9 | 4 |
| Next 30 days | 24 | 8 |
| Next 90 days | 31 | 9 |

Free rows whose start date is on or after 2026-10-18 (11 rows), soonest first:

| Date | Event | Category |
| --- | --- | --- |
| 2026-10-18 | Sunday Streets — Excelsior Community Block Party | Community & culture |
| 2026-10-24 | Lit Crawl SF | Books & ideas |
| 2026-10-24 | Afro-Filipino Jazz Project (YBG Festival) | Music & performing arts |
| 2026-10-30 | Scaregrove (SF Rec & Park, Stern Grove) | Community & culture |
| 2026-10-31 | Halloween Hoopla (YBG Festival, 26th annual) | Community & culture |
| 2026-11-13 | Bhangra & Beats Night Market | Community & culture |
| 2026-12-12 | Foodwise Black Holiday Market | Food & markets |
| 2027-02-20 | San Francisco Chinese New Year Parade | Community & culture |
| 2027-04-10 | Northern California Cherry Blossom Festival | Community & culture |
| 2027-07-03 | Fillmore Jazz Festival | Music & performing arts |
| 2027-10-10 | San Francisco Italian Heritage Parade | Community & culture |

Two more free programmes are running right now and are catalogued as seasons
rather than dated rows: **YBG Festival** (free outdoor performances through
November) and **Sunday Streets SF — 2026 season**.

## 4. Focus categories named in the brief

**Gaming & AI/technology (17 rows).** Only **2 are free**: *Day of the Devs —
San Francisco Edition* (the organizer states "Admission is always free, for
developers and players alike, and open to all ages") and *SF Tech Week — SFPL
programs* ("All programs are free"). The other 15 are trade conferences: 4 with
published prices (Cloudflare Connect, AI Engineer Code Summit, GDC Festival of
Gaming, Microsoft Ignite) and 11 whose official pages publish no price. This is
the clearest structural finding of the audit — **San Francisco's large gaming and
AI events are commercial, and the city's free gaming/AI programming is small and
institutional (library and nonprofit showcases), not festival-scale.**

**Music (24 rows, 14 free or partly free).** Free music is the strongest area of
the catalog: Hardly Strictly Bluegrass, Stern Grove Festival, Fillmore Jazz
Festival (2026 and 2027), YBG Festival and its Afro-Filipino Jazz Project,
Free Shakespeare in the Park, SF Porchfest, Comedy Day, People in Plazas, Golden
Gate Park Band, World Arts West, Bay Area International Deaf Dance Festival, and
Flower Piano (free with paid add-ons).

**Everything else.** Free or partly free rows by category: Community & culture
28, Music & performing arts 14, Fairs & nightlife 7, Books & ideas 3, Sports &
outdoors 2, Film & media 2, Food & markets 2, Technology/AI/gaming 2,
Professional & academic 1.

## 5. Recurring vs special — what the split shows

Regularly occurring programming (100 rows) is dominated by weekly farmers markets
and free museum days — dependable, free, and easy to verify from a city or
institutional source. Dated special events (52 rows) carry nearly all of the
paid/ticketed inventory and nearly all of the *cost not stated* rows, because a
one-off conference or festival is the format that publishes dates without
prices.

## 6. Irregularities carried to Flagged for Review

Four new flags were filed this session
(`flag-litcrawl-suggested-donation`, `flag-sunday-streets-route-conflict`,
`flag-sunday-streets-free-wording`, `flag-ybgf-season-end-source`), bringing the
register to 38. All are nonblocking: each publishes what the official sources
actually say and records the disagreement instead of resolving it by guesswork.
Two corrections were applied where the official page was more current than the
row — Lit Crawl's hours/cost wording and GDC 2027's pass-rate window, whose
"super early" deadline (Oct 9, 2026) had already passed on the audit date.
