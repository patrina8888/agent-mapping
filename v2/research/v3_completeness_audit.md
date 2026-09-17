# v3 — Completeness Audit (MECE Coverage Proof over the FULL updated map)

HTC internal · **2026-09-16** · Workstream-1 completeness gate. Audits the **combined digital + physical v3 map** for coverage (nothing missing) and exclusivity (nothing double-counted), applying the pipeline's completeness methodology (`v3_pipeline_spec.md` §A). This is the "did we miss anything" answer.

**What was audited (the combined inventory):**
- **Existing digital tracks** — the p3 frozen taxonomy's non-physical families: W1, W2, W3, W4, the W7 relational overlay, W8, W11, W12.1, W13, W14, plus the Services-Arbitrage (SA.\*) and Autonomous-Business-Ops (AO.1) overlays, and the **W15 recursive-R&D family** (W15.1/W15.2) that the scored dataset opened as two Tier-B rows (G2 decision #1 resolved toward opening it). *(The scored dataset is **78 rows** — the 76 frozen + W15.1/W15.2.)*
- **GPT-6 delta** (`v3_gpt6_delta.md`) — **zero integer rescores across 78 rows**; a handful of descriptive gate-notes and one conviction-basis firming (W2.4). The delta changes **no wage-bill figure and adds no cell**, so it changes nothing in a coverage sense. It is noted here only to confirm it introduced no new labor pool and retired none.
- **The new PhysicalAI family** (`v3_physicalai_architecture.md` + packs `v3_pack_P1…P8.md`) — **P1–P7** re-home the scattered physical rows (W5/W6/W9/W10-physical/W12.2) onto the environment-structure × task-physics axis; **P8** adds the net-new robot-economy labor overlay (physical twin of W8).

**Governing discipline (non-negotiable, carried from p0/p0b/p3):** (1) **coupling** — coupled value = capture-rate × displaced wage bill; never sum software-TAM + labor-TAM; overlays are non-additive re-cuts. (2) capability ≠ capture; physical capture <1.5% today. (3) physical gaps are a hardware timeline (5–15 yr). (4) `[W]` displaceable wage bill / `[L]` latent-unmet / `[$]` market-revenue proxy — **never sum `[W]` with `[$]`**.

---

## 1. MECE COVERAGE PROOF

MECE = **M**utually **E**xclusive (no dollar counted twice) and **C**ollectively **E**xhaustive (no labor pool with no home). We prove it against the three fixed denominators the pipeline mandates, then run the two mechanical tests (exhaustion, exclusivity).

### 1.1 The three denominators (pipeline §A.1)

| Universe | Size | Role in the proof |
|---|---|---|
| **Global wage bill** | **~$60T** (band $58–61T; formal-wage floor ~$48T) — ILO labour-income-share 52.4% × world GDP ~$118T (p0 §2) | The **dollar denominator**; every cell's `[W]` sums toward it, net of overlays and named carve-outs. |
| **Occupation universe** | **BLS SOC ~830** detailed occupations → **ISCO-08** (global) + O\*NET tasks | The **occupation denominator**; every SOC/ISCO code maps to a track or a named carve-out. |
| **Physical-task taxonomy** | O\*NET work-activities × a manipulation axis (grasp / deformable / locomotion / unstructured-env) | Catches dexterity/mobility labor the SOC codes bucket coarsely — the axis the PhysicalAI re-home is built on. |

Three, not one, because the dollar universe hides low-wage/high-headcount pools (the known dollar-weighting bias p6 flagged), the occupation universe hides net-new agent-/robot-economy roles with no SOC code yet (W8/P8), and the physical taxonomy catches manipulation work SOC smears together. **A cell is "covered" only when placed against all three.**

### 1.2 The partition — big buckets, each counted once

Figures are displaceable wage bill `[W]`, shown as p0 **family-prior bands** (the exhaustion anchor) with the **named-track point sum** from the scored dataset beside them, so the intra-family gap is visible rather than hidden.

