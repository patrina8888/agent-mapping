# Agent Mapping v2 — Full Rebuild Research Architecture

**Status**: PLAN — research design & agent orchestration only. Nothing executed yet.
**Date**: 2026-09-01 · **Baseline being rebuilt**: v1 (2025-Q1 → 2026-08, 205 tracks, SW $525B / Labor $9.92T / 18.9×)
**Author**: HTC research (Patrina + Claude)

---

## 0. Mandate — why a full rebuild, not another increment

Five documented reasons, each traceable to v1's own change log:

1. **Capability regime change.** v1's taxonomy predates every load-bearing capability of 2026-H2: Mythos-class models (Fable 5, ~80% SWE-bench Pro), long-horizon multi-agent autonomy (GPT-5.6 / Astra), production computer-use, production voice, robotic foundation models decoupling brain from body, 1M-token context as standard. The map was drawn for a world where agents did minutes of work; they now do days.
2. **New demand has been born, not just new supply.** v1 maps AI onto *existing* human labor — a one-way lens. It cannot see labor categories *created by* agents (agent ops, eval engineering, agent audit/insurance — AIUC's seed round is the tell) or agent-to-agent commerce (UCP/ACP protocol war). A map of substitution misses the market of creation.
3. **Observed drift in v1 itself.** 78 of 205 tracks (38%) untouched across 3 cycles — either dead weight or invisible to the lens. Meanwhile Code Generation absorbed +233% TAM in 16 months inside a *single* track while Marketing holds 21 stale micro-tracks. Granularity is wrong precisely where value concentrates.
4. **Value capture moved.** Model labs now eat the application layer directly (Claude Code = $8B ARR, 17% of Anthropic revenue); outcome-based pricing (Sierra per-resolution, XBOW per-finding) collapses the SW-TAM-vs-Labor-TAM distinction that v1 treats as fixed. "Who captures" is now a first-class axis, not a footnote.
5. **The $9.94T filter was inherited, never audited.** v1 began from a pre-filtered "addressable labor" pool. v2 starts from the full global labor compensation pool (~$50T prior, Phase 0 validates) and re-derives the filter itself. That is what top-down means.

**What survives from v1 (proven invariants):**
- Labor TAM as the honest ceiling (never oversell SW TAM)
- Labor/SW ratio as the headline opportunity metric
- Net Effect classification (Expansion / Compression / Mixed) + Jevons test
- 3-source displacement validation (GS / McKinsey / WEF, updated editions)
- 4-section deep-dive structure (workflow → step-level capability → gaps → strategy)
- Source-quality tiers; cross-validation rule (>$10B ⇒ 2 independent sources)
- Change-log discipline

**Design goals for v2:**
| Goal | Meaning |
|---|---|
| Falsifiable | Every track and the framework itself carry dated 12-month indicators that can prove them wrong |
| Anti-consensus | Every hot cluster gets an explicit "what consensus believes / where it's wrong" statement |
| Bidirectional | Top-down derivation must collide with bottom-up evidence; disagreement is treated as signal, not error |
| Velocity-aware | Predict *rate* of ratio compression per track, not just its level |
| Capture-aware | Every track gets a verdict: value lands with startup / incumbent / model lab / open-source deflation |

---

## 1. The v2 analytical engine

### 1.1 Retained invariants
Labor ceiling · ratio metric · net effect · displacement methodology · deep-dive structure · source tiers (as listed above).

### 1.2 Six new scoring axes (0–5 each, per track)

| Axis | Question | Why it earns a slot |
|---|---|---|
| **V** — Outcome verifiability | Can the work product be checked cheaply and objectively? | Empirically the strongest predictor of conversion speed — code (tests pass) compressed 40×→15.5× in 16 months; unverifiable judgment work barely moved |
| **H** — Autonomy horizon required | Does the job need single-shot / minutes / hours / days / weeks of unsupervised agency? | The frontier is moving hours→days (GPT-5.6, Astra); H tells you *when* a track unlocks |
| **P** — Physical gating | None / structured-environment robotics / dexterous-unstructured | Hardware timelines are independent of software progress (v1 principle, now scored) |
| **R** — Regulatory gating | None / disclosure duty / licensed sign-off / statutory prohibition — *plus direction of travel* | EU Digital Omnibus proved regulation can retreat; R is a variable, not a constant |
| **L** — Lab-capture risk | Will Anthropic/OpenAI/Google ship this natively? | Coding: maxed (Claude Code). Browsing: high (Atlas folded into ChatGPT). Therapy: low. Existential for any vertical-agent investment |
| **D** — Data/context moat | Is proprietary context (EMR, ERP, case history, ledger) the real barrier? | Determines whether incumbents or startups win when capability arrives |

### 1.3 Conversion Velocity Score — the model, not just the map
Fit weights on the ~20 observed ratio-compression datapoints in v1's own change logs (2025-Q1 → 2026-08):
anchors spanning the space — Code 40×→15.5× (V high, R none: fastest), Contract Review 140×→80× (V med, R high), CX ~21×→12.7× (V med, H minutes), Elder Care 225×→200× (P extreme: slowest).
Output: **a predicted 12-month ratio for every track**. This converts the framework from a static map into a falsifiable model — each bimonthly cycle becomes a test of the model, and residuals (tracks compressing faster/slower than predicted) become the anti-consensus signal generator.

### 1.4 Pricing-regime variable
Per track: seat / usage / **outcome** pricing, plus **labor-capture rate** = agent-vendor revenue ÷ displaced labor cost. Under outcome pricing, SW TAM growth mechanically consumes Labor TAM — the two columns are no longer independent, and v2 records the coupling instead of pretending otherwise.

### 1.5 Conviction & falsifiability (house style, institutionalized)
Every track: conviction H/M/L + one falsifiable 12-month indicator ("if X hasn't happened by 2027-09, this thesis is wrong") + anti-consensus note where applicable.

### 1.6 The 2030 anchor (reverse derivation)
Each work family carries an explicit 2030 end-state assumption (% of the family agent-executable at trajectory) from which 2026 entry points are back-derived. Grand-vision-first, then walk backwards — the method, made explicit and reviewable.

---

## 2. Phase 1 — Top-down decomposition

### 2.1 Base pool
Global labor compensation ≈ **$50T** (prior; Phase 0 validates via ILO Global Wage Report, World Bank, BLS OES for US precision). v1's $9.94T becomes a *derived* quantity, not an input.

### 2.2 Eight work families — partition by substitution physics, not software category

| # | Family | Definition | Example occupations | Pool prior (P0 validates) | Capability coverage now → +12mo |
|---|---|---|---|---|---|
| W1 | Digital, outcome-verifiable | Result checkable cheaply & objectively | Software eng, QA, data eng, reconciliation, quant reporting | $2.5–3.5T | High → very high |
| W2 | Digital, judgment-graded | Quality judged, not verified | Research, analysis, legal drafting, content, program mgmt | $6–8T | Med-high → high |
| W3 | Digital, real-time interpersonal | Live human interaction is the work | Sales, support, recruiting, teaching delivery, coordination | $4–5T | Med (voice unlock) → high |
| W4 | Licensed, sign-off gated | Capability exceeds permission | Audit, tax opinion, diagnosis, legal advice, fiduciary | $3–4T | High capability, R-gated |
| W5 | Physical, structured | Repeatable environments | Warehouse, line mfg, structured inspection, commercial cleaning | $6–8T | Low-med → med (robot FM ramp) |
| W6 | Physical, dexterous/unstructured | Open environments, fine manipulation | Trades, construction, care ADL, field service | $8–10T | Low → low (5–15y hardware) |
| W7 | Trust/relational premium | The relationship IS the product | Therapy alliance, executive leadership, high-stakes negotiation | $3–4T | Low, durable human premium |
| W8 | **Agent-economy labor** (born 2024–26) | Work that exists only because agents exist | Agent ops/supervision, eval engineering, context engineering, agent audit & insurance, MCP/integration, fleet ops | $50–150B, compounding | n/a — creation, not substitution |

**Cross-cutting overlay — the services-arbitrage pool** (new in v2, missed by v1): global outsourcing/BPO — contracted, SLA-measured, price-listed labor (contact centers 12M+ agents, IT services, back-office BPO). Already commodified and measured ⇒ converts *first*, regardless of family. India/SEA displacement is ground zero; TCS/Infosys guidance is a leading indicator.

### 2.3 Family-agent brief (×8, parallel)
Each family agent: (a) validate pool size with 2 Tier-1/2 sources; (b) decompose into task clusters; (c) score V/H/P/R/L/D per cluster; (d) derive candidate tracks with first-pass Labor TAM (headcount × comp, geo split); (e) state the family's 2030 end-state assumption; (f) emit structured output (schema below).

### 2.4 New-demand agent (×1)
Derives W8 bottom-up from first principles AND second-order: what jobs do the *other 200 tracks' agents* create as they deploy? (Supervision ratios, exception handling, trust infrastructure.)

### 2.5 Adversarial partition review (×3)
Three refuters attack the family partition: MECE violations, double-counting across families, missing pools (informal economy, gig, military, government-transfer-adjacent). Majority concerns force a re-cut before Phase 2.

**Gate G1** — Patrina reviews family partition + pool numbers before bottom-up spend.

---

## 3. Phase 2 — Bottom-up discovery (7 blind sweeps)

Each sweep runs blind to the others (multi-modal search: what one angle can't see, another can), emits a standard schema, then main-loop dedup + one completeness critic.

| # | Sweep | What it hunts | Key sources | Notes |
|---|---|---|---|---|
| S1 | Capital | Every disclosed AI-agent round Apr–Sep 2026, seed→growth, clustered; density map | Crunchbase/TC/TFN/PitchBook-proxies | Seed/A density matters more than mega-rounds for early signal |
| S2 | Accelerators & talent flow | YC S26 (**Demo Day Sep 10** — hard dependency), Neo, a16z Speedrun; departures from OpenAI/Anthropic/DeepMind → stealth cos | YC directory, LinkedIn analyses, The Information | T0 people-tracking: who left to build what |
| S3 | Labor-market counter-signal | Job-posting deltas (roles shrinking vs "agent" skills growing), freelance-platform category collapse (Upwork pricing), BPO guidance | Indeed/LinkedIn published data, earnings calls | The ground-truth channel — catches agent-washing |
| S4 | Product & protocol | Enterprise GA launches, MCP ecosystem stats, UCP/ACP adoption, agent-store formation | Vendor blogs, protocol repos | Protocol adoption = infrastructure-layer signal |
| S5 | Incumbent motion | Earnings-call AI revenue attach (MSFT/CRM/NOW/INTU), seat→outcome pricing changes, incumbent M&A of agent startups | 10-Qs, earnings transcripts | Where incumbents defend successfully, startup TAM is fiction |
| S6 | Non-US | China (profitable robotics, Qwen/ERNIE agent ecosystems, super-app agents), EU reg-arbitrage plays, India/SEA BPO displacement | Caixin, 36Kr-adjacent English, local coverage | Unitree profitability came from here first — don't be US-blind |
| S7 | Failure & churn (anti-hype) | Shutdowns, down-rounds, retired products (Atlas, Instant Checkout, Woebot), enterprise pilot-failure studies | Post-mortems, layoff trackers | The anti-consensus evidence base — what the narrative omits |

---

## 4. Phase 3 — Collision & taxonomy freeze

Reconciliation matrix: top-down predicted tracks × bottom-up observed clusters. Four quadrants, each with a defined action:

| | BU: dense | BU: empty |
|---|---|---|
| **TD: predicted** | ✅ Core track — proceed to evidence pack | 🎯 **White space** — early-signal watchlist; classify *why not yet*: too early / blocked (R, P, D) / thesis wrong |
| **TD: absent** | ⚠️ **Hype-check** — adversarial test: real new demand vs narrative bubble | Drop |

**Kill / merge / split rules for v1's 205:**
- Any track untouched 3+ cycles must justify its existence (Marketing's 21 and Public Services' 31 face the axe or a merge)
- Over-concentrated tracks split (Code Gen at $40B likely → autonomous SWE / spec-to-app / maintenance & migration)
- Micro-tracks below materiality merge

Expected output shape: ~8 families × 25–35 tracks ≈ **200–260 tracks**, with the old 10-category view preserved as a *presentation layer* for dashboard continuity.

**Gate G2 (the big one)** — taxonomy freeze. Patrina signs off before the expensive fan-out.

---

## 5. Phase 4 — Evidence-pack fan-out (the heavy phase)

### Standard pack schema (per track)
- Identity: name, family, category-view, definition, **boundary (what it is NOT)**
- Labor TAM: headcount × compensation, geo split, 2 sources
- SW TAM: 2 sources + vendor-ARR bottom-up triangulation
- Ratio + V/H/P/R/L/D scores + **12-month predicted ratio** (velocity model)
- Displacement: 3-source; step-level for priority tracks
- Pricing regime + labor-capture rate
- Players: funded cos w/ stage/valuation, incumbent response, lab-native threat
- Net effect + Jevons evidence
- Conviction + falsifiable 12-mo indicator + anti-consensus note

### Tiering & verification
- **Tier A** (~60 tracks: all ratio ≥20×, all new, all changed-this-year): one agent per track, then **adversarial verification** — every Labor TAM >$10B and every ratio >50× claim gets a refuter agent briefed to kill the number; 2-of-3 survival required. Numbers that die get re-researched or downgraded.
- **Tier B** (~160 tracks): batched 5-per-agent light packs, no per-number verify, explicitly flagged lower-confidence.

**Gate G3** — deep-dive selection from scored output.

---

## 6. Phase 5 — Deep dives (~25)

Selection by **composite score** (velocity × labor size × conviction), *not* raw ratio — v1's ratio-sorting over-weighted tiny-SW curiosities. Plus discretionary picks tied to the HTC robotics thesis (robotic FM platform, industrial, elder-care; CyberOrigin data-layer relevance).

Structure = v1's four sections plus two new:
- ① Workflow breakdown (15–25 steps)
- ② Step-level AI capability (FULL/PARTIAL/NO + tools, updated to Fable-5-era)
- ③ Critical gap analysis (severity + timeline)
- ④ Strategic insight & addressable TAM
- **⑤ Value-capture verdict** — startup / incumbent / model lab / OSS-deflation, with reasoning
- **⑥ Falsifiable indicators** — 3 dated predictions per track + entry-point map (where a seed/A check makes sense for HTC)

Each deep-dive gets one red-team pass attacking its thesis before it ships.

---

## 7. Phase 6 — Synthesis & products

1. **v2 master xlsx** — families + tracks, full score schema, change-log carried forward
2. **Evidence-pack database** — every pack, sourced and dated
3. **Deep-dive book** — 25 chapters, red-teamed
4. **Thesis memo** — 10–15 numbered falsifiable predictions + top 5 anti-consensus calls (the IC-ready artifact)
5. **Dashboard v2** — new views: velocity map (predicted vs observed compression), lab-capture-risk map, white-space board, family sunburst; old category view retained
6. **Update-skill v2** — regenerate the bimonthly-cycle skill so future updates inherit the v2 schema (the current skill encodes v1 and would silently corrupt v2)
7. **Portfolio cross-map** — HTC holdings and pipeline vs the map

---

## 8. Agent orchestration spec

| Phase | Agents | Topology | Verification | Gate | Est. session |
|---|---|---|---|---|---|
| P0 Foundation | 4 + 1 synth: capability-frontier matrix · labor-data refresh (ILO/BLS/GS/McKinsey 2026 eds) · pricing-regime survey · source-quality audit | parallel → synth | main-loop review | — | ½ session |
| P1 Top-down | 8 family + 1 new-demand + 1 services-arbitrage + 3 partition-refuters + 1 synth = **14** | parallel families → barrier → refuters | adversarial partition review | **G1** | 1 session |
| P2 Bottom-up | 7 sweeps + 1 completeness critic = **8** | parallel, blind | critic + main-loop dedup | — | 1 session (S2 completes after Sep 10) |
| P3 Collision | 2–3 hype-check judges; matrix work in main loop | main-loop + judges | quadrant logic | **G2 freeze** | ½ session + review |
| P4 Evidence packs | ~60 Tier-A + ~32 Tier-B batch + ~40 verify = **~130** | pipeline (research → verify per track, no barrier) | refuter-kill on >$10B / >50× claims, 2-of-3 | **G3** | 1.5–2 sessions |
| P5 Deep dives | 25 + 25 red-team = **50** | pipeline | red-team per dive | — | 1 session |
| P6 Synthesis | 4–6 builders (xlsx, dashboard, memo, skill) | main-loop-led | her review | **G4 publish** | 1 session |

**Totals**: ~210 agent runs; heaviest phase P4. Calendar: ~6–7 working sessions over ~2.5 weeks, sequenced so S2 lands after **YC S26 Demo Day (Sep 10)**.
**Model policy**: mechanical sweeps and Tier-B batches on the cheaper tier; family derivation, verification, and deep dives on the frontier tier.
**Execution notes**: phases run as journaled, resumable multi-agent workflows — each phase launches on explicit go; every number date-stamped; structured-output schemas enforced at the tool layer so agents can't return prose where the pipeline needs data.

---

## 9. Gate G0 — decisions needed before launch

| # | Decision | Recommendation |
|---|---|---|
| D1 | Labor-TAM geography | Global pools at family level; US-precision (BLS) × global multiplier at track level |
| D2 | Presentation continuity | Keep 10-category view as a lens over the 8 families (dashboard continuity) |
| D3 | W8 agent-economy as first-class family | Yes — it's the early-signal mandate embodied |
| D4 | P4 verification scale | Full adversarial verify on Tier A only; ~2× cost to verify everything, not worth it |
| D5 | Deep-dive count | 25 (v1 had 22) |
| D6 | Sequencing vs YC S26 | Start P0/P1 now; land P2 after Sep 10 so S26 is in-scope, not a patch |

---

## 10. Risks of the research itself (and mitigations)

| Risk | Mitigation |
|---|---|
| **AI-slop source pollution** — 2026's market-size "reports" are increasingly AI-generated spam citing each other | Tier enforcement; primary-data preference; vendor-ARR bottom-up as the tiebreaker on every SW TAM |
| **Agent-washing** in funding data — everything calls itself an agent | S7 failure sweep + revenue-quality checks (ARR vs bookings vs pilots) |
| **Code-extrapolation fallacy** — coding is sui generis (verifiable + self-serve buyer + builder-adjacent training data); its velocity is a ceiling, not a template | Velocity model fits per-axis weights instead of copying code's curve |
| **US/EN bias** | S6 as a first-class sweep, not an afterthought |
| **Consensus contamination** — VC narratives echo into search results, poisoning "independent" sources | Labor-data primacy (BLS/ILO don't read TechCrunch); S3/S7 counter-channels weighted equally |
| **Taxonomy overfit to today's capability snapshot** | Families designed for 12-month stability; tracks amendable per bimonthly cycle; amendment protocol in skill v2 |

---

*Next step on your go: answer D1–D6 (or accept recommendations), then Phase 0 launches.*
