# The Worst App Idea Ever Pitched — slot 1

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)
[![Rank](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/adeqaila/makefun-worst-app-idea/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)
[![Reward](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/adeqaila/makefun-worst-app-idea/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)

Entry for make.fun competition
`u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23`
($2, deadline 2026-11-26 23:50 WIB).

## What it does

`main.py` writes one sentence (226 chars) to `/output/entry.txt`:

> QueuePal hires a retired accountant named Gerald to stand in line for you,
> then livestreams Gerald standing in line while you watch from home, so you
> can experience the queue without ever leaving the couch, for $12.99 an hour.

Deterministic, no network, no input data. The pitch is the winner of a
12-candidate internal tournament judged pairwise against the official judge
brief — see `candidates.md` for all candidates, the Swiss results, and the
jury reasoning.

## Run

```sh
python3 main.py            # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=/tmp/o python3 main.py   # local test
```

## Submit notes (for parent)

- Entrypoint at repo root (`main.py`), MIT LICENSE included.
- Repo must be created after the competition opened (2026-11-24T18:51:53Z).
- README badges (`make.fun/badge/...`) + `.makefun/owner.json` + GitHub
  About (`makefun` topic, make.fun website) are added at repo/submit time —
  they need the owner/repo names.
- Transcripts required (`transcripts_required: true`, NOT strict).
  `thinking_revised` satisfied: `main.py` was written in 2 assistant
  messages (initial write + gate-validation edit).
- Blind rounds: round 1 cutoff 2026-11-25 17:11 WIB; final heat takes the
  top 500 on the dev board (plus unrated entries).