| Bucket | Home in the combined map | Family-prior band `[W]` | Named-track point sum (scored) | Counted once via |
|---|---|---:|---:|---|
| Digital, outcome-verifiable | W1.1–W1.8 | $2.5–3.5T | ~$2.3T | coding coupled pool (W1.1b+SA.4) reconciled to one $250–400B pool |
| Digital, judgment-graded | W2.1–W2.7 | $4–6T | ~$3.2T | W2 flagged internally overlapping — **do not sum within W2** |
| Digital, real-time interpersonal | W3.1–W3.7 | **$8–12T** | **~$2.3T** | ← the largest intra-family gap; see §2 |
| Licensed, sign-off gated | W4.1–W4.10 | $4–6T | ~$2.4T | W4.10↔SA.3 claims reconciled once |
| Public sector | W11.1–W11.3 | (within families) | ~$2.3T | education W11.2 blocked, not missing |
| ISR (digital) | W12.1 | — | ~$0.1T | disjoint from W12.2→P7 |
| Media/content | W13.1–W13.2 | — | ~$0.5T | — |
| Consumer personal assist (paid) | W14.1 | — | ~$0.05T (+ ~$11T `[L]`) | `[L]` overlaps P6 care — see exclusivity |
| Recursive R&D | W15.1–W15.2 | — | ~$0.12T | net-new/`[L]`, tiny elite headcount |
| **Physical / embodied (re-homed)** | **P1–P7** | W5 $5–7T + W6 $9–13T + W9/W12.2 | **~$15.0T** | each frozen physical row homed **once** (§1.4) |
| Agent-economy net-new (digital) | W8.1–W8.6 | $10–20B | ~$0.02T | intake rule: humans in, software `[$]` out |
| **Robot-economy net-new (physical)** | **P8** | $5–15B, >100% YoY | ~$0.01T | intake rule mirrors W8; **outside the $15T** |

**Overlays (non-additive re-cuts — excluded from the exhaustion sum by construction):** Services-Arbitrage SA.1–SA.6 (re-cut of W1/W2/W3), Autonomous Business Ops AO.1 (re-cut of W1+W2+W3), W7 relational premium (embedded in W2/W3/W4), and the W10-physical slices overlay-stamped into P2/P5. These are **views of dollars already counted**, never added.

### 1.3 Exhaustion test (does it reconcile to ~$60T?)

The test runs at two levels, and honesty requires showing both:

- **Family-prior level (the anchor):** p0's reconciliation holds — W1–W7 family-prior midpoints ≈ **$40–48T**, plus the named residual carve-out **$12–18T**, ≈ **$52–66T ⊇ $60T**. The PhysicalAI re-home is **inside** this: P1–P7 = **$15.0T**, squarely within W5 ($5–7T) + W6 ($9–13T) + W9/W12.2. **The re-home re-organizes the physical universe; it adds no displaceable dollar** (proof in §1.4). ✔ reconciles in-band.

- **Named-track level (the honest gap):** the 78 scored rows sum to only **~$24.7T** of point-estimate `[W]` (physical W-rows $13.7T incl. W10; digital $11.0T). Named tracks therefore **under-fill the family priors by ~$15–23T.** That under-fill is **not a hole in the families** — the families tile the $60T — it is **thin named-track coverage inside covered families**, and it is heavily concentrated in one place: the W3 real-time-interpersonal prior ($8–12T) vs its named tracks (~$2.3T). This is the single most important completeness finding and it is the subject of §2.

**Reconciliation, stated plainly:**
> ~$60T ≈ **named partition tracks (~$25T point / ~$35T at midpoints)** + **physical re-home already inside the family priors** + **named carve-outs ($12–18T)** + **intra-family thin cells ($15–23T, mostly in-person interpersonal/personal services)**. Every dollar is either in a named track, in a named carve-out, or in an explicitly-identified thin cell — none is silently lost.

**Named residual carve-outs (deliberately not force-fit into W1–W15, per p0 and architecture §4):** broad-acre row-crop agriculture (combines/planters = solved capital equipment, ~$2–4T), bulk mining/extraction & drilling, fishing/forestry harvest, fixed-process heavy industry (steel/refining), informal/subsistence labor, and unpaid domestic service. These are `[$]` capital-equipment or non-market stories with **no incremental embodied-AI *labor* wedge**; autonomous mining haulage (Komatsu FrontRunner, Caterpillar Command — real private-road fleets) is noted P3-adjacent/`[$]`, not a mass labor market. **Named and excluded, not dropped.**

### 1.4 Exclusivity test — no double-count (the guards, with the PhysicalAI check the task asked for)

Every SOC/ISCO occupation must have exactly one `home_track`; genuine straddlers are split once with a fixed percentage and the dollars counted once. Nine guards, each verified:

