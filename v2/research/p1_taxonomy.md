# Agent Mapping v2 — Phase 1 Frozen Candidate Taxonomy (G1 Freeze)

**Status:** CANDIDATE, frozen for G1 gate · **Date:** 2026-09-01 · **Track count:** 76 across 14 task families + 1 delivery-model overlay
**Scores:** V=verifiability · H=autonomy-horizon · P=physicality · R=regulatory gate · L=lab-capture risk · D=data/incumbent moat (0–5)
**labor_tam denominator tags:** `[W]` displaceable wage bill · `[L]` latent/unmet demand (not currently paid) · `[$]` market-revenue proxy (not a wage bill — never sum with `[W]`)
**Family type:** PARTITION families (W1–W6, W9–W13) partition the labor universe by task nature and their track TAMs approximately sum net of overlap; OVERLAY families (W7, W8-adjacent consumer, Services-Arbitrage) re-cut the partition by seniority or delivery model and are **NEVER summed** with their parents.

> **Honesty header.** This is now a *dollar-weighted, advanced-economy* map spanning white-collar, licensed, physical, mobility, public-sector, and consumer labor — no longer only the professional/physical core. The three P1 bookkeeping defects the reviews found (inconsistent `coupled`, Legal double-count, W5↔W6 double-listing) are fixed below. Six new families were forced in by the gaps review, pushing the count to 76 (above the 55–75 target); G1 must decide whether to defer the thinnest new families (W12/W13/W14) to keep Phase 2 tractable — see Open Questions.

---

## 1. Consolidated Candidate Taxonomy

### W1 — Digital, outcome-verifiable *(PARTITION; family prior $2.5–3.5T; now populated)*

| Track | Fam | labor TAM | V/H/P/R/L/D | Coupled? | Net | Conv |
|---|---|---|---|---|---|---|
| W1.1 Software Engineering & Code Generation | W1 | $0.9–1.3T `[W]` | 4/3/0/1/4/3 | Additive seats **+ coupled fixed-price fringe (→SA.4)** | Mixed | High |
| W1.2 Software QA & Test Automation | W1 | $150–250B `[W]` | 5/2/0/1/4/2 | Coupled | Compression | High |
| W1.3 Financial Reconciliation & Month-End Close | W1 | $200–350B `[W]` | 4/2/0/3/3/3 | Coupled | Compression | High |
| W1.4 Bookkeeping & SMB Accounting *(added)* | W1 | $100–200B `[W]` | 4/2/0/2/3/2 | Coupled | Compression | High |
| W1.5 Financial Reporting & Regulatory Filing (XBRL, trace-to-source) | W1 | $100–200B `[W]` | 4/3/0/4/3/4 | Coupled | Compression | Medium |
| W1.6 Medical Coding & Revenue-Cycle Management *(added)* | W1 | $100–150B `[W]` | 4/2/0/3/3/4 | Coupled | Compression | Medium |
| W1.7 Structured Data Entry & Digital Back-Office Ops | W1 | $300–500B `[W]` | 4/1/0/1/4/2 | Coupled | Compression | Medium |

*W1 tracks approx-partition to ~$1.85–2.95T ≈ the family prior. Gate on capture is not capability but SOX/audit/officer-certification liability (finance) and messy computer-use reliability (~20% OSWorld) for W1.7. **W1.1 & W1.7 deliberately overlap Services SA.4/SA.3 — reconcile the coding/back-office dollars once, do not double-book.***

### W2 — Judgment-graded knowledge work *(PARTITION but heavily overlapping — do NOT sum; prior $4.5–5.5T)*

| Track | Fam | labor TAM | V/H/P/R/L/D | Coupled? | Net | Conv |
|---|---|---|---|---|---|---|
| W2.1 Management & Strategy Consulting | W2 | $500–800B `[$/W]` | 1/4/0/1/4/2 | Coupled (fees=analyst hrs; external-vendor capture ≈0, incumbents internalize) | Mixed | Medium |
| W2.2 Financial & Investment Analysis | W2 | $400–600B `[W]` | 3/3/0/3/3/4 | Additive (seat copilots) | Expansion | High |
| W2.3 Marketing & Content Creation (copy/editorial) | W2 | $400–700B `[W]` | 2/2/0/0/5/1 | Additive | Mixed | Medium |
| W2.4 Enterprise Knowledge Research & Synthesis **(shrunk)** | W2 | $100–200B `[W]` *(was $800B–1.2T)* | 2/3/0/1/4/3 | Additive | Expansion | **Medium↓** |
| W2.5 Design & Creative Production (visual/UX/motion) | W2 | $400–700B `[W]` | 1/1/0/0/5/1 | Additive | Mixed | Medium |
| W2.6 Program & Project Management / Ops Coordination | W2 | $500–900B `[W]` | 2/4/0/0/4/4 | Additive (watch labor-denom shift) | Mixed | Medium |
| W2.7 Translation, Localization & Interpretation **(added)** | W2 | $60–80B `[$]` | 5/1/0/1/5/1 | Coupled | Compression | High |

