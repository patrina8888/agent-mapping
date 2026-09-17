# Phase v3 — GPT-6 Constraint-Delta Pass (targeted propagation, NOT a rescore)

HTC internal · **2026-09-16** · Governed by `p0b_capability_refresh_2026-09.md` (which explicitly states GPT-6 Astra is incremental and moves almost no binding constraint). This pass does the disciplined, honest propagation of that finding into the frozen 76-row taxonomy. It is a **delta**, not a re-scoring exercise.

> **The finding up front, so it is not buried:** GPT-6 Astra moves the map **almost not at all**. There are **zero integer rescores** across the 76 rows. What changes is a handful of *descriptive gate-notes*, **one** conviction-basis firming (W2.4), and a couple of "the tailwind reinforces an already-Additive/Expansion row" notes. Every BLOCKED and TOO-EARLY white-space cell stays exactly where it was. **The model was never the binding constraint — GPT-6 is the cleanest confirmation of that yet.** That *is* the result, and it is worth stating plainly rather than manufacturing motion.

Glossary of terms used below (glossed on first use per house style): **OSWorld 2.0** = a hard benchmark of 108 long, multi-step computer-use workflows (median ~1.6h of human time); "binary" = the task is scored fully-done-or-not, "partial" = partial credit for sub-steps. **METR horizon** = the length of task a model can do at a stated reliability (50% or 80% success). **V/H/P/R/L/D** = the six scoring axes (Verifiability / autonomy-Horizon / Physicality / Regulatory gate / Lab-capture / Data-incumbent moat, 0–5). **Net** = Expansion / Compression / Mixed. **Coupled** = sized as capture-rate × displaced wage bill (never SW + labor). **Additive** = software augments a durable human, never netted against the labor pool.

---

## 1. The constraint-delta ledger — what GPT-6 moved, and what it did not

This is the whole analysis in one table. Everything downstream is propagation from it. (Source: p0b §A–B; benchmark specifics are Tier-2 aggregators — Artificial Analysis strongest — pending OpenAI's model card, so treat levels as directional. OpenAI's own GPT-6 Astra system card, web-checked 2026-09-16, corroborates the reliability and cyber-gating rows.)

### Constraints that MOVED

| Constraint | Early-2026 (frozen) | Now (Sept 2026) | Moved? | Binding? | Tracks it touches |
|---|---|---|---|---|---|
| **Model IQ / reasoning ceiling** | GPT-5.x, Gemini DeepThink | Astra Intelligence Index 53 (tied Fable 5.1), FrontierMath-T4 97.6%, GPQA-D 96% | **Yes** | **No — never was the gate** | None directly |
| **80%-reliability autonomy gate** (OSWorld 2.0 binary, messy long-horizon computer-use) | **~20.6%** binary | **~31% binary** / 72.6% partial (Astra & Opus 5, 10 Sept) | **Partially** — real +~11pts binary | **Still binds** — production needs 80–98% | W1.7, SA.3, SA.5, W1.1b, W11.1 (gate *narrowed*, not opened) |
| **Long-horizon knowledge work** (AA-Briefcase Elo) | — | **+~90 Elo vs GPT-5.6 Sol** — a real long-horizon gain | **Yes, modest** | Not the sole gate on any track | W2.4, W2.2, W2.6 (all Additive) |
| **Verifiability tailwind** (hallucination, AA-Omniscience) | high | **92% → 51%** (halved, still 51%) | **Marginal** | Not sign-off grade | W2.4, W2.2, W1.8 (false-positive triage) — small tailwind, no unlock |
| **Coding** (DeepSWE, Terminal-Bench) | frontier | Astra ≈ **TIE** (DeepSWE ~74%; wins Terminal-Bench v4 at 59%) — no autonomy step-change | **No** | — | **W1.1a/W1.1b/SA.4 explicitly unchanged** |

### Constraints that did NOT move (the dominant ones)

| Constraint | Status | Moved? | Tracks it gates |
|---|---|---|---|
| **Pilot-to-production chasm** | MIT 95% zero-P&L; S&P 42% abandonment; <15% to production — an org/deployment problem, not a model problem | **No.** A better model does not cross the chasm. This is the dominant 2026 fact, untouched. | Every Conv=High track |
| **Regulatory sign-off (R)** | Astra *delayed* for cyber; classified by OpenAI as first model over the **Critical cybersecurity threshold**; gated behind the **Daybreak trusted-access cohort**; public model refuses cyber prompts | **No — adverse.** The self-imposed safety gate the framework flagged **tightened.** | W4.1/4.4/4.6/4.8/4.9, W1.5, W1.8 (build-dependency), W11.2/11.3, W12.x |
| **Incumbent / data moat (D)** | unchanged by model IQ; converging frontier (Astra ≈ Fable 5.1; Opus 5 co-leads computer-use at half price) makes **D more decisive, not less** | **No** | W1.1a, W1.8, W4.10, all coupled tracks, all physical |
| **The 80% reliability gate, broadly** | 50%-vs-80% gap intact; OpenAI's own card: "absence of observed failures does not establish reliability across settings" | **No** | H-axis map-wide |