**① PhysicalAI P1–P7 ↔ W5 / W6 / W9 / W10 / W12.2 — THE guard the task flagged. The architecture's reconciliation holds.**
- Architecture §3.1 maps **each frozen physical row → exactly one P home** (W5.3→P1, W5.1→P2, W9.\*→P3, W6.1/6.2/6.4/6.5→P4, W6.6/6.7→P5, W6.3→P6, W5.4/W12.2→P7). Sum of homes = **$15.0T = sum of absorbed rows.** No dollar created, none counted twice. ✔
- **The one live risk is presentational, and must be stated:** P1–P7 and the original W5/W6/W9/W12.2 rows are **two views of the same ~$15T.** The scored `its_ranked.csv` still carries the W-organized physical rows (it scores the 78-row W-taxonomy); the P-family is a **parallel capability re-cut.** Anyone who sums "78 W-rows **+** 8 P-rows" double-counts the entire physical ~$15T. **Enforcement: tag P1–P7 as non-additive-with-{W5,W6,W9,W12.2}; the combined map presents physical dollars through *one* organization at a time — the P-capability view for the gate, the W-industry view for the score — never summed.** With that tag, the guard holds. ✔
- **W12.1 ↔ W12.2:** disjoint — digital ISR *analysis* stays in W12.1 (digital, unchanged); autonomous defense *systems/logistics* home wholly in P7 (mobility-logistics scored-as-P3 but booked-in-P7 to avoid splitting a small $0.175T sovereign line). No overlap. ✔

**② W10 straddler (retail / hospitality / food-service front-of-house) — handled by dominant-slice + overlay stamp.** W10.1/10.2/10.3 mix a *physical* slice (shelf-stocking, delivery/reception robots, housekeeping soft-goods, food-running) and a *digital/transaction* slice (cashiering, ordering, reservations). The physical slice is **overlay-stamped into P2/P5 (NOT summed into the $15T)**; the transaction slice stays digital (W1.7/W3). W10's full ~$1.8T stays counted **once** in its industry rows; the P2/P5 stamps are non-additive re-cuts. ✔ *(Consequence to note: the $15T physical partition **excludes** W10 — "total embodied labor" = $15T + W10-physical-slice + P8. Minor, but keep it straight.)*

**③ W8 (digital net-new) ↔ P8 (robot-economy net-new).** Disjoint by intake rule: human supervises a *software* agent → W8.1; human tele-operates or physically services a *robot* → P8. Embodied-data frame-verification (P8) ≠ digital RLHF labeling (W8.4) — different data types, sized separately. Both sit **outside** the displaceable base (creation, never subtracted or summed). ✔

**④ W1.8 SOC (digital) ↔ P7 sensing/security (physical).** Deliberate structural mirror, zero overlap — SOC analysts vs security guards/inspectors are disjoint wage bills; both share the "understaffed → compression + `[L]` backlog" shape only. ✔

**⑤ Coding pool.** W1.1b junior (~$50–150B) + SA.4 commodity slice (~$200–250B) = one **$250–400B coupled coding-displacement pool, counted once**; W1.1a seat-ARR is additive/Expansion, never subtracted. ✔ (GPT-6 delta explicitly left this unchanged.)

**⑥ Insurance.** W4.10 claims wedge ↔ SA.3 transaction-processing reconciled once (RCM-twin profile). ✔

**⑦ Overlays.** SA.\*, AO.1, W7 tagged `non_additive:true`, excluded from the exhaustion sum. ✔

**⑧ Surgical / precision robotics — correctly excluded, not double-homed.** Web-verified (2026-09-16): autonomous soft-tissue surgery is preclinical only; da Vinci-class systems are teleoperated master-slave tools with the surgeon in the loop → additive `[$]` capital equipment, **not** a P sub-family. Named and excluded (mirror of W4.6 blocked-by-clearance). ✔

**⑨ Latent-`[L]` double-count — the one flag on the `[L]` column (not the wage bill).** W6.3/P6 personal-care informal (**~$11T `[L]`**) and W14.1 consumer/household personal assistance (**~$11T `[L]`**) look like the **same unpaid domestic-and-care pool** viewed from two families. This does not affect any `[W]` figure (both are latent), but if the two `[L]` tails are ever added, that is a ~$11T phantom. **Enforcement: treat P6-informal and W14.1-`[L]` as one pool, counted once; never sum the latent tails.** ⚠ flag.

**Exclusivity verdict:** all nine guards hold with the two enforcement tags above (① presentational non-additive tag; ⑨ single-count the informal-care `[L]`). No `[W]` dollar is double-counted in the combined map.

---

## 2. RESIDUAL WHITE CELLS — the "did we miss anything" answer, ranked by size

The white-cell finder (pipeline §A.3) run against the combined map. Two classes: (A) **thin cells** — a covered family exists but the named tracks under-fill it; (B) **un-homed cells** — labor with no family that cleanly claims it. Ranked by approximate displaceable wage bill.