*W2.4 rebuilt bottom-up to dedicated market-intel/research-associate/librarian headcount only; legal-research pushed to W4.3, market-intel to W2.2 — conviction downgraded, weakest basis in the map flagged. **Primary homes assigned:** AlphaSense/Hebbia/Rogo → W2.2. W2.6 now reciprocally excludes live scheduling (→W3.6).*

### W3 — Real-time interpersonal *(PARTITION; overlapping, comp-weighted; prior $8–12T, bottom-up ~$2.5–3.5T)*

| Track | Fam | labor TAM | V/H/P/R/L/D | Coupled? | Net | Conv |
|---|---|---|---|---|---|---|
| W3.1 Customer Support & Service Resolution | W3 | $0.45–0.6T `[W]` | **3↓**/1(val-wtd 3)/0/1/3/3 | Coupled | Mixed | High |
| W3.2 Outbound Sales Development (SDR/BDR) | W3 | $100–150B `[W]` | 3/2/0/2/2/3 | Coupled | Compression | Medium |
| W3.3 Sales Closing & Account Management (B2B AE) | W3 | $0.8–1.2T `[W]` | 2/4/1/1/2/3 | Additive (seat copilots) | Expansion | Medium |
| W3.4 Recruiting & Talent Sourcing | W3 | $0.15–0.25T `[W]` | 3/3/0/3/2/3 | Coupled (placement contingency) | Mixed | Medium |
| W3.5 Tutoring & Instructional Delivery | W3 | $0.15–0.25T `[W]` | 2/3/0/2/4/2 | Additive | Expansion | High |
| W3.6 Front-Office Coordination, Scheduling & Reception | W3 | $0.15–0.25T `[W]` | 4/1/0/1/3/3 | Coupled | Mixed | High |
| W3.7 Collections & AR Outreach | W3 | $50–90B `[W]` | 5/2/0/3/1/3 | Coupled | Mixed | High |

*CX V rescored 3 (family gate is genuine-resolution verification; audited resolution 35–45% vs 80% deflection claims). H shown at volume-median with value-weighted horizon in parens — the dollar-valuable residual is long-horizon. **Mercor removed from W3.4 (→W8.4); sw_tam de-inflated ~10×.** Formal classroom teaching, previously orphaned by W3.5, now homed in W11.2.*

### W4 — Licensed, sign-off gated *(PARTITION; prior $4–6T)*

| Track | Fam | labor TAM | V/H/P/R/L/D | Coupled? | Net | Conv |
|---|---|---|---|---|---|---|
| W4.1 External Audit & Statutory Assurance | W4 | $150–250B `[W]` | 3/3/0/5/4/3 | Additive (→coupled if per-engagement) | Compression | High |
| W4.2 Tax Preparation & Compliance Filing | W4 | $300–450B `[W]` | 4/2/0/4/4/3 | Coupled (per-return) | Mixed | High |
| W4.3 Legal Work Product (draft/review/research/diligence) **[MERGED W2+W4]** | W4 | $700–900B `[W]` *(of which non-delegable sign-off/malpractice residue ~$50–150B, R=5)* | 2/3/0/4/4/4 | Additive (seat) | Mixed | High |
| W4.4 Consumer / Access-to-Justice Legal (UPL frontier) | W4 | $100–200B `[L]` | 2/2/0/5/4/1 | Coupled (UPL-gated ≈0) | Expansion | Low |
| W4.5 Clinical Documentation & Decision Support | W4 | $150–300B `[W]` | 3/1/0/3/3/4 | Additive (seat) | Expansion | High |
| W4.6 Autonomous / Device-Cleared Diagnosis | W4 | $60–100B `[W]` | 5/1/1/5/2/5 | Coupled | Mixed | Medium |
| W4.7 Fiduciary Financial & Wealth Advisory **[MERGED W4+W7 Wealth]** | W4 | $100–200B `[W]` (US ~$37B, 266.8K advisors) | 3/4/0/4/2/3 | Additive (seat; AUM fee stays human) | Expansion | High |
| W4.8 Specialized Statutory Attestation (actuarial/ESG/PE-stamp/appraisal) | W4 | $50–100B `[W]` | 3/2/2/4/2/3 | Additive | Mixed | Medium |
| W4.9 Pharmacy — Licensed Dispensing & Verification **(added)** | W4 | $100B+ `[W]` | 5/1/2/5/2/3 | Coupled (dispensing robotics) + additive (verification SW) | Mixed | Medium |