**Two data-integrity corrections to carry (independent of the GPT-6 delta, but they touch the same axes):**
- **METR "~32h @50%" is retired.** Best *officially measured* 50% horizons sit single-digit-to-~12h; METR flags **>16h unreliable**; Astra/Opus 5 not yet officially scored. The 50%-vs-80% gap (the real story) is reaffirmed, not relaxed. This does **not** change any track's H integer — those were already scored on the gap logic, not the 32h headline.
- **OSWorld version-lock.** Every OSWorld citation must be tagged **Verified (~85%, the easier set, "beats humans" headline)** vs **2.0 (~31% binary, the hard set)**. The framework's "~20.6%" was always 2.0. Never let the ~85% number enter a displacement estimate.

---

## 2. Row-by-row propagation — the SPECIFIC tracks, old→new, with the honest "no change" stated

Discipline: I name every track a reader might expect to move, and for each give the actual verdict. **Expect few, and even the "few" are notes, not rescores.**

### The one track with a real (modest) tailwind

**W2.4 — Enterprise Knowledge Research & Synthesis** · frozen `2/3/0/1/4/3` · Additive · Expansion · Conv **Med↓ ("weakest basis")** · Tier B
- **Verdict: conviction-basis firming — the single closest thing to a GPT-6 delta on the map. No axis rescore, no Net change.**
- Why: W2.4 lives on exactly the two axes GPT-6 actually moved — long-horizon knowledge work (**+~90 Elo**, AA-Briefcase) and hallucination (**92%→51%**). Those are a genuine tailwind for a research-synthesis copilot, and they take the "weakest basis" flag off its worst footing.
- **What does NOT change, and why:** V stays **2** — halving fabrication reduces one failure mode but does not make a judgment-graded synthesis *output* cleanly checkable; verifiability is about outcome-checkability, not error rate. Net stays **Expansion** — a better research model makes a stronger *copilot* for a durable analyst; it does not displace the analyst. Conviction firms *within* Med (weak-basis flag eased) but does **not** cross into High. So: **Conv Med↓ → Med (basis firmed); all six axes unchanged; Net unchanged.**

### Additive tracks where the tailwind only reinforces existing Expansion (note, no change)