| # | Residual white / thin cell | Est. size `[W]` | Class | Why it has no clean home | Nearest home / proposed action |
|---:|---|---:|---|---|---|
| **1** | **In-person interpersonal & personal services tail** — hairdressing/beauty, fitness/personal training, paid childcare & early-ed aides, pet care, funeral, in-person event & personal service staff | **~$3–6T** | Thin (W3 under-fill) | The W3 prior ($8–12T) vs named tracks (~$2.3T) is the map's biggest gap. Much re-homes to P6 (care), W10 (retail/hospitality), W11 (public) — but a large **formal, paid, physical-presence, trust-gated** service tail fits **no named track and no P cell** (not manipulation-frontier, not digital). Dollar-weighting bias hid it. | Open **W3.8 "In-person consumer & personal services"** as a Tier-B thin cell with a headcount-companion figure; capture ≈ 0 (trust + presence gate), so low investability but needed for MECE. **Top gap.** |
| **2** | **General corporate knowledge/admin under-fill** — HR generalist/people-ops, corporate ops/admin, procurement/supply-planning coordinators not in W2.6, general analysts | **~$1–2T** | Thin (W2/W4 under-fill) | W2 is flagged "internally overlapping — do not sum," which correctly prevents double-count but leaves a real admin/HR/ops slice under-named. | Confirm these SOC codes straddle W2.6/W1.7; add a `straddle[]` note. Mostly Additive/Expansion; low urgency. |
| **3** | **Air / sea / rail transport crews** — airline pilots & cabin crew, merchant-marine & fishing crews, rail locomotive engineers/conductors | **~$0.3–0.6T** | Un-homed | **P3 is "open-ROAD" only.** There is no cell for non-road transport labor; aviation/maritime/rail fall through the P3 boundary. | Open **P3b "Non-road autonomous transport (air/sea/rail)"** as a watch-cell — heavily R=5 (safety-case), capture ~0 near-term, but a genuine boundary hole. |
| **4** | **Protein & food processing manipulation** — meat/poultry/seafood slaughter, cutting, deboning; high-injury, high-automation-interest | **~$0.15–0.3T** | Un-homed / smeared | Contact-rich **deformable** manipulation performed on a **structured plant line** — falls between P1 (structured cell) and P5 (deformable frontier); neither cleanly claims it. | Overlay-stamp into P5 with a P1-line note; it is a real deformable watch-target (the tissue analogue of garment folding). |
| **5** | **Apparel / textile / footwear sewing** — garment manufacturing labor (needle trades) | **~$0.2–0.5T** | Un-homed / smeared | Deformable-fabric manipulation in a semi-structured factory. p0b flagged textile handling as "smeared across W5.7/W6.5/W6.7"; P5 isolates the *frontier* but the large **manufacturing sewing wage bill** has no named row. | Home the sewing wage bill in P5 explicitly (currently only the frontier watch-line is there); it is the canonical "general deformable unsolved" pool. |
| **6** | **Waste, sanitation & recycling sorting** — refuse/recyclable collection, materials-recovery-facility sorting (AMP Robotics-class) | **~$0.1–0.2T** | Un-homed / smeared | Semi-structured mobility (collection) + deformable sorting (MRF); split across P2 (mobility) and P5 (sorting), homed in neither. | Overlay-stamp: collection→P2, MRF sorting→P5; note as one occupation split once. |
| **7** | **Utilities plant & field operations** — power/water/gas plant control-room operators + field line/pipe operations | **~$0.1–0.3T** | Thin / smeared | Control-room ops read as digital-ish (W1.7-adjacent); field line-work reads as P4 (unstructured field manipulation). No named utilities row. | Split once: control-room→W1.7 note; field→P4 note. Low urgency. |
| **8** | **Financial-markets execution** — traders/market-makers/execution desks (distinct from W2.2 analysis) | **~$0.05–0.15T** | Thin | High-comp, low-headcount; W2.2 covers *analysis*, not *execution*. Small dollars, but a named-gap. | Straddle-note under W2.2; likely Additive. Low urgency. |

