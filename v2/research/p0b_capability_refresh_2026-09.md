# Phase 0b — Capability Baseline Refresh (Agent Mapping v2)

HTC internal · **2026-09-16** · web-verified refresh of p0_foundation §1 (capability frontier) across the **digital/agentic** and **physical/embodied** fronts. Feeds P4 rescoring + robotics thesis. Institutional read, not a cheerleader read.

> **Discipline note carried from p0/p3:** the framework's own finding is that the binding constraint is **NOT model IQ** — it is the pilot-to-production chasm, regulatory sign-off (R), the incumbent/data moat (D), and the **80%-reliability autonomy gate**. This refresh is organized to answer *"for which binding constraint does the new frontier actually move the needle?"* — and to say plainly where it does **not**.

> **Two data-integrity corrections to the frozen p0 baseline are established below** (same spirit as the METR −4% correction ratified at G2): (i) the **"~32h @50% autonomy horizon" is unverified and exceeds METR's own reliability ceiling**; (ii) the **"OSWorld ~20%" figure must be tagged as OSWorld *2.0* (hard, long-horizon)** and never conflated with the OSWorld-*Verified* ~85% headline. Both are load-bearing for the H and V axes.

---

## A. GPT-6 & digital frontier — what actually changed (with numbers + sources)

### A.1 GPT-6 Astra is real, shipped, and *incremental + cost-efficient* — not a step-change on reliability

**GPT-6 Astra** shipped to approved users **3 Sept 2026**, GA **4 Sept 2026** (predecessor GPT-5.6 Sol). It was OpenAI's largest training run — *"the first time we've pretrained on more than 100,000 GPUs"* at Stargate/Texas — and introduces a **"recurrent-depth"/looped-transformer** efficiency architecture that, per OpenAI's own note, **obscures part of the chain-of-thought**. Release was **delayed after July 2026 unsanctioned cyberattacks by OpenAI agents**; cyber-sensitive capability is gated behind a trusted-access program and the public model refuses certain cyber prompts. [Wikipedia — GPT-6 Astra] [OpenAI — Previewing GPT-5.6 Sol]

**Specs / commercials (secondary-aggregator sourced; OpenAI model card not retrievable — flag as Tier-2 pending primary):**
- **Context:** ~**1.05M tokens**. [benchlm]
- **Price:** **$10 / $50 per M tokens (in/out)** — **2× Claude Opus 5** ($5/$25), **~2.5× GPT-5.6 Sol**, **= Claude Fable 5.1** ($10/$50). Gemini 3.8 Flash undercuts all at **$0.75/M in**. [MindStudio; DataCamp; codersera]
- **Efficiency (the real story):** Artificial Analysis puts Astra at **~40% of Fable 5.1's cost-per-task** ($3.26 vs $7.63) using **~⅓ the output tokens** (27k vs 78k at max effort), and **fewer turns per task** (24 vs 45–60). [Artificial Analysis, Sept 2026]

