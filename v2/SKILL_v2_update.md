---
name: ai-agent-tam-v2-update
description: Update/extend the Agent Mapping v2 framework (78 tracks · 14 work families + overlays · 6-axis · coupling-aware). Use whenever Patrina asks to refresh the v2 TAM map, add tracks, re-score, run a cycle, or map a new YC batch. ALWAYS use this over starting from scratch or over the v1 skill.
---

# Agent Mapping v2 — Update & Maintenance Skill

Supersedes the v1 skill (`ai-agent-tam-update`, which encodes the 205-track/10-category/additive-columns model and will corrupt v2). v2 is a **coupling-aware, 6-axis, falsifiable** rebuild.

## What v2 is
- **78 tracks** across **14 work families** (W1–W14) + 3 overlays (W7 relational, Services-Arbitrage, Autonomous Business Ops) + W15 R&D. Partitioned by **substitution physics**, not software category.
- Data of record: `research/v2_master.json` (78 rows), `AI_Agent_TAM_v2_2026-09.xlsx`, dashboard in `dashboard/`.
- Companion docs: `research/p6_ic_memo.md`, `research/p5_deepdives.md`, `research/p6_headcount_view.md`, `research/p3_frozen_taxonomy.md`, `research/p0_foundation.md`.

## The non-negotiable rules (never break these)
1. **Coupling.** For outcome-priced / labor-denominated tracks, SW-TAM and Labor-TAM are the SAME dollars. Size as **capture-rate × displaced-labor**. NEVER add the two columns. Additive (augment-copilot) tracks may keep SW separate. Every track carries a `coupled` boolean.
2. **Denominator tags.** `[W]` displaceable wage bill · `[L]` latent/unmet demand · `[$]` market-revenue proxy. Never sum across tags. Overlay families are non-additive re-cuts of parents.
3. **Sourcing.** Labor TAM built bottom-up from Tier-1 (BLS OEWS / ILO), primary over VC narrative. Any figure >$10B needs ≥2 independent sources or it is logged "unverified" and excluded from headlines. Distinguish real ARR from bookings/pilots/valuation (agent-washing rife; the verified-ARR set is ~8 names deep).
4. **Production discount.** Deployment lags capability ~10× (MIT 95% zero-P&L). Discount any high-conviction claim not corroborated by PRODUCTION evidence (not POC/press).
5. **Ranges not points; dated falsifiable indicator per track; anti-consensus note where you disagree with VC consensus.**

## The 6 scoring axes (0–5, per track)
- **V** outcome verifiability (strongest displacement predictor — gate here first)
- **H** autonomy-horizon required (0 single-shot → 5 weeks unsupervised; today ~1.5 days @50% reliability, far shorter @80%; OSWorld real-world ~20%)
- **P** physical gating (0 none → 5 dexterous-unstructured; brain mature, body is the moat)
- **R** regulatory gating (0 none → 5 statutory prohibition; note direction — can retreat, e.g. EU Omnibus)
- **L** lab-capture risk (0 safe → 5 labs ship it natively; rising — Cowork, ChatGPT Work, Gemini/Antigravity)
- **D** data/context moat (doc-moat eroded; durable moat = proprietary/workflow-embedded/physical data)

Plus per track: pricing regime, current capture rate, value-capture verdict (startup/incumbent/model-lab/oss-deflation/mixed), predicted-12mo direction, conviction, HTC entry point.

## Update procedures (5 types + velocity)
1. **New track** — qualify (identifiable labor market? agent-delivered? distinct? commercial evidence?), assign family, score 6 axes, size (coupled model if outcome-priced), tag [W]/[L]/[$], set net-effect + conviction + falsifiable indicator. Reconcile double-counts ONCE (e.g. W1.1 code ↔ SA.4 AMS).
2. **TAM revision** — re-derive bottom-up; carry the 4×/5×/6× comp band for physical families; ranges only.
3. **Displacement/score change** — update V/H/P/R/L/D + net-effect; require production evidence for upward moves.
4. **Capability unlock** — new model/product → which steps move FULL/PARTIAL/NO in which deep-dive tracks; update L (lab-capture) where labs ship a native vertical.
5. **Players** — funded cos with stage/valuation, VERIFIED flag (ARR vs bookings vs valuation), incumbent response, lab-native threat.
6. **Velocity** — maintain the predicted-12mo ratio per track; each cycle tests it; residuals (compressing faster/slower than predicted) are the anti-consensus signal generator.

## Cycle workflow (bimonthly) — multi-agent
Reuse the P0–P6 pipeline pattern (see the workflow scripts under `.claude/.../workflows/scripts/`):
1. **P0 Foundation refresh** — capability frontier (METR horizon, new models), labor-pool deltas, pricing-regime shifts, source audit.
2. **P2 Blind sweeps** (7) — capital / accelerators+talent / labor-signal / product+protocol / incumbent / non-US / failure. Run BLIND to the taxonomy; collide after.
3. **P3 Collision** — reconcile bottom-up vs the frozen 78; CORE / WHITE-SPACE (too-early/blocked/thesis-wrong) / HYPE-CHECK / DROP. Kill/merge/split.
4. **P4 Evidence packs** — Tier-A (full + adversarial verify on >$10B / >50× claims) vs Tier-B (light batch). Verify separates real ARR from agent-washing.
5. **P6 Synthesis** — regenerate v2_master.json → data.js → dashboard, xlsx, and refresh the IC memo's falsifiable predictions.

## Guardrails
- Gate at taxonomy-freeze (G2): get Patrina's sign-off on family/track count and Tier-A budget before the P4 fan-out.
- Watch the leading indicators from the IC memo: W8 (agent-economy job-creation) growth rate, coupled-revenue mix, audited BPO-operator guidance, METR horizon doubling.
- Deploy is MANUAL (`vercel --prod` if hosted) — see [[project-agent-mapping-deploy]].
- Sessions can hit account usage limits on big fan-outs — run P4/P5 in moderate (~13-agent) chunks; workflows are resumable (`resumeFromRunId`).