*W4.3 is now the single legal home; radiologist read-time lives **only** in W4.6 (excluded from W4.5). W4.7 reconciled to BLS 266,800 advisors and R=4; relationship premium is a sub-line, not a separate W7 track. W4.8 ESG-assurance TAM actively shrinking (EU Omnibus in force 18 Mar 2026).*

### W5 — Physical, Structured *(PARTITION; re-split vs W6 by ENVIRONMENT STRUCTURE; prior ~$5.75T)*

| Track | Fam | labor TAM | V/H/P/R/L/D | Coupled? | Net | Conv |
|---|---|---|---|---|---|---|
| W5.1 Warehouse goods-movement & AMR intralogistics | W5 | $0.7–1.0T `[W]` | 5/2/3/1/1/3 | Coupled | Mixed | High |
| W5.2 Piece-picking, packing & palletizing (dexterous) | W5 | $0.6–0.9T `[W]` | 5/2/4/1/2/4 | Coupled | Mixed | Medium |
| W5.3 Discrete manufacturing machine tending | W5 | $2.0–2.8T `[W]` | 4/2/3/1/2/3 | Coupled | Compression | High |
| W5.4 Structured visual QC & inspection | W5 | $0.15–0.25T `[W]` | 5/1/1/1/3/3 | **Coupled (RECOUPLED)** | Mixed | Medium |
| W5.5 Commercial floor cleaning — **structured open-floor slice** | W5 | $150–250B `[W]` (of $0.4–0.6T pool) | 4/3/2/1/1/2 | Coupled | Mixed | High |
| W5.6 Structured construction, site-layout & offsite prefab | W5 | $0.5–0.8T `[W]` | 4/3/4/2/1/4 | Coupled | Expansion | Medium |
| W5.7 Structured food/beverage production (CPG/commissary; incl. dairy/livestock robotics) | W5 | $0.3–0.5T `[W]` | 4/2/3/2/2/3 | Coupled | Mixed | Medium |

*W5 = fixtured/engineered/structured-subtask value. Vendor assignments (one home each): Avidbots/Brain Corp/Gausium/Whiz/Tennant → W5.5; Dusty/Built/Toggle/Canvas → W5.6; Chef Robotics (CPG) → W5.7; Lely/DeLaval dairy → W5.7 sub-line.*

### W6 — Physical, dexterous/unstructured *(PARTITION; residuals NET OF W5; prior ~$8.5–11T)*

| Track | Fam | labor TAM | V/H/P/R/L/D | Coupled? | Net | Conv |
|---|---|---|---|---|---|---|
| W6.1 Skilled Construction Trades — MEP install & repair | W6 | $1.0–1.4T `[W]` | 4/3/5/4/1/4 | Coupled | Expansion | Medium |
| W6.2 General Construction — unstructured structural/finishing **(residual net of W5.6)** | W6 | $2.0–2.7T `[W]` *(resized down)* | 4/3/5/3/1/4 | Coupled | Expansion | Medium |
| W6.3 Personal Care & ADL assistance | W6 | $0.9–1.3T `[W]` (+~$11T informal `[L]`) | 2/4/5/4/1/4 | Coupled | Expansion | Medium |
| W6.4 Field Service & industrial equipment repair | W6 | $0.9–1.3T `[W]` | 4/2/5/3/1/3 | Coupled (FSM software excluded — additive, not here) | Mixed | Medium |
| W6.5 Cleaning & janitorial — **unstructured residual** (restroom/detail/clutter/home; net of W5.5) | W6 | $0.5–0.75T `[W]` *(resized down)* | 4/3/4/1/1/2 | Coupled | Mixed | High |
| W6.6 Specialty-crop agriculture — selective harvest & handling | W6 | $0.4–0.7T `[W]` | 5/3/5/1/1/4 | Coupled | Expansion | High |
| W6.7 Commercial food prep — QSR/unstructured | W6 | $0.6–0.9T `[W]` | 4/2/4/2/2/4 | Coupled | Mixed | Medium |

*W6 = variable/occupied/unstructured residual. Miso/Hyphen → W6.7; front-of-house/waitstaff EJECTED → W10.3; companionship/monitoring robots EJECTED → W14. W6.4 keeps the map's best coupling hygiene (FSM software is additive, deliberately excluded from the coupled TAM).*

