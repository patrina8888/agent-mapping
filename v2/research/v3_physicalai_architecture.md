# v3 — PhysicalAI / Embodied Labor: First-Class Family Architecture

HTC internal · **2026-09-16** · Workstream-2 architecture step. Governs a new first-class dimension of the Agent-Mapping v2 taxonomy: **Family P — PhysicalAI / Embodied**. Builds on p0_foundation (coupling rule, capture rates, pilot-to-production chasm), the p3 frozen 76-row taxonomy (physical rows scattered across W5/W6/W9/W10/W12), and the p0b capability refresh (2026-09-16), which **governs every capability claim here**.

> **Why this document exists.** In the frozen map, physical/embodied labor was scored correctly row-by-row but was **organized by industry vertical** (warehouse, manufacturing, construction, mobility, retail, defense) and **scattered across five families** (W5, W6, W9, W10, W12). Industry is the wrong primary axis for physical work, because robotics capability does **not** gate work by industry — it gates by *how structured the environment is* and *how hard the manipulation is*. A single industry (a hotel, a farm, a hospital) mixes near-solved tasks and 15-year-out tasks. The frozen organization therefore hid the one thing an investor needs to see: **which physical dollars are capturable now, which are hardware-timeline-blocked, and where the hardware-decoupled investable layer sits.** This architecture re-homes the scattered rows onto the axis that actually predicts the gate, adds the net-new "robot-economy labor" overlay the map structurally missed (the physical twin of W8), and does so **without adding a single new displaceable wage dollar** to the map.

---

## 0. The three non-negotiables carried from p0/p0b (repeated because they discipline every number below)

1. **Coupling.** For a coupled track, vendor-realized TAM = **capture-rate × displaced wage bill**. Never sum software TAM and labor TAM — they are two views of one quantity. Overlays (P8, and the W10/defense slices) are **non-additive re-cuts**, never summed into the partition total.
2. **Capability ≠ capture, and physical capture is <1.5% today.** Deployment lags capability by ~10× (MIT 95% zero-P&L; S&P 42% pilot abandonment). Better robot "brains" (π0.7, Gemini Robotics 1.5, GR00T-N2, Skild) improved cross-embodiment and compositional generalization in *software* over the last 6–9 months; they did **not** move humanoid deployment reliability, cost, or fleet count. Realized physical capture stays where p3 pinned it: **<1–1.5%, ceiling in structured manufacturing.**
3. **Physical gaps are a HARDWARE-TIMELINE problem (5–15 yr), largely independent of model IQ.** The binding gate for most embodied work is actuation, dexterity, cost-per-unit, MTBF (mean time between failures — no OEM discloses it, which is itself the tell), and safety-case/regulatory sign-off — **not** the language model. The investable layer is therefore the hardware-decoupled **data / teleoperation / simulation** stack (Family overlay P8), **not** the humanoid OEM (original-equipment manufacturer — the company that builds the robot).

---

## 1. The partition axis — and why this one

### 1.1 The axis: **Environment-structure × Task-physics (dexterity/contact)**

Every unit of embodied labor can be located on two roughly orthogonal capability dimensions, and **together they predict the hardware-timeline gate better than any industry label:**

- **Environment structure** — how controlled, known, and engineered-for-robots the workspace is. This gates the *perception, navigation, and safety* problem.
  - **Structured** — fixtured, caged, engineered around the machine; the world is known and repeatable (a robot cell, a CNC station, a lab bench). *Deployed today.*
  - **Semi-structured** — mapped and bounded but human-shared and variable (a warehouse aisle, a store floor, a sidewalk, a road network). *Deploying now, gated by edge-cases or by regulation.*
  - **Unstructured** — open, novel, dynamic, unbounded (a home, a construction site, an open field, a disaster zone). *5–15 years out.*

- **Task-physics (dexterity / contact)** — the manipulation difficulty of the physical act itself. This gates the *actuation, control, and tactile* problem.
  - **Perception-dominant / near-zero manipulation** — sense, patrol, inspect, read a gauge, watch (light or no actuation).
  - **Locomotion / transport** — move self or a payload; minimal manipulation (drive, carry, scrub a floor).
  - **Gross rigid manipulation** — grasp and place known rigid objects; tend a machine (pick-and-place).
  - **Fine / deformable / contact-rich manipulation** — thin/slippery/multi-layer fabric, food, wires, tissue, assembly, wound care (the dexterity frontier).
  - **(orthogonal modifier) Direct sustained human physical contact** — the safety/trust/licensing gate jumps a full tier when the "object" being manipulated is a person.

### 1.2 Why this axis beats the alternatives