**Note on the net-new leading-indicator cells (W8 $10–20B, P8 $5–15B, W15 R&D ~$0.12T):** these are **thin by design**, not gaps — they are the creation-side leading indicators the map added on purpose. P8 is the *most important* thin cell to grow (it is the CyberOrigin/robotics-thesis layer and the pipeline's own top open white cell), but it is a **known, opened** cell, not a miss.

**What is correctly NOT a white cell** (so the audit is honest about its exclusions): agriculture broad-acre, bulk mining/extraction, fishing/forestry, fixed-process heavy industry, unpaid domestic labor, and informal/subsistence work — all **named carve-outs** ($12–18T), excluded by design as capital-equipment or non-market stories with no embodied-AI labor wedge. BLOCKED cells (W1.5, W4.1/4.4/4.6/4.8/4.9, W11.2/11.3) and TOO-EARLY cells (P4/P5/P6, W10) **have homes** — they are gated, not missing.

---

## 3. CONSOLIDATED VERDICT

**Is the v3 map exhaustive enough to stand behind? — Yes, with two enforcement tags and one new thin cell to open.**

The combined digital + physical map is **collectively exhaustive at the family level**: the 15 families + PhysicalAI P1–P8 + named carve-outs tile the ~$60T global wage bill within its stated band, and every big bucket has a home. It is **mutually exclusive**: all nine double-count guards hold, and — the check the task asked for — **the PhysicalAI-vs-W5/W6/W9/W10/W12.2 reconciliation holds**: P1–P7 re-home each frozen physical row exactly once, add no displaceable dollar, and the only live risk is presentational (never sum the P-view and the W-view of the same $15T; never sum the two ~$11T informal-care `[L]` tails). The GPT-6 delta changed no cell and no dollar, so it is coverage-neutral — as expected.

The **one material honesty point** is the named-track under-fill: the 78 scored rows sum to ~$25T of point-estimate `[W]` against $40–48T of in-family labor, a ~$15–23T intra-family gap concentrated in **in-person interpersonal / personal services** (the dollar-weighting bias p6 already flagged). This is thin *named-track* coverage inside covered families, not a missing family — but it is large enough that a "total agent TAM" headline is silently biased against low-wage, high-headcount, in-person service labor. Ship the headcount-companion view alongside, exactly as G2 decision #3 recommended.

**Top 3 coverage gaps to close next (ranked):**

1. **Open W3.8 "In-person consumer & personal services" (~$3–6T).** The single largest hole — the W3 interpersonal prior minus its named tracks. Low investability (trust + physical-presence gate, capture ≈ 0), but required for a defensible MECE claim and to de-bias the headline. Falsifiable trigger: does any funded vendor pin a production wage-replacing metric in personal services by Q4-2027? (Base case: no — it stays a headcount-companion carve-in.)

2. **Close the P-family boundary holes — non-road transport (P3b, ~$0.3–0.6T) and protein/textile deformable manufacturing (into P5, ~$0.35–0.8T combined).** These are genuine *un-homed* cells created by the P-axis's own boundaries (P3 = road-only; P1/P5 seam on structured-line deformable work). Cheap to close by adding one watch-cell and two overlay stamps; all capture ≈ 0 near-term, so this is a completeness fix, not an investability call.

3. **Formalize the two enforcement tags in the dataset so the map cannot be mis-summed:** (a) mark P1–P7 `non_additive_with:[W5,W6,W9,W12.2]` and present physical dollars through one organization at a time; (b) mark the P6-informal and W14.1 `[L]` tails as one pool counted once. Both are latent-today mis-sum risks worth ~$15T and ~$11T respectively if an automated run ever adds the wrong columns — precisely what the pipeline's human gate (§D.3) exists to prevent, but better hard-coded in `coverage_ledger.json` than left to vigilance.

**One-line close:** the v3 map is exhaustive at the family level and clean on double-counting once the two non-additive tags are enforced; the real completeness debt is **thin named-track coverage of the in-person-services long tail**, not a missing family — open W3.8, close the three P-boundary seams, and it stands behind an institutional audit.

---

### Sources / provenance
**Internal (governing):** `p0_foundation.md` (denominator ~$60T, family priors, coupling rule, residual carve-out instruction), `p0b_capability_refresh_2026-09.md` (capability baseline; §F missing-verticals scan), `p3_frozen_taxonomy.md` (frozen 78-context rows, white-space board, reconciliation rulings), `v3_gpt6_delta.md` (zero-rescore delta), `v3_physicalai_architecture.md` (P1–P8 partition + no-double-count proof §3), `v3_pack_P1…P8.md` (per-sub-family evidence), `v3_pipeline_spec.md` §A (completeness methodology: three denominators, exhaustion/exclusivity tests, four-detector white-cell finder), `pipeline/its_ranked.csv` (78-row scored point estimates), `v2_master.json`.
**Discipline:** all `[W]`/`[L]`/`[$]` tags per p0; no software-TAM summed with labor-TAM; carve-outs named not dropped; net-new cells (W8/P8/W15) held outside the displaceable base. Figures are bands (R6 ranges-not-points); named-track point sums are from the scored dataset and are deliberately conservative relative to the family priors — the gap between them **is** the finding, not an error.
