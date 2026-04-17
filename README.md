# Agent Mapping — AI Agent TAM Atlas

Interactive single-page dashboard mapping the AI Agent opportunity across **10
categories × 201 sub-tracks**, comparing **Software TAM** (AI product layer) to
**Labor TAM** (human spend addressable by AI Agents).

Live: https://agent-mapping.vercel.app  *(once deployed)*

## What's in this repo

```
├── index.html       # Self-contained dashboard (Chart.js via CDN)
├── data.js          # Generated data — window.TAM_DATA = [...]
├── build_data.py    # Parser: reads the source .xlsx → emits data.js
└── README.md
```

The site is pure static HTML/JS, so Vercel serves it with no build step.

## Features

- **6 live KPI cards** — totals recompute as filters change
- **5 filters + full-text search** — category, AI impact, net effect, valuation tier, status
- **4 Chart.js visualizations**
  1. Log-scale horizontal bar — SW vs Labor TAM per category
  2. Log-log bubble scatter — primary × secondary TAM, bubble size = displacement rate, clickable
  3. Donut — AI impact type distribution
  4. Donut — valuation tier distribution
- **Sortable, expandable table** — click any row for methodology, representative companies, funding, insight

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
- Software TAM total: **$496B**
- Labor TAM total: **$9.60T**
- Average Labor/SW leverage: **24.4×**