**W2.2 — Financial & Investment Analysis** · `3/3/0/3/3/4` · Additive · Expansion · Conv High · Tier A
- **No change.** Hallucination-halving is a small tailwind (financial analysis penalizes fabrication), but the row is already Additive/Expansion/High. GPT-6 makes the analyst copilot better = **more Expansion, not displacement**. Note only. (Directly relevant to HTC's own workflow: a better research model is a better analyst tool, and it stays in the Expansion column — do not re-read it as capture.)

**W2.6 — Program/Project Mgmt & Ops Coordination** · `2/4/0/0/4/4` · Additive · Mixed · Conv Med · Tier B
- **No change.** The long-horizon-Elo gain touches its H=4 profile, but the track was never gated on the *50%* horizon — it is gated on 80% reliability + org adoption for autonomous multi-step execution, neither of which moved. Note only.

**W1.8 — Security Operations & Threat Triage (SOC t1/2)** · `3/2/0/2/3/4` · Coupled · Mixed · Conv Med–High · Tier A
- **No change — but a genuinely two-sided note.** (a) *Small tailwind:* lower hallucination + better reasoning marginally help false-positive triage. (b) *Offsetting headwind:* the frontier cyber-capability gate **tightened** — Astra crossed the Critical cyber threshold, is gated behind Daybreak trusted-access, and the public model refuses cyber prompts, which constrains what an autonomous-SOC startup can build on top of the best models. V stays **3** (the catastrophic false-*negative*/missed-breach test is still not machine-checkable — the exact CX-style logic), D stays **4** (the SIEM/EDR telemetry moat is untouched and, with models converging, more decisive). **No axis, Net, or conviction change.**

### Digital back-office / services-arbitrage: gate-note update only, no score change

**W1.7 — Structured Data Entry & Digital Back-Office** · `4/1/0/1/4/2` · Coupled · Compression · Conv Med · Tier B
- **Descriptive note updates; nothing else.** The rationale refrain **"OSWorld ~20% gate" → "OSWorld 2.0 ~31% binary / 72.6% partial (Sept 2026)."** H stays **1**, Conv stays **Med**, Net stays Compression. This is the cleanest example on the whole map of *the number moved but the score did not*: +11pts of binary completion is real, and still nowhere near the 80–98% an unattended back-office deployment needs. Gate **narrowed, not opened.**
- **SA.3 (∩W1) and SA.5 (∩W1)** — identical treatment: same gate-note update, no score/conviction/Net change; still sub-production.
- **W11.1 (Benefits/Case Processing)** — same back-office reliability note, but it is *also* R=5 procurement-gated (blocked-adjacent), and GPT-6 touches procurement not at all. **No change.**

### Coding — required explicit no-change

**W1.1a / W1.1b / SA.4** — **GPT-6 did not move W1.1.** Astra coding is a **tie** (no autonomy step-change), so C1's capture-expansion thesis and its **Q4-2027 coupled-revenue-mix resolver stand entirely unchanged.** Do not rescore any coding row on GPT-6. (Stated explicitly because a reader will assume a new frontier model must have moved the most-deployed agent labor market. It did not.)

### Physical families — untouched, and for a structural reason

**W5.x, W6.x, W9.x, W10.x, W12.2, and the W6.3 robotics cell** — **No change from GPT-6, full stop.** GPT-6 Astra is a *digital* language model; it has no bearing on dexterity, hardware, or deployment reliability of robots. The real physical-capability progress (VLA cross-embodiment: π0.7, Gemini Robotics 1.5, GR00T-N2, Skild) is a **separate software story** documented in p0b §C — and even *that* moves the *rationale*, not the W5/W6 **Net or capture (<1.5%)**, because those gates are hardware-timeline (5–15yr), not brain-IQ. Attributing any physical-track movement to GPT-6 would be a category error.

### Everything else on the 76 rows

No change. No other track's V/H/P/R/L/D, Net, or conviction is affected by GPT-6 Astra.

---

## 3. BLOCKED and TOO-EARLY white-space — cell by cell, did GPT-6 unlock any?

**Answer: none. Zero cells unlock.** Stated per cell so it is auditable, not asserted.

### BLOCKED (capability was already ready; a hard R/D gate throttles the dollars — so a better model cannot help by construction)

| Cell | Gate | GPT-6 unlock? | Why not |
|---|---|---|---|
| **W1.5** Financial Reporting / XBRL filing | R=4 officer/SOX **certification liability** | **No** | Better drafting/lower hallucination improves the *draft*; the gate is who signs and is liable, not model capability. (YC S26 check, 2026-09-16: no XBRL-filing agent surfaced — consistent with the gate, not the model, binding.) |
| **W4.1** External Audit & Statutory Assurance | R=5 + Big-4 **internalize** | **No** | GPT-6 does not change Big-4 internalization economics; external-vendor capture ≈0 regardless of model. |
| **W4.4** Consumer / Access-to-Justice Legal | R=5 **UPL** (unauthorized practice of law) | **No** | UPL is a legal prohibition, entirely model-independent. |
| **W4.6** Autonomous / Device-Cleared Diagnosis | R=5 FDA + **reimbursement** (only 2 CPT codes) | **No** | Already V=5 — capability was *never* the bottleneck; the wall is payment/clearance. |
| **W4.8** Specialized Statutory Attestation | R=4 + **EU Omnibus** (shrinking) | **No** | Gate is regulatory + a contracting market; part thesis-wrong. |
| **W4.9** Pharmacy — Licensed Dispensing | R=5 + physical dispensing | **No** | Licensing gate + hardware; neither is a language-model question. |
| **W11.2** Public Education Delivery | R=5 procurement + political | **No** | Procurement/political gate, model-independent. |
| **W11.3** Public-Safety Records & Permitting | R=5 procurement; Palantir/ServiceNow-gov captured | **No** | Incumbent + procurement capture; GPT-6 touches neither. |

> Note the direction of travel is **adverse, not neutral,** for the R-gated cluster: GPT-6's own launch *tightened* the frontier cyber-capability gate (Astra delayed, cyber gated behind trusted access). If anything, a labs-self-gating world makes BLOCKED cells marginally harder to attack, not easier.

### TOO-EARLY (hardware/dexterity clock, not a legal gate — and GPT-6 is a digital model)

| Cell | Gate | GPT-6 unlock? | Why not |
|---|---|---|---|
| **W6.1** Skilled Trades — MEP install/repair | P=5 dexterous-unstructured | **No** | Digital LLM has zero bearing on dexterous hardware. |
| **W6.2** General Construction — unstructured | P=5 | **No** | Hardware-timeline; largest blocked pool, still no software wedge. |
| **W6.5** Cleaning & janitorial — unstructured residual | P=4 | **No** | Hardware/dexterity clock. |
| **W6.6** Specialty-crop selective harvest | P=5 + seasonal | **No** | Hardware + niche economics. |
| **W10.1** Retail Floor & Cashiering | presence-gated + P | **No** | Physical presence + dollar-weighting; not a model question. |
| **W10.2** Hospitality & Hotel Operations | presence-gated + P | **No** | Same. |

**Cell-by-cell conclusion:** every BLOCKED cell is gated by regulation, liability, incumbency, or reimbursement; every TOO-EARLY cell by hardware/dexterity. GPT-6 Astra — a better, cheaper, tied-on-coding digital reasoner — moves **none** of those. The uniform "no unlock" is not laziness; it is the framework's central thesis (the model is not the binding constraint) surviving contact with a genuine new frontier model. The one thing GPT-6 *did* do to this board — tighten the cyber R-gate — pushes a cell (W1.8's build dependency, W12.x) the *wrong* way.