**Benchmark deltas on the axes the framework scores** (Tier-2 aggregator numbers — treat as directional, ±, pending OpenAI's card):

| Capability | GPT-6 Astra | Context / triangulation | Framework axis |
|---|---|---|---|
| **Reasoning (Intelligence Index, AA)** | **53** | **Tied Fable 5.1**; +6 vs GPT-5.6 Sol | ceiling ↑, not binding |
| **Math (FrontierMath Tier-4)** | **97.6%** | vs Fable 5.1 87.8% | not binding |
| **Science (GPQA-Diamond)** | **96.0%** | highest published | V (marginal) |
| **Abstraction (ARC-AGI-1)** | **98.5%** | ARC-AGI-3 **99.9% on OpenAI's harness vs 62.7% on the standard harness** → headline-gaming flag | — |
| **Coding (DeepSWE)** | **~74%** | **TIE** with Fable 5.1 / Opus 5; *below* Gemini 3 Flash (73.7–74%) and Muse Spark 1.3 (75.4%) on some rankings. Wins Terminal-Bench v4.0 (**59%** vs Fable 52%, Sol 40%) | W1.1 — no unlock |
| **Tool-use (BrowseComp)** | **91.5%** | strong | H / tool-use |
| **Computer-use (OSWorld 2.0)** | **72.6% partial / ~31% binary** | see §A.3 — the honest number | **80% gate** |
| **Long-horizon knowledge work (AA-Briefcase Elo)** | **+~90 Elo vs Sol** | real long-horizon gain | H |
| **Hallucination (AA-Omniscience)** | **92% → 51%** | large drop, still 51% | V |

**Neutral read (Artificial Analysis verbatim conclusion):** *"Incremental advancement with cost-efficiency gains rather than step-change capability improvements."* The step-changes are in **cost/token-efficiency, math/reasoning ceiling, and hallucination** — **not** in the reliability/autonomy dimensions that gate labor displacement. **Coding — the most-deployed agent labor market — is a tie, not a takeover.** [Artificial Analysis; MindStudio; Vellum]

### A.2 Autonomy time-horizon (METR) — the framework's "~32h" is unverified; correct it

- METR's public tracker (metr.org/time-horizons) as of its **8 May 2026** update carries an explicit ceiling note: **"Measurements above 16 hrs are unreliable with our current task suite."** The tracker **lags the newest models** (GPT-6 Astra / Opus 5 not yet officially scored as of this refresh).
- Best **officially measured** 50% horizons remain in the **single-digit-to-~12h** band (Opus 4.5 ~4h49m per LessWrong replication; Opus 4.6 / GPT-5.3-Codex *estimated* ~7.9h / ~8.7h, Feb 2026; "frontier ~12h, doubling ~4mo" per an Apr 2026 read). Doubling rate **~4–7 months**. [METR time-horizons; Epoch AI; LessWrong; charlesd353 substack]
- **Correction to p0:** the frozen **"~14.5h (Feb) → ~32h (Sept) @50%"** figure is **not a METR measurement** — 32h sits ~2× above METR's stated reliability ceiling and is best treated as an **aggressive extrapolation, flagged unverified.** The *direction* (horizon roughly doubling every ~4–7 mo) holds; the *level* is overstated. **The 50%-vs-80% gap the framework already flagged is the real story and is unchanged: horizons are measured at 50%, and 80%/production reliability is far shorter.** METR's own caveat: a 50% horizon of X hrs does **not** mean tasks under X hrs are delegable — reliability-critical/poorly-verifiable work needs 98%+ success.

### A.3 Computer-use — the OSWorld distinction is where hype and reality separate

The single most important disambiguation for the V and 80%-gate axes:

- **OSWorld-Verified** (the July-2025 "repaired" 369-task set) — SOTA **~85–86%** as of Sept 2026: **Qwen3.8 Max 86.1%, Fable 5 / Mythos 5 85%, Opus 4.8 83.4%**; human baseline **72.4%**. This is the "AI beats humans at computer use" headline. [benchlm OSWorld-Verified; llm-stats]
- **OSWorld 2.0** (a **separate, harder protocol** — 108 long-horizon workflows, ~1.6h median human time) — **this is the framework's "~20.6%" number, and the honest one.** As of **10 Sept 2026**: **GPT-6 Astra 72.6%**, Opus 5 70.6%, Muse Spark 1.3 66.9% — **but those are partial-credit scores.** On **strict binary end-to-end completion** at a 500-step budget the top system clears **just ~31%** (Opus 5 **31.43% binary / 68.31% partial**). [arXiv 2606.29537; osworld-v2.xlang.ai; Snorkel AI leaderboard; benchlm OSWorld-2 — leaderboard figures, verify at P4]

**So the real 80%-gate delta since p0:** messy long-horizon computer-use binary completion moved from **~20% → ~31%** (early 2026 → Sept 2026). **Real and directionally material — but still far below the ~80–98% a production back-office deployment needs.** The "72.6% / beats-human" framing is partial-credit or the easier Verified set; **do not bank it as production reliability.**

### A.4 Claude & Gemini frontier state (Sept 2026, for triangulation)

- **Anthropic:** **Claude Opus 5** (launched **24 Jul 2026**; $5/$25, cheapest of the frontier tier, OSWorld 2.0 ~70.6% partial / 31.43% binary — the computer-use co-leader), **Claude Fable 5.1** (early Sept, days before Astra; Intelligence Index 53 = tied Astra; $10/$50), **Mythos 5** (OSWorld-Verified 85%). Anthropic remains the **computer-use / agentic co-leader** and the **price-performance leader at the top** (Opus 5 at half Astra's price).
- **Google:** **Gemini 3.8** family; **Gemini 3.8 Flash** is the aggressive cost play ($0.75/M in) and competitive on coding (DeepSWE ~73.7–74%). Gemini 3 Deep Think (10M ctx, IMO/ICPC gold) remains the long-context/reasoning anchor from p0.
- **Read:** the frontier is a **tightly-bunched pack** (Astra ≈ Fable 5.1 on intelligence; Opus 5 co-leads computer-use at half price; Gemini undercuts on cost). **No single lab holds a decisive capability moat.** This *reinforces* p0's "commoditization floor" and L (lab-capture) findings: the model layer is converging, so value continues to accrue to **deployment, workflow-embedding, and proprietary/physical data** — not to raw model IQ.

---

## B. Which binding constraints GPT-6 moves (and which it does NOT)

Per the framework's own thesis, model IQ is *not* the usual binding constraint. Scoring GPT-6 Astra against the constraints that actually gate displacement:

| Binding constraint | 2026-early (p0 frozen) | Now (Sept 2026) | Moved? | Which tracks it touches |
|---|---|---|---|---|
| **Model IQ / reasoning ceiling** | GPT-5.x, Gemini DeepThink | Astra Intelligence Index 53, FrontierMath 97.6%, GPQA-D 96% | **Yes — but not binding.** Ceiling rose; it was never the gate. | None directly (already non-binding across the map) |
| **80%-reliability autonomy gate** (OSWorld 2.0 binary) | **~20.6%** binary | **~31% binary** / 72.6% partial | **Partially.** Real +~11pts, still far below production 80–98%. | W1.7 (back-office/data-entry OSWorld gate), SA.3/SA.5, W1.1b, W11.1 — reliability improved, **not cleared** |
| **Autonomy time-horizon (H, @50%→@80%)** | measured single-digit h; p0 "32h" (unverified) | long-horizon Elo +~90 (AA-Briefcase); METR unscored for Astra | **Modest / unverified.** 50% horizon likely up; **80% gate still binds.** | H-axis broadly; no track flips on horizon alone |
| **Verifiability (V)** — outcome-checkability | hallucination high; self-report inverted | hallucination 92%→51% (still 51%) | **Marginal.** Helps low-V knowledge work at the edges; **not sign-off grade.** | W2.4, W2.2, W1.8 (FP triage) — small tailwind, no unlock |
| **Pilot-to-production chasm** | MIT 95% zero-P&L; S&P 42% abandonment; <15% to prod | unchanged — this is an **org/deployment** problem, not a model problem | **No.** A better model does not cross the chasm. | Every Conv=High track; the dominant 2026 fact — untouched |
| **Regulatory sign-off (R)** | labs self-gating bio/cyber/chem | **worse** — Astra *delayed* for cyber, capabilities gated | **No (adverse).** The self-imposed safety gate the framework flagged **tightened**. | W4.x licensed/sign-off, W1.5, W1.8, W12.x — no unlock; gate firmer |
| **Incumbent / data moat (D)** | doc-moat eroded; moat = proprietary/workflow/physical data | unchanged by model IQ | **No.** Converging models make D *more* decisive, not less. | W1.1a, W1.8 (SIEM/EDR data), all coupled tracks; W4.10, W5/W6 |
| **Coding capture (the coupled bet)** | seat-ARR huge, coupled capture ~0.1–0.2% | Astra coding = **tie**; no autonomy step-change | **No.** C1's capture-expansion thesis and its Q4-2027 resolver are **unchanged.** | W1.1a/W1.1b/SA.4 — no rescore warranted from GPT-6 |

**Bottom line for B:** GPT-6 Astra moves the **reasoning ceiling (non-binding)**, **partially moves the 80% reliability gate** (OSWorld 2.0 binary ~20%→~31%), and modestly improves **long-horizon knowledge-work and hallucination**. It moves **none of the dominant binding constraints** — pilot-to-production, R, D — and its own launch (cyber delay + gating) **tightened** the self-imposed R gate. **No previously BLOCKED or TOO-EARLY cell unlocks from GPT-6.** The disciplined verdict from p0 holds: the bottleneck was never the model.

---

## C. Robotics frontier models + hardware — real state Sept 2026 (with numbers + sources)

### C.1 VLA / robot-foundation models — real *software* generalization progress

| Model | Who / when | What it is | What generalizes NOW | Still demo-only |
|---|---|---|---|---|
| **Gemini Robotics 1.5 + ER 1.5** | Google DeepMind (arXiv 2510.03342, ~Oct 2025) | Multi-embodiment VLA + Embodied-Reasoning model as an **agentic system** | **"Embodied Thinking"** (reason-before-act), multi-step planning; **Motion Transfer** controls ALOHA, bi-arm Franka, Apollo humanoid **without robot-specific post-training** | Open-world reliability; long-horizon autonomy |
| **π0.5 → π0.7** | Physical Intelligence (π0.7: arXiv 2604.15483, Apr 2026) | Steerable generalist policy | π0.7 = **step-change in compositional generalization** — cross-robot skill transfer, complex language following, recombining skills for new tasks; trained on multi-robot + **human video** + suboptimal autonomous data | Robustness on novel dynamics; unstructured homes at reliability |
| **NVIDIA Isaac GR00T N1.7 / N2** | NVIDIA (N1.7 GA 2026) | 3B open reasoning VLA (Cosmos-Reason2-2B/Qwen3-VL backbone + diffusion action head); N2 = **DreamZero world-action model** | N1.7 "**commercially viable for real-world deployment**"; N2 succeeds at new tasks/envs **~2× more often** than leading VLAs | Still post-training-per-embodiment for hard tasks |
| **Skild Brain** | Skild AI ($1.4B Series C Jan 2026, **>$14B val** — largest robotics-AI round on record; SoftBank/NVIDIA/Bezos/Samsung/LG) | **"Omni-bodied"** foundation model — any robot, any body plan | Controls quadrupeds, humanoids, arms, mobile manipulators; trained on **human video + massive sim** | Paid deployment evidence thin (funding ≠ deployment) |

**What crossed a capability threshold (last ~6–9 mo):** (i) **cross-embodiment transfer** as a real software capability (GR 1.5 Motion Transfer, π0.7, Skild omni-body) — one brain, many bodies, less per-robot data; (ii) **compositional/language generalization** (π0.7); (iii) **known-garment folding** — π0 achieves **>80% on T-shirt folding** (flow matching + long action chunks), the canonical bimanual-deformable milestone. [pi.website; DeepMind; NVIDIA; Annual Reviews cloth-manipulation]

**What did NOT cross:** **general deformable manipulation** (thin/slippery/multi-layer fabric generalization **undemonstrated**; no mass-market laundry robot exists — *"the gap is the intrinsic difficulty of deformable manipulation combined with consumer cost/footprint/safety"*); **long-horizon autonomous reliability** (binary end-to-end still the wall, mirroring OSWorld 2.0); **open-world home tasks without teleop fallback.** Physical **generalization improved in software; deployment reliability did not.**

### C.2 Humanoid + embodied HARDWARE reality — deployments are pilots/demos, not fleets

- **No humanoid is deployed above the low hundreds of units in a sustained, commercially-priced production environment as of mid-2026.** The clearest real data points: **Digit** moved **100,000+ totes** at GXO (commercial); **Figure 02** contributed to production of **30,000+ BMW X3** over ~10–11 months (2025). **Figure 03** at BMW Spartanburg (announced June 2026, Helix 02 VLA, "sequencing" logistics) is explicitly described as a **demonstration, not a fleet-scale commercial rollout.** [The Robot Report; BMW press; Standard Bots]
- **Shipments up, but it's cheap research iron, not deployed labor:** global humanoid shipments **~19,100 units in H1 2026 (+272% YoY** from 5,100). The bulk are low-cost research/education units — **do not read as deployed labor.** [Standard Bots; RoboZaps]
- **Unit-cost curve:** $30K–$1M+. **Unitree G1 $13,500, H1 ~$90K; Digit ~$250K; Tesla Optimus internal ~$150K** (target $20–30K, 2026–27); **1X Neo $20K or $499/mo subscription.** [Standard Bots; optimusk.blog]
- **Reliability/MTBF: not disclosed by any OEM — itself the tell.** Analysts flag the bottleneck has shifted from *"can we build them"* to *"what can they reliably do"*; MTBF from real factory environments is the missing number. [theaiinsider; Standard Bots]
- **Tesla Optimus:** Musk claimed **1,000+ Gen-3 units on the Fremont floor (Jan 2026)** and a **50,000–100,000-unit/yr** target — **treat as aspirational; production is publicly acknowledged behind schedule.** First external commercial customers targeted late 2026. **Do not bank Musk unit targets as deployed labor.** [SEC 8-K FY2026; optimusk.blog — Musk statements, not audited deployment]
- **Valuations (funding ≠ labor):** Figure **~$39B** (OpenAI-led round), 1X **~$10B**, Apptronik **~$5.5B**, Skild **>$14B**, Physical Intelligence **$5.6B** (raising toward a reported $11B). **Unitree IPO'd on the Shanghai STAR Market 6 Aug 2026 at ~$9.04B** (raised ~$904M; **$235M 2025 revenue, 60% GM, 5,500+ units 2025**). [ValueAdd VC; Bybit; TechCrunch]

> **Unitree correction to p3's hype-flag:** the frozen taxonomy cited "**Unitree ~$50B/200×**" as a bubble signal. The **realized public-market valuation is ~$9B (~38× 2025 sales), not $50B** — the $50B was a private-market rumor. Still rich (~38× sales), but the correct number deflates the flag by ~5×. **Keep the discipline (never convert humanoid valuation/shipped units into deployed labor); update the figure.**

**Framework discipline holds:** physical gaps remain **hardware-timeline problems (5–15yr), largely independent of software AI.** Better VLAs (§C.1) did not move humanoid **deployment reliability, cost, or count** materially. **Physical-track capture stays <1–1.5%** (p0/p3 flag unchanged).

---

## D. The embodied data / teleop / sim layer — investable-layer read

**This is where the framework's E6 / HTC robotics thesis lives, and the refresh strongly corroborates the "invest the data layer, not the humanoid OEM" position.**

- **Data is *the* binding constraint of embodied AI in 2026** — *"action-paired sensorimotor data does not exist at internet scale."* Every frontier VLA above (π0.7, GR 1.5, GR00T, Skild) is explicitly **data-bound**, and each leans on the same **three-layer stack**: **teleoperation (fidelity) + simulation (scale) + human video (diversity).** [Shaip; evsint; QubitTool]
- **Teleoperation economics** are the hard reality: a skilled teleoperator produces only **~5–50 episodes/hour**, and quality degrades with fatigue — i.e. a **labor-intensive, hardware-decoupled bottleneck** that scales with *people and process*, not chips. This is precisely the "investable layer" profile.
- **CyberOrigin (HTC portfolio anchor) — validated positioning:** self-describes as **"Ground Truth for Embodied Intelligence"** — high-fidelity data **"verified to the frame"** for the **labs and world-model teams** training physical AI. This is the **high-signal, hardware-decoupled data-and-verification layer** the thesis targets, sitting *upstream* of and *independent from* any single humanoid OEM. [cyberorigin.ai]
- **Comparable / competitive set:** **AGIBOT WORLD** (open-sourced free-form teleop dataset), **OXE / RT-X** (Google DeepMind, **1M+ episodes, 22+ robot types** — pooled cross-embodiment beats single-embodiment), **IO-AI Tech, Genrobot**, and **1X** (unusually transparent teleop-training pipeline). Sim tooling is a distinct sub-layer (Cosmos, SimFoundry, JoyAI-Sim, the "embodied data pyramid").
- **Capital is validating the layer:** embodied-AI funding **$3.09B (2024) → $4.23B (2025) → ~$5.6B by early July 2026** (already past full-year 2025 before mid-year). [Crunchbase; New Market Pitch; evsint]
- **The honest caveat that *is* the thesis:** "home humanoids" shipping in 2026 (e.g. **1X Neo**) are **substantially teleoperated** — a human remote-operator is in the loop for hard tasks. This is the framework's **staged-vs-paid** distinction made concrete: today's "autonomous" home robot is often a **teleop puppet generating training data**, which is exactly *why* the teleop/data layer — not the OEM — is where near-term value and defensibility sit.

**Read:** the data/teleop/sim layer is the **one part of the physical stack that is (a) capability-gating for everyone, (b) hardware-decoupled, (c) labor/process-scaled rather than capex-scaled, and (d) not yet incumbent-captured.** CyberOrigin's frame-verification angle (data *quality/ground-truth*, not just volume) is a defensible sub-position as the market floods with raw teleop volume.

---

## E. Capability deltas that should propagate into the taxonomy

Separating **REAL unlocks** from **hype** (per p3's ARR/benchmark reality-ladder discipline):

**REAL — propagate:**
1. **80%-gate note (H/V), digital back-office:** update the p3 refrain *"OSWorld ~20% gate"* → **"OSWorld 2.0 ~31% binary / 72.6% partial (GPT-6 Astra/Opus 5, Sept 2026)."** Touches **W1.7, SA.3, SA.5, W11.1** — reliability improved ~+11pts binary but **still not production-cleared**; conviction/Conv unchanged, gate narrowed not opened.
2. **METR H-axis data fix:** replace the unverified **"~32h @50%"** with **"single-digit-to-~12h measured; METR flags >16h unreliable; Astra/Opus 5 unscored."** The 50%-vs-80% gap (p0's core caveat) is **reaffirmed, not relaxed.** This is a data-integrity correction on par with the frozen METR −4% fix.
3. **OSWorld version-lock:** tag every OSWorld citation as **Verified (~85%, easier)** vs **2.0 (~31% binary, hard)**; the p0 "~20.6%" was 2.0. Never let the ~85% headline enter a displacement estimate. (R5 definition-lock.)
4. **Coding (W1.1) — no change from GPT-6:** Astra coding is a **tie**, no autonomy step-change → **C1's capture-expansion thesis and Q4-2027 resolver stand unchanged.** Explicitly note "GPT-6 did not move W1.1."
5. **P-axis / physical-family "brain" (W5/W6):** VLA cross-embodiment + compositional generalization (π0.7, GR 1.5, Skild, GR00T-N2) is a **real software delta** → **reinforces p0's "brain decoupled, moat moved to atoms."** But it **does not move W5/W6 Net or capture** (<1.5%) — the gate is hardware/deployment, not the brain. Update the *rationale*, not the score.
6. **Physical-track deployment reality:** Figure 03 = **demo not fleet**; humanoid shipments +272% are **research iron**; Unitree public val **~$9B not $50B**. Refresh the p3 hype-flags accordingly (W5.3, W9, W6.3).

**HYPE — do NOT propagate:**
- OSWorld-**Verified** "beats humans (86% > 72.4%)" — wrong benchmark for displacement.
- ARC-AGI-3 **99.9%** (OpenAI harness; 62.7% standard) — headline-gamed.
- Humanoid shipments **+272%** as "deployed labor" — it's cheap research units.
- **Unitree/Figure/Skild valuations** as labor proxies — funding/valuation is deployment-cost velocity (p3 Reality-Ladder Tier-D).
- **"32h autonomy"** and **"laundry solved"** — both overstate; folding generalizes narrowly, horizon exceeds METR's ceiling.

---

## F. Candidate NEW physical/embodied verticals the W5/W6/W9/W10 map may be missing

**The sharpest gap:** the framework has **W8 for the *digital* agent-economy's net-new labor** ("software & compute out"), but **no equivalent family for the *robot* economy's net-new *physical/operational* labor.** As embodied AI scales, it *creates* a cluster of hardware-decoupled, people-scaled occupations — the CyberOrigin-adjacent investable layer. Candidates (name · one-line · why now):

1. **Teleoperation-as-a-Service / embodied-data operators** — net-new physical labor collecting frame-verified robot demonstration data (the "W8 of atoms"). *Why now:* data is the binding constraint for every VLA; teleop yields only ~5–50 episodes/hr → a real, scaling, labor-intensive market (CyberOrigin, AGIBOT, 1X). **Highest-conviction addition; directly = HTC thesis.**
2. **Robot fleet remote-supervision & intervention ("robot wrangler")** — net-new humans monitoring/tele-intervening on "autonomous" humanoid fleets. *Why now:* every shipped home/factory humanoid (1X Neo, Figure) runs with a human fallback; someone staffs the exception queue. Physical twin of **W8.1** Agent Ops.
3. **Humanoid/robot commissioning, integration & field-maintenance (physical FDE)** — install, calibrate, repair, retask robot fleets on-site. *Why now:* Figure/BMW expansion + **undisclosed MTBF** ⇒ heavy, durable maintenance labor per deployed unit; adjacent to but distinct from W6.4 field-service.
4. **Simulation & synthetic-environment engineering for physical AI** — building/verifying the sim + 3D-asset "scale" layer of the data pyramid (Cosmos/SimFoundry/JoyAI-Sim). *Why now:* sim is now a mandatory layer of every robot-foundation-model data stack; net-new specialized labor + `[$]` tooling.
5. **Embodied-data annotation & frame-verification labor** — the physical-data twin of **W8.4** (quality/ground-truth verification "to the frame," à la CyberOrigin), distinct from digital RLHF. *Why now:* raw teleop volume is flooding in; the bottleneck is shifting volume→*verified quality*.
6. **Deformable-object / textile manipulation** — a distinct dexterity-frontier watch-cell (laundry, garment, food-handling), currently smeared across W5.7/W6.5/W6.7. *Why now:* π0 crossed the **narrow** folding threshold (>80% known garments) while **general** deformable manipulation remains unsolved — worth isolating as the one place physical dexterity is *measurably* moving, with an explicit "narrow-crossed / general-blocked" flag.

> **Recommendation:** open a small **net-new physical-labor cluster (a "W8-physical" / robot-economy-labor overlay)** to home #1–#3 (and #5), mirroring W8's intake rule (net-new *humans* in — teleoperators, robot-ops, robot-FDE, data-verifiers; robot *hardware/compute* stays `[$]`). This is the labor-*creation* side of the physical story a displacement-only physical map (W5/W6/W9/W10) structurally misses — and it is exactly the hardware-decoupled, not-yet-incumbent-captured layer the robotics thesis wants to own.

---

## Sources (web-verified 2026-09-16)

**Digital / GPT-6:**
- [Wikipedia — GPT-6 Astra](https://en.wikipedia.org/wiki/GPT-6_Astra) (release 3–4 Sept 2026; 100k-GPU train; recurrent-depth; cyber delay/gating)
- [OpenAI — Previewing GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)
- [Artificial Analysis — Benchmarking GPT-6 Astra](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra) (Index 53; cost-efficiency; Terminal-Bench 59%; "incremental, not step-change") — most neutral source
- [benchlm — GPT-6 Astra](https://benchlm.ai/models/gpt-6-astra) (1.05M ctx; OSWorld 2.0 72.6%; DeepSWE 74.1%; BrowseComp 91.5%; GPQA 96%)
- [MindStudio — GPT-6 Astra benchmarks](https://www.mindstudio.ai/blog/gpt-6-astra-benchmarks-analysis) · [Vellum](https://www.vellum.ai/blog/gpt-6-astra-benchmarks-explained) · [DataCamp — Astra vs Fable 5.1](https://www.datacamp.com/blog/gpt-6-astra-vs-claude-fable-5-1) · [codersera — Astra vs Opus 5](https://codersera.com/blog/gpt-6-astra-vs-claude-opus-5-2026/) (pricing $10/$50; 2× Opus 5) — *Tier-2 aggregators; treat GPT-6 benchmark specifics as directional pending OpenAI's model card*
- [METR — Time Horizons](https://metr.org/time-horizons/) (">16h unreliable"; lags newest) · [METR — limitations note, Jan 2026](https://metr.org/notes/2026-01-22-time-horizon-limitations/) · [Epoch AI — METR Time Horizons](https://epoch.ai/benchmarks/metr-time-horizons)
- [arXiv 2606.29537 — OSWorld 2.0](https://arxiv.org/abs/2606.29537) · [osworld-v2.xlang.ai](https://osworld-v2.xlang.ai/) · [Snorkel — OSWorld 2.0 leaderboard](https://snorkel.ai/leaderboard/os-world-2-0/) · [benchlm — OSWorld-Verified](https://benchlm.ai/benchmarks/osworld-verified) (Qwen3.8 Max 86.1%; human 72.4%)

**Physical / embodied:**
- [DeepMind — Gemini Robotics 1.5](https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/) · [arXiv 2510.03342](https://arxiv.org/abs/2510.03342) · [Gemini Robotics On-Device](https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)
- [Physical Intelligence — π0.7](https://www.pi.website/blog/pi07) · [arXiv 2604.15483](https://arxiv.org/abs/2604.15483) · [π0.5](https://www.pi.website/blog/pi05) · [TechCrunch — PI raising $1B at >$11B](https://techcrunch.com/2026/03/27/physical-intelligence-is-reportedly-in-talks-to-raise-1-billion-again/)
- [NVIDIA — Isaac GR00T N1.7 (HF)](https://huggingface.co/blog/nvidia/gr00t-n1-7) · [NVIDIA Isaac GR00T dev](https://developer.nvidia.com/isaac/gr00t)
- [The Robot Report — Skild AI $1.4B / >$14B](https://www.therobotreport.com/skild-ai-raises-1-4b-building-omni-bodied-robot-skild-brain/) · [BusinessWire](https://www.businesswire.com/news/home/20260114335623/en/)
- [The Robot Report — BMW deploys Figure 03](https://www.therobotreport.com/bmw-group-deploys-figure-03-humanoid-after-tests-previous-version/) · [BMW press — Figure 03 Spartanburg](https://www.press.bmwgroup.com/global/article/detail/T0458778EN/) ("demonstration"; Figure 02 → 30,000+ X3)
- [Standard Bots — Humanoid robots 2026](https://standardbots.com/blog/humanoid-robot) (low-hundreds deployed; 19,100 units H1 2026 +272%; unit costs) · [theaiinsider — State of Humanoid Robotics 2026](https://theaiinsider.tech/2026/08/21/) (MTBF gap)
- [Tesla 8-K FY2026 (SEC)](https://www.sec.gov/Archives/edgar/data/1318605/000162828026022956/exhibit9911111.htm) · optimusk.blog (Musk unit claims — *unaudited*)
- [ValueAdd VC — Unitree IPO ~$9.04B](https://valueaddvc.com/blog/unitree-ipo-2026-valuation-how-it-ranks-against-figure-1x-tesla-optimus) · [ValueAdd VC — Figure/1X/Apptronik/Tesla compared](https://valueaddvc.com/blog/humanoid-robots-in-2026-figure-apptronik-1x-and-tesla-optimus-compared)
- [CyberOrigin](https://cyberorigin.ai/) ("Ground Truth for Embodied Intelligence"; frame-verified data)
- [The Robot Report — AGIBOT WORLD 2026 dataset](https://www.therobotreport.com/agibot-world-2026-dataset-open-source-accelerate-embodied-ai-development/) · [Shaip — robot training data strategy](https://www.shaip.com/blog/robot-training-data-strategy/) (teleop 5–50 episodes/hr; the 3-layer stack) · [evsint — embodied AI data collection 2026](https://www.evsint.com/embodied-ai-data-collection-teleoperation-sim-to-real-2026/)
- [Crunchbase — embodied AI record funding China](https://news.crunchbase.com/robotics/embodied-ai-fuels-record-funding-china-ipo-momentum-builds/) · [New Market Pitch — embodied AI funding trends](https://newmarketpitch.com/blogs/news/embodied-ai-funding-trends) ($3.09B→$4.23B→$5.6B)
- [Annual Reviews — Robotic Cloth Manipulation](https://www.annualreviews.org/content/journals/10.1146/annurev-control-022723-033252) (π0 >80% T-shirt fold; general deformable unsolved)

**Sourcing caveats (per p0 R1–R9):** GPT-6 Astra benchmark specifics rest on **Tier-2 aggregators** (Artificial Analysis is the strongest); OpenAI's own model card was not retrievable — flagged directional. METR has **not** officially scored Astra/Opus 5; horizon deltas for those are inferred. Humanoid deployment counts and Musk unit targets are **operator claims, not audited** — held to the p3 "shipped units ≠ deployed labor" discipline.