### W7 — Trust/Relational Premium *(OVERLAY — top-comp slice of W2/W3/W4; NON-ADDITIVE; prior $3–5T)*

| Track | Fam | labor TAM | V/H/P/R/L/D | Coupled? | Net | Conv |
|---|---|---|---|---|---|---|
| W7.1 Psychotherapy & Clinical Mental-Health Alliance | W7 | $50B US / $100–130B global `[W]` | 1/4/1/4/4/2 | Additive (access-priced) | Expansion | Medium |
| W7.2 Executive & Leadership Coaching | W7 | $6–10B `[W]` *(report-mill $100B rejected)* | 1/4/0/0/3/1 | Additive | Expansion | Medium |
| W7.3 High-Stakes Negotiation & Mediation | W7 | $3–6B `[W]` | 2/3/1/1/1/1 | **Additive (reclassified — no outcome-priced vendor exists)** | Mixed | High |
| W7.4 Senior M&A / Capital-Markets Dealmaking (origination) | W7 | $10–15B relational subset ($29–32B fee pool `[$]`) | 4/4/0/3/1/3 | **Additive (reclassified — vendor seat-priced, outcome-capture ≈0)** | Mixed | High |
| W7.5 Strategic / C-Suite Relationship Selling | W7 | $80–150B `[W]` (top-slice of W3.3) | 4/4/0/1/2/2 | **Additive (reclassified)** | Mixed | Medium |
| W7.6 Trusted Strategic Counsel (senior partner/board/GC) | W7 | $50–100B relational premium `[W]` | 1/5/0/4/1/2 | Additive | Mixed | High |
| W7.7 Real-Estate Brokerage & Property Management **(added)** | W7 | $100–200B commission pool `[$]` | 2/3/1/2/2/3 | Additive (commission stays human) | Expansion | Medium |

*Every W7 dollar overlaps a parent (W2/W3/W4) and is NON-ADDITIVE. Primary vendor homes: Rogo/Hebbia → W2.2; Gong/Clari → W3.3; Jump/Zocks → W4.7. W7 lists them only as "also-appears." The W4/W7 wealth duplicate is resolved by merging into W4.7.*

### W8 — Agent-economy labor (NET-NEW) *(prior $10–20B SW / ~$25–45B wage bill; now populated)*

| Track | Fam | labor TAM | V/H/P/R/L/D | Coupled? | Net | Conv |
|---|---|---|---|---|---|---|
| W8.1 Agent Ops & Fleet Supervision (T4) | W8 | $10–20B `[W]` net-new | 3/3/0/2/3/3 | Additive (net-new) | Expansion | Medium |
| W8.2 Forward-Deployed Integration / FDE (T6) | W8 | $8–15B `[W]` | 3/4/0/1/2/3 | Additive | Expansion | Medium |
| W8.3 Agent Evaluation, Red-Team & Safety Testing (T5) | W8 | $3–8B `[W]` | 3/3/0/3/3/3 | Additive | Expansion | Medium |
| W8.4 AI Training-Data & Labeling / Expert Sourcing **(homes Mercor)** | W8 | $5–10B+ `[W]` | 3/2/0/1/3/3 | Coupled-ish (per-task) | Mixed | Medium |
| W8.5 Agent Trust, Insurance & Audit (T7) | W8 | $2–5B `[W]` | 2/3/0/4/2/3 | Additive | Expansion | Low |

*W8 is the map's leading indicator — its growth rate proxies how fast W1–W7 actually deploy. Durable human residue is the accountability/liability floor (T4/T5/T7).*

### W9 — Transportation & Mobility **(NEW PARTITION; ~$1.5–2.5T)**

| Track | Fam | labor TAM | V/H/P/R/L/D | Coupled? | Net | Conv |
|---|---|---|---|---|---|---|
| W9.1 Rideshare, Taxi & Robotaxi | W9 | $0.3–0.5T `[W]` | 5/2/5/5/2/5 | Coupled (capex/RaaS $/mile) | Mixed | Medium |
| W9.2 Long-haul & Regional Trucking | W9 | $0.5–0.9T `[W]` (US $200B+) | 5/2/5/5/2/5 | Coupled | Mixed | Medium |
| W9.3 Last-mile Delivery & Courier (incl. drone/sidewalk) | W9 | $0.3–0.6T `[W]` | 5/2/5/4/2/4 | Coupled | Mixed | Medium |