- **vs. Industry vertical (the frozen organization).** Industry mixes difficulty tiers inside one row. A hotel contains near-solved delivery-robot mobility (semi-structured locomotion), the deformable-manipulation wall of bed-making and room-cleaning (unstructured deformable), and a purely digital check-in transaction. Scoring "hotel ops" as one physical cell blurs a deployed capability with a 15-year one. The capability grid cuts **across** verticals and lands each task at its true gate.
- **vs. "humanoid vs. non-humanoid" (the hype axis).** Form factor is a distraction. What gates the work is the *task*, not whether the machine is shaped like a person. A $30k humanoid and a $250k fixed arm can both tend a machine; neither can fold arbitrary laundry. Partitioning by capability cell keeps the map honest about the hardware-timeline gate and immune to the humanoid-fleet valuation bubble (p0b: Unitree public-market ~$9B, not the $50B private rumor; no humanoid deployed above low hundreds of units in a sustained commercially-priced setting).
- **vs. a pure 3×5 matrix.** A full grid would produce ~15 cells, most near-empty and few mappable to a nameable wage bill. So we use the two axes as the **ordering principle** that generates a small set of **contiguous capability bands**, each of which (a) sits at one binding gate, and (b) maps to nameable occupations with a `[W]` wage bill. That yields **eight** sub-families (seven partition bands + one net-new overlay), each a coherent band on the difficulty diagonal.

### 1.3 The diagonal, in one line

Physical work becomes robot-doable roughly along the diagonal **structured-cell manipulation → bounded mobility → open-road mobility (regulatory-gated) → unstructured dexterous → deformable/contact-rich → human-contact care**, with **perception/inspection** running *alongside and ahead* of the whole manipulation ladder (sensing is easier than acting), and a net-new **robot-economy human labor** layer created *underneath the whole thing* to build, supervise, and feed it. The eight sub-families are exactly those bands.

---

## 2. The sub-family table (Family P — PhysicalAI / Embodied)

Scores are **V**erifiability · autonomy-**H**orizon · **P**hysicality · **R**egulatory-gate · **L**ab-capture · **D**ata/incumbent-moat, each 0–5, re-derived to the capability band (not merely averaged from the absorbed rows). Wage-bill figures are the **sum of the absorbed frozen rows' bands, counted once** — no inflation (see §3). `[W]` = displaceable wage bill; `[L]` = latent/unmet; `[$]` = market-revenue proxy (never summed with `[W]`).

