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

- Source file: `AI_Agent_TAM_2026-04.xlsx`
- Software TAM total: **$496B** (was $450B in 2025-Q1 baseline → **+$47B / +10%**)
- Labor TAM total: **$9.60T** (workforce sizes stable)
- Overall Labor/SW ratio: **19.4×** (was 19.9× → tightening as software catches up in AI-native categories)
- 2026-04 cycle: 30 changes — see in-app banner for the full list

### 2026-04 update highlights

- **Code Generation Agent** — SW TAM $12B → **$28B** (+133%, largest single revision). Cursor $60B / $2B ARR; Claude Code & Codex mainstream.
- **Legal cluster** (Contract / Compliance / Case / IP / Tax) — SW TAMs +45-75% on Harvey $11B, Legora $5.55B, YC W26 super-agent platforms.
- **CX & Translation** — Decagon $4.5B Series D, Sierra $10B / $150M ARR, Wonderful $2B redefines translation-CX boundary.
- **Drug Discovery** — Insilico INS018_055 Phase IIa success; SW TAM $4B → $6.5B; displacement 35-50% → 45-65%.
- **Humanoid robotics** — Figure AI $39B + Helix 02 VLA breakthrough; physical-task steps moving PARTIAL → FULL.
- **Capability** — Claude Opus 4.6, GPT-5.4, Gemini 3.1 Pro all at 1M context. Computer-use upgraded to FULL on UI workflows.
- **Q1 2026 macro** — record $300B quarterly VC, AI = 80% ($242B). Mega-rounds: OpenAI $122B / Anthropic $30B Series G / xAI $20B / Waymo $16B.
