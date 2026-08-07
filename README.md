# Agent Mapping — AI Agent TAM Atlas

Interactive single-page dashboard mapping the AI Agent opportunity across **10
categories × 201 sub-tracks**, comparing **Software TAM** (AI product layer) to
**Labor TAM** (human spend addressable by AI Agents).

Live: https://agent-mapping.vercel.app  *(once deployed)*

## What's in this repo

```
├── index.html       # Self-contained dashboard (Chart.js via CDN)
├── data.js          # Generated track data — window.TAM_DATA = [...]
├── update.js        # Generated change log — window.TAM_UPDATE = {...}
├── build_data.py    # Parser: reads the source .xlsx → emits data.js + update.js
└── README.md
```

The site is pure static HTML/JS, so Vercel serves it with no build step.

## Features

- **📅 What's Changed banner** — collapsible section at the top shows TAM revisions, displacement updates, capability unlocks and key player signals from the latest bimonthly cycle (auto-extracted from the Change Log sheet)
- **6 live KPI cards** — totals recompute as filters change
- **5 filters + full-text search** — category, AI impact, net effect, valuation tier, status
- **4 Chart.js visualizations**
  1. Log-scale horizontal bar — SW vs Labor TAM per category
  2. Log-log bubble scatter — primary × secondary TAM, bubble size = displacement rate, clickable
  3. Donut — AI impact type distribution
  4. Donut — valuation tier distribution
- **Sortable, expandable table** — click any row for methodology, representative companies, funding, insight
- **Track-name click-through** — clicking a track in the update banner auto-filters the table to that track

## Refreshing the data

1. Replace the source .xlsx (see `SRC_PATH` at the top of `build_data.py`)
2. `python3 build_data.py`  → regenerates `data.js`
3. Commit & push — Vercel auto-redeploys

## Methodology

Software TAM and Labor TAM figures cross-validated from Goldman Sachs
Occupational Automation Study, McKinsey Task Automation Fractions, WEF
Future of Jobs, Grand View Research and MarketsandMarkets.

- 🔴 **Net Compression** — AI primarily substitutes labor; total spend declines
- ✅ **Net Expansion** — AI creates new demand / democratizes access; total market grows
- 🟡 **Mixed** — both dynamics present, net direction depends on price elasticity

## Current baseline

- Source file: `AI_Agent_TAM_2026-08.xlsx`
- **Tracks: 205** (was 201 → **+4 new tracks**, first count change since baseline)
- Software TAM total: **$525B** (was $496B in 2026-04 → **+$29B / +5.8%**)
- Labor TAM total: **$9.92T** (was $9.60T → +$315B from the 4 new tracks)
- Overall Labor/SW ratio: **18.9×** (was 19.4× → 4th consecutive tightening cycle)
- 2026-08 cycle: 18 changes + 4 new tracks — see in-app banner for the full list

### 2026-08 new tracks (Type 1)

- **Autonomous Penetration Testing Agent** (#14, Dev & Tech) — SW $3B / Labor $25B / 8.3× / Expansion. XBOW $1B+, Hex Security $172M; distinct from defensive Security Scanning.
- **Robotic / Embodied Foundation Model Platform** (#28, Agent Infra) — SW $2.5B / Labor $120B / **48×** / Expansion. Skild $15B, Physical Intelligence, World Labs — pure-software robot brain, highest Labor/SW arbitrage in the framework.
- **Ambient Clinical Documentation / Scribe Agent** (#21, Healthcare) — SW $2B / Labor $90B / **45×** / Expansion. Abridge $5.3B, Ambience $1.25B.
- **Voice Agent Platform / Infrastructure** (#29, Agent Infra) — SW $3.5B / Labor $80B / 22.9× / Mixed. Vapi $500M, ElevenLabs $11B; Gartner: convo-AI cuts $80B contact-center labor in 2026.

### 2026-08 update highlights

- **SpaceX acquired Cursor** for **$60B** all-stock (Jun 16) — largest VC-backed startup acquisition ever; preempted the planned $50B Series E.
- **Code Generation Agent** — SW TAM $28B → **$40B** (+43%). Claude Code alone $8B ARR / 54% share; displacement 55-75% → **65-85%** on Fable 5 (~80% SWE-bench Pro).
- **Anthropic** closed **$65B Series H at $965B** (May 28) + confidential IPO filing Jun 1; $47B ARR overtakes OpenAI (~$25B).
- **Capability tier shift** — Claude Fable 5 / Mythos-class (Jun 9); GPT-5.6 Sol/Terra/Luna (Jul 9); OpenAI "Astra" announced Aug 1 with 10 solved open math problems.
- **Humanoid inflection** — Unitree launches first profitable-humanoid IPO (STAR Market, $620M at ~$5.9B, 35% net margin); Figure 03 hits 1,000th unit; Industrial Robot SW TAM $8.5B → $10.5B.
- **Financial Services opens** — first-ever category entries: Ramp $750M @ $44B, Mercury $200M @ $5.2B, Capital One × Brex $5.15B.
- **Drug Discovery** — Isomorphic $2.1B Series B (largest AI-drug round ever) + Insilico × Takeda; SW TAM $6.5B → $8.5B.
- **Compliance headwind** — EU Digital Omnibus delays Annex III high-risk obligations to Dec 2027; first downward-timing signal in the framework.
- **Q2 2026 macro** — $200B+ quarterly VC (2nd-largest ever), H1 $510B > all of 2025; OpenAI + Anthropic = 43% of H1 funding.
