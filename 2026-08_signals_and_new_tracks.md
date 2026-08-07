# 2026-08 — Full Signal Sweep + New-Track Proposal

Companion to `AI_Agent_TAM_Update_2026-08.md`. This is the piece that was missing:
(a) systematic macro **and** early/weak signals, (b) UPDATE TYPE 1 (new-track qualification),
which is why the first pass wrongly left the count at 201.

---

## Part 0 — Why the first pass said "201 unchanged" (the gap)

The skill defines 5 update types. First pass ran 4 (TAM / displacement / capability / players)
and **skipped Type 1 (new-track qualification)** — the only one that changes the count.
Research was also macro-biased: chased confirmable mega-rounds, under-weighted emerging
categories and seed/early signals. This file fixes both.

---

## Part 1 — MACRO signals (big, high-confidence)

| Signal | Detail | Framework effect |
|---|---|---|
| SpaceX × Cursor $60B | All-stock, Jun 16; largest VC-backed acq ever; killed the $50B Series E | #48 (applied) |
| Anthropic $65B Series H @ $965B | May 28; $50B new + $15B hyperscaler; IPO filing Jun 1; ARR $47B > OpenAI ~$25B | Model layer (applied) |
| Sierra $950M @ $15.8B | May 4; expanding support → sales/retention | #44 (applied) |
| Isomorphic $2.1B Series B | May 12; largest AI-drug round ever; + Insilico×Takeda Jul 1; NVIDIA×Lilly $1B | #104 (applied) |
| Unitree IPO (STAR Market) | $620M @ ~$5.9B; **profitable, 35% net margin**; subscription Aug 10 | #134 (applied) |
| Ramp $750M @ $44B / Mercury $200M @ $5.2B | Jun 4 / May 20; Fin Services opens | Fin Svcs (applied) |
| Q2 macro | Q2 $200B+ (2nd-largest ever); H1 $510B > all of 2025; OpenAI+Anthropic = 43% of H1 | Summary (applied) |
| Claude Fable 5 / Mythos tier | Jun 9; first public Mythos-class; ~80% SWE-bench Pro | Capability (applied) |
| GPT-5.6 (Jul 9) + Astra (Aug 1) | Sol/Terra/Luna; Astra = 10 solved open math problems, long-horizon multi-agent | Capability (applied) |

### Frontier-lab supply explosion (NOT yet reflected — context for agent economics)
- **Reflection AI** $27.5B val ($2.5B round Mar; open-weight, ex-DeepMind)
- **Thinking Machines Labs** $50B val ($5B Series B Mar; Mira Murati)
- **SSI** (Sutskever) stealth, ~$1B+ base; **Mistral** $1.5B Series C
- Implication: first-order model supply is commoditizing fast → pushes agent margin
  into the application/infra layer, reinforcing the "SW catches labor" thesis.

---

## Part 2 — EARLY / WEAK signals (what the first pass ignored)

| Signal | Stage | Why it matters |
|---|---|---|
| **XBOW** $120M Series C @ $1B+ ($237M total) | Growth | Autonomous pentest crossed to unicorn — a category that didn't exist 18 mo ago |
| **Hex Security** $172M (YC W26) | Early-growth | Second credible autonomous-pentest player = category, not one-off |
| **Vapi** $500M val (beat 40 rivals for Amazon Ring) | Series B-ish | Voice-agent infra consolidating; Retell 30M calls/mo | 
| **AIUC** (AI Underwriting Co) $15M seed (Nat Friedman, Ben Mann) | Seed | **Insurance FOR AI agents** — brand-new category, watch |
| **Corgi** $108M | Growth | AI-native insurer (full-stack underwriting+claims+policy) |
| **Skild AI** $1.4B @ $15B / **Physical Intelligence** $400M / **World Labs** $1.23B | Growth | Robotic foundation model = pure-SW brain licensing layer; no track home |
| **Resolve AI / Cleric / Traversal / incident.io** + Datadog Bits, Dynatrace (Jul 27) | Mixed | Autonomous SRE crossed concept→product category in 2026; MTTR −70% |
| **Braintrust** $80M Series B @ $800M; **Langfuse → ClickHouse** (Jan) | Growth | Agent eval/observability consolidating (updates existing infra tracks) |
| **Abridge** $5.3B (+$316M Series E ext Apr; $800M+ total) / **Ambience** ~$1.25B | Growth | Ambient clinical scribe = one of the largest vertical-AI revenue categories, NOT in framework |
| **Puzzle** $66.5M / **Digits** "Autonomous GL" / Numeric / Basis / Rillet | Series A/B | SMB autonomous bookkeeping; CPA shortage 340K driver |
| **Agentic commerce**: UCP (Google+Shopify), ACP (OpenAI+Stripe), Perplexity Instant Buy | Protocol war | New transaction modality; OpenAI sunset Instant Checkout Mar 5 (inventory infra gap) |
| **AI browsers**: Comet (global), Atlas (retired Aug 9), Browser Use, Strawberry | Product | Computer-use-as-product; updates #18 Web Automation + capability |

---

## Part 3 — NEW-TRACK PROPOSAL (UPDATE TYPE 1)

Each ran through the skill's qualification filter (labor market? agent-delivered? distinct? commercial evidence?).
**Numbers are first-pass triangulations — flagged Medium pending 2-source cross-validation for any >$10B.**

### HIGH conviction (recommend add)