*Single largest agent/robotics-addressable blue-collar pool in the map; capture <1% today, safety/DOT/insurance-gated (R=5) for a decade in the dexterous tail. Waymo, Aurora, Kodiak, Gatik, Nuro, Zipline, Wing.*

### W10 — In-person Frontline Commerce & Hospitality **(NEW PARTITION; ~$2–3T)**

| Track | Fam | labor TAM | V/H/P/R/L/D | Coupled? | Net | Conv |
|---|---|---|---|---|---|---|
| W10.1 Retail Floor & Cashiering (+physical security/guarding sub-line) | W10 | $0.8–1.2T `[W]` | 3/1/3/1/3/2 | Coupled (partial; presence-gated) | Mixed | Medium |
| W10.2 Hospitality & Hotel Operations | W10 | $0.5–0.8T `[W]` | 3/2/3/1/3/2 | Coupled (partial) | Mixed | Low |
| W10.3 Food-Service Front-of-House & Ordering **(homes W6.7 FOH ejection)** | W10 | $0.5–0.9T `[W]` | 3/1/3/1/3/2 | Coupled (partial) | Mixed | Medium |

### W11 — Public-Sector Service Delivery & Administration **(NEW PARTITION; ~$2–4T)**

| Track | Fam | labor TAM | V/H/P/R/L/D | Coupled? | Net | Conv |
|---|---|---|---|---|---|---|
| W11.1 Benefits/Case Processing & Citizen Service | W11 | $0.5–1.0T `[W]` | 4/2/0/5/2/4 | Coupled (procurement-gated) | Compression | Medium |
| W11.2 Public Education Delivery **(homes ~85M teachers)** | W11 | $1.5–2.5T `[W]` | 2/3/2/5/3/3 | Additive (presence-gated) | Expansion | Medium |
| W11.3 Public-Safety Records, Permitting & Administration | W11 | $0.3–0.6T `[W]` | 3/2/1/5/2/4 | Coupled | Compression | Low |

*High capability, capture throttled by procurement + civil-service protection + political economy (an R=5 parallel to W4, but the gate is political not licensing). Palantir gov, ServiceNow public sector, Accenture Federal.*

### W12 — Defense & Intelligence **(NEW; ~$200–500B)**

| Track | Fam | labor TAM | V/H/P/R/L/D | Coupled? | Net | Conv |
|---|---|---|---|---|---|---|
| W12.1 Intelligence / ISR Analysis | W12 | $100–250B `[W]` | 3/3/0/5/2/5 | Additive (analytic) | Expansion | Medium |
| W12.2 Autonomous Defense Systems & Logistics | W12 | $100–250B `[W]` | 3/3/5/5/2/5 | Coupled | Expansion | Medium |

*Clearances/classified-data moat (D=5) → sovereign/incumbent capture, near-zero merchant SW TAM. Anduril, Palantir, Helsing, Shield AI, Scale (gov).*

### W13 — Media & Entertainment Production **(NEW; ~$0.5–1T)**

| Track | Fam | labor TAM | V/H/P/R/L/D | Coupled? | Net | Conv |
|---|---|---|---|---|---|---|
| W13.1 Screen & Video Production (film/TV/VFX/animation) | W13 | $0.3–0.6T `[W]` | 2/2/1/1/5/2 | Coupled/Mixed | Mixed | Medium |
| W13.2 Music, Audio, Voice & Interactive/Game Content | W13 | $0.2–0.4T `[W]` | 1/2/0/1/5/2 | Coupled/Mixed | Mixed | Medium |

