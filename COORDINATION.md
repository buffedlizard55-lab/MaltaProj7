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