| # | Proposed track | Category | SW TAM | Labor TAM | Ratio | Disp | Net | Key evidence |
|---|---|---|---|---|---|---|---|---|
| N1 | **Autonomous Penetration Testing / Offensive Security Agent** | Dev & Tech | $2.5B | $25B | 10x | 55-70% | ✅ Expansion | XBOW $1B+, Hex $172M — distinct from existing #8 *defensive* Security Scanning |
| N2 | **Robotic / Embodied Foundation Model Platform** | Agent Infra | $4B | $150B | 37.5x | 10-20% | ✅ Expansion | Skild $15B, PI $400M, World Labs $1.23B — pure-SW brain, distinct from #134 hardware |
| N3 | **Ambient Clinical Documentation / Scribe Agent** | Healthcare | $4B | $90B | 22.5x | 60-75% | ✅ Expansion | Abridge $5.3B/$800M raised, Ambience $1.25B — no scribe track exists today |
| N4 | **Voice Agent Platform / Infrastructure** | Agent Infra | $5B | $80B | 16x | 50-65% | 🟡 Mixed | Vapi $500M, Retell, ElevenLabs $11B — horizontal voice layer under CX/sales |

### MEDIUM conviction (add or hold)

| # | Proposed track | Category | SW TAM | Labor TAM | Ratio | Disp | Net | Note |
|---|---|---|---|---|---|---|---|---|
| N5 | **Autonomous SRE / Incident Remediation Agent** | Dev & Tech | $3.5B | $70B | 20x | 40-55% | 🟡 Mixed | Overlaps #6 Monitoring/#13 Anomaly — but *remediation* (fixes, not alerts) is new |
| N6 | **Agentic Commerce / Checkout Protocol** | Agent Infra | $3B | $40B | 13x | 20-35% | ✅ Expansion | Overlaps #20 Price-Monitor-Auto-Buy — would reposition #20 as consumer-side |

### EARLY watch (not yet a track — revisit 2026-10)
- **Insurance-for-AI-agents** (AIUC) — too early ($15M seed), but a genuinely new liability category
- **AI-native insurer full-stack** (Corgi) — likely updates Fin Svcs #8/#9/#10 rather than new track

---

## Part 4 — Existing-track UPDATES this sweep surfaced (beyond first pass)

| Track | Update | Source |
|---|---|---|
| Agent Infra #5/#6/#13 (Behavior Monitor / Eval / Benchmarking) | Braintrust $800M; Langfuse→ClickHouse; AgentOps — eval/observability now funded category | player |
| Agent Infra #18 (Web Automation) | Comet global, Atlas retired Aug 9, Browser Use — computer-use-as-product | player + capability |
| Agent Infra #23 (Accounting Firm Super-Agent) | Puzzle/Digits "Autonomous GL", CPA shortage 340K | player/TAM |
| Fin Svcs #8/#9/#10 (Credit/Insurance/Claims) | Corgi $108M, insurtech 95.2% AI, $1.63B Q1 | player/TAM |
| Healthcare #7 (Medical Insurance Review) | Abridge prior-auth via Availity (Jan) | capability |

---

## Part 5 — If all 6 new tracks added

- Track count **201 → 207**; category counts: Dev&Tech 13→15, Agent Infra 27→30, Healthcare 20→21
- SW TAM +~$22B on top of the $514B → ~$536B (needs Labor-side cross-validation before locking)
- N2 (37.5x) and N3 (22.5x) would enter the >20x priority band; N2 near the 50x deep-dive threshold if Labor TAM sizes higher
- Deep-dive sheets NOT auto-created (none >50x on first-pass numbers)

## Recommendation
Add **N1–N4** (high conviction) this cycle; hold N5/N6 for 2026-10 pending overlap resolution
and the 2-source Labor-TAM cross-validation. Add the Part-4 existing-track updates as change-log entries.

---

## STATUS: APPLIED (2026-08-06)

N1–N4 written into `AI_Agent_TAM_2026-08.xlsx` after source-validating each TAM (the
cross-validation revised 3 of 4 SW figures **down** to match published reports):

| Track | Cat | # | SW | Labor | Ratio | Disp | Net | Conf | Key sources |
|---|---|---|---|---|---|---|---|---|---|
| Autonomous Penetration Testing | Dev&Tech | 14 | $3B | $25B | 8.3x | 55-70% | ✅ | Med | Fortune $3.09B; MnM $4.39B |
| Robotic/Embodied Foundation Model | Agent Infra | 28 | $2.5B | $120B | 48x | 10-20% | ✅ | Med | Marketintelo $2.26B (FM segment) |
| Ambient Clinical Scribe | Healthcare | 21 | $2B | $90B | 45x | 60-75% | ✅ | Med-High | Fortune $1.46B; JAMA $265.6B admin |
| Voice Agent Platform | Agent Infra | 29 | $3.5B | $80B | 22.9x | 50-65% | 🟡 | High | GVR $3.51B; Gartner $80B labor cut |

Framework: tracks **201 → 205**, SW **$514B → $525B**, Labor **$9.60T → $9.92T** (+$315B), ratio **18.9x**.
N5 (Autonomous SRE) and N6 (Agentic Commerce) held for 2026-10 pending overlap resolution with
#6 Monitoring / #20 Auto-Buy. Part-4 existing-track updates (Braintrust, Comet/Atlas, Puzzle,
insurtech) also deferred to 2026-10 as change-log-only entries.