> **Discipline flag for the reader (so nobody mis-attributes momentum):** the YC S26 batch *does* show real bottom-up motion in **insurance (W4.10)** and **digital back-office (W1.7)** — Qlo (commercial-underwriting agents), Huscarl (AI actuary), Rapidfolio (bank back-office: KYB/KYC, loan underwriting), Async, and Clicks (an **F25**, i.e. pre-GPT-6, computer-use back-office agent). This validates the p3 hunting-ground calls — but it is **market formation on pre-GPT-6 document-agent capability, not a GPT-6 unlock.** The capability those startups use shipped well before Astra. Do not credit Astra for it. [YC S26 companies; DEV "Insurance…AI Agent Wedge in YC 2026", web-checked 2026-09-16]

---

## 4. Bottom line — 2–3 sentences an IC can act on

**GPT-6 Astra changes the investable map essentially not at all: zero rescores across 76 rows, a handful of gate-note updates (OSWorld reliability ~20%→~31% *binary* — narrowed, still far below the 80–98% production needs), one modest conviction-basis firming on an Additive/Expansion research track (W2.4), and coding moved *not at all* (a tie).** It unlocked **zero** BLOCKED or TOO-EARLY white-space cells — every one is gated by regulation, liability, incumbency, or hardware, none of which a smarter model touches, and Astra's own cyber-capability gating actually *tightened* the regulatory gate. **IC action: do not re-weight a single position on GPT-6; keep underwriting the gates that actually bind — pilot-to-production, R (regulatory/liability sign-off), and D (data/incumbent moat) — and the coupled-capture-expansion resolvers (coding's Q4-2027 revenue-mix test, W4.10/W1.8 gate-movement triggers), because the model was never the constraint, and this frontier release is the strongest evidence yet that the thesis holds.**

---

### Sources (web-verified 2026-09-16; governing baseline is p0b)
- Governing: `p0b_capability_refresh_2026-09.md` §A–E (GPT-6 incremental; constraint-delta table; propagation list) · `p0_foundation.md` (coupling rule, capture rates, pilot-to-production) · `p3_frozen_taxonomy.md` (frozen 76 rows, white-space board, C1/C3/hype rulings) · `v2_master.json`
- [OpenAI — GPT-6 Astra System Card / Deployment Safety Hub](https://deploymentsafety.openai.com/gpt-6-astra) ("absence of observed failures does not establish reliability"; Critical cyber threshold; conceals part of reasoning)
- [Artificial Analysis — Benchmarking GPT-6 Astra](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra) ("incremental, not step-change"; Index 53; Terminal-Bench 59%) — most neutral source
- [arXiv 2606.29537 — OSWorld 2.0](https://arxiv.org/abs/2606.29537) · [Snorkel — OSWorld 2.0 leaderboard](https://snorkel.ai/leaderboard/os-world-2-0/) (Astra 72.6% partial / ~31% binary)
- [METR — Time Horizons](https://metr.org/time-horizons/) (">16h unreliable"; Astra/Opus 5 unscored) — the "~32h" correction
- [YC — S26 companies](https://www.ycombinator.com/companies/) · [DEV — "Insurance Might Be the Most Underrated AI Agent Wedge in YC 2026"](https://dev.to/eliofbm/insurance-might-be-the-most-underrated-ai-agent-wedge-in-yc-2026-3552) (Qlo, Huscarl, Rapidfolio, Async, Clicks-F25 — bottom-up, pre-GPT-6 capability)
- **Sourcing caveat:** GPT-6 benchmark specifics rest on Tier-2 aggregators (Artificial Analysis strongest); OpenAI's full model card not retrievable for per-benchmark numbers — levels treated as directional per p0b. The *finding* (GPT-6 moves no binding constraint) does not depend on any single contested figure.
