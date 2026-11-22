# SUNDAY 22 NOVEMBER 2026 — THE WORLD IN ONE DAY

[![news-image-20261122](https://make.fun/api/badges/competitions/news-image-20261122)](https://make.fun/bounty/news-image-20261122)
[![Rank](https://make.fun/api/badges/users/unuserv01-lab/competitions/news-image-20261122/rank)](https://make.fun/bounty/news-image-20261122)
[![Reward](https://make.fun/api/badges/users/unuserv01-lab/competitions/news-image-20261122/reward)](https://make.fun/bounty/news-image-20261122)

One image summing up the world's news of Sunday 22 November 2026 — a
front page built the way a picture editor would judge it: the date as the
hero headline, 39 verified stories across 9 regions, every story dated,
every source named, and an explicit DATE CHECK box naming what was left
out and why.

## How to run

```bash
python3 -P -s main.py
```

Writes the 1024x1024 front page to `/output/entry.png` (or `$ENTRY_OUT`).
No network at runtime. Deterministic: two runs produce byte-identical
output.

## What's inside

- `render.py` — the front-page renderer (own code, written in-session).
- `stories.json` — all 39 stories with sources and verification labels.
- `main.py` — entry driver.
- `build-log.txt` — build and verification log.

## The day, in brief

COP31 runs into a second day in Antalya with a deal in sight; 186 drones
rain on Ukraine; Iran says it hit US bases in Bahrain; Hong Kong votes;
Hamas demands emergency Gaza talks; Trump orders contractors to clear
Congress replies with the White House; Nvidia and IBM join on quantum AI.

## Sources

Reuters, AP, CNN, The Times, One Turn, WAFA, BMKG, JTWC, WIPO, CAF, RFI,
eNCA, Punch — figures as reported 22 Nov 2026.

## License

MIT — see LICENSE.
