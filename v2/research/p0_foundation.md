# Phase 0 — Foundation Brief (Agent Mapping v2)

HTC internal · 2026-09-01 · 5 agents, 262k tokens, live web research. Feeds P1.

## 1. Capability frontier (Sept 2026)
Frontier is **long-horizon agentic autonomy**, not raw Q&A. Binding constraints moved off model
capability/context onto: **outcome verifiability, reliability-at-horizon, physical hardware + proprietary
real-world data**, and two structural risks (lab-capture, self-imposed safety gating).

- **Autonomy horizon doubled in 6 months**: METR 50%-reliability horizon ~14.5h (Opus 4.6, Feb) → ~32h (Sept), doubling rate accelerating 7mo→4mo. Concrete: Stripe 50M-line Ruby migration in a day (Fable 5). **Caveat: that's the 50% mark.** 80%-reliability horizon far shorter; messy real-world computer-use best system only **~20.6% (OSWorld 2.0)**. "Runs for a day" = true for well-scoped verifiable code-shaped work; NOT for open-ended real-world.
- Anchors: **Fable 5 / Mythos 5** (Anthropic, Jun 9 — 95% SWE-bench Verified, safety gate ships in-model), **Opus 4.8** (powers Cowork), **GPT-5.6 Sol/Terra/Luna** + **Astra** (OpenAI — Astra "cannot rule out" Critical cyber; frontier now gated by safety not ability), **Gemini 3 Deep Think** (10M ctx, IMO/ICPC gold), **DeepSeek V4-Pro + Harness** (open commoditization floor).
- **Axis read**: V = strongest displacement predictor (gate on it first). H = ~1.5 days@50%, gated@80%. P = brain decoupled, moat moved to atoms. R = labs self-gating bio/cyber/chem ahead of regulation. **L = lab-capture rising sharply** (Cowork, ChatGPT Work, Gemini/Antigravity ship native verticals over thin startups). D = doc-moat eroded (1M std/10M frontier); moat now proprietary/workflow-embedded/physical data. Voice = production-real (19% inbound contact-center volume).

## 2. Labor base pool
- **Global pool ~$60T** (band $58–61T; formal-wage floor ~$48T). Basis: ILO labour-income-share 52.4% × world GDP ~$118T. **The $50T prior was 15–20% low.**
- **8 family priors** (Low–Med confidence; comp-per-head drives error, NOT headcount):

| Family | Pool | Conf |
|---|---|---|
| W1 Digital outcome-verifiable | $2.5–3.5T | Med |
| W2 Digital judgment-graded | $4–6T | Low |
| W3 Digital real-time interpersonal | $8–12T | Med |
| W4 Licensed sign-off gated | $4–6T | Med |
| W5 Physical structured | $5–7T | Low |
| W6 Physical dexterous/unstructured | $9–13T | Med |
| W7 Trust/relational premium | $3–5T | Low |
| W8 Agent-economy labor (net-new) | $10–20B, >100% YoY | Low |

- **MECE caveat**: families do NOT sum to the pool. W1–W7 midpoints ≈ $40–48T; ~$12–18T residual = agriculture (~$2–4T), informal/subsistence, domestic/personal service, low-skill misc — carve out separately, don't force-fit. Straddlers exist (nurse = W4+W6).
- **Services-arbitrage pool (converts FIRST)**: ~$0.9–1.1T vendor revenue (ITO ~$650B + BPO ~$330B). Contact-center **15–17M heads globally** = single most exposed concentration, clearest near-term wedge.
- **Conversion ordering (fast→slow)**: services-arbitrage/BPO → W1 → W3-support/W2-analysis → W5 → W4 → W6 → W7. W8 = net-new offset + leading indicator.
- Weakest families to pressure-test: **W2, W5, W7, W8**.

## 3. Pricing & the coupling correction (MAJOR methodological change)
- Regimes 2026: per-seat **declining** (21→15%), usage **ubiquitous as component** (~92%), **outcome/resolution rising fastest** (VC favorite ~26%, concentrated where success unit is clean), **hybrid now the standard primary** (~37–41%).
- **Coupling thesis**: outcome pricing meters the *worker's output* against the *human wage*, not a software budget. SW TAM and Labor TAM are then **two views of one quantity, not two**. Capture rates: **Sierra ~11%, Intercom Fin ~7%, Decagon ~4–11%, XBOW ~20–40%** of displaced labor cost.
- **Deflationary transfer**: task moving from ~$13.50 human → ~$1.00 agent evaporates ~$12.50 of measured activity. **Adding SW+Labor columns double-counts AND overstates (by 60–93% of the labor line in coupled categories).**
- **v2 sizing rule**: (1) segment by pricing metric — only outcome/labor-denominated categories are coupled; seat/token augment-copilots stay additive. (2) For coupled categories model ONE contested pool split into human-retained + vendor-captured (capture×displaced) + disappeared-surplus. (3) **Vendor realized TAM = capture-rate × displaced-labor** — the bet is capture-rate *expansion*, not adding two big numbers.

## 4. Sourcing rules (enforce on every figure)
Tier-1 = BLS OEWS / ILO / OECD / World Bank / IMF / WEF (sentiment) / GS-McKinsey-BCG (ranges not points) / company filings / peer-review / registries. Tier-2 (corroborate, never anchor) = Gartner-IDC-Forrester / report mills (Grand View, M&M, Mordor — direction/CAGR only) / PitchBook-Crunchbase (funding) / press (events not sizing) / aggregators (cite underlying).
**R1** >$10B needs ≥2 independent sources (≥1 Tier-1) else "unverified". **R2** labor-data primacy over VC narrative. **R3** vendor-ARR bottom-up as SW-TAM tiebreaker. **R4** provenance trace mandatory. **R5** definition-lock (reject >1.5× same-market-year spread). **R6** ranges not points. **R7** recency+methodology gates (reject >18mo stale). **R8** conflict disclosure. **R9** verify citation exists.
Slop flags: PR-wire-only provenance, circular citation, definition-shifting, false precision + round CAGR, no methodology, self-serving author, hallucinated citation, AI-boilerplate tells.

## 5. Handoff to P1
1. Don't treat 8 families as a partition or sum them; carve out the $12–18T residual; anchor to ISCO/BLS SOC crosswalks.
2. Decompose by geography-of-heads (advanced-econ comp 5–15× developing for same job); start with weak families W2/W5/W7/W8.
3. Gate scoring on **V and reliability-at-horizon** (50% vs 80%), not the horizon headline; OSWorld ~20% is the reality check.
4. Tag every track by pricing metric; apply coupling model to outcome-denominated tracks; capture rates low today, thesis is capture-expansion.
5. Sequence by conversion ordering; flag lab-capture (L) risk per track; carry W8 as net-new offset + leading indicator.