| ID | Sub-family | Binding gate | Wage bill (each frozen $ once) | V/H/P/R/L/D | Cpl? | Net | Capture today | Conv |
|---|---|---|---|---|---|---|---|---|
| **P1** | **Structured-Cell Manipulation & Production** | unit-economics / integration | **~$4.2T `[W]`** (W5.2+W5.3+W5.6+W5.7) + net-new lab/pharma & precision-assembly (~$20–40B) | **4/2/4/1/2/4** | Coupled | **Compression** | **~1–1.5%** (the map's ceiling, driven by W5.3) | **High** |
| **P2** | **Bounded-Space Mobility & Frontline Service-Physical** | last-10% edge cases / unit-economics | **~$1.05T `[W]`** (W5.1+W5.5) + physical slice of W10.1/W10.3 & delivery-robot slice of W10.2 *(overlay, not summed)* | **5/2/3/1/2/3** | Coupled | **Mixed** | **<1%** | **High** |
| **P3** | **Open-Road Autonomous Mobility (AV / Transport)** | **R=5 safety-case + liability + insurance** | **~$1.55T `[W]`** (W9.1+W9.2+W9.3) | **5/2/5/5/2/5** | Coupled | **Mixed** | **<1%** | **Medium** |
| **P4** | **Unstructured Dexterous & Field Manipulation** | **hardware-timeline (5–15 yr)** | **~$5.3T `[W]`** (W6.1+W6.2+W6.4+W6.5) | **4/3/5/3/1/4** | Coupled | **Expansion / Mixed** | **~0%** (too-early) | **Low–Med** |
| **P5** | **Deformable & Contact-Rich Manipulation** | **dexterity frontier (narrow-crossed / general-blocked)** | **~$1.3T `[W]`** (W6.6+W6.7) + housekeeping slice of W10.2 *(overlay)* | **4/2/5/2/2/4** | Coupled | **Mixed** | **~0%** | **Low** |
| **P6** | **Human-Contact Care & Physical Assistance** | **human-safety + licensing + trust** | **~$1.1T `[W]` paid + ~$11T informal `[L]`** (W6.3) | **2/4/5/4/1/4** | Coupled | **Expansion** | **~0%** | **Low–Med** |
| **P7** | **Embodied Sensing, Inspection & Security** | telemetry/site-data moat; sovereign slice R=5 | **~$0.5T `[W]` + large `[L]`** (W5.4+W12.2 + net-new security/guarding + energy-mining/infra inspection) | **4/2/3/3/3/4** | Coupled (+ sovereign-additive) | **Mixed** | **<1%** | **Medium** |
| **P8** | **Robot-Economy Labor — teleop / supervision / commissioning / data-verify / sim** *(NET-NEW OVERLAY — physical twin of W8)* | data is the binding constraint of embodied AI | **~$5–15B `[W]` net-new, >100% YoY** | **3/3/1/2/3/3** | Additive (net-new creation) | **Expansion** | n/a (no displaced pool) | **Medium** |

**Partition total (P1–P7, each frozen physical row counted exactly once): ~$15.0T `[W]`** — squarely inside the p0 physical-family priors (W5 $5–7T + W6 $9–13T ≈ $14–20T, before W9/W10-physical/W12.2). The re-home **re-organizes** the physical universe; it does **not** grow it. P8 is net-new `[W]` and sits *outside* that $15T (creation, not displacement).

---

## 3. Reconciliation — the no-double-count proof

**Rule:** every existing physical wage dollar is homed in **exactly one** partition sub-family (P1–P7). Overlays (P8, and the minority slices of straddler rows) are **non-additive re-cuts**, explicitly flagged and never summed into the $15T.

### 3.1 Partition map — each frozen row → one home (dollar counted once)

| Frozen row | Frozen band (mid) | → Home | Why this cell |
|---|---|---|---|
| W5.2 Piece-picking/packing/palletizing | ~$0.75T | **P1** | structured cell, gross rigid manipulation |
| W5.3 Discrete-mfg machine tending | ~$2.4T | **P1** | structured cell, the deployed anchor (capture ceiling) |
| W5.6 Structured construction & offsite prefab | ~$0.65T | **P1** | *prefab in a structured factory* is a fixed-station cell (onsite construction is W6.2→P4) |
| W5.7 Structured food/beverage production | ~$0.4T | **P1** | structured line, gross-to-fine rigid manipulation |
| W5.1 Warehouse goods-movement & AMR | ~$0.85T | **P2** | semi-structured mapped space, locomotion/transport |
| W5.5 Commercial floor cleaning (structured slice) | ~$0.2T | **P2** | bounded floors, locomotion + low manipulation |
| W9.1 Rideshare/Taxi/Robotaxi | ~$0.4T | **P3** | public road, transport, R=5 |
| W9.2 Long-haul & regional trucking | ~$0.7T | **P3** | public road, transport, R=5 |
| W9.3 Last-mile delivery & courier | ~$0.45T | **P3** | road/sidewalk transport, R≈4–5 |
| W6.1 Skilled trades — MEP install & repair | ~$1.2T | **P4** | unstructured buildings, fine contact-rich, non-human-contact |
| W6.2 General construction — unstructured | ~$2.35T | **P4** | unstructured site, gross-to-fine (largest single pool) |
| W6.4 Field service & equipment repair | ~$1.1T | **P4** | unstructured customer sites, diagnostic dexterity |
| W6.5 Cleaning & janitorial — unstructured residual | ~$0.625T | **P4** | unstructured, gross manipulation + mobility |
| W6.6 Specialty-crop selective harvest | ~$0.55T | **P5** | outdoor-variable, deformable delicate produce |
| W6.7 Commercial food prep — QSR | ~$0.75T | **P5** | contact-rich deformable food handling |
| W6.3 Personal care & ADL assistance | ~$1.1T (+$11T `[L]`) | **P6** | direct sustained human physical contact |
| W5.4 Structured visual QC & inspection | ~$0.2T | **P7** | perception-dominant, near-zero manipulation |
| W12.2 Autonomous defense systems & logistics | ~$0.175T | **P7** | ISR/surveillance-physical + logistics mobility, sovereign-gated (R=5/L=5 flag) |

Sum of homes = **$15.0T**, identical to the sum of the absorbed rows. **No dollar is counted twice; none is created.**

### 3.2 The three straddler cases — handled by the dominant-slice rule, minority slice overlay-stamped (not summed)

1. **W10.1 Retail floor & cashiering / W10.3 Food-service front-of-house & ordering.** These are *industry* rows that mix (a) embodied physical service — shelf-stocking, inventory scanning, food-running/bussing, reception/delivery robots — and (b) a **digital/transaction** slice — cashiering, self-checkout, order-taking (voice/kiosk). **Treatment:** the physical-service slice is **overlay-stamped into P2** (and the delivery-robot slice of W10.2 into P2); it is **not** added to the $15T partition total. The cashiering/ordering/transaction slice **stays in its digital home** (W1.7 back-office / W3 interpersonal / self-checkout `[$]` capital). This is the "overlay/re-cut vs. partition" distinction the map already uses for Services-Arbitrage and AO.1: W10's *full* $2.35T is never re-summed into PhysicalAI — only its embodied slice is stamped, once.
2. **W10.2 Hospitality/hotel ops — housekeeping.** Bed-making and room-cleaning are **unstructured deformable/contact-rich manipulation** → overlay-stamped into **P5**; the delivery/reception-robot slice → **P2**; the reservations/front-desk **voice** slice stays digital (W3.6). Again, the full $0.65T is not re-summed — the physical slices are re-cuts.
3. **W12.2 Autonomous defense — mobility-logistics vs. sensing.** Autonomous convoys/logistics are capability-twin to P3 (open mobility) and drones/ISR are capability-twin to P7 (sensing). To keep the frozen $0.175T line **intact and counted once**, W12.2 is homed **wholly in P7** with a **sovereign-gated overlay flag (R=5, L=5)**, and a note that its mobility-logistics portion is *scored as* P3-class but *booked in* P7 to avoid splitting a small sovereign line across two cells. **No overlap with W12.1** (digital ISR *analysis* stays digital, unchanged).

### 3.3 Cross-family boundary guards (no double-count with the digital map)

- **P8 ↔ W8.** W8 counts net-new *digital* agent-economy humans (agent ops, digital FDE, agent eval/red-team, RLHF labeling, agent trust/insurance). **P8 counts net-new *robot*-economy humans** (teleoperators, robot-fleet wranglers, physical robot-commissioning/field-maintenance FDEs, embodied-data frame-verifiers, sim/scenario authors). Boundary: *if the human supervises a software agent → W8.1; if the human tele-operates or physically services a robot → P8.* **Embodied-data frame-verification (P8) ≠ digital RLHF labeling (W8.4)** — different data types (action-paired sensorimotor episodes vs. text/image labels), different labor, counted separately. State it, size it separately.
- **P3 ↔ AV capex.** Only the **driver wage bill** is the `[W]` denominator. The autonomous-vehicle hardware/compute/RaaS spend (Waymo, Aurora, Kodiak) is `[$]` capital, never summed into labor.
- **P7 ↔ W1.8 (SOC).** Deliberate structural mirror, zero overlap: W1.8 is *digital* security-operations triage; P7 is *physical* security/inspection rounds. Both share the "understaffed → compression + `[L]`-backlog expansion" shape, but the wage bills (SOC analysts vs. security guards/inspectors) are disjoint.

---

## 4. MECE-exhaustiveness argument

**Claim:** P1–P8 partition all physical/embodied labor, mutually-exclusively (each dollar once) and collectively-exhaustively.

**Every embodied occupation resolves to exactly one primary cell by its *dominant* capability demand:**

- Is the task **perception-dominant with near-zero manipulation** (patrol, inspect, monitor, read)? → **P7**. (Runs alongside/ahead of the manipulation ladder because sensing is easier than acting.)
- Else, is it **locomotion/transport-dominant**?
  - in **bounded/facility** space → **P2**;
  - on **open public road** (regulatory-gated) → **P3**.
- Else it is **manipulation-dominant**; split by environment × contact:
  - **structured cell**, rigid/gross-to-fine → **P1**;
  - **unstructured** env, rigid/gross-to-fine, **no human contact** → **P4**;
  - **deformable / contact-rich** (any env), the dexterity frontier → **P5**;
  - **direct sustained human physical contact** → **P6** (the contact modifier dominates the gate).
- Finally, **net-new human labor the robot economy itself creates** (build/supervise/feed the robots) → **P8** (creation side, additive, never summed into the displaceable base).

**Tie-break / dominant-slice rule** (makes it mutually exclusive): a straddling occupation is homed by its *binding* capability demand, and any minority physical slice is overlay-stamped (§3.2), counted once. A nurse (care + dexterous clinical tasks) homes in P6 by the human-contact gate, with clinical-documentation in W4.5 (digital) — unchanged.

**Exhaustiveness / residual carve-out.** The physical labor the grid does **not** claim as an embodied-AI *labor* market is the already-mechanized, capital-equipment domain — **broad-acre row-crop agriculture** (combines/planters are solved capital equipment, not agent labor), **bulk mining extraction and drilling**, **fishing/forestry harvest**, **fixed-process heavy industry** (steel, refining). These are `[$]` capital-equipment stories with no incremental embodied-AI *labor* wedge, and they are consistent with p0's explicit instruction to carve out the ~$12–18T residual (agriculture, informal/subsistence, heavy-capital) **separately** rather than force-fit it. Autonomous **mining haulage** (Komatsu FrontRunner, Caterpillar Command — real deployed fleets on **private** haul roads) is capability-twin to P3 but sits at a *lower* R gate (private road, no public liability); it is noted under P7/P3-adjacent as a small, mostly-`[$]`-capital line, not a mass labor market. This residual is named and excluded, not silently dropped.

---

## 5. First-pass scores, coupling, net, conviction — sub-family by sub-family

Each block: the score rationale, the coupling/net call, the capture reality, and the falsifiable trigger and HTC read. All capability claims obey p0b.

### P1 — Structured-Cell Manipulation & Production · V4/H2/P4/R1/L2/D4 · Coupled · **Compression** · Conv **High**
- **Scope.** Fixed-station manipulation in engineered environments: machine tending, piece-picking/packing/palletizing, structured food & beverage lines, offsite/prefab construction, **plus net-new lab & pharma automation** (liquid-handling, sample prep — Automata/robotic-lab class) and **precision electronics/micro-assembly**.
- **Scores.** V=4 (throughput/QC measurable). H=2 (short repetitive cycles). P=4 (real manipulation, but the world is engineered to be easy). R=1 (industrial safety only). **L=2** — the "brain" is decoupled and commoditizing (p0b: cross-embodiment VLAs), so lab-capture is low; value accrues to OEMs/integrators. **D=4** — the moat is the industrial-automation incumbent + integrator stack (FANUC, ABB, KUKA, Siemens) and the fixturing/process data, not a model.
- **Coupling / net / capture.** Coupled; **Compression** — *this is the one cell where displacement is actually happening.* Capture **~1–1.5%**, the map ceiling (p3-verified: ~0.9M machine-tending robots ≈ 20% of the 4.66M industrial stock, ~$30–40B captured / ~$2.0–2.8T pool). Everywhere else in Family P, capture rounds to zero.
- **HTC / falsifier.** The OEM/integrator layer is incumbent-owned and capital-heavy — **not** the seed wedge. Investable adjacency is the *data/commissioning* layer (P8), not the arm. Falsifier for accelerating capture: machine-tending-robot installed base > ~1.3M units by 2028 with disclosed labor-avoidance.

### P2 — Bounded-Space Mobility & Frontline Service-Physical · V5/H2/P3/R1/L2/D3 · Coupled · **Mixed** · Conv **High**
- **Scope.** Autonomous mobility + light manipulation in mapped, bounded, human-shared spaces: warehouse AMR intralogistics/goods-movement, commercial floor cleaning, indoor/sidewalk delivery & reception robots, retail shelf-stocking/inventory, food-running/bussing (the embodied slice of W10).
- **Scores.** V=5 (did the tote/tray move — binary). H=2. P=3 (mobility, light manip). R=1 (minor sidewalk-robot permits). L=2 (AMR OEMs, not labs). D=3 (Amazon internalized 1M+ robots; logistics-automation incumbents).
- **Coupling / net / capture.** Coupled; **Mixed** (displacement of movement labor + throughput expansion). Capture **<1%**; structurally understated because Amazon's internalized robotics surfaces as avoided hiring, not vendor ARR.
- **HTC / falsifier.** Seed door largely closed in horizontal AMR; live wedges are vertical/edge-case mobility and the software/fleet-ops layer (→ P8). Falsifier: sidewalk/indoor delivery-robot fleets clear unit-economics at > ~10k sustained commercial units.

### P3 — Open-Road Autonomous Mobility (AV / Transport) · V5/H2/P5/R5/L2/D5 · Coupled · **Mixed** · Conv **Medium**
- **Scope.** Locomotion/transport on public road networks: robotaxi, autonomous trucking/line-haul, road last-mile.
- **Scores.** V=5 (trip completion binary). H=2. P=5 (full physical, public road). **R=5 — the binding gate** (DOT/safety-case/liability/insurance). L=2. **D=5** (Waymo's mapping/telemetry moat + capex).
- **Coupling / net / capture.** Coupled; **Mixed**. Capture **<1%**; a **decade-long tail** in trucking (only ~40% line-haul slice AV-addressable near-term) and last-mile. The gate is *regulatory/safety-case*, not dexterity — which is why P3 is split from P2 despite both being "locomotion": their binding constraints differ.
- **HTC / falsifier.** Capex/RaaS, not a labor-software seed market; value is in the AV stack (`[$]`) and the **teleop-assist** layer (→ P8, and note: AV remote-assistance is the most mature teleop-as-a-service sub-market, ~$0.55B in 2026 per Fact MR, report-mill — direction only). Falsifier: driverless trucking revenue-miles cross a disclosed commercial threshold on interstate lanes by 2028.

### P4 — Unstructured Dexterous & Field Manipulation · V4/H3/P5/R3/L1/D4 · Coupled · **Expansion/Mixed** · Conv **Low–Med**
- **Scope.** Gross-to-fine manipulation in open, novel, dynamic environments, non-human-contact: skilled trades / MEP install & repair, general unstructured construction, field service & equipment repair, unstructured janitorial.
- **Scores.** V=4. H=3. **P=5 — the hardest physical band.** R=3 (trade licensing, building codes). **L=1** (not lab-captured; better VLAs help perception but the hardware/dexterity gate dominates). D=4 (trade knowledge/relationships/incumbents).
- **Coupling / net / capture.** Coupled; **Expansion/Mixed** — mostly augmentation on durable labor plus latent demand; **too-early**, capture **~0%**. This is the **largest notional partition (~$5.3T) with ~zero realized capture** — the single clearest "huge pool, hardware-timeline-blocked" cell in the map. Do not let the $5.3T read as addressable.
- **HTC / falsifier.** Not a seed-software question — a robotics-timeline question (5–15 yr). Watch π-class dexterity milestones, not app-layer startups. Falsifier: a general-purpose site/field manipulator clears a real trade task at > ~80% autonomous success outside a demo.

### P5 — Deformable & Contact-Rich Manipulation · V4/H2/P5/R2/L2/D4 · Coupled · **Mixed** · Conv **Low**
- **Scope.** The specific capability frontier of thin/slippery/multi-layer deformable and contact-rich manipulation: specialty-crop selective harvest, commercial food prep/QSR cooking, textile/garment/laundry, hotel housekeeping (soft-goods, bed-making).
- **Scores.** V=4 (yield/output checkable). H=2. **P=5.** R=2 (food safety). L=2. D=4.
- **Coupling / net / capture.** Coupled; **Mixed**; capture **~0%**. **Explicit narrow-crossed / general-blocked flag (p0b §C.1):** π0 achieves **>80% on known-garment T-shirt folding** (the canonical bimanual-deformable milestone) — *narrow crossed* — while **general deformable manipulation** (arbitrary fabric, slippery multi-layer, novel food) remains **undemonstrated and blocked**; there is no mass-market laundry robot. This is isolated as its own cell precisely because it is the **one place physical dexterity is measurably moving** — worth a dedicated watch-line rather than being smeared across P1/P4.
- **HTC / falsifier.** The falsifiable indicator *is* the cell: does deformable generalization move from known-garment folding to **arbitrary** fabric/food at >80% by ~2028? Yes → P5 begins to convert; No → it stays a research frontier.

### P6 — Human-Contact Care & Physical Assistance · V2/H4/P5/R4/L1/D4 · Coupled · **Expansion** · Conv **Low–Med**
- **Scope.** Fine manipulation with **direct, sustained human physical contact** and the highest safety/trust/licensing gate: personal care & ADL (activities-of-daily-living) assistance, patient handling/lift/mobility, rehabilitation.
- **Scores.** **V=2** (care quality is hard to verify — the low-V gate on displacement). H=4. P=5. **R=4** (eldercare/healthcare licensing + safety). L=1. D=4.
- **Coupling / net / capture.** Coupled; **Expansion** — augmentation (lift-assist, monitoring) on durable human labor, atop the **largest latent pool in the entire map (~$11T informal/unpaid `[L]`)**. Capture **~0%**.
- **The one distinctive tailwind — inverted social license (E6).** Under demographic-shortage mandates (Japan's ~11M-worker gap, METI robotics push; Korea's chaebol-captive programs), the social license is **inverted**: near-zero displacement politics, so care is the **least-friction deployment path** for embodied AI even though its raw capability gate is among the hardest. This is the cell that **directly feeds the HTC robotics thesis** — but the investable expression is the data/teleop layer under the shortage mandate (P8), not the care-robot OEM.

### P7 — Embodied Sensing, Inspection & Security · V4/H2/P3/R3/L3/D4 · Coupled (+sovereign-additive) · **Mixed** · Conv **Medium**
- **Scope.** Perception-dominant, low-manipulation autonomy: commercial security & guarding (ground patrol robots, drone-in-a-box), autonomous facility rounds, infrastructure/energy/mining inspection, structured visual QC, and defense ISR/surveillance-physical & logistics (W12.2, sovereign-gated).
- **Scores.** V=4 (detection is measurable; but the **false-negative/missed-event** test is not cleanly machine-checkable and is catastrophic when wrong — same V-logic as W1.8 SOC). H=2. P=3 (mobility + sensing; light manip). R=3 blended (commercial low; **defense slice R=5**). L=3. **D=4** — the moat is the site/telemetry data + integration, the physical twin of the SOC data moat.
- **Coupling / net / capture.** Coupled (commercial) + additive/sovereign (defense); **Mixed** — *compression of the staffed guard/inspector rung + `[L]` expansion into never-patrolled coverage* — the exact structural shape of W1.8 SOC. Capture **<1%**. **Web-verified (2026-09-16):** Knightscope K5 deployed at campuses/dealerships/malls, **K7 outdoor limited-series H2-2026**, priced **~$7–11/hr vs $25–45/hr human guard** — and framed as *"extending what one guard can supervise,"* i.e., compression-plus-expansion, not clean replacement (RoboticsTomorrow/DSP, Tier-2 — direction only).
- **HTC / falsifier.** This is the **structural mirror of the SOC hunting ground in the physical world**, and the most-deployed-today band because actuation is light. Investable wedge is the **detection/site-telemetry data + fleet-supervision layer** (understaffed → no displacement backlash), not the patrol-robot chassis. Falsifier: a pure-play security-robot fleet discloses > ~$100M retained ARR at coverage-hours a guard force can't match.

### P8 — Robot-Economy Labor *(NET-NEW OVERLAY — physical twin of W8)* · V3/H3/P1/R2/L3/D3 · Additive (creation) · **Expansion** · Conv **Medium**
- **Scope.** The **net-new human wage bill the robot economy creates** — the physical mirror of W8's digital-agent-economy labor:
  1. **Teleoperation-as-a-Service & embodied-data collection** — humans remotely operating robots to collect frame-verified sensorimotor demonstration data (the binding input for every VLA; teleop yields only **~5–50 episodes/hr**, so it scales with *people and process*, not chips — the defining "investable-layer" profile). **CyberOrigin (HTC portfolio anchor) sits here** — *"Ground Truth for Embodied Intelligence,"* frame-verified data for the labs/world-model teams.
  2. **Robot-fleet remote supervision & intervention ("robot wrangler")** — humans staffing the exception queue for "autonomous" fleets (every shipped home/factory humanoid — 1X Neo, Figure — runs with a human fallback). Physical twin of W8.1.
  3. **Robot commissioning, integration & field-maintenance (physical FDE)** — install, calibrate, repair, retask fleets on-site; durable and heavy per deployed unit given undisclosed MTBF. Adjacent to but distinct from P4 field service (this services *robots*, not customer equipment).
  4. **Embodied-data frame-verification & annotation** — quality/ground-truth verification "to the frame" (CyberOrigin's angle), distinct from digital RLHF (W8.4).
  5. **Simulation & synthetic-environment / scenario authoring** — building and verifying the sim "scale" layer of the embodied-data pyramid (Cosmos/SimFoundry class); net-new specialized labor + `[$]` tooling.
- **Scores.** V=3. H=3. **P=1** — the labor is **hardware-decoupled** (screens, teleop rigs, verification tools); this is the whole point. R=2. **L=3** (labs run in-house data ops, but the layer is *not* lab-monopolized — the strongest argument for a defensible independent). D=3.
- **Coupling / net / capture.** **Additive / net-new creation** (no displaced pool — like W8, never subtracted from or summed into the $15T displaceable base). **Expansion.** Size today **~$5–15B `[W]`, >100% YoY** (mirrors W8's $10–20B scale; the managed-service teleop model is already forming — AV teleop ~$0.55B 2026, robot-teleop-cloud $4.2B 2025, "managed service" 44% of revenue per report-mill sources — `[$]` service proxies, **not** the labor line; the human-operator wage bill is the P8 `[W]`).
- **Intake rule (locked, mirrors W8).** Net-new *humans* in (teleoperators, wranglers, robot-FDEs, frame-verifiers, sim authors); **robot hardware/compute stays `[$]`, out.** An embodied-data infra vendor is a `[$]` entry; only the **headcount its category implies** lands in P8.
- **Why it's the thesis.** This is the **one part of the physical stack that is (a) capability-gating for everyone, (b) hardware-decoupled, (c) labor/process-scaled not capex-scaled, and (d) not yet incumbent-captured** — exactly the layer p0b §D and the HTC robotics thesis target. The map structurally missed it because the frozen taxonomy tracked physical *displacement* (W5/W6/W9/W10) but had no physical *creation* family. P8 is that family. Falsifier: does frame-verified embodied-data revenue (CyberOrigin/AGIBOT/1X-class) sustain >100% YoY into 2027, or does synthetic/sim data collapse the human-teleop wage bill before it scales?

---

## 6. Track-qualification decisions on the candidate NEW verticals (p0b §F.b)

Each candidate tested against the **Wage-Bill Denominator Test** (can you name the displaced/created human occupation?) and the framework discipline (coupled, capture <1.5%, hardware-timeline honest):

| Candidate vertical | Verdict | Where it lands |
|---|---|---|
| **Embodied security & inspection** (surveillance/drone/rounds) | **PASSES** — nameable occupation (security guards ~$120–180B global `[W]`, inspectors), real coupled pricing ($7–11/hr vs $25–45/hr), understaffed → compression+`[L]`, deployed today (Knightscope) | **New — becomes the core of P7** |
| **Energy / mining field robotics** | **PASSES (partial)** — inspection (drones/rovers) is real; autonomous haulage is deployed but private-road capital-equipment | **Inspection → P7; haulage → P3-adjacent/`[$]` note (residual §4)** |
| **Deformable / food manipulation** | **PASSES as a watch-cell** — measurably moving (π0 folding), but capture ~0 | **Isolated as P5** |
| **Lab & pharma automation** | **PASSES (small)** — structured-cell liquid-handling/sample-prep; modest lab-tech wage bill; autonomous "self-driving lab" is R&D-adjacent (E3/W15 watch) | **Folds into P1** (flagged) |
| **Surgical / precision-controlled robotics** | **FAILS the displacement bar** — da Vinci-class systems are **teleoperated master-slave tools with the surgeon in the loop**; **web-verified (2026-09-16): autonomous soft-tissue surgery is preclinical only** (porcine/phantom, autonomy-level-3, deformability unsolved), R=5 device-cleared. Does **not** displace the surgeon → **additive tool + `[$]` capital equipment**, not a coupled labor track (mirror of W4.6 blocked-by-payment/clearance) | **Excluded to `[$]`/additive watch-line** — not a P sub-family |

**Net additions to the map from the new verticals:** the security/inspection wage bill (largely net-new `[W]` + `[L]`) folded into **P7**; deformable isolated as **P5**; lab/pharma into **P1**. Surgical robotics and bulk-mining/ag capital equipment are **named and excluded** to the `[$]`/residual ledger — the map does not inflate on hype verticals that fail the wage-bill test.

---

## 7. What this architecture changes, in one paragraph

The frozen map scored physical labor correctly but **filed it by industry across five families**, which hid the gate. Family **P** re-files the same ~$15T of physical wage bill onto the axis that actually predicts robot-doability — **environment-structure × task-physics** — into seven capability bands (**P1** structured-cell / **P2** bounded mobility / **P3** open-road AV / **P4** unstructured dexterous / **P5** deformable frontier / **P6** human-contact care / **P7** sensing-inspection-security) plus one **net-new overlay (P8) robot-economy labor** that the displacement-only map structurally missed. The re-home **adds no displaceable dollars** (each frozen row homed once; straddler/defense slices overlay-stamped, not summed; P8 is additive creation). The organizing payoff is investment-legible: **capture is real only in P1 (~1–1.5%) and forming in P7; P4/P5/P6 are hardware-timeline-blocked at ~0% for 5–15 years regardless of model IQ; and the investable, hardware-decoupled, not-yet-captured layer is P8 (teleop / fleet-supervision / commissioning / frame-verification / sim) — where CyberOrigin sits — not the humanoid OEM.**

---

## Sources

**Internal:** `p0_foundation.md` (coupling rule, capture rates, pilot-to-production chasm, family priors), `p3_frozen_taxonomy.md` (frozen physical rows W5/W6/W9/W10/W12, scoring axes, wage-bill denominator test, W8 intake rule), `p0b_capability_refresh_2026-09.md` (robotics frontier §C, embodied data/teleop layer §D, missing-verticals scan §F — **governs all capability claims**), `v2_master.json` (frozen scores).

**Web-verified 2026-09-16 (net-new verticals; Tier-2 unless noted — direction only):**
- Knightscope K5/K7 deployment, pricing, GSX 2026 — [RoboticsTomorrow](https://www.roboticstomorrow.com/news/2025/11/13/knightscope-unveils-the-all-new-k7-autonomous-security-robot/25804), [Drone Strategic Partners cost comparison](https://www.dronestrategicpartners.com/post/security-guards-vs-robots-vs-drones-the-2026-cost-and-performance-comparison)
- Supervised autonomous soft-tissue surgery status (preclinical, autonomy-level-3) — [Science Translational Medicine](https://www.science.org/doi/10.1126/scitranslmed.aad9398), [arXiv 2107.01288](https://arxiv.org/pdf/2107.01288)
- Teleoperation-as-a-service / managed remote-supervision market — [Fact MR AV teleoperation](https://www.factmr.com/report/autonomous-vehicle-teleoperation-services-market), [Dataintelo robot-teleoperation-cloud](https://dataintelo.com/report/robot-teleoperation-cloud-platforms-market) *(report-mill; sizing distrusted per p0 R-rules, cited for direction only)*
- CyberOrigin frame-verified embodied data (HTC portfolio anchor) — carried from p0b §D.
