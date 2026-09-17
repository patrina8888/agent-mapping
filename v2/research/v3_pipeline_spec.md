# Phase v3 — The Living Investability-Triage Pipeline (buildable spec)

HTC internal · **2026-09-16** · Workstream 3. A concrete, buildable specification — not an essay. It turns the frozen 78-track v2 map into a **standing pipeline** wired to a recurring cloud routine, so the map keeps proving it is complete and keeps surfacing the most investable *new* domains without a human re-running the whole rebuild.

**The two questions this answers (Patrina's own framing):**
1. **"How do we make sure we cover EVERYTHING?"** → Section A (completeness / MECE proof + a repeatable white-cell finder).
2. **"How do we quickly surface the most investable NEW domains?"** → Section C (a computable triage score + a state-change trigger) and Section D (the alerting + cron wiring).

**Non-negotiable framework rules this pipeline inherits and never breaks** (from p0 / p0b / p3):
- **COUPLING.** For coupled tracks, realized value = capture-rate × displaced wage bill. **Never sum software-TAM + labor-TAM.** Overlays (Services-Arbitrage, Autonomous Business Ops, W7 relational) are non-additive re-cuts and are never added into a total.
- **Capability ≠ capture.** Deployment lags capability ~10× (MIT 95% zero-P&L; S&P 42% abandonment; <15% reach production). Physical capture is <1.5% today. A better model does **not** cross the pilot-to-production chasm.
- **Physical gaps are a hardware timeline (5–15 yr), largely independent of model IQ** (p0b §C confirmed: better VLAs did not move humanoid deployment reliability, cost, or count).
- **Sourcing discipline (R1–R9).** Tier-1/2 with dates; distrust valuation-as-ARR, bookings, deal-counts, work-units, vendor deflection %; the verified-ARR spine is ~8 names deep. Flag anything unverified.
- **Glossary discipline.** Every jargon term is glossed in plain language on first use (Patrina's explicit last-round feedback: opaque prose and missing competitive landscape were the two biggest failures).

**Where this pipeline lives (real paths):**
- Reads: `research/v2_master.json` (the 78-row dataset), `research/p0b_capability_refresh_2026-09.md` (governing capability baseline), `research/p3_frozen_taxonomy.md` (frozen taxonomy + hunting grounds), `research/p4_tierA.json` / `p4_tierB.json` (evidence packs).
- Writes: `research/pipeline/` (new sub-tree, defined in §D.4).
- Surfaces to Patrina: a Chinese-language alert digest via `PushNotification`, in the same deep, T0-company-tracking, "so what" voice as the existing daily AI brief (routine `trig_01Dg6fiFT2KddJ9f5tyd7Ru4`).

---

## A. COMPLETENESS METHODOLOGY — proving the map is exhaustive (MECE)

**Goal:** be able to say, defensibly, *"every dollar of global labor maps to exactly one cell, and here is the repeatable machine that finds any labor pool we do not yet have a home for."* MECE = **M**utually **E**xclusive (no double-count) and **C**ollectively **E**xhaustive (nothing missing).

### A.1 — Define the denominator (three independent universes that must reconcile)

Completeness is only provable against a fixed denominator. We anchor to three, cross-checked:

| Universe | What it is | Value / size | Source of truth | Role |
|---|---|---|---|---|
| **Global wage bill** | Total labor income paid worldwide per year | **~$60T** (band $58–61T; formal-wage floor ~$48T) | ILO labour-income-share 52.4% × world GDP ~$118T (p0 §2) | The **dollar denominator** — the number every cell's `[W]` must sum toward (net of overlays). |
| **Occupation universe** | Every job that exists, named | **BLS SOC** ~830 detailed occupations (US) crosswalked to **ISCO-08** (global) + **O\*NET** task detail | BLS OEWS, ISCO, O\*NET | The **occupation denominator** — every SOC/ISCO code must map to a track or an explicit carve-out. |
| **Physical-task taxonomy** | The dexterity/mobility axis the digital occupation lists under-describe | O\*NET work-activities + a manipulation taxonomy (grasp / deformable / locomotion / unstructured-environment) | O\*NET "Work Activities" + robotics literature (p0b §C, §F) | Catches physical labor that SOC codes bucket coarsely (e.g. "laborers" hides deformable-object work). |

**Why three, not one.** The dollar universe alone hides headcount-heavy / low-wage pools (a known dollar-weighting bias — that is why p6 built a headcount companion view). The occupation universe alone hides *net-new* agent-economy roles that have no SOC code yet (W8 family). The physical taxonomy alone catches dexterity work the digital SOC lists smear together. A cell is only "covered" when it is placed against all three.

### A.2 — The partition test (mutual exclusivity + collective exhaustion)

**Build one artifact: `coverage_ledger.json`.** It is the crosswalk that makes MECE auditable. One row per BLS SOC / ISCO occupation code, each carrying:

```
{ "soc":"15-1252", "title":"Software Developers", "isco":"2512",
  "us_headcount": ..., "us_wage_bill_$b": ..., "global_wage_bill_$b": ...,
  "home_track":"W1.1a", "straddle":["W1.1b","SA.4"], "carveout": null,
  "coupled": true, "last_reviewed":"2026-09-16" }
```

**Two mechanical tests run monthly against the ledger:**

1. **Exhaustion test (nothing missing).** `Σ(global_wage_bill over all SOC rows)` must reconcile to **$60T ± 5%** once you add the explicit residual carve-outs. The residual (~$12–18T) is *deliberately* not force-fit into W1–W14: agriculture (~$2–4T), informal/subsistence, domestic/personal service, low-skill misc. **A residual that drifts above ~$18T is the alarm that a real labor pool has no home** — it means occupations are silently falling into "misc" instead of a track. Carve-outs are named line-items, never a junk drawer.

2. **Exclusivity test (no double-count).** Every SOC row has exactly **one** `home_track`. Where an occupation genuinely spans two cells (nurse = W4 licensed + W6 dexterous; junior coder = W1.1b + SA.4), the split is recorded once in `straddle[]` **with a fixed percentage split**, and the reconciliation notes enforce "count the dollars once" (the same discipline that reconciled W1.1↔SA.4 coding and W4.10↔SA.3 claims in p3). Overlays (SA.\*, AO.1, W7) are tagged `non_additive:true` and are **excluded from the exhaustion sum by construction** — they are re-cuts of parent `[W]` dollars, not new dollars.

**Output of the partition test:** a one-page **Coverage Report** each month: `covered $X.XT of $60T (YY%)`, residual carve-out $Z.ZT, list of any SOC codes whose `home_track` is null, list of any straddles whose split percentages don't sum to 100%. This is the artifact that literally answers "did we miss anything."

### A.3 — The residual white-cell finder (the repeatable "did a new labor pool appear" machine)

Coverage against *today's* occupations is not enough — the agent economy **creates** occupations (W8: teleoperator, agent-ops, AI-evals engineer) and **re-cuts** others faster than BLS updates SOC codes. The white-cell finder is the standing query set that reveals a labor pool with **no home**. It runs on the ingestion feeds (§B) and fires a candidate when a signal has no `home_track`.

**Four detectors, each a concrete query/feed pattern:**

1. **Orphan-occupation detector.** Cross the ingestion stream (YC batches, funding rounds, job-title data) against `coverage_ledger.json`. Any **company or job title whose one-line description names a human task that no existing track's denominator covers** is an orphan → candidate white cell. Concrete trigger: a funded company where the buyer replaces a role you cannot point to a SOC code + home_track for. (This is exactly how W1.8 SOC, W4.10 insurance, W8.6 context-engineering entered the map.)
2. **Net-new-role detector (the W8 / robot-economy edge).** Standing queries against labor-market feeds for **fastest-growing job titles that did not exist 24 months ago** — LinkedIn "fastest-growing roles," O\*NET "new & emerging," Gartner-named roles. p0b §F flagged the sharpest current gap: the map has W8 for the *digital* agent economy's net-new labor but **no family for the *robot* economy's net-new physical labor** (teleoperation-as-a-service, robot fleet remote-supervision, physical FDE, embodied-data verification). This detector is what would have caught it; it is the highest-priority open white cell today (see §C.5 worked trigger).
3. **Residual-drift detector.** If the monthly exhaustion residual moves >±$2T between runs, decompose *which* SOC codes shifted. A rising residual = occupations leaking out of tracks (a track's definition is too narrow); a falling residual = a carve-out is being absorbed into a real market (e.g. domestic personal-assistance `[L]` starting to be paid → W14.1 / a new cell).
4. **Physical-task-gap detector.** Run O\*NET manipulation categories against the physical families W5/W6/W9/W10. A manipulation class with real labor volume but **smeared across ≥3 tracks** (p0b flagged deformable/textile handling, currently split over W5.7/W6.5/W6.7) is a candidate to *isolate* as its own watch-cell — not because it is investable now, but because it is the one place physical dexterity is measurably moving (π0 >80% known-garment folding) and needs a clean home to track the general-vs-narrow gap.

**Every white-cell candidate the finder emits carries, at birth:** a proposed denominator (which SOC/ISCO codes, est. wage bill band), a proposed family, a coupled/additive call, and a **falsifiable dated indicator** (what would confirm or kill it by when). It enters the pipeline as a **provisional row** (tier "P") in a staging file, never straight into `v2_master.json` — promotion requires the monthly re-score + a human gate (§D).

**A.4 — What "proven complete" means, stated plainly.** The map is *never* provably complete in the absolute — new occupations appear. What *is* provable, and what this section delivers, is: **(i)** every dollar of the $60T is either in exactly one cell or a named carve-out (the partition test), and **(ii)** there is a standing, repeatable machine that will surface any new labor pool within one ingestion cycle (the white-cell finder). Completeness becomes a **maintained property with an audit trail**, not a one-time claim.

---

## B. INGESTION SOURCES + CADENCE — the standing feeds

Three cadences, chosen so cost scales with signal: a cheap **weekly** scan that only looks for state-changes, a **monthly** re-score that recomputes the triage function, and a **bi-monthly deep** pass that re-verifies evidence and re-runs the white-cell finder end-to-end. Every pulled figure inherits the R1–R9 sourcing gates and the ARR Reality Ladder (p3 Part B): metric-type label → definition-lock → churn/break-clause → corroboration → production gate, before it can move a score.

| Feed | What to pull | Cadence | Pipeline stage it feeds | Tier / caveat |
|---|---|---|---|---|
| **YC batch** (each new batch, incl. S26 backfill) | New cos + one-line "who they replace"; flag any orphan occupation | Per batch (~2×/yr) + weekly scan of interim launches | White-cell finder (A.3 #1); door-open (competitive density) | Tier-2; a launch ≠ revenue |
| **Funding rounds** — Crunchbase, PitchBook, **tradedvc ("TRADEVC")** | New rounds in agent-labor categories; who; size; stage; whether a *first credible vendor* appears in a white cell | Weekly light; reconciled monthly | Trigger rule (first-vendor); door-open (D/L); ITS re-score | Tier-2; **funding-raised is NOT revenue or TAM** (never size a track off it) |
| **Frontier model + robotics releases** — Artificial Analysis, METR, OSWorld 2.0 leaderboard, arXiv (VLA), OEM press | Capability deltas on the axes we score: OSWorld 2.0 binary (the 80% gate), METR horizon, coding parity, VLA cross-embodiment, humanoid deployment counts (fleet vs demo) | Weekly headline scan; monthly re-read; **bi-monthly deep = a p0b-style refresh** | Capability-readiness `K`; trigger rule (capability-crosses-threshold) | Governing doc is **p0b**; distrust partial-credit / "beats-human" framings and shipped-units-as-labor |
| **BLS OEWS / WEF / ILO / O\*NET** labor data | Occupation headcount + wage updates; new & emerging roles; entry-vs-senior composition | Bi-monthly (data is slow) | Coverage ledger; exhaustion/residual test; net-new-role detector | Tier-1; the anchor that outranks VC narrative (R2) |
| **Key incumbents** — Microsoft (Agent 365/Copilot), Salesforce (Agentforce), ServiceNow, CrowdStrike/Palo Alto, Duck Creek/Guidewire, Workiva/DFIN, the frontier labs' native verticals | Native-feature ship events that **feature-ize** a startup wedge (the recurring falsifier across the map) | Weekly headline; monthly | Trigger rule (feature-ization → door closes, L→5); ITS `W` term | Tier-1/2; incumbent land-grab is the dominant seed-door risk (p3 Finding 3) |
| **T0-company / people signals** (matches the daily-brief mandate) | Named T0 companies + key people: senior-employee posts, stealth emergences, new narratives ("新说法"), technical breakthroughs; frontier neo-labs (SSI, Thinking Machines, World Labs), top researchers, big VCs/YC | Weekly (this is the daily-brief's own stream, re-used) | White-cell finder; trigger rule; the "so what" in the digest | Depth over breadth — 宁深毋滥 (per `feedback_daily_brief_depth`) |

**Cadence summary:** **Weekly light scan** = only detect state-changes on the trigger rule (§C.5), no full re-score; cheap. **Monthly re-score** = recompute ITS for all 78 rows + provisional rows, run the partition/coverage test, run the white-cell finder. **Bi-monthly deep** = re-verify Tier-A evidence packs, run a p0b-style capability refresh, promote/retire provisional rows through the human gate. This mirrors the existing `ai-agent-tam-update` bimonthly skill so the deep pass *is* the bimonthly framework update, not a parallel process.

---

## C. THE INVESTABILITY-TRIAGE SCORING FUNCTION (ITS)

An explicit, computable score that ranks every track (and every white-cell candidate) for **HTC seed/Series-A investability** — deliberately different from "how big is displacement." It is built from the six frozen axes **V/H/P/R/L/D** (verifiability / autonomy-horizon / physicality / regulatory-gate / lab-capture / data-moat, each 0–5) plus the additions Patrina specified: labor-TAM size, capture-**expansion** headroom (not current capture), seed/A white-space, near-term reg-gate penalty, capability-readiness, and coupling type.

### C.1 — The five components (each normalized 0–5)

1. **E — Reachable capture-expansion headroom.** The return engine. `raw_headroom = ceiling(V) − current_capture`, then **gated by readiness** so unreachable headroom does not count: `reachable = raw_headroom × readiness`; `E = 5 × reachable / 32`. The ceiling is set by verifiability (the strongest displacement predictor): `{V0:3%, V1:5%, V2:8%, V3:12%, V4:20%, V5:32%}` — calibrated to observed capture (CX ~V3 tops out ~11%; security-testing/XBOW ~V5 reaches ~30%). **Current capture is read, then subtracted** — so a track that is already ~10% captured (CX) has *less* headroom than one at <1% with the same ceiling. **This is the "capture-expansion, not current-capture" instruction made computable.** Additive/augment tracks are ×0.5 (their value is software-seat expansion, not labor capture — reading seat-ARR as capture is the recurring ~10× error).
2. **S — Labor-TAM size.** `log10` of the displaceable wage bill ($2B–$2000B) scaled to 0–5. Deliberately the **lowest-weighted** term: raw dollar-size is a known value trap (a $2T physical pool at <1.5% capture is worth less than a $50B digital pool at reachable 20%). Size only matters *through* reachable capture, which E already carries.
3. **K — Capability-readiness.** `readiness × 5`, where `readiness = (V/5) × (1 − 0.18·P) × (0.6 + 0.10·H)`, clamped. Verifiability-gated, **hardware-timeline-discounted** (P=5 collapses readiness to ~0.10 — the non-negotiable "physical is a hardware clock, not a model-IQ question"), horizon-modulated. `readiness` also gates E, so a hardware-blocked cell cannot score high on the return engine no matter how large its nominal headroom.
4. **W — Seed/A white-space (door-open).** `5 − L`, i.e. the inverse of lab/incumbent-capture. L is the operative "is the seed door open" axis: coding (L=5) and CX/translation (L=5) score **W=0** — capability-ready but the door is closed, so *not* a seed hunting ground, exactly as the frozen board concluded.
   > **Deliberate, stated deviation from the brief.** Patrina's spec said "inverse incumbent-moat **D**." I use **L (lab-capture)** as the primary door-open axis and treat **D as a moat-ownership *modifier*, not a penalty** — because the framework's own #2 hunting ground, Autonomous SOC (W1.8, **D=4**), proves an *ownable* data moat (SIEM/EDR telemetry) is an **asset**, not a barrier. Penalizing high D would have ranked SOC as un-investable, contradicting the frozen hunting list. So: `W = 5 − L`, then a **moat-ownership multiplier** applies — ×0.6 when a live feature-ization flag says an incumbent already holds the moat (e.g. Duck Creek shipped the UW+FNOL wedge; DFIN shipped AI-iXBRL), ×1.15 when D≥3 *and* the moat is startup-buildable. In the batch run the multiplier is neutral (1.0) so the score is fully reproducible from `v2_master.json`; the flag is set from the live feeds (§B) and the track's `falsi`/`anti` fields.
5. **Rc — Near-term reg-gate clearance.** `5 − R`. A high regulatory gate (R=5: FDA/reimbursement, defense, public procurement) throttles realized dollars for years regardless of capability — so it is a direct penalty, framed here as clearance so all weights are positive.

### C.2 — The formula (weights + gates)

```
ITS_base = 20 × ( 0.34·E  +  0.12·S  +  0.16·K  +  0.24·W  +  0.14·Rc )      # → 0–100
ITS      = ITS_base × chasm(conv)      chasm = { High:1.00, Medium:0.85, Low:0.65 }
```

**Weights, and why.** For a *seed/A* investor the return dies if the door is closed or the capability isn't reachable, and dollar-size is a trap — so weight flows to **E (0.34, the reachable return)** and **W (0.24, door-open)**, with **K (0.16)** and **Rc (0.14)** as timing terms and **S (0.12)** deliberately smallest. The **chasm multiplier** is the pilot-to-production discipline made mechanical: a Medium-conviction (pre-production) track is docked 15%, a Low-conviction one 35% — encoding "deployment lags capability ~10×; a POC is not a deployment." A track only earns the full score with production-grade (not bookings/POC) evidence.

**Reference implementation** (runs against `v2_master.json`; ~40 lines) is committed at `research/pipeline/triage.py`. It is fully reproducible: every input is a field already in the dataset (V/H/P/R/L/D, `labor_b`, `coupled`, `conv`, `capture`).

### C.3 — Worked examples (three real tracks, actual outputs)

| Track | V H P R L D | coupled / conv / net | ceiling → current = raw → **reachable** headroom | E · S · K · W · Rc | **ITS** | Read |
|---|---|---|---|---|---|---|
| **W2.7 Translation/Localization** | 5 1 0 1 5 1 | C / High / Compression | 32% → 3% = 29 → **20.3 pt** | 3.17 · 2.33 · 3.50 · **0.00** · 4 | **49.6** | Cleanest displacement in the whole map (V=5), *huge* reachable capture — **but door-open W=0 (L=5, already commoditized/lab-captured).** High absolute score, **not a seed bet.** The score correctly separates "real displacement" from "investable." |
| **W4.10 Insurance UW & Claims** | 4 2 0 4 3 4 | C / Medium / Compression | 20% → 2% = 18 → **11.5 pt** | 1.80 · 3.13 · 3.20 · **2.00** · 1 | **36.0** | The frozen #1 hunting ground. Real reachable headroom, door still ajar (L=3) — but **docked by the reg gate (R=4 → Rc=1)** and the Medium-conviction chasm (×0.85). Honest: capability-ready, pre-production, feature-ization-threatened (Duck Creek). |
| **W5.3 Discrete-mfg machine tending** | 4 2 3 1 2 3 | C / High / Compression | 20% → 1% = 19 → **5.5 pt** | 0.86 · **5.00** · 1.47 · 3.00 · 4 | **48.2** | The **$2T dollar trap, defused.** Max size (S=5.00) and open door, but the **readiness gate (0.29, physicality P=3) crushes reachable headroom to 5.5 pt**, so E=0.86. The score refuses to let a giant hardware-gated pool look investable — the non-negotiable physical rule, enforced numerically. |

### C.4 — The ranking (top slice of the 78-row batch, neutral modifiers)

Full table is regenerated each monthly run into `research/pipeline/its_ranked.csv`. Top ~18 as of 2026-09-16:

| # | Track | ITS | conv | net | why it ranks here |
|---:|---|---:|---|---|---|
| 1 | **W3.7** Collections & AR outreach | 69.5 | High | Mixed | V=5 verifiable, P=0, **door wide open (L=1)** — an under-consensus clean digital coupled cell |
| 2 | W5.1 Warehouse goods-movement | 58.8 | High | Mixed | high V + open door; readiness caps it (P=3) — the ceiling of "structured physical" |
| 3 | W5.5 Commercial floor cleaning (structured) | 54.6 | High | Mixed | structured-physical, door open |
| 4 | **W1.2** Software QA & test | 53.5 | Med | Compression | V=5, high readiness; door tighter (L=4) — Ford-rehire chasm keeps conv=Med |
| 5 | **W2.7** Translation | 49.6 | High | Compression | huge reachable capture, **door closed (W=0)** — displacement ≠ investable |
| 6 | **W3.6** Voice — physical-industry ops | 49.0 | High | Mixed | hunting-ground #7; verifiable voice, open-ish door |
| 7 | W1.4 SMB bookkeeping | 48.3 | High | Compression | finance back-office, Basis/Ramp/Digits adjacency |
| 8 | W5.3 Machine tending | 48.2 | High | Compression | **$2T trap defused by readiness gate** |
| 9 | W5.4 Structured visual QC | 47.9 | Med | Mixed | V=5 inspection |
| 10 | W6.5 Cleaning — unstructured | 47.3 | High | Mixed | door open but readiness low (physical) |
| 11 | SA.4 Managed-delivery code (arbitrage) | 47.1 | High | Mixed | high readiness, **door closed (L=5)** |
| 12 | W1.3 Fin reconciliation & close | 46.8 | High | Compression | verifiable finance back-office |
| … | … | | | | |
| — | **W4.10** Insurance (hunt #1) | 36.0 | Med | Compression | reg-gate + chasm discount |
| — | **W1.5** XBRL filing (hunt #3) | 38.5 | Med | Compression | door closing (DFIN/Workiva feature-izing) |
| — | **W1.8** Autonomous SOC (hunt #2) | 30.5 | Med | Mixed | thin size + Medium conv; incumbent land-grab |
| — | **AO.1** Company-in-a-box (hunt #4) | 26.9 | Med | Mixed | near-zero current capture, lab-exposure |

**Reconciling the ranking with the frozen hunting grounds (important, and honest).** The raw ITS ranks high-verifiability digital cells (collections, QA, voice, finance back-office) at the top, while several *named* hunting grounds (W4.10, W1.8, AO.1) sit mid-pack. This is **not** a contradiction — it is two extra filters the raw score deliberately does **not** bake in, plus one honest correction:
- **The proven-anchor exclusion.** The hunting list excludes coding/CX because their seed door is *closed*; ITS encodes this via **W=0** (they still show a high absolute score because they *are* attractive markets — they're just not seed-investable). **Investable frontier = high ITS *and* W≥2 *and* a live trigger**, not ITS alone.
- **The production-chasm correction.** W4.10 and W1.8 are docked to Medium conviction (×0.85) precisely because they are capability-ready but **pre-production and feature-ization-threatened** — which is the truth, and the score should say so rather than flatter the hunting list.
So ITS is used as a **screen and a monitor**, not an oracle: it ranks the standing map, and its *movement over time* (below) is what surfaces new domains.

### C.5 — The NEWLY-INVESTABLE trigger rule (the state-change detector — this is the "surface NEW domains" engine)

A high static score is not a buy signal; a **state-change** is. Each run, for every track and provisional cell, the pipeline stores the prior component vector and fires a **NEWLY-INVESTABLE** alert when any of these transitions occurs — each carries a required **falsifiable, dated indicator** so it can be killed:

| Trigger | Fires when | Falsifiable dated indicator attached |
|---|---|---|
| **T1 — Reg gate moves** | `R` drops ≥2 (a reimbursement code opens, a licensing/UPL barrier loosens, a procurement path clears) → Rc jumps, ITS re-ranks up | Name the specific gate + a date it must clear by, else revert (e.g. W4.6: "≥3 new CPT reimbursement codes for autonomous diagnosis by Q4-2027, else stays blocked") |
| **T2 — First credible vendor appears in a white cell** | The white-cell finder's orphan detector pins a *funded, production-metric* vendor in a cell that had none (the S1+S3 "insurance had zero vendors" pattern, now filled) | "≥1 vendor at verified (not bookings) ARR + a production logo by [date], else the cell reverts to white space" |
| **T3 — Capability crosses a reliability threshold** | A tracked benchmark crosses the deployment-relevant bar: **OSWorld 2.0 binary ≥50%** (back-office autonomy), METR 80%-horizon past a task length, a VLA hitting general (not narrow) deformable manipulation | The exact benchmark + threshold + the tracks it unlocks (e.g. "OSWorld 2.0 binary ≥50% → re-score W1.7/SA.3/SA.5 back-office"); today binary is ~31% (p0b), so this is **not** tripped |
| **T4 — Door opens (de-feature-ization) or closes** | `L` or the feature-ization flag flips: an incumbent *retreats* (door opens), or ships native (door closes, L→5) — the CrowdStrike/Palo-Alto/Agent-365 land-grab pattern | "If [incumbent] ships [native feature] at production scale by [date], W→×0.6 and the cell exits the hunt list" |
| **T5 — New white cell promoted** | The finder emits a provisional cell that clears the monthly human gate (denominator + coupled call + falsifier defined) | The birth falsifier (§A.3); e.g. the **robot-economy net-new labor family** (teleop-as-a-service, robot-wrangler, physical FDE) — the top open white cell today |

**Trigger arithmetic is real, not rhetorical** (computed from the reference implementation):
- **T1 worked example — W4.6 Autonomous/Device-Cleared Diagnosis:** baseline ITS **41.1** (R=5). If reimbursement opens and R drops 5→3: ITS **45.9 (+4.8)** and it jumps the ranking — the alert says *"a reg gate the map flagged as the binding constraint just moved; re-underwrite."*
- **T2/chasm worked example — W1.8 Autonomous SOC:** baseline ITS **30.5** (conv=Medium). If a pure-play crosses **≥$100M verified ARR at >120% net revenue retention and stays independent** (its own falsifier), conviction → High: ITS **35.8 (+5.3)** — but note the *base-case* falsifier is the opposite (feature-ization by CrowdStrike/Palo Alto/Microsoft, already shipping at RSAC-2026), which would fire **T4-close** and drop W instead. The pipeline tracks both legs.

**Every surfaced candidate must carry a falsifiable indicator with a date** — this is enforced at emit time: an alert with no dated falsifier is a bug, not a signal (mirrors the per-track `falsi` field already in `v2_master.json` and Patrina's "conviction + falsifiable leading indicator" house style).

---

## D. ALERT RULES + OUTPUT + THE CRON WIRING SPEC

### D.1 — What each run emits (the alert taxonomy)

The recurring agent emits **only state-changes and their "so what,"** never a re-listing of the map (宁缺毋滥 — better to omit than pad). Four alert classes:

1. **NEW WHITE CELL** — the finder found a labor pool with no home. Emits: proposed denominator + family + coupled call + birth falsifier. *So what:* is this a cell HTC should open a provisional thesis on?
2. **CELL CROSSED A THRESHOLD** — a track crossed a capture ratio or a capability/reg threshold (T1/T3/T4). Emits: which axis moved, old→new, the ITS delta, the tracks re-ranked. *So what:* re-underwrite / the binding constraint moved.
3. **NEWLY-INVESTABLE CANDIDATE** — a track/cell entered the investable frontier (high ITS **and** door-open **and** a live trigger). Emits: the specific wedge, the named T0 companies in it, the HTC entry note, the dated falsifier. *So what:* a concrete seed/A action.
4. **HUNTING-GROUND FALSIFIER TRIPPED** — a falsifier on one of the 8 frozen hunting grounds fired (e.g. an incumbent internalized a wedge → door closed). Emits: which thesis just weakened or died. *So what:* stop hunting here / the door closed.

Each alert is **named-entity, T0-company-and-people specific** with an explicit "so what" thesis implication — never a sector-level roundup (per `feedback_daily_brief_depth`: 宁深毋滥). Sources are Tier-tagged and dated inline (R4 provenance).

### D.2 — The Patrina-facing digest (matches the daily-brief voice)

Chinese-language, delivered by `PushNotification` from the cloud run, in the deep T0-tracking style of the existing daily brief. Structure:

```
【TAM 管线周报 / 月度重评】 YYYY-MM-DD
TL;DR：本轮 N 个状态变化 / M 个新可投候选 / K 个假设被证伪
1. 新可投候选（NEWLY-INVESTABLE）— 具体 wedge + T0 公司/人 + HTC 切入 + 可证伪指标(带日期)
2. 阈值穿越 / 门移动（capability 或监管）— 哪条约束动了，old→new，牵动哪些 track，so what
3. 新白格（white cell）— 无归属的劳动力池，拟定分母 + family + 出生假设
4. 假设被证伪 / 门关闭 — 哪个 hunting ground 走弱（incumbent internalize 等），thesis 影响
（每条：来源分级+日期；coupling 纪律；宁深毋滥）
```

Weekly runs emit only sections that changed (often just a one-line "无重大状态变化，residual $Xt 稳定"). Monthly runs include the re-score delta and the coverage report. Bi-monthly deep runs additionally attach the refreshed capability read and the promote/retire proposals for the human gate.

### D.3 — The human gate (what is *never* automated)

The routine **surfaces and stages; it does not mutate the frozen map.** No cron run edits `v2_master.json` or promotes a provisional cell on its own. Promotion (provisional → tracked row), any score-weight change, and any capability-baseline change require Patrina/analyst sign-off at the bi-monthly deep pass — the same discipline as the existing manual Vercel deploy (`vercel --prod` is manual; git push does not auto-deploy). This keeps the frozen taxonomy auditable and prevents an agent-washed funding headline from silently re-ranking the map.

### D.4 — The exact cron wiring spec

**Reads (inputs, read-only):**
- `research/v2_master.json` — the 78-row dataset (scored).
- `research/p0b_capability_refresh_2026-09.md` — governing capability baseline (for the K/threshold logic).
- `research/p3_frozen_taxonomy.md` — hunting grounds + falsifiers.
- `research/pipeline/coverage_ledger.json` — the MECE crosswalk (§A).
- `research/pipeline/state_prev.json` — last run's component vectors + residual, for delta detection.
- Live feeds per §B (search / official sites / LinkedIn reposts — the cloud sandbox egress-blocks instagram.com, so TRADEVC is reached via search/reposts, same workaround as the daily brief).

**Runs (compute):**
1. Ingest feeds → normalize to candidate signals (apply ARR Reality Ladder gates).
2. `triage.py` → recompute ITS for all rows + provisional cells → `its_ranked.csv`.
3. White-cell finder (A.3) → new provisional cells → `provisional_cells.json`.
4. Partition/coverage test (A.2) → `coverage_report_YYYY-MM.md`.
5. Diff against `state_prev.json` → fire alerts (T1–T5) → `alerts_YYYY-MM-DD.json`.

**Writes (outputs, under `research/pipeline/`):**
- `its_ranked.csv` — full re-ranked 78+ rows with component breakdown.
- `provisional_cells.json` — staged white cells awaiting the human gate.
- `coverage_report_YYYY-MM.md` — the "did we miss anything" one-pager.
- `alerts_YYYY-MM-DD.json` — the run's state-changes + dated falsifiers.
- `state_prev.json` — overwritten with this run's vectors (for next diff).
- `digest_YYYY-MM-DD.md` — the Chinese Patrina-facing digest (also pushed).

**Surfaces to Patrina:** `PushNotification` with the digest; the digest links the written artifacts.

**Cadence (cron):**
- **Weekly light scan** — `0 17 * * 1` UTC (Mon 10am PT, aligned to the daily-brief slot; drifts to 9am when PST starts, same note as `trig_01Dg6fiFT2KddJ9f5tyd7Ru4`). State-change detection only; usually a short digest.
- **Monthly re-score** — `0 17 1 * *` UTC (1st of month). Full ITS re-score + coverage test + white-cell finder.
- **Bi-monthly deep** — every 2nd month with the monthly run: re-verify Tier-A packs, run a p0b-style capability refresh, emit promote/retire proposals for the human gate. This **is** the existing `ai-agent-tam-update` bimonthly cycle — one process, not two.

**Runtime:** cloud routine on `claude-sonnet-5` in the existing default cloud env (as with the daily brief); create as a sibling routine to `trig_01Dg6fiFT2KddJ9f5tyd7Ru4`. Deletion/edit via the web UI. **Set-up is a separate action** (create the routine + seed `coverage_ledger.json` + commit `triage.py`) — this document is the spec; it does not itself create the cron.

---

## Build checklist (to stand this up)

1. `mkdir research/pipeline/`; commit `triage.py` (reference implementation, §C.2).
2. Seed `coverage_ledger.json` — crosswalk BLS SOC/ISCO → the 78 tracks; run the exhaustion test; confirm reconciliation to $60T ±5% and residual ≤$18T.
3. Seed `state_prev.json` from a first full `triage.py` run (baseline vectors).
4. Author the routine prompt (feeds §B, alert taxonomy §D.1, digest template §D.2, human-gate rule §D.3) and register the three crons (§D.4).
5. First deep run: verify the white-cell finder emits the **robot-economy net-new labor family** (teleop-as-a-service / robot-wrangler / physical FDE / embodied-data verification — p0b §F), the highest-priority open white cell and the one most aligned with the CyberOrigin robotics thesis.

**One-line statement of what this delivers:** a standing machine that (A) keeps every labor dollar in exactly one cell and flags any pool with no home, (B) ingests the right feeds at three sensible cadences, (C) scores every cell for *seed/A investability* with a reproducible formula that refuses the physical-size and displacement-≠-investable traps, and (D) emits only dated, falsifiable, T0-specific state-changes to Patrina in the daily-brief voice — with the frozen map never mutated without a human gate.