*L=5 lab-capture; IP/rights litigation is the binding gate (parallels W4's R-story). Runway, ElevenLabs, Suno, Udio, generative-video labs.*

### W14 — Consumer/Household Personal Assistance **(NEW — EXPANSION OVERLAY; ~$50–100B paid + ~$11T latent)**

| Track | Fam | labor TAM | V/H/P/R/L/D | Coupled? | Net | Conv |
|---|---|---|---|---|---|---|
| W14.1 Consumer/Household Personal Assistance (life-admin, DIY finance/tax, health nav, companionship/eldercare-monitoring) | W14 | $50–100B paid `[W]` / ~$11T `[L]` | 2/3/1/2/5/1 | Additive (access-priced) | Expansion | Medium |

*The largest actual agent-economy revenue line in 2026 (consumer ChatGPT/Claude/Gemini) with displaced-wages ≈0 — the inverse framing from the rest of the map. L=5 bites hardest here; labs own the consumer surface. Homes the ejected W6.3 companionship robots.*

### Services-Arbitrage **(OVERLAY — delivery-model re-cut of W1/W2/W3; each stamped with parent; NON-ADDITIVE; ~$0.9–1.1T vendor rev)**

| Track | ∩ Parent | labor TAM | V/H/P/R/L/D | Coupled? | Net | Conv |
|---|---|---|---|---|---|---|
| SA.1 Contact-Center CX Resolution | ∩ W3.1 (outsourced slice) | $200–250B `[W]` | 3/1/0/2/5/2 | Coupled | Compression | High |
| SA.2 Outbound & Collections Voice BPO | ∩ W3.2 + W3.7 | $30–50B `[W]` | 3/1/0/4/4/2 | Coupled | Mixed | Medium |
| SA.3 BPO Back-Office F&A & Transaction Processing | ∩ W1 | $120–180B `[W]` | 4/2/0/3/3/3 | Coupled | Compression | Medium |
| SA.4 Application Services / AMS Code-Factory | ∩ W1.1 code | $400–500B `[W]` | 4/3/0/1/5/2 | Coupled (fixed-price) + additive (staff-aug seats) | Mixed | High |
| SA.5 IT Operations & Service Desk | ∩ W1 | $150–250B `[W]` | 4/2/1/1/4/3 | Coupled | Compression | High |
| SA.6 KPO — Knowledge/Research/Analytics | ∩ W2 | $125B `[$]` ($50–125B spread) | 2/3/0/2/4/4 | Coupled | Mixed | Medium |

*SA figures are INTERSECTIONS of their parent partitions, reconciled to one wage bill (SA.1 = the outsourced ~$200–250B subset of W3.1's $0.45–0.6T, not an independent estimate). Highest lab/platform-capture cohort in the map (Agentforce, ServiceNow, coding agents).*

---

## 2. Changes Made From Reviews

**Structural / MECE (Review 1 & 3 P1):**
- **Typed every family PARTITION vs OVERLAY** at the schema level. W1–W6, W9–W13 = partition (approx-summable net of overlap). W7, Services-Arbitrage, W14 = overlay (non-additive, each stamped with parent). W8 = distinct net-new family.
- **Fixed the `coupled` contradiction (Review 3 P1, upstream of everything).** Adopted one principle: **COUPLED = the task is substituted and the vendor dollar is carved out of displaced labor (never add SW+labor; size = capture-rate × displaced labor); ADDITIVE = the human is durable and the vendor augments capacity (SW and labor are different dollars).** This honors both of Review 3's asks even though they were literally inconsistent: W7 Wealth/Selling/M&A → **reclassified coupled→additive** (vendors are seat-priced copilots, human keeps the fee, outcome-capture ≈0); W5.4 QC → **recoupled false→true** (per-station license is economically bounded by displaced-inspector cost, so it is *not* additive to the inspector pool). W7.3 Negotiation also reclassified additive (no outcome-priced vendor exists).
- **Legal double-count merged (both reviews, P0.1/P1).** W2 "Legal Knowledge Work" + W4 "Legal Work Product" → single **W4.3**, sized once at $700–900B, L/D reconciled to 4/4, home in W4 (the binding constraint *is* the non-delegable sign-off). The non-delegable signature/malpractice residue (~$50–150B, R=5) is stated explicitly as the sub-line of what actually remains human. W2 keeps a cross-reference only.
- **W4/W7 wealth duplicate merged (Review 1 P1.3, Review 3 P2).** W4 Fiduciary + W7 Relationship Wealth → **W4.7**, reconciled to one denominator (BLS 266,800 US advisors) and one R (=4). Relationship premium is a sub-line, not a phantom second track.
- **W5↔W6 re-partitioned by ENVIRONMENT STRUCTURE (both reviews, P0.3/P1).** W5 = fixtured/structured subtask value; W6 = unstructured residual explicitly net of W5. **Resized W6.5 cleaning $0.7–1.0T→$0.5–0.75T, W6.2 construction $2.5–3.5T→$2.0–2.7T** by carving out the W5 slice; reconciled the $0.4–0.6T vs $0.7–1.0T janitorial conflict. Each robot vendor assigned exactly one home.
- **Services-Arbitrage retyped as delivery-model overlay** with each track stamped to its parent (SA.1→W3.1, SA.2→W3.2+W3.7, SA.3/4/5→W1, SA.6→W2). SA.1 reconciled to be an explicit subset of W3.1, not a disagreeing independent estimate.
- **W2 Knowledge Research shrunk** from $800B–1.2T (top-down "5–10% of $40T," the map's weakest basis per Review 3) to $100–200B dedicated MI/librarian headcount, conviction downgraded; legal-research→W4.3, market-intel→W2.2.
- **Player registry, one primary home each:** Harvey/Legora/CoCounsel→W4.3; AlphaSense/Hebbia/Rogo→W2.2; Gong/Clari→W3.3; Jump/Zocks→W4.7; Sierra/Decagon/Parloa→W3.1; Chef→W5.7, Miso→W6.7; Dusty/Built/Toggle/Canvas→W5.6; Avidbots/Brain Corp/Gausium→W5.5. Elsewhere listed as "also-appears," ARR counted once.

**Rescores / resizes (Review 3 P2):**
- CX **V 4→3** (both W3.1 and SA.1) — resolution is not cleanly machine-checkable (35–45% verified vs 80% deflection).
- H shown at volume-median with a **value-weighted-horizon caveat** on every H=1 short-horizon track (W3.1/3.6/3.7, SA.1/SA.5) — the dollar-valuable residual is long-horizon at 80% reliability, not the cheap single-turn median.
- W5.4 QC recoupled (above). Legal L/D and wealth R reconciled (above).
- **labor_tam denominator tags added** (`[W]`/`[L]`/`[$]`) so wage bills, latent demand, and market-revenue proxies are never silently summed.

**Reassignments:** Mercor $2B ARR → W8.4 (it is AI-lab data-labeling, not recruiting; de-inflates W3.4 sw_tam ~10×). Radiologist read-time → W4.6 only (out of W4.5). Formal classroom teaching → W11.2. Companionship/eldercare robots → W14. FSM software kept excluded from W6.4 (best-practice preserved).

---

## 3. Missing Pools Added (and Rejected)

**Added — new families (gaps review P0/P1):**
- **W9 Transportation & Mobility** (~$1.5–2.5T) — rideshare/robotaxi, trucking, last-mile. Fixes the internal contradiction where W3.3/W5/W6 ejected drivers "to a physical family" that didn't exist.
- **W10 In-person Frontline Commerce & Hospitality** (~$2–3T) — retail/cashier, hotel, food-service FOH. Homes the ejected W6.7 front-of-house and retail-floor selling.
- **W11 Public-Sector Service Delivery** (~$2–4T) — benefits/case processing, public education (homes the orphaned ~85M teachers), public-safety/permitting.
- **W12 Defense & Intelligence** (~$200–500B) — ISR analysis, autonomous systems/logistics. Hot 2026 funding, previously absent.
- **W13 Media & Entertainment Production** (~$0.5–1T) — screen/video/VFX, music/audio/voice/games (distinct from W2 marketing).
- **W14 Consumer/Household Personal Assistance** (~$50–100B paid + ~$11T latent) — the biggest realized-revenue blind spot; framed as expansion, not displacement.

**Added — tracks into existing families:**
- **W2.7 Translation, Localization & Interpretation** ($60–80B, V=5/L=5) — the oldest, most-verifiable, already-converted displacement case; its absence undercut W1/W2's completeness claim.
- **W1.4 Bookkeeping & SMB Accounting** ($100–200B) and **W1.6 Medical Coding & RCM** ($100–150B) — the fastest-converting W1 pockets, previously only mentioned.
- **W4.9 Pharmacy** (licensed, $100B+) — a sign-off-gated profession missing from W4.
- **W7.7 Real-Estate Brokerage & Property Management** ($100–200B commission pool) — relationship/commission-gated, a natural W7 parallel to wealth/dealmaking.
- **Sub-lines (not standalone tracks):** livestock/dairy robotics → W5.7; physical security/guarding → W10.1; companionship/eldercare-monitoring → W14.1.

**Rejected as out-of-scope (declared explicitly):**
- **The ~$11T ILO unpaid-care/household shadow pool** — retained as *expansion optionality* flagged on W6.3 and W14.1, never as a displaceable wage-bill track (it is `[L]`, not `[W]`).
- **Gig/freelance as its own family** — rejected as a standalone pool; instead treated as a cross-cutting slice folded into each W2/W3/W9 track's basis (the substitutable segment of the parent), per the review's alternative. Data-labeling gig → W8.4; rideshare/delivery gig → W9.
- **Veterinary, aquaculture/forestry, scientific-R&D/drug-discovery, CAD/EDA, standalone insurance vertical** — deferred, not added. Vet → future W4 sub-track; insurance underwriting/claims already split across W4.8 (actuarial) + SA.3 (claims) and cross-referenced rather than given a phantom home; R&D/CAD is net-new-heavy and parked for a W8 or W12 decision at G1. Flagged as known gaps, not silently ejected.

---

## 4. Coupling Ledger

**Rule:** COUPLED tracks must be sized as **capture-rate × displaced-labor** — SW TAM and labor TAM are the *same* dollars, never summed. ADDITIVE tracks may sum SW to labor (different dollars — augment/copilot on a durable human).

**COUPLED (outcome-denominated — capture-rate sizing; do NOT add SW+labor):**
`W1.1(fixed-price fringe), W1.2, W1.3, W1.4, W1.5, W1.6, W1.7` · `W2.1(fees=analyst hrs, external capture≈0), W2.7` · `W3.1, W3.2, W3.4, W3.6, W3.7` · `W4.2, W4.4(UPL-gated≈0), W4.6, W4.9(dispensing)` · `W5.1, W5.2, W5.3, W5.4(recoupled), W5.5, W5.6, W5.7` · `W6.1, W6.2, W6.3, W6.4, W6.5, W6.6, W6.7` · `W8.4(per-task)` · `W9.1, W9.2, W9.3` · `W10.1, W10.2, W10.3 (partial/presence-gated)` · `W11.1, W11.3` · `W12.2` · `W13.1, W13.2 (mixed)` · **all six Services-Arbitrage tracks (SA.1–SA.6)**.

**ADDITIVE (augment-copilot — SW additive to labor):**
`W1.1(seat portion)` · `W2.2, W2.3, W2.4, W2.5, W2.6` · `W3.3, W3.5` · `W4.1(seat today), W4.3, W4.5, W4.7, W4.8, W4.9(verification SW)` · **all seven W7 tracks (reclassified — underlying labor is outcome-denominated but the vendor is seat-priced; outcome-capture ≈0%)** · `W8.1, W8.2, W8.3, W8.5` · `W11.2` · `W12.1` · `W14.1`.

**Split-regime (both — do NOT double-count the two lanes):** W1.1 / SA.4 (staff-aug seats = additive; fixed-price managed delivery = coupled) · W4.1 (seat now, coupled if it moves to per-engagement) · W4.9 (dispensing coupled, verification additive).

**Capture-rate reality flags:** coupled ≠ deflection — CX ~7–11% captured vs 80% deflection claimed; warehouse/manufacturing physical tracks <1–1.5% of the labor pool captured today despite mature hardware; autonomous diagnosis throttled to near-zero $ by reimbursement (2 CPT codes), not capability; W9 mobility capture <1%, reg/liability-gated for a decade.

---

## 5. Open Questions for the G1 Gate (decide before Phase 2)

1. **Scope discipline vs completeness.** The gaps review forced 6 new families and pushed the count to 76 (above the 55–75 target). Does Patrina want all 14 families sized in Phase 2, or **defer the thinnest/lowest-conviction new families (W12 Defense, W13 Media, W14 Consumer)** to a v2.1 addendum so Phase 2/3 stay tractable? These three are Medium/Low conviction and lack the bottom-up rigor of the original core.

2. **`coupled` principle — ratify the substitution-vs-augmentation definition.** I resolved the two-definitions contradiction with "substitution carves the vendor dollar from displaced labor." This flipped 4 tracks (W7 wealth/selling/M&A → additive; QC → coupled). If Patrina prefers the stricter literal "vendor-pricing-mechanism" definition instead, QC flips back and the whole ledger must be re-derived — so this is the one call to lock **first**, because it is upstream of every family rollup.

3. **W1/W8 authority — populate vs assert.** W1 now carries the map's most aggressive substitution claim (~60% task-value executable; code 40x→15.5x) with newly-drafted tracks, and W1.1 code collides with SA.4 AMS ($0.4–0.5T potential double-count). Does Phase 2 do the bottom-up BLS/ILO re-derivation for the new W1 tracks, or do we ship them "asserted, unverified" and flag conviction accordingly?

4. **The global comp multiplier.** Every W5/W6/W9 physical TAM rides a single unverified "global ≈ 5–6× US" constant; a 4× vs 6× swing moves multiple trillions across the two largest families. Does G1 want an explicit sensitivity band (4×/5×/6× scenarios) carried through Phase 2/3, rather than point ranges?

5. **Headcount-vs-dollar framing for "total TAM."** The four mass-headcount, low-comp pools now added (mobility, frontline commerce, public sector, consumer) are exactly what the dollar-weighting de-emphasizes. Should the map publish a **stated caveat that it is a dollar-weighted advanced-economy map** (so any "total agent TAM" reasoning is explicitly biased low on blue-collar/public/consumer), or additionally produce a headcount-weighted companion view for the four new pools?