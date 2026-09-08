# HTC 早期猎场 #1-4 · 详尽报告(工作步骤 × AI 能力时间线)

Hat-Trick Capital · 2026-09-03 · 每份含:工作步骤全拆解 + 逐步能力表(2025年底 vs 2026年9月 vs 是否解锁)+ 关键解锁点 + 硬门槛 + 投资读法

---

I have everything I need — the frozen taxonomy context, the existing deep-dive底稿, and fresh web verification on every load-bearing date. Per the workflow instructions I'm returning the full report inline (not writing a new .md file). Here is the deliverable.

---

# W4.10 — 保险核保与理赔裁定 (Insurance Underwriting & Claims Adjudication)
## HTC 猎场 #1 · 机构级深研 + 时间维度 · 2026-09-03 · Fable-5 时代

> **一句话结论(先给答案):** 这是全图上「白空间」最干净的一格,能力也确实高(~45–55% 任务工时技术上可自动化),但它是一场**由核心系统巨头(Duck Creek/Guidewire)和承保方自己吃掉的世俗慢磨,不是初创的圈地运动**。真正决定这 9 个月的,**不是模型跨过了某个能力门槛,而是两件事同时发生:(1) 2026-04 Duck Creek 作为 core-system 现任把 agentic 楔子直接产品化上线;(2) 2026 年 7 个州的 AI-理赔法把「不利裁决必须人类签字」这道墙重新夯实。** 对 HTC 而言,这 9 个月主要是**把水平赛道的门关上了**,而不是开了一扇新窗。冻结时把 W4.10 排为猎场 #1 是基于「白空间干净」——**这个排名现在在水平楔子上已经过时**,深研自己下调了它。唯一撑得住的种子级 wedge 是**结果计价的代位求偿/追偿(subrogation/recovery)**,外加两条谨慎的 specialty 支线。

**冻结行:** `W4.10 · $150–220B [W] · V4/H2/P0/R4/L3/D4 · Coupled · Net=Compression · Conv=Med · Tier A`

---

## 一、这是什么 + 为什么是早期猎场

### 定义与边界

W4.10 是**两份相邻的持牌工作,共享一条"文档-agent 脊柱"**:

- **核保(Underwriting):** 评估风险敞口、定价、决定承保/拒保/转介/修改条款、出报价并 bind 保单。持牌岗位 = 保险核保员(BLS SOC 13-2053,美国 ~105,420 人,2025-05)。
- **理赔裁定(Claims Adjudication):** 从 FNOL(首次损失通知)到覆盖判定、证据取证、损失定额、责任认定、欺诈筛查、批准/拒付裁决、赔付结算、代位追偿、合规。持牌/半持牌岗位 = 理赔查勘/审核/调查员(SOC 13-1031,美国 ~356,100 人,2024)+ 理赔与保单处理文员(SOC 43-9041,~230k)。

**理赔占工时池约 2.5:1 压过核保。** 这两份工作合起来 ~69 万美国岗位。

### 不包括什么(边界清晰化)

- **不包括物理现场查勘/野外定损**(cat 财产、全损、人伤体检)——那是原子不是比特,评分 P=0 只覆盖"桌面"切片。
- **不包括保险销售/代理/经纪**(那是 W3 关系型)。
- **不包括再保定价/精算建模的核心研究**(高判断、无干净成功单元)。
- **不包括医疗理赔中的临床决策**(那在 W4.5/W4.6)。
- **代位求偿(subrogation)** 是本格内最干净的子切片,单独在第六部分处理。
- **与 SA.3(交易处理)和 W1.6(RCM)的边界:** 理赔处理美元只在本格计一次,不与 SA.3/W1.6 重复入账(冻结时已裁定)。

### 劳动盘子(Labor TAM)

**$150–220B `[W]`,中点 ~$185B**(dollar-weighted,advanced-economy)。推导依据:

| 岗位 | 美国头数 | 依据 |
|---|---|---|
| 理赔查勘/审核/调查员 (13-1031) | ~356,100 | BLS OOH 2024 |
| 保险核保员 (13-2053) | ~105,420 | BLS May-2025 |
| 理赔与保单处理文员 (43-9041) | ~230,000 | BLS |

美国这 ~69 万头 × 全负荷成本(工资×~1.4 loaded)≈ 美国 ~$70–90B 职业工资单;按 advanced-economy 全球加权(美国占全球高薪保险劳动约 35–45%)→ **$150–220B `[W]`**。这是**被替代的人力美元分母**,不是软件市场规模——严守耦合规则,软件收入 = capture-rate × 这个分母,**绝不相加**。

### 为什么值得 HTC 下种子/A 轮(以及为什么要打折)

**值得看的理由:**
1. **能力已由"孪生赛道"证明。** 理赔的文档-抽取-裁定脊柱与医疗 RCM(W1.6)是同一套能力,RCM 已跑通,所以保险的技术可行性不是问号。
2. **成功单元干净、可结果计价。** 尤其是追偿(recovered dollars)和 touchless STP 的每单裁定,这是耦合(Coupled)显示得最清楚的地方。
3. **监管顺风存在**(CMS-0057-F 标准化 PA API)——把管道铺平,但**不移除人类问责地板**(见下)。

**但必须打折的理由(这决定了投资读法):**
- **实现的劳动捕获只有 1–3%(dollar-weighted),真正耦合、砍头数的 <0.5%。** 能力 ~50% ≠ 捕获 1–3%,中间隔着 pilot-to-production 折扣(RCM 孪生 ~22% 进生产;MIT 95% 零 P&L;S&P 42% 弃用率)。
- **绑定约束是 R=4(监管签字),不是模型能力。** 白空间在 P3 冻结到今天之间**关闭得比冻结假设的快**——Duck Creek 2026-04 上线了完全一样的 wedge,Guidewire 在买入,CCC 早就把伤残/工伤这条道整合掉了。

---

## 二、工作步骤全拆解(20 步 / 5 阶段)

以美国工资基数 dollar-weight 各步工时占比(理赔:核保 ≈ 2.5:1):

| # | 阶段 / 步骤 | ~% 工时 | 岗位真实动作 |
|---|---|---:|---|
| | **A. 提交 & FNOL 受理(~20%)** | | |
| 1 | 摄入 submission/FNOL(ACORD、经纪邮件、loss run、门户、来电)+ 文档抽取 | 7% | 从非结构化来源把承保/理赔信息结构化 |
| 2 | 分诊、appetite/覆盖资格核对、严重度&复杂度评分、路由 | 6% | 判断"这单归谁、有多急、走不走快通道" |
| 3 | 数据增补(第三方拉取:MVR、财产/灾害、cat 模型、医疗、财务) | 7% | API 编排、外部数据接入 |
| | **B. 核保风险 & 定价(~18%)** | | |
| 4 | 风险/敞口评估 | 6% | 标准风险 + specialty/E&S 长尾判断 |
| 5 | 费率&定价(rating engine + 精算因子) | 4% | 确定性费率表 + judgment 层 |
| 6 | 参照核保手册/再保 treaty 限额/监管费率备案 | 3% | 检索 UW manual 与合规约束 |
| 7 | **核保决策**(承保/拒保/转介/改条款) | 3% | 干净风险 vs 转介/拒保/例外判断 |
| 8 | 报价生成 & **bind** / 保单签发 | 2% | 出正式报价并绑定 |
| | **C. 理赔调查(~24%)** | | |
| 9 | 覆盖判定(套用保单语言、核在保、除外条款) | 6% | 干净案件自动 vs 争议/含糊语言(bad-faith 风险) |
| 10 | 证据取证(照片/telematics、警方/医疗报告、记录) | 6% | 结构化(自动定损)强,非结构化取证弱 |
| 11 | **物理现场查勘/野外定损**(cat 财产、全损、人伤) | 6% | 原子层,无人机/telematics 只辅助 |
| 12 | 录音陈述/索赔人&证人访谈 | 6% | 对抗性、可信度加权 |
| | **D. 裁定 & 决定(~22%)** | | |
| 13 | 损失/定额估算、医疗账单审核、准备金设定 | 7% | 标准化定损强,人伤准备金判断 |
| 14 | 责任/因果认定 | 6% | 清晰车损自动,争议责任人类 |
| 15 | 欺诈检测 / SIU 转介 | 4% | AI 打分/标记强,调查对抗性人类 |
| 16 | **裁定决策**(批准/拒付/部分)+ 书面理由 | 5% | 例行可自动,**拒付&复杂=受监管持牌行为** |
| | **E. 结算、追偿 & 合规(~16%)** | | |
| 17 | 结算计算/赔付/**谈判** | 5% | 例行赔付自动,谈判/大额人类 |
| 18 | 拒付函/EOB/监管通知起草 + **持牌签字** | 4% | 不利处置=最高责任、州法监管 |
| 19 | 代位求偿/追偿识别 & 追讨 | 4% | ~$20B/年漏损,成功单元=追回美元 |
| 20 | 合规、审计留痕、申诉 & 投诉处理 | 3% | 留痕可自动,申诉判断人类 |

---

## 三、逐步 AI 能力评估(核心表 —— 加时间维度)

> **判定口径:** FULL = agent 在标准路径上无监督完成;PARTIAL = agent 起草/决策但人负责例外或签字;NO = 仍纯人工。**2025年底基线** = 前沿约 Opus-4.5/GPT-5.5 级、文档 AI 成熟、点工具(Federato/Cytora/Sixfold copilot 版/Tractable/Liberate)已存在但多为"推荐+人决策",Duck Creek 的 agentic 平台**尚未上线**。**2026年9月** = Fable 5/Mythos 5(6-9)、GPT-5.6(7-9)、Cytora Autopilot(3-18)、Duck Creek Agentic 平台(4-28)、Sixfold STP quote-and-bind(6-12)均已上线。

| # 步骤 | 2025年底能力 | 2026年9月能力 | 9个月是否解锁 | 备注 |
|---|---|---|---|---|
| **1 摄入/抽取** | **FULL** — 文档 AI 到年底已成熟(RCM 孪生),Cytora/Sixfold 已做抽取 | **FULL** — Duck Creek *Agentic FNOL*(多渠道 capture/validate/route,Gemini)、Cytora *Autopilot*、Liberate "Nicole" 语音 | **NO(能力已满)** / 产品化 YES | 已商品化,front-of-funnel 是向零竞赛 |
| **2 分诊/严重度/路由** | **FULL** — Federato *RiskOps*、分类任务年底已解 | **FULL** — Federato、Qantev、EvolutionIQ(CCC) | NO | 高 V 分类,可对 ground truth 验证 |
| **3 数据增补** | **FULL** — API 编排年底已成熟 | **FULL** — Duck Creek("自动化数据收集")、Cytora | NO / 产品化 YES | 良好边界,商品层 |
| **4 风险评估** | **PARTIAL** — 标准风险可,specialty 需人 | **PARTIAL** — Federato/Sixfold/Cytora;Fable5 推理略升清晰案 | 部分(模型推理边际提升) | E&S 长尾仍人类 |
| **5 费率/定价** | **FULL(标准)** / PARTIAL(specialty) — 费率表长期确定性 | **FULL(标准)** / PARTIAL(specialty) | NO | 已 rate-filed;specialty 是判断 |
| **6 手册/treaty 检索** | **FULL** — RAG 年底成熟 | **FULL** — 对 UW manual 检索 | NO | 可验证检索 |
| **7 核保决策** | **PARTIAL** — Sixfold/Cytora copilot 出推荐+理由,**人决策** | **PARTIAL→FULL(干净风险)** — Sixfold *STP quote-and-bind*(6-12);清晰单可 touchless | **YES ✅ — Sixfold STP(6-12)+ Fable5/GPT5.6 推理** | 但仅限 guardrail 内清晰风险;转介/拒保/例外仍人+appetite 判断 |
| **8 报价 & bind** | **PARTIAL** — 报价生成辅助,**人 bind** | **FULL(标准/清晰)** — Sixfold 从 intake→quote→bind 无中间人(carrier 设 guardrail 内) | **YES ✅ — 本窗口最清晰的门槛跨越(Sixfold 6-12)** | 仍受"清晰风险"上限约束 |
| **9 覆盖判定** | **PARTIAL** — 点工具处理清晰案 | **PARTIAL** — Duck Creek *Agentic FNOL* 做保单/覆盖核对(4-28)、Qantev | 部分 YES(核心系统产品化,4-28) | 清晰案更自动;含糊/争议语言=bad-faith 风险→人类,门未过 |
| **10 证据取证** | **PARTIAL** — Tractable CV 对结构化车损强 | **PARTIAL(结构化近 FULL)** — Tractable(Admiral 90% touchless、98% <15 分钟);置信度评分路由 | 边际(Tractable 置信度路由成熟) | 结构化自动定损强;非结构化证据仍弱 |
| **11 物理查勘/野外** | **NO** | **NO** — 无人机/telematics 仅辅助 | **NO** | 原子非比特;P=0 桌面切片排除;野外定损耐久 |
| **12 录音陈述/访谈** | **NO/PARTIAL** — 语音 agent 仅 intake | **NO/PARTIAL** — Liberate 语音仅受理 | NO | 对抗性、可信度加权、信任负载 |
| **13 定额/医疗审/准备金** | **PARTIAL→FULL(自动定损)** — Tractable 自动估已 FULL;Qantev 医疗 | **PARTIAL→FULL(自动定损)** — 同上,更多 touchless | 边际 | 标准化定损强;人伤准备金=判断 |
| **14 责任/因果** | **PARTIAL** — 清晰车损自动,争议人类 | **PARTIAL** — EvolutionIQ/Qantev;Fable5 略助清晰案 | 边际 | 争议责任仍人类 |
| **15 欺诈/SIU** | **PARTIAL** — AI 打分/标记 FULL,调查人类 | **PARTIAL** — Shift/Qantev + Duck Creek intake-早期欺诈(4-28) | 边际(标记前移到 intake) | 调查对抗性→人类,永不完全闭合 |
| **16 裁定决策** | **PARTIAL** — 例行自动裁定(某大型健康险 80%+ 例行 touchless),人在环 | **PARTIAL** — Duck Creek 置信度评分人在环;例行自动 | 例行 部分 YES(4-28) / **不利裁决 NO(州法夯实)** | **拒付&复杂=受监管持牌行为**;dollar-weighted 核心未过 |
| **17 结算/谈判** | **PARTIAL** — 例行赔付自动,谈判人类 | **PARTIAL** — Liberate/核心系统赔付 | 边际 | 大额/谈判人类 |
| **18 拒付/通知 + 签字** | **PARTIAL(起草)/ NO(签字)** | **PARTIAL(起草)/ NO(签字)** — 2026 州法**夯实**人类签字 | **NO(反向:监管收紧)** | 不利处置=最高责任,州 AI 法监管(见四/五) |
| **19 代位/追偿** | **PARTIAL** — 识别部分,追讨手工(Intellivo 30 年增量 AI) | **FULL(识别)/ PARTIAL(追讨)** — Intellivo(新任 Chief AI Officer)、健康险侧 RapidClaims *RapidRecovery* 语音-AI 自动 payer 跟进(4-13) | 部分 YES(追偿追讨语音-AI,4-13,健康险场景) | ~$20B/年漏损;成功单元=追回美元(干净);见备注:RapidRecovery 实为**医疗 RCM 拒付管理**,非 P&C 代位 |
| **20 合规/审计/申诉** | **PARTIAL** — 留痕 FULL,申诉人类 | **PARTIAL** — CMS-0057-F 标准化 PA API + 拒付指标报送(3-31 起) | 基础设施 部分 YES | 可追溯 FULL;申诉判断人类 |

**加权:技术上可自动化 ≈ 45–55% 任务工时**(FULL 步 ~25pp + PARTIAL 半额 ~25pp)。**但这是能力,不是捕获。** 套 pilot-to-production 折扣后,真正在头部承保方生产环境跑 touchless 的 ≈ **例行理赔量的 ~15–30%**——而这是低美元/单的尾部,所以 **dollar-weighted 实现的劳动捕获只有 ~1–3%**,其中大部分还是"骑在仍在职查勘员上的按座席计价增量收入"(Expansion 味,不是替代)。**真正耦合、砍头数的捕获今天 <0.5%。**

---

## 四、2025→2026 的关键解锁点(报告最有价值的部分)

### 时间线:9 个月里到底发生了什么

```
2025-10  Liberate $50M B @ $300M(Battery)· Nicole 语音 · 承保后台深入
2025-11  Federato $100M D(>$180M 总)+ ~$751M 二级 · RiskOps 水平巨头
2026-01  Sixfold $30M B —— Guidewire 战略入股(信号:core-system 现任买入)
2026-03  Cytora Autopilot(3-18)—— 首个"端到端自运行"承保+理赔 agentic 工作流产品化
         Aspire 采用 Liberate AI FNOL(3-10)
2026-04  ★ Duck Creek Agentic AI 平台 + Agentic UW Workbench + Agentic FNOL(4-28)
           —— core-system 现任亲自上线楔子,Gemini/Google Cloud,neuro-symbolic
         RapidClaims RapidRecovery(4-13,注意:医疗 RCM 拒付管理,非 P&C 代位)
2026-06  ★ Claude Fable 5 / Mythos 5(6-9)—— 前沿模型跳跃(Mythos 级 > Opus)
         ★ Sixfold AI Underwriter STP quote-and-bind(6-12)—— touchless bind 门槛跨越
2026-07  GPT-5.6(7-9)· Fable 5 再 bump(7-12)
2026 全年  ★ 7 个州通过 AI-健康险法(Utah SB319、WA SB5395、IN HB1271、MD HB1563…)
           —— 把"不利裁决须持牌人独立判断"重新夯实
```

### 真正跨过门槛的步骤(YES),以及是什么让它跨过

1. **步骤 7/8(核保决策 & bind)—— 唯一清晰的"能力门槛跨越"。**
   - 2025年底:Sixfold/Cytora 是"推荐+理由,人决策、人 bind"(PARTIAL)。
   - 2026年9月:**Sixfold AI Underwriter STP quote-and-bind(6-12)** 让清晰商业风险在 carrier 设定的 guardrail 内**从 intake 直接走到 quote 和 bind、无中间人**。客户覆盖 $270B GWP(Zurich、Generali、Guardian、Axis、NY Life),承保采用率 90%+。
   - **让它跨过的能力:** (a) STP quote-and-bind 产品本身;(b) Fable 5(6-9)/GPT-5.6(7-9)把多步推理可靠度抬高,使"清晰单 touchless"在可接受错误率内。
   - **但诚实说:** 这只在**清晰风险**上过门槛;dollar-weighted 的核心(specialty/E&S/争议)没动。而且 Sixfold 是 **Guidewire 战略入股**的——门槛跨越的价值流向 **incumbent-adjacent**,不是独立初创。

2. **步骤 1–3 / 9 / 16(例行侧)—— "产品化解锁",不是"能力解锁"。**
   - 这些步骤的**原始能力在 2025年底就已存在于点工具**;9 个月里发生的是 **Cytora Autopilot(3-18)+ Duck Creek Agentic 平台(4-28)** 把它们**从"点工具能力"打包成"跑在核心系统里的端到端 agentic 工作流"**。Duck Creek 的关键在 neuro-symbolic + 直接吃 carrier 现有 data/manuscript/config/API——这是**分发解锁**(core-system 现任把楔子占了),不是模型解锁。**这是本窗口对 HTC 最重要的事件:白空间被现任在 4 月关上了。**

3. **步骤 19(追偿追讨)—— 健康险场景的语音-AI 部分解锁。**
   - **RapidClaims RapidRecovery(4-13)** 上线了语音 AI 自动 payer 跟进 + 自动申诉引擎(拒付翻转率 70%、申诉时限从 40 天压到 72 小时内)。**但必须纠正深研底稿的一个标签错误:RapidRecovery 是医疗 RCM 的拒付管理(provider 侧,属 W1.6),不是 P&C 承保方代位求偿。** 真正的健康险代位现任是 **Intellivo(30 年老牌,2026 Inc 5000,刚任命 Chief AI Officer 补 AI)**——即代位这条道的 AI 化,也主要是**现任在加 AI**,不是 agentic-native 初创空场。

### 被宣传成解锁、但其实没到生产的(诚实清单)

- **"Touchless STP 全面到来":** 能力上线(Sixfold 6-12)是真的,但**只够清晰风险**,受 pilot-to-production 折扣,dollar-weighted 捕获仍 1–3%。不要把它读成砍头数。
- **Duck Creek "$80B 年度美国影响"(BCG 引用):** 这是**部署支出/影响投影**,不是实现的替代捕获。不能入账为 displacement。
- **Gallagher Re "AI = 2026-Q1 insurtech 融资 95.2%、$1.55B/68 单":** 这是**部署支出与融资速度**,不是捕获。
- **"不利裁决自动化":** 不但没解锁,**2026 年 7 个州的 AI-健康险法在同一窗口反向把人类签字夯实了**——这一步在这 9 个月里**变难了**,不是变易了。
- **前沿模型跳跃(Fable 5 / GPT-5.6)对本格的作用被高估:** 模型确实更强,但**绑定约束是 R=4 监管签字,不是模型能力**;所以模型跳跃**没有**解锁不利裁决/拒付/争议责任这些 dollar-weighted 核心步骤。这是本格与编码/SOC 的关键区别。

---

## 五、仍然做不了的(2026年9月的硬门槛)

| 门槛 | 严重度 | 为什么撑得住 | 预计跨过时间 |
|---|---|---|---|
| **1. 不利裁决签字 & bad-faith 责任**(拒付、覆盖争议)—— 步 16/18 | **CRITICAL(监管/信任)** | 不公平理赔实践法 + bad-faith 侵权 + **2026 州法浪潮**:Utah SB319(2027-01 生效,须持牌人独立医学判断、不受 AI 主导)、WA SB5395(禁 PA 单靠 AI 拒/延、须持牌人做不利裁决)、IN HB1271(禁 AI 单独 downcode 除非人先审病历)、MD HB1563(2026-06 生效,季度披露 AI 拒付)、TX Ch.4201(禁 AI 做不利裁决)。CMS-0057-F 标准化 PA API(2026 阶段、2027-01 全量)但**不移除人类问责地板**。 | **不完全闭合。** 随"有意义的人工审查"被定义,3–5+ 年软化;持牌签字是耐久残留,像编码的资深层 |
| **2. 复杂/争议判断**(大额、人伤、责任争议、specialty/E&S 核保)—— 步 4/14/16/17 | **LARGE** | 长尾、低可验证性(V 在争议切片掉)、高严重度美元——恰是 dollar-weighted 核心 | 部分 2–4 年;最高严重度尾部无限期人类 |
| **3. 物理查勘 & 野外定损**(cat 财产、全损、人伤体检)—— 步 11 | **MODERATE(物理)** | P=0 是桌面分;野外是原子;无人机/telematics 辅助不替代 | 机器人/无人机时钟,3–5 年部分 |
| **4. 欺诈调查 / SIU**—— 步 15 | **MODERATE(信任/对抗)** | AI 标记好,调查对抗且证据性;欺诈者博弈模型 | 2–3 年部分;对抗均衡永不完全闭合 |
| **5. 索赔人谈判 & 信任**(尤人伤/大额)—— 步 12/17 | **MODERATE(信任/关系)** | 结算谈判受关系与诉讼阴影约束 | 耐久 |
| **6. carrier 数据接入、集成 & 监管级可解释性**—— 横切 | **MODERATE(部署非能力)** | 不是模型缺口,是分发缺口;core-system 现任拥有轨道和监管要的审计留痕 | 这是价值泄漏机制,不是时钟——见第六部分 |

**绑定约束是 R=4(监管签字),不是模型能力。** 按 P3 白空间纪律:盯**闸门的移动**(州 AI-理赔法、CMS PA 规则、DOI 市场行为姿态),而不是盯模型。

---

## 六、投资读法(机构级,不做啦啦队)

### 价值去哪了(三处泄漏,决定为什么不是初创圈地)

1. **核心系统现任。** Duck Creek 2026-04-28 上线 Agentic UW Workbench + Agentic FNOL(BCG 称"$80B 美国年度影响")。Guidewire 走资产负债表——**战略入股 Sixfold $30M B(2026-01)**。CCC 买 **EvolutionIQ ~$730M 宣布/~$674M 最终对价(2025-01-06 完成)** 拿下伤残/工伤理赔。冻结称"空"的楔子正被按计划殖民。
2. **承保方内部化**为"避免招聘"(Amazon-仓库模式)——Cytora 的 Markel 部署报 **written-premium-per-FTE +113%**;这显示为 carrier margin,不是 vendor ARR。
3. **OSS/模型-实验室通缩**文档抽取商品层(步 1–3)——front-of-funnel 是向零竞赛,不是护城河。

### 耦合捕获数学(capture-rate × 被替代人力,绝不 SW+labor)

- 被替代人力分母:**$150–220B `[W]`**,中点 **~$185B**。
- **今天实现捕获 ≈ 1–3% → ~$2–6B** 被 vendor 触及——但多为**增量座席收入骑在仍在职查勘员上**(Expansion 味)。**真正耦合、砍头数的捕获今天 <0.5%(<~$1B)。**
- **天花板:** STP 或达例行**量**的 ~40–50%,但那是低 LAE 尾部;dollar-weighted 人类残留(复杂/争议/受监管/野外)耐久,7–10 年可替代人力封顶 **~35–45%**;净三处泄漏后 vendor 捕获份额 ~25–40%。→ **vendor-realized-TAM 天花板 ≈ 0.40 × 0.30 × $185B ≈ ~$22B**,对比今天真正耦合的 **<$1B**。
- **这是 ~20–30× 的捕获扩张下注,Medium conviction,门控在 R=4 签字时钟 + STP 可靠度**——多年慢磨,**不是阶跃**。别把 "$80B 影响" 或 "95.2% insurtech 融资" 当替代——都是部署支出与增量。

### 可下注的种子/A 轮 wedge(护城河不迁移的具体细分)

**INVESTABLE —— 真实但有纪律的一条种子道:** 种子–A,**~$15–60M post**,进入 **agentic-native、carrier-data-护城河的纯玩家,按裁定后的每单/追回美元 OUTCOME 计价(非座席)**,攻 core-system 结构性服务不好、也不会拥有好的切片。三个排名子细分:

1. **代位求偿 / 追偿 / 理赔漏损(最高信心)。** 成功单元 = **追回美元**——干净可结果计价,carrier 乐于分成,且**它是 pro-carrier,不带拒付那种 bad-faith/不利裁决责任(门槛 #1)**。~$20B/年漏损,AI 提升追回 10–30%。**但注意:健康险代位现任 Intellivo(30 年、刚补 Chief AI Officer)已占据;RapidRecovery 实为医疗 RCM 侧。** 所以只投**跨承保方数据网络或 core-system 单家拼不出的护城河**,别投"IT-agent 指向代位"。
2. **Specialty / E&S 核保**(非许可、定制、MGA/program 业务)——对 Duck Creek/Guidewire 路线图太小、太定制、变化太快;它们为许可标准/个人/标准商业 STP 优化。
3. **健康/寿/伤残/工伤理赔裁定(谨慎)。** Qantev(>€40M,AXA/Generali/FWD,12 国)/ EvolutionIQ 画像——**但 EvolutionIQ 已被收购出场(CCC),这条道在整合**;只投单家 core-system 拼不出的跨承保方数据网络护城河。

### 该避开什么

- **水平 UW/理赔 copilot——门已关、定价已过 HTC:** Liberate $50M B @ $300M(2025-10)、Federato $100M D />$180M 总、~$751M 二级(2025-11)、Sixfold $30M B 携 Guidewire(2026-01)、Cytora Autopilot。这些恰是现任在内部化的东西。
- **个人车险 P&C**——Duck Creek Agentic FNOL(个人车险优先)+ Tractable($100M+,CV,Admiral 90% touchless)已占。
- **唯一护城河是"carrier 核心系统上一层薄 agent 工作流"的任何东西**——价值 toll 回 SoR 拥有者。
- **座席/copilot 计价**——若非按每单/追回美元结果计价,就是增量产品,现任 ship native 后续约时会被压。

### 3 条带日期的证伪信号(到 2027Q4)

1. **初创可投(BULL):** 到 2027-Q4,**≥1 家独立、carrier-data 护城河的保险-AI 纯玩家跨 ~$75–100M 已核验 ARR、按 outcome/每单(非座席)计价、且未被 core-system vendor 或 carrier 收购。** → 耦合真实且可被初创捕获;保 W4.10 为活种子格。
2. **现任捕获(BEAR —— 基准情形):** 到 2027-Q4,**Duck Creek + Guidewire agentic UW+FNOL 模块在各 >20–30 家 carrier 达生产 STP 率提升,且 ≥2 家头部纯玩家(Sixfold/Cytora/Qantev 级)被 core-system vendor 或 carrier 收购**(EvolutionIQ→CCC 模式重演)。→ 种子门关;价值归现任;把 W4.10 从猎场 #1 降级。
3. **劳动确认(裁 Compression vs 增量):** **2027-05 BLS OEWS:理赔查勘/审核/调查员(13-1031,2024 年 356,100)YoY 下降 且/或 核保员(13-2053,~105k)跌破 ~100k。** → 生产替代为真(升替代信心)。若两者到 2027 都平-升 → 是慢世俗磨/增量,实现耦合捕获保持 <3%,坐实"世俗慢磨非阶跃"。

*(横切确认器:按 outcome/每单计价的保险-AI ARR 到 2027-Q4 达品类 ARR 的 ≥25%,从今天座席主导的基数升上来——耦合是否为真的裁决器。)*

---

## 分析师给投委会的底线

W4.10 曾按"白空间干净"排猎场 #1。**这个排名在水平楔子上现已过时**——Duck Creek 2026-04 上线、Guidewire 买入、CCC 早把伤残/工伤这条道整合掉。这 9 个月的真相是:**唯一清晰的能力门槛跨越(Sixfold STP quote-and-bind,6-12)价值流向 Guidewire-adjacent;最大的事件是核心系统现任把楔子产品化(Duck Creek 4-28)的分发解锁;而监管在同一窗口反向夯实了不利裁决的人类签字(7 个州法)。** 耦合捕获数学仍说替代真实但慢(1–3% 实现、~$22B vendor 天花板、门控 R=4 签字墙、Medium conviction)。**HTC 唯一耐久的种子论点是结果计价的代位/追偿**(pro-carrier、无 bad-faith 门、干净成功单元),specialty/E&S 与健康险理赔为谨慎、暴露于整合的次选。所有水平的东西定价都已过种子门、且指向现任退出。承保时盯 retained ARR、NDR、每单捕获深度、未被收购的独立性——不是 bookings 或 "$80B/95.2%" 头条。

---

**数据核验(2026-09-03 web-verified):**
- Cytora Autopilot 上线 **2026-03-18**(Zurich 全球规模化)· Duck Creek Agentic AI 平台 + Agentic UW Workbench + Agentic FNOL **2026-04-28**(Gemini/Google Cloud,neuro-symbolic)· Sixfold AI Underwriter STP quote-and-bind **2026-06-12**($270B GWP 客户,采用率 90%+)
- Liberate $50M B @ $300M post **2025-10-15**(Battery,Nicole 语音,1.3M 自动处置)· Federato $100M D **2025-11** · Sixfold $30M B(Guidewire 入股)**2026-01**
- 州 AI-健康险法 2026:Becker's "7 部通过";Utah SB319(2027-01 生效)、WA SB5395、IN HB1271、MD HB1563(2026-06 生效)、TX Ch.4201 —— 均要求不利裁决须持牌人
- CMS-0057-F:PA 运营条款 2026-01 生效、拒付指标报送 2026-03-31 起、四 FHIR API 2027-01-01 截止
- EvolutionIQ→CCC ~$730M 宣布/2025-01-06 完成 · Qantev €30M(2024-09,总 >€40M,AXA/Generali/FWD)· Tractable(Admiral 90% touchless、98% <15 分钟)· Intellivo(健康险代位 30 年,2026 Inc 5000,新任 Chief AI Officer)· RapidClaims RapidRecovery **2026-04-13(医疗 RCM 拒付管理,非 P&C 代位——纠正底稿标签)**
- 模型:Claude Fable 5 / Mythos 5 **2026-06-09**、Fable 5 bump 2026-07-12;GPT-5.6 **2026-07-09**
- Gallagher Re:AI = 2026-Q1 insurtech 融资 95.2%、$1.55B/68 单(部署支出,非捕获)
- 内部:p0_foundation(耦合规则、pilot-to-production 折扣)、p3_frozen_taxonomy(W4.10 冻结行、猎场排名)、p5_deepdives(W4.10 底稿)

**关键纠正(相对底稿):** (1) RapidClaims RapidRecovery 是**医疗 RCM 拒付管理**,非 P&C 代位求偿,不应作为"代位 wedge 已有 agentic-native 初创"的证据;(2) Qantev €30M 是 **2024-09**、非 2026 窗口内解锁——它是既有玩家而非本窗口新解锁;(3) 健康险代位现任 **Intellivo** 已占位(30 年,现补 AI),使代位 wedge 的"空场"论点需要收紧——只在跨承保方数据网络护城河处成立。

---

I have a thoroughly web-verified evidence base covering both the Sept-2026 snapshot and the 2025→2026 delta. Per the workflow instructions I'm delivering the full report as my response (not writing a separate .md file). Here it is.

---

# W1.8 — 自主 SOC / 安全运营与告警分诊(Autonomous SOC)
## HTC 猎场 #2 · 详尽报告 · 2026-09-03 · Fable-5 时代

**冻结行:** `W1.8 · $25–50B [W] + large [L] · V3/H2/P0/R2/L3/D4 · Coupled · Net=Mixed · Conv=Med–High · Tier A`
**一句话结论:** 这是全数字盘面上**原始可自动化任务占比最高(~75%)**、且带着「真实人力短缺」政治掩护的赛道——但真实耦合捕获 <1%,~10–15% 的天花板正被 telemetry 巨头当作**捆绑功能**吃掉(Charlotte 在本报告前一天刚发下一代 SOC),纯玩家退出已经以 sub-$1.5B 收购兑现(Radiant→Cribl)。**可下注面不是横向 SOC agent 本身,而是三个「护城河不迁移」的邻区:OT/ICS-SOC、DFIR、以及作为劳动力交付的中端 MDR。**

> **贯穿全篇的时点校准(2025年底 vs 2026年9月):** 这9个月里 SOC AI 的「大新闻」几乎全部发生了——但需要冷静拆分成两类:一类是**真能力解锁**(多 agent 协同调查),数量很少;一类是**分销/捆绑解锁**(MS 把 Security Copilot 免费塞进 E5、CrowdStrike/Palo Alto 把 agent 做成平台原生功能),数量很多,而且**对创业公司是利空不是利多**。Gartner 的市场渗透率在 2025 和 2026 两版 Hype Cycle 上都停在 **1–5%**——最干净的一句「产品发了、捕获没动」的证据。

---

## 一、这是什么 + 为什么是早期猎场

### 定义与边界

被替代的岗位是 BLS **15-1212 Information Security Analysts**(美国 ~193k 岗位,中位薪 $129,180,BLS May-2025),**具体只指其中 tier-1/2 SOC 监控-分诊(monitoring-and-triage)这一楔子**——即 7×24 盯 SIEM/EDR/身份/云/邮件告警、做初筛、误报过滤、初步调查、升级的那批人(含 MSSP/BPO 交付的外包 SOC 座席)。

**不包括(重要边界):**
- **不含**安全架构师、GRC/合规、AppSec、渗透测试、红队——这些是 15-1212 里判断权重高、验证性低的高端切片,不是本赛道。
- **不含 tier-3 事件响应 / 取证的核心签字**——这是邻区 DFIR(见第六节),单独护城河。
- **不含「保护 agent」这一层**(agent security / governance / NHI:Zenity、Obsidian、Astrix)——那是并行的 `[$]` 软件-TAM 台账,**没有工资盘子做分母,不是劳动力赛道**。必须锋利区分:**agent 去干 SOC 的活 = W1.8(邻区可投);给 agent 做安全 = 不是劳动力赛道**。
- **不含**分类/政府 cyber-ISR(留在 W12.1)。W1.8 只算商业/MSSP 侧。

### 劳动盘子(Labor TAM)与依据

- **分母(被替代工资盘子):$25–50B `[W]`** 全球 tier-1/2 SOC 分诊工资盘子(高收入经济体加权)。锚点:美国 ~193k 信息安全分析师 × $129,180 × ~1.4 加载系数 ≈ **$35B** 该职业总盘,其中 tier-1/2 分诊楔子是可寻址切片;全球高收入加权 SOC-ops ~$60–100B。
- **外加一条很大的 `[L]`(未被满足的潜在需求):** 这是本赛道区别于其它 W1 赛道的关键——短缺不是靠裁员释放的,而是**从来没招够人**。**ISC2 2025 工作力研究**(16,029 名受访者,2025-12)**史上第一次拒绝发布「缺口人数」**,理由是**技能缺口已盖过纯人头短缺**成为约束:59% 报告关键/重大技能缺口(同比 +15pp),33% 说没资源把团队配齐。**这条 `[L]` 就是「没有裁员反弹」的政治掩护**——agent 先吃的是「本来就没人看的告警积压」,而不是抢现有座席的饭碗。

### 为什么值得 HTC 下种子/A 轮

三个理由,但每个都带刺:
1. **能力真高。** 加权后 tier-1/2 SOC **~72–78% 的班次工时技术上可自动化**(FULL 步骤 ~25pp + PARTIAL 半计 ~25pp,详见第三节),是数字盘面最高的原始可自动化占比。这是 W1.8 被选为「最强新劳动力市场」的机械原因。
2. **有政治掩护。** `[L]` 短缺 → 早期没有裁员/工会/监管的替代反弹,采纳阻力低。
3. **成功单元干净。** 定价已是 **per-investigation(Dropzone ~$9/次)不是 per-seat**,机械证明了 Coupled——output 被直接对着人力单价计价。

**但下注前必须内化的反面:** 上面这三条恰恰也是巨头的理由。能力高 + 掩护好 + 单元干净 = telemetry 巨头(CrowdStrike/Palo Alto/Microsoft)自己做原生功能的完美对象。所以 HTC 的种子/A 轮**不能投横向 SOC agent**(门已关、已被巨头殖民),只能投**巨头 EDR/SIEM-telemetry 护城河不迁移的邻区**(第六节)。

---

## 二、工作步骤全拆解

把 tier-1/2 SOC 分析师的班次端到端拆成 **15 个离散步骤**,分 4 个阶段,% = 占分诊分析师班次工时的估计份额。

| # | 阶段 / 步骤 | ~% 工时 |
|---|---|---:|
| | **A. 监控与分诊(~30%)** | |
| 1 | 跨 SIEM/EDR/身份/云/邮件的告警摄取与归一化 | 5% |
| 2 | 初筛、严重度打分与优先级排序 | 10% |
| 3 | 误报过滤 / 告警疲劳管理 ← **全岗位最大的单一耗时** | 15% |
| | **B. 调查(~35%)** | |
| 4 | 上下文富化(威胁情报、资产/用户上下文、IOC 查询) | 8% |
| 5 | 跨源关联与时间线重建 | 10% |
| 6 | 影响范围 / blast-radius 判定 | 7% |
| 7 | 根因分析 + 真/误报**裁定(verdict)** | 10% |
| | **C. 响应与遏制(~18%)** | |
| 8 | 遏制动作(主机隔离、账号禁用、IOC 封堵) | 6% |
| 9 | 升级至 tier-3/IR + 组好 case package | 5% |
| 10 | 修复指导与工单化 | 4% |
| 11 | 高后果动作的人工决策/审批 | 3% |
| | **D. 狩猎、检测工程与报告(~17%)** | |
| 12 | 假设驱动的威胁狩猎(threat hunting) | 5% |
| 13 | 检测工程 / 规则调优 / 新检测编写 | 5% |
| 14 | case 文档化、指标与合规报告 | 4% |
| 15 | 交班 / 客户与 CISO 汇报 | 3% |

**耗时分布的关键含义:** 最大耗时(step 3 误报过滤,15%)恰恰是**最可自动化**的那一步——这是「最强新劳动力市场」判断的机械基础;而最难的两步(step 7 裁定、step 11 高后果审批)耗时不大(合计 13%)却承载**几乎全部责任与信任风险**——这是留给人的、验证性最低/后果最高的残余。

---

## 三、逐步 AI 能力评估(核心表)

**FULL** = agent 在标准路径上无监督完成;**PARTIAL** = agent 起草/决策但人负责例外或签字;**NO** = 仍纯人工。所有工具/模型基于真实 2026 产品。

| 步骤 | 2025年底能力 | 2026年9月能力 | 9个月是否解锁 | 备注 |
|---|---|---|---|---|
| **1 摄取/归一化** | **FULL** — 连接器/解析类工作,2025 已商品化(Torq、XSOAR、7AI) | **FULL** — 7AI(60+ agents)、Charlotte、Cortex AgentiX、Exabots | **NO**(窗口前已解锁) | 纯管道活,护城河为零 |
| **2 初筛/优先级** | **FULL(标准)** — Charlotte Agentic Response(RSA-2025)、Cortex AgentiX(Oct-2025)、MS phishing-triage agent 已能在结构化 telemetry 上打分 | **FULL** — Charlotte 声称 98% 分诊准确率、Cortex AgentiX、MS phishing triage GA | **NO**(2025 已基本到位,2026 巩固) | 「98%」是受控演示数,非生产替代 |
| **3 误报过滤** | **FULL** — Dropzone、7AI 年底已做 FP 消除 | **FULL** — 7AI 声称 95–99% FP 消除 | **NO**(杀手级应用,窗口前已解锁) | 最高耗时=最可自动化,赛道存在的理由 |
| **4 上下文富化** | **FULL** — 自动 IOC/资产/身份查询 2025 已解 | **FULL** — 单事件成本 $25–50 → **$2–5** | **NO** | API 编排,已通缩到接近 token 成本 |
| **5 跨源关联/时间线** | **PARTIAL(弱)** — 2025 底多为**单域** agent(Charlotte 单次调查、Cortex 刚发),跨域关联仍靠人缝合 | **PARTIAL(强)** — CrowdStrike **2026-09-02** 发**协同多-agent 跨 endpoint/identity/SaaS/cloud/network 同时调查**,共享上下文/持久记忆;Cortex AgentiX 多-agent | **✅ YES** — **多-agent 协同调查(Charlotte Agentic SOAR, Sept-2026)** 是本窗口最真实的能力跨门槛 | 已知 kill-chain 强,新型多阶段入侵仍退化 |
| **6 影响范围/blast-radius** | **PARTIAL(弱)** — 依赖 telemetry 完整度;行为基线缺口 | **PARTIAL** — 多-agent+共享上下文改善;但 **RSAC-2026「agent 行为基线缺口在三家巨头都没补上」**(VentureBeat),覆盖盲区仍在,OT 尤甚 | **部分 YES(仅 IT 面)/ NO(结构上)** | telemetry 看不到的地方就 scope 不准 |
| **7 裁定(真/误报)** | **PARTIAL** — FP 裁定机器可验;漏报(false-negative)不可干净验证,人签字 | **PARTIAL** — 同前;**2026 调研:57% 团队仍要求人工复核每一个 verdict** | **NO** — 责任地板未移动 | V=3 天花板的机械原因;漏报灾难性 |
| **8 遏制** | **PARTIAL(弱)** — 多为「仅建议」,自动遏制罕见 | **PARTIAL(配置门控)** — Charlotte Agentic SOAR 客户自设自治级别、Torq Socrates safe auto-remediation;可逆动作可按配置自动执行 | **部分 YES(能力)/ NO(采纳)** — 闭环遏制能力已发,但**仅 30% 团队对低风险动作自动执行** | 不可逆/高 blast-radius 动作仍门控给人 |
| **9 升级 + case package** | **FULL** — 自动生成调查叙事,2025 已解 | **FULL** — 全平台 | **NO** | |
| **10 修复/工单** | **PARTIAL** — playbook 驱动 | **PARTIAL** — Torq、Cortex;跨团队修复判断仍人 | **NO** | |
| **11 高后果审批** | **NO** — 保留的人 | **NO** — 责任地板(accountability floor) | **NO** | 这就是留下来的那个人 |
| **12 威胁狩猎** | **PARTIAL(弱)** — agent 执行预定义狩猎 | **PARTIAL** — Charlotte/Exaforce agent 执行狩猎,多-agent 助力;新假设生成仍人主导 | **边际** — 执行改善,假设生成 NO | 对抗性:攻击者主动探 agent 盲点 |
| **13 检测工程/规则调优** | **PARTIAL** — agent 提议检测 | **PARTIAL** — Cortex AgentiX(训练于 12亿次 playbook 执行)提议;人验证 FP/FN 成本不对称 | **NO(增量)** | 上哪条检测=业务风险判断,非模式活 |
| **14 文档/合规报告** | **FULL** — 自动摘要 case notes | **FULL** — 全平台 | **NO** | |
| **15 交班 / CISO 汇报** | **PARTIAL** — 机器摘要 FULL;信任汇报人 | **PARTIAL** — 同前 | **NO** | 关系/信任汇报durable |

**加权技术可自动化 ≈ 72–78% 班次工时(~75% 中位)。** 但这是**能力,不是捕获**。套 pilot-to-production 折扣:<15% 企业 agent 部署到生产;绝大多数活跃 SOC 部署跑「supervised autonomy」——agent 分诊、人签 verdict(step 7/11);职业本身还在 **+21% 增长(BLS 2025–35)**。所以**真实耦合捕获 <1%**——~75% 能力 vs <1% 捕获这条鸿沟,就是整个 thesis。

---

## 四、2025→2026 的关键解锁点

这一节是本报告最有价值的部分:把9个月窗口讲清楚,并**诚实区分「真能力解锁」「分销解锁」「被宣传成解锁但没到生产」**。

### 4.1 真能力解锁(数量少,但真实)

**① 多-agent 协同调查(step 5 关联,部分 step 6 scope)——唯一干净的能力跨门槛。**
- **2025年底状态:** SOC agent 基本是**单域**的。CrowdStrike Charlotte「Agentic Response」(RSA-2025 发)是单次调查驱动;Palo Alto Cortex AgentiX 刚在 **Oct-28-2025** 发布,独立平台/XDR 支持要等「2026 早期」;跨 endpoint+identity+SaaS+cloud 的关联仍靠人把多个 agent 的输出缝起来。
- **2026年9月状态:** CrowdStrike **2026-09-02(Fal.Con)发下一代 Agentic SOC**——**首个协同多-agent 调查,跨 endpoint/identity/SaaS/cloud/network 同时进行**,建立**共享上下文层 / 跨 agent 持久记忆**,消除交接,多个 domain agent 在同一次调查里协作。Cortex AgentiX 独立平台+XDR 也已 GA。
- **是哪个能力让它跨门槛:** 底层是**模型推理自主时长的翻倍**(METR 50%-可靠时长:Opus 4.6 Feb ~14.5h → Sept ~32h,翻倍速度从 7 月加速到 4 月一次)+ 多-agent 编排 + 共享记忆架构。这让 step 5 从「PARTIAL-弱」升到「PARTIAL-强」,已知 kill-chain 的关联/时间线重建接近 FULL。
- **诚实边界:** 提升集中在**已知 kill-chain**;**新型多阶段入侵仍退化**(见第五节)。80%-可靠时长仍远短于 50% 的头条数字,所以「可靠地无监督跑一整场调查」还没到。

**② 闭环遏制的自治配置(step 8)——能力发了,采纳没跟上。**
- **2025年底:** 遏制多为「recommend-only」,自动执行罕见。
- **2026年9月:** Charlotte Agentic SOAR 支持**客户自设自治级别**,Torq Socrates 提供 **safe auto-remediation**;可逆动作(隔离、禁用、封 IOC)可按企业配置自动闭环。
- **但:** 这是**能力解锁,不是采纳解锁**——2026 调研 **仅 30% 团队对低风险动作自动执行**,57% 仍人工复核每个 verdict。

### 4.2 分销/捆绑解锁(数量多——而且**对创业公司是利空**)

这是9个月里最响的变化,但它**不是能力跨门槛,是护城河转移**:

- **Microsoft 把 Security Copilot 免费捆进 M365 E5**——Ignite Nov-2025 宣布,2025-11-18 开始滚动到 2026-06-30,自 2026-04-20 起 E5 免费(每 1000 个 E5 座席 400 SCU/月);Defender 里 phishing-triage agent GA(声称检出快 550%)。**零边际 CAC 把 agentic 分诊塞给已有 telemetry 的客户。**
- **Palo Alto Cortex AgentiX** 从 Oct-2025 的「仅 Cortex Cloud+XSIAM」扩到 2026 早期独立平台+XDR GA,声称 MTTR 降 98%、手工减 75%。
- **CrowdStrike** 从单域 Agentic Response(2025)→ AgentWorks 生态(Mar-25-2026)→ 协同多-agent SOC(Sep-2-2026),全程作为 **Falcon 平台原生功能**、训练于 Falcon Complete 分析师决策(EDR-telemetry 护城河,纯玩家无法复制)。

**投资含义:** 这些捆绑**收窄了纯玩家的可寻址市场**。当 agent 跑在 telemetry 平台**内部**,巨头以近零 CAC 捕获价值——~10–15% 的天花板大部分归 CrowdStrike/Palo Alto/Microsoft,不归独立 ARR。这正是价值捕获判断的核心机制。

### 4.3 被宣传成解锁、但其实没到生产(诚实清单)

- **「98% 分诊准确率 / 98% MTTR 降 / 550% 更快」**——全是**厂商受控演示/模拟场景**数,不是生产替代。硬证据反向:**Gartner Hype Cycle 市场渗透率在 2025 和 2026 两版都停在 1–5%**(2025-10-16 Gartner 才给品类命名「AI SOC Agents」为 Innovation Trigger;2026-06-05 升到 Peak of Inflated Expectations,但渗透率没动);**57% 人工复核每个 verdict、30% 才自动执行低风险动作**。产品发了,生产没动。
- **完全自主的漏报(false-negative)裁定**——**没解锁**,窗口里纹丝不动,仍是责任地板(见第五节)。
- **OT/ICS 自主 SOC**——**没解锁,而且结构上没关**。**Dragos OT Watch 明确是「人主导的 IR,不做实时自主执行」**;Claroty(2026-01-22 关 $150M F 轮)、Nozomi 加了 AI 检测但没加自主响应。OT 侧的白空间**没被这9个月填上**——这是 HTC 猎场的核心机会所在(第六节)。

**一句话时间线:** 9个月里,**真正跨门槛的只有「多-agent 协同调查」这一条能力**;最吵的变化是**分销捆绑,它伤创业公司**;而**硬门槛(裁定责任、OT 自主、漏报)全部没动**——Gartner 渗透率两年停在 1–5% 就是铁证。

---

## 五、仍然做不了的(2026年9月的硬门槛)

| 门槛(步骤) | 严重度 | 为什么撑得住 | 预计跨越 |
|---|---|---|---|
| **漏报 / 错过入侵的责任(step 7/11)** | **CRITICAL(信任+监管)** | 「这是良性」这个 verdict **不可机器验证**,错了灾难性;SEC 泄露披露、网络保险背书、DORA/NIS2 都要求**有名有姓的可问责人**。V=3 天花板。 | **2027 前不关** — 只随责任/保险框架开始接受 agent verdict 才松,是法律问题不是模型问题 |
| **telemetry 覆盖 / 行为基线缺口(step 6)** | **LARGE(技术)** | agent 只能分诊它看得见的;RSAC-2026 三家巨头都没补上 agent 行为基线;instrumentation 稀薄处自主 scope 不可靠,OT 尤甚 | IT 面 12–24 月;**OT 面结构性敞开**(第六节) |
| **高后果遏制权(step 8/11)** | **LARGE(物理/运营)** | 隔离医院 EHR 主机、跳 ICS 控制器有物理/安全 blast-radius;企业不会把不可逆动作交出去。OT 里一个错误遏制能停一台涡轮或一条产线 | 持久;仅在可逆动作类上侵蚀 |
| **新型/多阶段入侵推理(step 5/12)** | **MODERATE(技术,对抗性)** | agent 擅长已知 kill-chain,遇真正新型 tradecraft 退化;攻击者主动探 agent 盲点(E7「config-worm」需求尾风) | 跟随前沿推理;收窄但对手自适应,永不完全关 |
| **检测工程 FP/FN 成本判断(step 13)** | **MODERATE(信任)** | 上哪条检测=在告警疲劳与漏报风险间权衡,是业务风险判断非模式活 | 18–36 月;部分自动化+人签字 |

**durable 人力残余 ≈ 20–28% 工时,集中在最高后果、最低验证性的步骤**——正是「持照/可问责签字」类比所在。这正是 W1.8 是 **Mixed(压缩已配座席 + `[L]` 积压扩张)而非纯 Compression** 的原因。

---

## 六、投资读法

### 6.1 核心门:已关

**横向企业 SOC 分诊在种子/A 轮不可进入。** 7AI/Exaforce/Torq 已在 A/B/D 轮、$700M–$1.2B 估值(**7AI $130M A / 总 $166M / $700M,Index 领投,Dec-2025**;**Exaforce $125M B / 总 $200M / $725M,May-2026**;**Torq $332M 总 / $1.2B**;Dropzone $37M B,2026-06 撤下公开定价);telemetry 巨头 RSAC-2026 全都发了捆绑 agentic 分诊;**Radiant Security→Cribl(资产/IP 收购,2026-08-19)是 NHI-模式退出的正在兑现的 base case**。**不要投横向「AI SOC 分析师」——它唯一的护城河是「客户 SIEM/EDR 上的一个 agent」,而这护城河会流向拥有 telemetry 的巨头。**

### 6.2 可下注的种子/A wedge(巨头 EDR/SIEM-telemetry 护城河**不迁移**的三处)

**(a) OT/ICS-SOC —— HTC 强制猎的方向,也是唯一最干净的不迁移。**
- IT-SOC agent 训练于 IT telemetry(Falcon、Sentinel),这护城河**跨不进**工业协议(Modbus、DNP3、S7)、气隙/后果驱动环境、安全仪表系统(SIS)。
- **但必须门控这张支票的 nuance:** OT-**可见性**巨头已握 OT telemetry——**Dragos(OT Watch)、Claroty($150M F, Jan-2026)、Nozomi、Armis**——并在加 agentic 层。所以这是**给新纯玩家的真白空间,只在护城河是「OT-协议原生检测工程数据 + 后果/安全管理(IT agent 做不了的物理 blast-radius 判断)」时成立**,不是「把 IT SOC agent 指向 OT」。
- **阶段/估值:** 种子 / pre-A,**~$8–30M post**。承保:OT-协议原生检测深度 + 后果管理(物理安全)问责层 + 资产所有者设计伙伴(公用事业/制造/油气)。
- **要打败的对手是 OT 可见性巨头(Dragos/Claroty),不是 CrowdStrike**——把护城河尺寸对着它们量。当前唯一点名的 agentic-OT-SOC 进入者 Shieldworkz(利雅得,2024)很薄/几乎无融资——白空间是真的,执行是问题。

**(b) DFIR / 事件响应与取证自动化。**
- 护城河 = 取证 chain-of-custody + 法庭/保险可采信的证据处理——一个 durable 的人签字残余(类比持照背书),IT-SOC agent 不碰。
- **Cydelphi**(AI-native DFIR,**$3M 种子,2026-02-12,Glasswing 领投**,声称把勒索恢复成本/时间平均砍 75%)是唯一钉住的纯玩家;传统玩家(Magnet Forensics)是 legacy。**阶段:种子 <$15M post。**

**(c) Agent-native 中端 / SMB MDR,作为劳动力交付(把 `[L]` 积压货币化)。**
- 把从没配过人的告警积压当 service-as-software 卖给从没有过 SOC 的公司。**AirMDR($15.5M)、Conifers($25M,MSSP-原生多-agent mesh)、Qevlar($30M,MSSP+F500)** 是种子/A 梯队。
- **阶段:~$15–40M post——但承保 retained ARR / NDR,不是 bookings;Radiant→Cribl 是收购退出的 base case,这是 build-to-flip 不是 build-to-independence。**

### 6.3 该避开什么

1. **横向企业 SOC 分诊**(价已过种子门、被巨头殖民)。
2. **任何护城河=「客户 SIEM/EDR 上的 agent」的纯玩家**(护城河流向 telemetry 所有者)。
3. **agent-安全/治理/NHI 基础设施**(Zenity/Obsidian/Astrix)——那是并行 `[$]` 软件-TAM 台账不是劳动力赛道,且敌对(Agent 365 / ServiceNow Control Tower 殖民、NHI 被收购出局:Astrix→Cisco、Oasis→Cyera)。
4. **座席/copilot 定价**——不是 per-investigation 就是增强产品,巨头发原生后续约被砍。

### 6.4 三条带日期的证伪信号(到 2027Q4)

1. **独立捕获 vs 功能化(核心 resolver)。** 到 Q4-2027,是否 ≥1 纯玩家(7AI/Exaforce/Torq/Dropzone)披露 **≥$100M 已验证 ARR、NRR >120%、且保持独立**?**BULL → 独立劳动力捕获成立。** **BEAR / 功能化(base case,给定 RSAC-2026 出货 + Radiant→Cribl):品类以 <$1.5B 收进巨头(NHI 模式:Astrix→Cisco、Oasis→Cyera),或 CrowdStrike/Palo Alto/Microsoft 披露的自主分诊 attach 明显封住纯玩家净新增企业 logo。**
2. **OT-SOC 护城河不迁移(HTC 猎场 resolver)。** 到 Q4-2027,是否有 **OT/ICS-协议原生自主 SOC 纯玩家、以 OT-原生检测+后果管理募到 >$40M 定价 A 轮、且未被 Dragos/Claroty/Nozomi 收购**?**YES → OT 护城河真不迁移,值得现在写种子票。** **NO → OT 可见性巨头把 agentic SOC 吸进平台(OT 侧护城河也守住),wedge 关闭,这票不该写。**
3. **耦合方向 / 职业轨迹(Mixed vs Compression)。** 到 2027-05(及 2028)BLS OEWS,信息安全分析师就业(基 ~193k)是否**沿 +21% 路径持平-向上、且 per-investigation 定价压过 per-seat**?**→ 确认 Mixed/Expansion**(短缺掩盖、`[L]` 积压被吸收、职业增长——耦合但非 Compression 的 base case)。**若 infosec-analyst 人头同比下降 且 MSSP/BPO tier-1 SOC 座席收缩 → 替代终于可见;把 W1.8 翻向 Compression、提升替代 conviction。**

---

### 给投委会的底线

W1.8 有数字盘面最高的原始可自动化占比(~75%)和真实短缺的政治掩护——但**真实耦合捕获 <1%**,~10–15% 的天花板正被 telemetry 巨头当捆绑功能拿走(Charlotte 在本报告前一天刚发下一代 SOC),纯玩家退出已以 sub-$1.5B 收购兑现(Radiant→Cribl)。**Gartner 渗透率两年停在 1–5%,57% 团队仍人工复核每个 verdict——产品发了、生产没动。** 9个月窗口的真能力解锁只有一条(多-agent 协同调查);其余的响动是分销捆绑,对创业公司是利空。**可投面不是 SOC agent 本身,是三个护城河不迁移的邻区——OT/ICS-SOC(现在猎,~$8–30M,打 Dragos/Claroty 不是 CrowdStrike)、DFIR(Cydelphi 类,种子)、中端 MDR-as-labor(build-to-flip,承保 NDR)。** 其余要么被巨头捕获,要么是 `[$]` 基础设施台账的伪装。

---

**主要来源(2026-09-03 网络核实):** CrowdStrike 下一代 Agentic SOC(2026-09-02, Fal.Con)· Charlotte Agentic Response(RSA-2025)/ AgentWorks(2026-03-25)· Palo Alto Cortex AgentiX(2025-10-28,标准平台+XDR 2026 早期 GA)· Microsoft Security Copilot 入 E5(Ignite Nov-2025 宣布,2025-11-18→2026-06-30 滚动,2026-04-20 起免费,phishing-triage GA)· Gartner「AI SOC Agents」品类命名(2025-10-16, Innovation Trigger)→ Hype Cycle 2026-06-05(Peak, 1–5% 渗透)· 7AI $130M A(Index, Dec-2025, 总 $166M / $700M)· Exaforce $125M B(May-2026, 总 $200M / $725M)· Dropzone ~$9/investigation、$37M B、2026-06 撤价 · Torq $1.2B / Socrates · Cribl 收购 Radiant Security AI-SOC IP(2026-08-19)· Claroty $150M F(2026-01-22)· Dragos OT Watch(人主导 IR,非自主执行)· Cydelphi DFIR $3M 种子(Glasswing, 2026-02-12)· RSAC-2026 agent 行为基线缺口(VentureBeat)· 2026 调研:57% 人工复核每 verdict / 30% 自动执行低风险 · ISC2 2025 工作力研究(16,029 人,史上首次不发缺口数,59% 关键技能缺口 +15pp)· BLS 15-1212 信息安全分析师 ~193k / $129,180 / +21% · METR 自主时长 14.5h(Opus 4.6, Feb)→32h(Sept)。**内部:** p0_foundation(耦合规则、pilot-to-production 折扣、模型锚)、p3_frozen_taxonomy(W1.8 行、E1/C3 裁定、猎场排名)、p5_deepdives(W1.8 Sept-2026 能力底稿)。

---

I have a complete, web-verified evidence base. Writing the report now as my return value (per harness constraints — delivered as text, not a separate `.md` file, matching the existing deep-dive pattern in the file).

---

# W1.5 — 财报与合规申报 / XBRL 溯源（Financial Reporting & Regulatory Filing）
## v2 深研 · HTC 内部 · 2026-09-03 · Fable-5 时代 · HTC 猎场 #3

**冻结行:** `W1.5 · Financial Reporting & Regulatory Filing (XBRL, trace-to-source) · $100–200B [W] · V4/H3/P0/R4/L3/D4 · Coupled · Net=Compression · Conv=Med · Tier B ·⚑hunt`

**一句话论点:** 这是 map 上**唯一「blocked-but-adjacent」的白点**——能力早已就位(不是模型瓶颈),真正的墙是 **SOX/高管签字责任(R=4)**。但过去 9 个月窗口里,这个白点**正被 incumbent 从两侧填平**:DFIN 的 AI-iXBRL(2026-06)与 Workiva 的 tie-out / examiner-ready-narrative 智能体(Q2-26)恰好是冻结板上写的「内部化 falsifier」,它**已经开火**。护城河(officer-certification)在 2026 年不但没软化,反而随 **SEC 于 2026-03-31 成立专职 SOX 执法组**而**硬化**。结论:横向「AI 10-K/XBRL 起草器」的种子门**已基本关闭**;真正剩下的 HTC 可下注面,是**监管护城河不迁移的两条窄缝**——(1)FDTA(2026-10 生效)开出的**非 SEC 结构化监管报送新面**;(2)**认证证据/溯源审计链基础设施**。相较冻结板,本篇把 W1.5 的 conviction 进一步**下调**:窗口正在关闭,不是打开。

---

## 一、这是什么 + 为什么是早期猎场

### 定义
W1.5 是**公司对外财务报告与法定/监管申报的端到端生产工作**——从「已结账的试算表」出发,产出并报送**经审计/受监管的对外财务信息**:美股发行人的 10-K/10-Q/8-K、iXBRL 结构化数据、SOX 302/404 认证包;以及银行的 Call Report/FR Y-9C、保险的 NAIC 法定报表、基金的 N-CSR/N-PORT、(在范围内的)CSRD/ESRS 可持续报告。核心动作串是**起草 → 溯源勾稽(trace-to-source) → XBRL 结构化 → 审计对接 → 高管签字 → 报送**。

**对应岗位(美国 BLS 锚):**
- Accountants & Auditors(SOC 13-2011)≈ **160 万人**(2025),median $83,680,其中对外/法定报告条线约占 10–15%。
- Financial Managers / Controllers(SOC 11-3031)≈ **879,700 人**,median $166,570;其中 SEC/财报条线的 controller、technical-accounting、财报经理是核心。
- 加上 filing agent(Workiva/DFIN/Toppan Merrill/DataTracks)与银行/险企/基金内部的 **XBRL 与法定报送专才**。

### 边界(不包括什么)——防止与相邻 track 重复计数
- **不含**日常记账/AP/AR/结账机械(那是 W1.3 月结、W1.4);W1.5 从**已结账试算表**开始。
- **不含**外部审计与鉴证(那是 W4.1——审计师那一侧;本篇只含发行人「配合审计」的动作)。
- **不含**报税申报本身(W4.2);但流入财报的 **ASC 740 所得税拨备**在范围内。
- **不含** IR 叙事策略/盈利电话、FP&A 预算预测(W2 判断型)。

### 劳动盘子(Labor TAM)= $100–200B `[W]`(冻结值,本篇维持)
**依据(自下而上,美元加权):** 美国对外报告条线 ≈(会计师中 ~16–24 万 + 财报口 controller/经理 ~10–15 万 + XBRL/法定报送专才)× loaded comp $120–200k ≈ **$60–100B**;发达经济体加权(欧/日/英法定报送 + iXBRL/ESEF)≈ **$100–200B**。这是**会计大职业里的一个楔子**(不是全部会计),按美元加权后落在冻结带内。**注意 R2(劳动数据优先于 VC 叙事):** 该职业 2025–35 预计 accountants +5%、financial managers +10% ——**盘子在温和增长,不是萎缩**,这本身就压低「Compression 已发生」的先验(见第五节)。

### 为什么值得 HTC 下种子/A 轮(以及为什么要非常克制)
1. **能力已就位,门是法律不是模型**——这是 map 上少见的「blocked-but-adjacent」结构:白点旁边就是被重金 funding 的财务后台集群(Basis $1.15B、Ramp、Digits、BlackLine),但**没有一个 sweep 钉到过一个「申报/XBRL 智能体 pure-play」**。
2. **护城河可被 startup 拥有**:officer-certification 责任 → 需要**审计可辩护的溯源链**,这是文档工具不自带的合规滩头。
3. **但——窗口正在关闭**(这是本篇对冻结板的核心修正):DFIN(2026-06)与 Workiva(2026 Q2)已经在**内部化**这块楔子,财务后台集群也在**向上延伸到报告层**。横向门口的价格已经被 incumbent 而非 startup 占据。所以「值得下注」只在**两条护城河不迁移的窄缝**成立,横向叙事应当回避。

---

## 二、工作步骤全拆解(22 步 / 6 阶段)

占工时 % 为对外报告条线一个申报周期的时间加权。

| # | 阶段 / 步骤 | ~% 工时 |
|---|---|---:|
| | **A. 结账交接与合并**(~15%) | |
| 1 | 汇总各主体已结账试算表、校验结账完整性与调整分录 | 4% |
| 2 | 多主体合并、内部交易抵销、外币折算 | 6% |
| 3 | 报表模型 roll-forward:试算表映射到财报行项目 | 5% |
| | **B. 财报与披露起草**(~26%) | |
| 4 | 起草四张主表(资产负债 / 利润 / 现金流 / 权益) | 5% |
| 5 | 起草附注 / 披露(债务、租赁、收入、分部、所得税、承诺或有) | 9% |
| 6 | 起草 MD&A / 管理层叙述 + 逐项变动分析 | 6% |
| 7 | Non-GAAP 指标、调节表、KPI 表 | 3% |
| 8 | 复杂 / 判断性事项技术会计备忘(收入、企业合并、减值、诉讼准备) | 3% |
| | **C. 溯源勾稽、支撑底稿与内部复核**(~20%) | |
| 9 | **Tie-out 勾稽:每个数字溯源到底稿 / 子账 / 上期(trace-to-source 核心)** | 7% |
| 10 | 支撑底稿装订 + 披露检查表(disclosure checklist) | 5% |
| 11 | 内部复核循环(controller / 技术会计 / **披露委员会**) | 5% |
| 12 | 法务 / IR / 高管复核与意见回填 | 3% |
| | **D. XBRL / iXBRL 结构化**(~14%) | |
| 13 | XBRL/iXBRL 打标:每个 fact 映射 US-GAAP/DEI 分类元素(标准元素) | 6% |
| 14 | 扩展元素、自定义轴 / 成员、计算 / 定义 linkbase | 4% |
| 15 | XBRL 校验(SEC EFM、DQC 质量规则)+ 对标同业标签复核 | 4% |
| | **E. 审计对接与高管签字**(~15%) | |
| 16 | 审计 PBC 支持 / 审计请求满足 / 审计答辩 | 5% |
| 17 | ICFR(SOX 404)文档、控制证据、管理层有效性评估 | 4% |
| 18 | 披露控制程序 + CEO/CFO 分级 sub-certification 链 | 2% |
| 19 | **高管签字认证(SOX 302/906)——CEO/CFO 本人签字** | 1% |
| | **F. 报送与报送后**(~10%) | |
| 20 | EDGAR 组包与报送(filing agent / EDGAR Next 权限委派) | 4% |
| 21 | 非 SEC 监管报送(银行 Call Report/FR Y-9C、保险 NAIC、基金 N-CSR/N-PORT、CSRD) | 4% |
| 22 | 报送后:SEC comment-letter 回复、更正 / 重述、下期模型 setup | 2% |

**结构要点:** 真正「写字」的起草只占 ~26%;**溯源勾稽(20%)+ XBRL 结构化(14%)+ 审计对接与签字(15%)= 49%** 的工时是**可验证、可结构化、但责任负重**的动作——恰恰是能力高、但被 R=4 卡住变现的地带。这就是 W1.5「能力就位、门是签字」的机械原因。

---

## 三、逐步 AI 能力评估(核心表)

**判据:** FULL = agent 在标准路径上无监督完成;PARTIAL = agent 起草/决策、人负责例外或签字;NO = 仍纯人工。基于真实 2026 产品与模型,不拍脑袋。**模型锚:** Fable 5 / Mythos 5(Anthropic,2026-06-09,长文档财务推理 ~90.34% FinanceReasoning-hard)、GPT-5.6 Sol(~90.34–90.76%)——2026 年模型层在长财务文档推理上跨过 ~90% 门槛。

| # | 步骤 | 2025 年底能力 | 2026 年 9 月能力(+ 具体工具/产品) | 9 个月解锁? | 备注 |
|---|---|---|---|:--:|---|
| 1 | 汇总试算表/校验结账 | PARTIAL — 结账工具+规则,多源需人 | **FULL** — Ramp Accounting Agent 实时结账(Feb-26)、BlackLine Studio360、Numeric/FloQast | 部分 YES | 实时结账把「等结账」压缩;非标调整仍需人 |
| 2 | 合并/抵销/折算 | PARTIAL(标准 ERP 确定性;复杂主体需人) | **FULL(标准)/PARTIAL(复杂)** — Rillet AI-native ERP、BlackLine、SAP/Oracle | NO | ERP 早已确定性求解;AI 边际,非解锁 |
| 3 | Roll-forward 映射 | PARTIAL — 模板 roll-forward | **FULL** — Workiva AI roll-forward、IRIS CARBON AI roll-forwards | 部分 YES | 减少重工,但映射逻辑确定性为主 |
| 4 | 起草主表 | PARTIAL — connected reporting 模板 | **FULL** — Workiva connected reporting;从映射后 TB 确定性生成 | NO | 模板早已解决 |
| 5 | 起草附注/披露 | PARTIAL — 嵌入式 genAI 起草,一致性/引用弱 | **FULL(通用附注)/PARTIAL(判断项)** — **BlackLine Footnote Generator(Apr-26)**、**Workiva Knowledge「与上期一致的披露 + 可供检查的 audit trail」(Q2-26)**、Fable 5 长文档 | **YES** | **关键解锁**:脚注首稿 + 「prior-filing-consistent」叙述 2026 年才产品化 |
| 6 | MD&A/叙述+变动分析 | PARTIAL — genAI 首稿,通用泛化 | **PARTIAL→FULL(首稿)** — **BlackLine Variance Automation(变动首稿解释)**、Workiva narrative agent、Fable5/GPT-5.6 | YES(变动自动解释) | 前瞻性陈述/口径判断仍人;SEC 对 MD&A 高度审阅 |
| 7 | Non-GAAP/调节/KPI | PARTIAL | **FULL(计算)/PARTIAL(选哪个口径)** | 部分 | 计算确定;「披露哪个 non-GAAP」是判断+SEC 审阅高发区 |
| 8 | 复杂技术会计备忘 | NO/PARTIAL — 检索式草稿 | **PARTIAL** — Fable5/GPT-5.6(90% FinanceReasoning)、Trullion(ASC 606)、检索起草 | YES(推理跃升)但未到生产判断 | 会计判断 + 签字仍人;错判=重述风险 |
| 9 | **Tie-out 勾稽/溯源** | PARTIAL — 人工为主 + 少量自动 | **FULL(源数字化时)** — **Workiva tie-out agent(Q2-26)**、Trullion trace-to-source、Black Ore 工作底稿逐点回链 | **YES** | **本 track 的旗舰解锁**:审计可辩护的自动勾稽 2026 才成为产品 |
| 10 | 支撑底稿+披露检查表 | PARTIAL | **FULL** — 披露检查表自动化、底稿装订 agent | 部分 | 结构化任务 |
| 11 | 内部复核循环 | NO — 人治理 | **PARTIAL** — AI 一致性/异常标记;**披露委员会判断+问责仍人** | NO | 治理与问责,非能力问题 |
| 12 | 法务/IR/高管复核回填 | PARTIAL | **PARTIAL** — 意见机械回填 FULL;复核判断人 | 部分 | — |
| 13 | XBRL/iXBRL 打标(标准元素) | PARTIAL — ML 自动打标(IRIS CARBON),重人工复核;**无 genAI 标签建议** | **FULL(标准)** — **DFIN AI-iXBRL 标签生成+校验(Jun-26)**、IRIS CARBON 边写边打标、Workiva 校验 | **YES** | **最清晰的解锁**:genAI 打标 2026 年由 incumbent 落地(2025 末还只有规则/ML) |
| 14 | 扩展元素/自定义轴/linkbase | NO/PARTIAL | **PARTIAL** — AI 辅助,扩展元素+calc linkbase 需人 | 部分 | 错标=SEC comment/重述,false-negative 不可机检 |
| 15 | XBRL 校验+对标复核 | PARTIAL — 规则 EFM/DQC 已强 | **FULL** — **Workiva 异常/同业 benchmarking agent(Q2-26)**、DQC | YES(对标 agent) | 校验早已强;AI 离群检测为新增 |
| 16 | 审计 PBC 支持/答辩 | PARTIAL | **PARTIAL** — 证据抽取/请求满足 FULL;审计答辩判断人;**审计师侧(W4.1)受门** | 部分 | — |
| 17 | ICFR(SOX404)文档/评估 | PARTIAL(文档)/NO(评估) | **PARTIAL** — 控制证据采集自动;**ICFR 有效性评估+控制归属=人**;PCAOB QC1000(Dec-26)、SEC SOX 执法组(Mar-26)在硬化 | NO | 问责地板 |
| 18 | 披露控制+分级 sub-cert 链 | NO | **NO/PARTIAL** — 认证链是人的问责结构 | NO | — |
| 19 | **高管签字认证(SOX302/906)** | **NO** | **NO** — CEO/CFO 个人**刑事**责任;SEC SOX 执法组(Mar-26)**硬化** | **NO** | **永不随能力曲线关闭**——这是护城河 |
| 20 | EDGAR 组包与报送 | PARTIAL — filing agent 自动化 | **FULL** — EDGAR Next API + filing agent;确定性 | 部分 | EDGAR Next(2026)改访问模型;结构化数据错误自 Mar-16-26 起**直接 suspend** |
| 21 | 非 SEC 监管报送(Call Report/NAIC/N-CSR/CSRD) | PARTIAL — Regnology/Wolters Kluwer 传统自动化 | **PARTIAL** — **DFIN AI-iXBRL 先上 N-CSR/TSR(Jun-26)**;**FDTA 新增结构化面(Oct-26 生效)** | YES(部分) | **新面**:FDTA 把机读报送扩到 9 家监管机构 |
| 22 | 报送后(comment/更正/下期) | PARTIAL | **PARTIAL** — V7 Go 披露分析、comment-letter 起草辅助;重述判断人 | 部分 | — |

**加权技术可自动化 ≈ 55–62% 工时**(FULL ~30pp + 半计 PARTIAL ~28pp)。**但这是能力,不是变现。** 套用两道强制折扣:
- **管道可靠性衰减 + pilot-to-production**(MIT NANDA 95% 零 P&L、S&P 42% 放弃):真正在生产中无监督跑通的**端到端申报 ≈ 0**——因为链条终点是不可机检的 officer-certification。
- **耦合口径(capture-rate × displaced-labor,永不 SW+labor):** 今天绝大多数变现是**按 seat/订阅计价、骑在仍在岗的报告团队上的 augmentation**(Workiva $255M/季订阅 +19%,但横跨 SEC+ESG+审计+GRC,W1.5 申报切片只占其一部分)。**真正耦合、减头的 realized capture < 0.5–1%。**

---

## 四、2025→2026 的关键解锁点(报告最有价值的部分)

这 9 个月里,**四步从「做不了/半自动」跨到「标准路径可自动」**——但**跨门的是 incumbent 和模型,不是新 startup**,这是投资读法的全部要害。

**真解锁(已进生产或受控生产):**

1. **XBRL/iXBRL 打标从「规则/ML+重人工」→「genAI 标签生成」(步骤 13)。** 2025 末:IRIS CARBON 有 ML 模式匹配自动打标,但 **Workiva 到 2026-04 仍无 genAI 标签建议(只做校验)**。2026-06-10:**DFIN 推出 AI-iXBRL 标签生成+校验**(先上 TSR/N-CSR,受控生产 pilot,H2-26 扩到 ActiveDisclosure;私有云、SOC2/ISO27001、不用客户数据训第三方模型)。**这是把 map 上「无人钉到的 XBRL 楔子」由 incumbent 直接内部化的时刻。**

2. **溯源勾稽 tie-out 产品化(步骤 9)。** 2026 Q2:**Workiva 发布 tie-out agent + benchmarking agent + Workiva Knowledge**,明确指向「生成与上期一致的披露、产出**examiner-ready、带完整 audit trail** 的叙述」。这正是 W1.5 论点里「trace-to-source + 审计可辩护」的**滩头**——被 incumbent 抢先占。配套的源侧溯源(Trullion 的 ASC 606/842 逐点回源、Black Ore Tax Autopilot 每个数据点回链底稿,broad availability Apr-26)也已成熟。

3. **脚注与变动分析首稿生成(步骤 5、6)。** 2026-04:**BlackLine Variance Automation & Footnote Generator**(变动解释与脚注首稿)+ Agentic Financial Operations / Studio360。财务后台集群从「结账」向上延伸到「报告层」的证据。

4. **模型层长文档财务推理跨 ~90%(步骤 5/6/8/22)。** **Fable 5(2026-06-09)**定位「文档密集型分析」,与 GPT-5.6 Sol 在 FinanceReasoning-hard 上并列 ~90.34%(GPT-5.6 Sol Pro 90.76%)。这把附注/MD&A 起草、技术会计检索、comment-letter 起草的**首稿质量**抬到可用线。

5. **需求面扩张(不是能力,但改变盘子形状):**
 - **FDTA 联合最终规则 2026-06-09 发布、2026-10-01 生效**,各机构专项规则 2 年内落地,把机读/结构化(XBRL 族)报送扩到 **9 家监管机构(OCC/Fed/FDIC/NCUA/CFPB/FHFA/CFTC/SEC/Treasury)**——为**非 SEC 结构化报送**开出全新面(见第六节窄缝 1)。
 - **EDGAR Next**(用户级授权、委派报送)2026 上线;**结构化数据错误自 2026-03-16 起直接 suspend**(不再仅警告)——结构化准确性变成硬门,抬高工具价值。

**被宣传成解锁、但其实没到生产的(诚实清单):**

- **「AI 全自动出 10-K」**——没有。附注/MD&A 首稿是 FULL,但**披露决策(materiality、going-concern、subsequent events、分部、non-GAAP 口径)仍 PARTIAL/NO**,且 SEC 审阅高发。
- **「XBRL 全自动打标」**——只到**标准元素 FULL**;**扩展元素/自定义轴/calc linkbase 仍需人复核**,错标 false-negative 不可机检,直接对应 SEC comment / 重述。DFIN 明确是「AI + expert human oversight」「controlled production pilot」,不是无人。
- **「ICFR/SOX 自动化」**——控制**证据采集**可自动,但**有效性评估与控制归属**是人;2026 年方向是**收紧**(PCAOB QC1000 Dec-26、SEC SOX 执法组 Mar-26、404 审计新增 AI 提问),不是放松。
- **CSRD/ESRS 的 XBRL 打标 TAM**——被 **Omnibus I(Directive (EU) 2026/470,2026-03-18 生效)暂停**(在 ESEF 更新前不强制标可持续部分),范围亦被抬高门槛缩小(>1,000 人 & >€450M)。这块「解锁」是**萎缩**,与冻结板 W4.8 读一致——不要把 ESG 打标当增长面。

---

## 五、仍然做不了的(2026 年 9 月的硬门槛)

| 门槛 | 严重度 | 为什么撑得住 | 预计跨过 |
|---|---|---|---|
| **1. 高管签字认证(SOX 302/906,步骤 19)** | **CRITICAL(监管签字)** | CEO/CFO 承担**个人刑事**责任;agent 不能做可问责的签字人。**2026 年在硬化:SEC 2026-03-31 成立专职 SOX 执法组,officer-cert 造假持续产生九位数和解。** | **不随能力曲线关闭。** 只会在「AI 辅助认证安全港」被 SEC/PCAOB 定义后才软化——这是法律/责任问题,不是模型问题。**这是护城河本身。** |
| **2. ICFR(SOX 404)设计与有效性签字(步骤 17/18)** | **LARGE(监管/问责)** | 必须有可问责的人拥有控制;大加速申报人还需审计师按 AS 2201 单独 attest。PCAOB QC1000(2026-12-15 生效)进一步压实事务所质控。 | 3–5 年逐步定义「有意义的人工复核」;高级签字层是**持久残余**(像编码的资深层)。 |
| **3. 披露判断与重大性(步骤 5/6/7/8/11)** | **LARGE(判断+责任)** | 披露什么、going-concern、subsequent events、诉讼准备、分部、non-GAAP 口径——低可验证性、高责任美元,恰是 SEC comment / 重述高发区。 | 部分 2–3 年;最高责任尾部长期留人。 |
| **4. XBRL 扩展元素/自定义轴/linkbase 终选(步骤 14)** | **MODERATE→LARGE(可靠性)** | 错标 false-negative 不可机检,直接触发 SEC comment letter 与结构化数据 suspend(Mar-26 起)。DFIN/Workiva 均保留人工复核。 | 标准元素已 FULL;扩展元素随分类法工具化 1–2 年逐步收窄,但复核残余持久。 |
| **5. 审计师侧鉴证(步骤 16 的对侧,W4.1)** | **LARGE(监管)** | 发行人配合审计可自动,但**审计意见与鉴证**受 R=5 门(Big-4 内部化、PCAOB),外部 startup 变现≈0。 | 见 W4.1;不在 W1.5 变现面内。 |

**约束是 R=4/R=5(签字与鉴证),不是模型能力。** 按 P3 白点纪律:**跟踪「门」的移动**(SEC SOX 执法组动作、PCAOB QC1000、AI-认证安全港是否出现、FDTA 各机构专项规则),而不是模型。

---

## 六、投资读法

### 可下注的种子/A 轮 wedge——只在护城河不迁移处

**横向门:关闭中(明说)。** 横向「AI 10-K 起草器 / XBRL 打标 copilot」在种子/A **不可入**:Workiva(Q2-26 tie-out/benchmarking/Knowledge agent,$255M/季 +19%,>$500k 合同 +33%)与 DFIN(AI-iXBRL,Jun-26)已内部化;财务后台集群(Basis $1.15B、Ramp Accounting Agent、BlackLine Footnote Generator)从结账向上延伸。**冻结板已把 conviction「下调、窗口关闭」——本篇确认横向门已基本关上。**

**护城河不迁移的两条窄缝(可下注,须克制):**

1. **FDTA 驱动的非 SEC 结构化监管报送(最高信念的新面)。** FDTA(2026-10 生效,2 年内各机构落地)把机读报送扩到 9 家监管机构——**银行 Call Report/FR Y-9C、信用社、保险 NAIC 法定报表、券商 FOCUS**。Workiva/DFIN 是 **SEC 倾斜**的,这块长尾的 incumbent 是**传统 reg-reporting 厂商(Regnology、Wolters Kluwer/AxiomSL、Vermeg)**,AI-native 覆盖薄。**阶段/估值:种子 ~$10–25M post(参考 2026 AI 种子 median pre ~$17.9M)。护城河=分类法-原生的结构化报送数据 + 监管导航;要打的是 Regnology/Wolters Kluwer,不是 Workiva。**

2. **认证证据 / 溯源审计链基础设施(护城河本身的变现)。** 让自主起草**审计可辩护**、支撑 officer-certification 的**trace-to-source + 认证证据层**——冻结论点里点名的「certification workflow」。这是文档工具不自带的合规滩头。**但 Workiva Knowledge(audit trail)+ tie-out agent(Q2-26)正在殖民**,所以只在**它够不到的深度**成立:多主体/跨司法辖区法定合并、pre-IPO/私有公司复杂法定报送(IFRS/本地 GAAP),即 SEC-filer 数量线之下、Workiva 太贵的层。**阶段:种子 ~$8–20M post。**

### 该避开什么
- **横向「AI 10-K/披露 起草器」与「XBRL 打标 copilot」**——Workiva/DFIN 已内部化,thin agent 无护城河。
- **任何用 Workiva 收入当「displacement」定盘子**的读法——那是横跨多品类的 **augmentation seat ARR**,不是耦合减头。
- **ESG/CSRD XBRL 打标**——被 Omnibus I 暂停 + 缩小范围,萎缩面。
- **EDGAR 之上的薄壳报送 agent**——filing agent(Toppan Merrill/DataTracks)+ EDGAR Next 已确定性覆盖。
- **只被 seat/copilot 定价、无 per-filing/per-outcome 口径**的产品——续约时被 incumbent 挤。

### 3 条带日期的证伪信号(到 2027Q4)

1. **内部化 = 基准情形(BEAR,对 startup)。** 到 **2027Q4**,若 **Workiva Knowledge/tie-out + DFIN ActiveDisclosure AI-iXBRL 达成规模化生产**(premium tier 普遍 attach、DFIN AI-iXBRL GA),**且无独立 XBRL/申报 pure-play 跨 ~$50M ARR 且未被收购** → 横向楔子已归 incumbent,**不写横向支票**(这是当前最可能路径)。

2. **FDTA 新面 resolver(窄缝 1 是否成立)。** 到 **2027Q4**,是否有**独立的结构化监管报送 agent**在 **FDTA 驱动的非 SEC(银行/保险法定)报送**上完成一轮定价 Series A,**且未被 Regnology/Wolters Kluwer/Workiva 收购** → **YES:护城河确不迁移,种子支票属于这条缝;NO:传统 reg-reporting incumbent 把它吸收,缝关闭。** (跟踪 FDTA 各机构专项规则 2026–28 落地节奏。)

3. **门的移动 = 护城河耐久度(officer-cert)。** 到 **2027Q4**(并盯 PCAOB QC1000 Dec-26 生效 + SEC SOX 执法组动作),SEC/PCAOB 是否**定义任何「AI 辅助认证安全港」或接受 agent 生成的 ICFR 证据**? **若签字责任继续硬化**(更多执法、无安全港)→ 护城河耐久,价值归**拥有审计可辩护溯源链的一方**(偏认证证据基础设施,窄缝 2);**若软化**→ 自主申报加速,但 incumbent 内部化同样加速——对 startup 反而更不利。

**(佐证/劳动 confirm:** 2027-05 BLS OEWS——accountants & auditors(SOC 13-2011,~160 万)与 financial managers(~88 万)。若**持平至上行**(基准,+5%/+10% 预测)→ 压缩是慢磨/augmentation,realized 耦合 capture 持续 **<1%**,确认「secular grind、非 step-change」。)

---

**分析师底线(供 IC):** W1.5 是 map 上唯一「blocked-but-adjacent」的白点——能力 2026 年已越过标准路径线(DFIN AI-iXBRL 打标、Workiva tie-out/examiner-ready 叙述、BlackLine 脚注生成、Fable5/GPT-5.6 长文档推理 ~90%),**但跨门的是 incumbent 与模型,不是新 startup**。护城河(SOX/officer-certification,R=4)在 2026 年**硬化**(SEC SOX 执法组 Mar-26、PCAOB QC1000 Dec-26),这既是墙、也是可拥有的护城河。冻结板把它列为猎场 #3、conviction「下调、窗口关闭」——**本篇确认横向门已基本关上**:realized 耦合 capture <0.5–1%(vs $100–200B 盘子),绝大多数是骑在在岗团队上的 augmentation seat ARR。**HTC 唯一活着的入口是两条护城河不迁移的窄缝——FDTA 开出的非 SEC 结构化报送新面(打 Regnology/Wolters Kluwer,不是 Workiva)、与认证证据/溯源审计链基础设施(在 Workiva Knowledge 够不到的私有/跨辖区法定深度)。** 横向的一切,要么已被 incumnbent 内部化,要么是伪装成 displacement 的 augmentation seat ARR。

---

**来源(2026-09-03 web 核实):** [DFIN AI-iXBRL Tagging, Jun-10-2026 — PRNewswire](https://www.prnewswire.com/news-releases/dfin-introduces-ai-powered-ixbrl-tagging-for-sec-filings-delivering-breakthrough-speed-accuracy-and-control-for-regulatory-compliance-302795797.html) · [Workiva Q2-2026 结果与 AI agents(tie-out/benchmarking/Knowledge)— investor.workiva.com](https://investor.workiva.com/news-releases/news-release-details/workiva-announces-second-quarter-2026-financial-results) · [Workiva XBRL/iXBRL solution](https://www.workiva.com/solutions/xbrl-and-ixbrl) · [BlackLine Agentic Financial Operations / Footnote Generator](https://investors.blackline.com/news-releases/news-release-details/blackline-expands-agentic-ai-capabilities-accelerate-future) · [Ramp Accounting Agent, Feb-2026 — PRNewswire](https://www.prnewswire.com/news-releases/ramp-launches-accounting-agent-to-automate-bookkeeping-with-real-time-close-302686214.html) · [Basis $1.15B — thefinancestory](https://thefinancestory.com/basis-ai-agent-raises-usd-100mn-to-disrupt-accounting) · [Black Ore Tax Autopilot GA, Apr-2026 — CPA Practice Advisor](https://www.cpapracticeadvisor.com/2026/04/29/black-ore-launches-tax-autopilot-for-broad-availability/182311/) · [Trullion 溯源/ASC 606](https://trullion.com/blog/revenue-recognition-asc-606-principle/) · [IRIS CARBON AI auto-tagging](https://iriscarbon.com/blog/sec-reporting-software-guide/) · [FDTA 联合最终规则, Federal Register 2026-06-25(2026-10-01 生效)](https://www.federalregister.gov/documents/2026/06/25/2026-12787/financial-data-transparency-act-joint-data-standards) · [SEC FDTA 新闻稿 2026-53](https://www.sec.gov/newsroom/press-releases/2026-53-sec-establishes-joint-data-standards-required-under-financial-data-transparency-act-2022) · [EDGAR 结构化数据 suspend, Mar-16-2026](https://www.sec.gov/newsroom/whats-new/edgar-suspend-filings-incorrect-or-incomplete-structured-data-filing-fee-exhibits) · [SOX 302/404 与 2026 SEC SOX 执法组、PCAOB QC1000 — compliancestack](https://www.compliancestack.ai/guides/sox-compliance-checklist-2026) · [PCAOB AI/ICFR 立场 — Houseblend](https://www.houseblend.io/articles/pcaob-ai-guidance-sox-icfr-audits-netsuite) · [FinanceReasoning benchmark(Fable 5 / GPT-5.6)— AIMultiple](https://aimultiple.com/finance-llm) · [Omnibus I / CSRD XBRL 暂停 — Gibson Dunn](https://www.gibsondunn.com/omnibus-simplification-of-eu-sustainability-rules-csrd-and-csddd-enacted/) · [BLS Accountants & Auditors(~160 万,$83,680,+5%)](https://www.bls.gov/ooh/business-and-financial/accountants-and-auditors.htm) · [BLS Financial Managers(879,700,$166,570,+10%)](https://www.bls.gov/ooh/management/financial-managers.htm)。内部:p0_foundation.md(耦合规则、pilot-to-production 折扣)、p3_frozen_taxonomy.md(W1.5 白点 Bucket-1 裁定、猎场 #3)、p6_ic_memo.md(#3 seed ~$15–30M、DFIN 内部化 falsifier 已开火)、p5(W4.10/W1.8/AO.1/SA.1 底稿方法论)。

---

**给调用方的返回说明:** 按 harness 约束以正文交付,未另写 `.md`;可存为 `p5_W1.5_deepdive.md` 追加到 p5_deepdives.md。核心修正 vs 冻结板:**W1.5 从「blocked-but-adjacent 猎场」进一步下调为「内部化 falsifier 已开火、横向门基本关闭」**——DFIN AI-iXBRL(Jun-26)+ Workiva tie-out/Knowledge(Q2-26)是 p6 已预警「window closing」的产品化实证。护城河(SOX/officer-cert)在 2026 年随 SEC 专职 SOX 执法组(Mar-26)与 PCAOB QC1000(Dec-26)**硬化**,是墙也是可拥有的合规滩头。可下注面收窄到两条护城河不迁移的窄缝:**FDTA 非 SEC 结构化报送新面(种子 ~$10–25M,打 Regnology/Wolters Kluwer)** 与 **认证证据/溯源审计链基础设施(种子 ~$8–20M,在 Workiva 够不到的私有/跨辖区法定深度)**;realized 耦合 capture <0.5–1%,横向叙事回避。

---

I have a complete, web-verified picture of the end-2025 → Sept-2026 delta. I have everything needed to write the report with the time dimension added. Per the workflow constraints, I return the full report as my response text (not a written .md file).

---

# AO.1 — 公司即 API / 自主经营（Company-in-a-box / Autonomous Business Ops）
## HTC 猎场 #4 · 机构级深研（时间维度版） · 2026-09-03

> **本报告与已有 p5 底稿的区别**：p5 是 2026-09 的静态快照。本报告把同一份工作拆解**放到时间轴上**——逐步对比「2025 年底能做到什么」与「2026 年 9 月能做到什么」,把这 9 个月的解锁点、假解锁点、和仍然撑住的硬门槛讲清楚。这是给 IC 做尽调时序判断用的。
>
> **两条纪律贯穿全文**：(1) 替代型赛道 **软件收入 = capture-rate × 被替代人力,绝不与人力盘子相加**;(2) 每一条能力主张都过 **pilot-to-production 折扣**(能力 ≠ 已交付替代)。

---

## 一、这是什么 + 为什么是早期猎场

### 定义
AO.1 是一个**非叠加的覆盖层(overlay)**,不是一个新职业。它把「一家早期/微型公司的运营脊柱」——**老板本人的行政工时 + 头几个 ops/BizOps/行政/记账/客服/市场雇员的工时**——作为被替代的对象。它横跨 W1(数字可验证)/W2(判断型)/W3(实时人际)三个族,每一步都**盖章归到母赛道计一次,绝不在本层重复相加**。

真正的价值不在打包产品(「agent 帮你开公司/agent CEO」)那一层,而在其下的**「公司即 API」基元层**——把开公司、发工资、收付款、开发票、供电话号/邮箱/算力这些**受监管的金融+身份+电信轨道**打包成 agent 可调用的单一 API。这一层的代表是 **Naïve**,不是「agent CEO」那类。

### 边界(不包括什么)
- **不包括**「agent 当 CEO 做战略/定价/融资决策」——这是 V=2、无干净成功单元、H4 判断,是营销话术密度最高的部分,不投。
- **不包括**物理履约腿(拣货/打包/发货/库存实操)——P>0,归 W5,靠 3PL 外包而非自己做。
- **不包括**已被现有巨头拿走的后台切片(记账→Intuit、支出/AP→Ramp、工资/HR→Sage/Warp/Gusto、电商→Shopify)——横向 bundle 是在**租**这些,不是**拥有**。
- **不包括**受牌照签字门控的终局动作(报税 §6694 签字、法律工作成果背书、动公司资金、签合同)——这是 fiduciary/liability 底板。

### 劳动盘子(Labor TAM)
**~$300–600B `[W]`(发达经济体、按美元加权)**,是 W1/W2/W3 的**再切分,永不与母赛道相加**。

依据:
- 美国 SMB 老板 ~36% 工作周 / ~16 hrs 耗在行政上;记账是老板最想外包的第一任务;用了 AI 的老板报告每周回收 6–8 hrs([OnPay 2025 小企业展望](https://onpay.com/insights/2025-small-business-outlook/)、[Xero](https://www.xero.com/us/guides/time-tax-small-business/))。
- 分母 = 老板行政工时的机会成本(imputed)+ 头几个后台雇员的薪资(记账 ~$45k、行政/办公室经理 ~$45k、客服 ~$38k、市场协调 ~$55k、运营协调 ~$60k),按发达经济体薪资、美元加权到 $300–600B。
- **关键校正(为什么 Net = Mixed 而非 Compression)**:AO.1 活动里 **~40–60% 是需求「创造」而非工资「替代」**——solopreneur、faceless TikTok/YouTube 频道、一人自动化代理所做的事,他们**本来根本不会雇人**。这部分没有工资可替代,是 Expansion / 软件毛利,**不进 coupled 替代线**。所以真正可替代的分母比标题小,coupled 线更小。

### 为什么值得 HTC 下种子/A 轮
不是因为今天的 capture——今天 realized coupled capture 是 **~0.01–0.05%(约 $30–60M 厂商 ARR / $300–600B),四舍五入是零**。值得下注的原因是**这 9 个月里「公司即 API」基元层从"论文"变成了"可融资的现实"**(Naïve 从 0 到 30k 开发者、低双位数百万 ARR、$28.5M A,全部发生在 2026);而**横向 operator 层同期被 labs 和 Runable 关上了种子门**。窗口把一扇门开了、另一扇门关了——HTC 的活是精确站到**开着的那扇门**(基元层 + 垂直数据护城河),而不是被叙事拖进关着的那扇。

---

## 二、工作步骤全拆解(20 步 / 6 阶段)

覆盖层的核心:没有单一职业拥有这套动作,它是一个**溶解了「工具/操作者」边界的 bundle**。每步盖章到母赛道(计一次)。

| # | 阶段 / 步骤 | ~% 工时 | 母赛道 |
|---|---|---:|---|
| | **A. 设立与基础设施**(多为一次性) | **8%** | |
| 1 | 注册公司、EIN、注册代理、银行/收单账户开立 | 3% | W1.7 |
| 2 | 技术栈供给:邮箱、域名、电话号、支付、存储、算力、CRM | 3% | W1.7 |
| 3 | 网站/店铺/App 搭建与部署 | 2% | W1.1b/SA.4 |
| | **B. 需求生成与市场** | **22%** | |
| 4 | 市场/竞品研究、ICP、定位 | 5% | W2.4 |
| 5 | 内容生产(文案、社媒、SEO/AEO、视频) | 8% | W2.3/W13.2 |
| 6 | 外呼获客 / 线索清单构建 | 5% | W3.2 |
| 7 | 广告投放 / PPC / campaign 管理 | 4% | W2.3 |
| | **C. 销售与营收运营** | **18%** | |
| 8 | 入站线索资格判定与路由 | 4% | W3.1 |
| 9 | 报价、提案、订单录入 | 4% | W1.7 |
| 10 | 履约/交付协调/库存与物流 | 10% | W1.7 + **W5.1(物理腿)** |
| | **D. 财务与后台** | **24%** | |
| 11 | 记账 / 归类 / 对账 | 8% | W1.4/W1.3 |
| 12 | 开票、AP/AR、催收 | 6% | W3.7 |
| 13 | 工资单与承包商付款 | 4% | W1.4 |
| 14 | 报税、申报、合规日历 | 6% | W4.2 |
| | **E. 客户与沟通** | **18%** | |
| 15 | 客户支持(邮件/聊天/语音) | 8% | W3.1/SA.1 |
| 16 | 排期、前台、收件箱/日历分诊 | 6% | W3.6 |
| 17 | 供应商/伙伴沟通与采购 | 4% | W3.6 |
| | **F. 治理、战略与例外** | **10%** | |
| 18 | 现金流规划、定价、战略决策 | 4% | W2.2/W2.6 |
| 19 | 监管/法律例外、合同、纠纷 | 3% | W4.3 |
| 20 | 银行/凭证/**信任动作**(动钱、签字) | 3% | —(fiduciary 底板) |

---

## 三、逐步 AI 能力评估(核心——时间维度表)

定义:**FULL** = agent 在标准/干净路径上无监督完成;**PARTIAL** = agent 起草/决策,但人负责例外或签字;**NO** = 仍纯人工。

**能力锚点**:
- 端到端计算机操作的现实门 = **OSWorld 2.0 最优系统 ~20.6%**(中位任务需人类 1.6 小时);原始 OSWorld 已从 2024-04 的 12% 冲到 2026-06 的 ~85%,但长时程仍是 20% 量级。
- METR 50%-可靠时程:~14.5h(Opus 4.6, 2026-02)→ ~32h(2026-09);**80% 可靠时程远短于此**——「跑一整天」只对良好界定、可验证的代码型工作成立。
- 端到端链式可靠性:20 步 × 80%/步 ⇒ 0.8²⁰ ≈ **1.2%** 无监督成功率——这是「运营整家公司」过度承诺的机械原因。

| # 步骤 | 2025年底能力 | 2026年9月能力(具体工具/模型/产品) | 这9个月解锁? | 备注 |
|---|---|---|---|---|
| **1** 注册/开户 | **PARTIAL** — doola/Stripe Atlas 是面向人的 SaaS,无 agent 可调 API;KYC/开户人工 | **PARTIAL** — Naïve 内嵌 **doola Formation API**(2026-06),agent 可代开 50 州 LLC/C-Corp、含注册代理+EIN;但 **KYC/KYB + 银行审批仍人工** | **部分 YES** — 「agent 可调的公司注册基元」是新的(doola×Naïve, 2026-06);但受监管的 KYC/开户子步**没跨过** | 注册进入 in-flow;银行/KYC 仍是人/监管 NO 子步 |
| **2** 技术栈供给 | **NO/手工** — 需人跨 Stripe/Twilio/AWS/Workspace 手动拼装或写胶水 | **FULL** — **Naïve 单一 API** 一次供给 邮箱/电话/支付/算力/存储 | **YES(旗舰解锁)** — Naïve(2026-06),基元层本身在窗口内诞生 | 这是 Naïve 的实际产品,也是 AO.1 最干净的新基元 |
| **3** 网站/App 搭建 | **FULL(商品化)** — Lovable/Bolt/v0/Replit Agent 2025 已能出全栈 App | **FULL** — Replit Agent(内置 DB/auth/hosting/30+ 集成)、Fable 5 | **NO** — 端-2025 已解;最早被攻克的面 | 硬化非新解锁;品牌级创意仍 PARTIAL |
| **4** 市场/竞品研究 | **PARTIAL** — GPT-5.2/Gemini 3 DeepThink deep-research;表层综合可,定位判断人 | **PARTIAL** — Gemini 3 Deep Think / Runable market-analysis | **NO** — 边际改善;V=2 判断门未动 | W2.4 最弱基础 |
| **5** 内容生产 | **FULL(商品化)** — 量产内容(GPT-5.2、video-gen、ElevenLabs) | **FULL** — Runable / ElevenLabs / video-gen / Fable 5 | **NO** — 已商品化 | 品牌定义级创意仍 PARTIAL |
| **6** 外呼获客 | **PARTIAL** — Clay 清单构建 FULL;**自主外呼已被证伪**(11x churn) | **PARTIAL** — 同上;W3.2 capture≈0 | **NO** | 自主外呼是 thesis-wrong,capture 近零 |
| **7** 广告/PPC | **PARTIAL** — 规则型优化工具,非 agentic 自主 | **PARTIAL→FULL(垂直)** — **Atomic One** 13-agent PPC/出价/预算优化(2026-08) | **部分 YES** — 垂直 agent(Atomic One, 2026-08)攻下结构化出价/预算 | 创意策略仍人 |
| **8** 线索资格/路由 | **FULL** — Decagon/Sierra 结构化分诊已生产 | **FULL** | **NO** — 已解 | |
| **9** 报价/提案 | **PARTIAL** — 模板化 | **PARTIAL** — Runable/ops agents;模板 FULL,定制人 | **NO/边际** | |
| **10** 履约/物流 | **PARTIAL** — 数字协调可;物理 NO | **PARTIAL** — Atomic One 库存/物流 agent 数字协调 FULL;**物理拣打发仍 NO→3PL** | **部分 YES** — 垂直数字协调 agent(2026-08);物理腿未动 | P>0,归 W5 |
| **11** 记账/对账 | **FULL(结构化)** — **Intuit Intelligence 2025-10-28 上线**;Basis/Digits | **FULL** — Intuit Accounting Agent 成熟(~82.5% SMB 份额) | **NO/边界** — 恰在端-2025 门槛跨过,2026 硬化 | **现有巨头已占**;不是初创白space |
| **12** 开票/AP/AR | **PARTIAL→FULL** — Ramp 强但 AP 尚未全自主 | **FULL** — **Ramp 自主 AP**(2026:自动编码/查欺诈/建议审批/付款,$1B ARR) | **部分 YES** — Ramp 自主 AP(2026) | 争议催收仍 PARTIAL;付款执行「控制权留给客户」 |
| **13** 工资/承包商付 | **PARTIAL** — Gusto/Rippling 计算;非 agentic 主动;动钱人工 | **PARTIAL** — **Gusto Cofounder / Sage HCM agent(2026-04)/ Warp 自跑工资($60M B, 2026-06)**;计算/草稿 FULL,**动钱授权仍人「最后手段」** | **部分 YES(计算/草稿侧)** — Gusto/Sage/Warp(2026) | 动钱授权 NO 未变 |
| **14** 报税/申报 | **PARTIAL** — Black Ore 仅早期访问(~75 家);未广泛可用;签字人工 | **PARTIAL→FULL(制表侧)** — **Black Ore Tax Autopilot GA(2026-04-29)** 全生命周期自主制表;**§6694 签字仍人** | **YES(制表侧)** — Black Ore GA(2026-04) | 牌照签字 NO 未变;40% Top-20 CPA 所已用 |
| **15** 客户支持 | **FULL(tier-1)** — Decagon/Sierra/Fin 已生产;capture 7–11% | **FULL** — 同上;Fin 被 Salesforce 收购(2026-06, ~$3.6B) | **NO** — 已解 | realized capture 仅 7–11%,非「deflection」标题 |
| **16** 排期/前台 | **PARTIAL→FULL** — 语音 agent 成熟中(Retell/Vapi/Bland) | **FULL** — 语音生产级(<800ms、占入站 ~19%)、Cowork | **部分 YES** — 语音在窗口内跨到生产级(~18mo experimental→production) | |
| **17** 供应商/采购沟通 | **PARTIAL** — 例行沟通;谈判人 | **PARTIAL** — ops agents;谈判人(W7.3 已删) | **NO** | |
| **18** 现金流/定价/战略 | **NO** — 仅 copilot | **NO** — Cowork/ChatGPT Work/Gemini 仅 copilot;V=2,H4 | **NO** — 「agent CEO」不存在 | 无干净成功单元 |
| **19** 监管/法律例外 | **NO** — Harvey 类起草 + 人签 | **NO** — R4 门;**2026 法律 sanctions 潮再度巩固人**(W4.3) | **NO** — 被炒作、反被巩固 | |
| **20** 银行/凭证/信任动作 | **NO** — 人工 | **NO(fiduciary/签字)** — 但出现**受限购买轨道**:Visa TAP(2025-10)、AP2 mandates、**Ramp Agent Cards(早期访问)**、x402;agent 可做**人授权的受限购买**,但**不能当会计签字人/动公司资金/签合同** | **NO(仅受限购买部分)** — 见第四节「假解锁」 | x402 真实 ~$41M vs 报告厂 $50B |

**诚实能力阶梯(2026-09)**:

| 口径 | 数值 |
|---|---|
| 任务级能力(孤立、50–80% 可靠) | **~64%** 运营工时 |
| 可靠自主、人设检查点、已生产 | **~15–25%** 运营工时 |
| Realized **coupled capture**(替代工资的收入 / 工资盘) | **~0.01–0.05%** |

---

## 四、2025→2026 的关键解锁点(报告最有价值的部分)

### A. 真解锁(从做不了 → 做得了)

**1. Step 2 技术栈供给 —— 旗舰解锁,基元层本身诞生。**
端-2025 根本没有「一个 API 供给一家公司」这个东西——要人跨 Stripe/Twilio/AWS/Workspace 手动拼。**Naïve(2026-06 公开发布)** 把它变成单一 API:6 个月内 30k 开发者、ARR 10× 到低双位数百万、$28.5M A(Nexus 领投,YC 跟投)。**这是 AO.1 在这 9 个月里最大的结构变化——HTC 的 Lane (a) 从论文变成可融资现实。** 让它跨门的不是某个新模型,而是**把受监管的金融/身份/电信轨道打包成 agent 可调 API 这件工程 + 合规活**(doola Formation API 内嵌是配套)。

**2. Step 12 自主 AP —— Ramp(2026)。** 端-2025 Ramp 已强但 AP 未全自主;2026 自主 AP 上线(自动编码发票行、查欺诈、建议审批、完成卡付款),Ramp 同期 $750M F @ $44B、$1B ARR。

**3. Step 13 工资计算/草稿侧 —— Gusto Cofounder / Sage(2026-04)/ Warp(2026-06)。** 从「计算工具」变成「主动 agentic 工资」——但**动钱授权仍是人**(Warp 明说「只把该做的动作作为最后手段抛给人」)。

**4. Step 14 报税制表 —— Black Ore Tax Autopilot GA(2026-04-29)。** 从 ~75 家早期访问,变成广泛可用的全生命周期自主制表(W-2/1099/K-1/券商单全自动分类提取+联邦州税法逻辑+工作底稿),40% 的 Top-20 CPA 所在用。**但 §6694 牌照签字仍是人。**

**5. Step 7/10 垂直广告+物流协调 —— Atomic One(2026-08)。** 13-agent 系统跑 Amazon 店的定价/PPC/库存/物流,「自动化最多 80% 运营任务」,自主 agent 系统 2026-08-27 上线。

**6. Step 16 前台语音 —— 跨到生产级(窗口中段)。** 语音 agent 在 ~18 个月内从实验走到生产(Retell/Vapi/Bland,<800ms,占入站 ~19%),这个跨越正好落在窗口内。

**7. Step 1 agent 可调注册(部分)—— doola×Naïve Formation API(2026-06)。** 注册本身进入 in-flow;银行/KYC 子步未跨。

**8. 元层解锁(投资含义最大):** 同一个 9 个月里,**基元层(Naïve)+ 横向 operator(Runable)+ labs 原生 bundle(ChatGPT Workspace Agents & Gemini Enterprise Agent Platform,均 2026-04-22;Cowork GA 2026-04-09)全部出货**。窗口**同时开了 Lane (a) 的种子门、关了横向 operator 的种子门**。

### B. 假解锁(被宣传成解锁、其实没到生产)

**1. 「agent 运营整家公司」(Runable 的 pitch)—— 没到。** 链式可靠性 0.8²⁰≈1.2% + OSWorld 2.0 长时程 20.6% 意味着端到端无监督运营**不存在**,仍需人设检查点。Runable $2M ARR / 1.5M 用户 = **$1.33/用户**(大多不付费),典型的 vanity metric。

**2. agent 动钱权威 —— 支付轨道 ≠ fiduciary 权威。** Visa TAP(2025-10-14)、Mastercard Agent Pay/AP2(2025)、OpenAI ACP×Stripe、Ramp Agent Cards、x402 全在窗口内出现——但它们处理的是**人授权、有 mandate、单次绑定金额的受限购买**,**不是**「当会计签字人 / 动公司资金 / 签合同」。x402 真实成交 ~$41M vs 报告厂喊的 $50B。G1(动钱/信任)因此只是**被部分触碰**,fiduciary 底板没塌。

**3. 自主报税「申报」—— 制表 ≠ 签字。** Black Ore 全自主制表,但 §6694 签字是人。

**4. 「多天自主工作流」(Gemini Enterprise「跑好几天」)—— 只对良好界定、可验证的工作成立**,不是开放式运营(METR 是 50% 而非 80% 时程)。

---

## 五、仍然做不了的(2026年9月的硬门槛)

| 门槛 | 严重度 | 为什么撑得住(2026-09 现状) | 预计跨过 |
|---|---|---|---|
| **G1 动钱 & 凭证/信任动作**(授权工资、签合同、KYC、动资金) | **CRITICAL**(信任/监管) | Prohibited-action class;fiduciary + liability 底板;agent 不能当会计签字人。窗口内出现的支付轨道(TAP/AP2/Ramp Agent Cards)只解决**受限购买**,没解决**受托权威**。 | **不在能力曲线上关闭**——需要一条 agent-授权 + 保证金/保险 的**轨道**。3–5+ 年,可能永远不完全 |
| **G2 牌照签字**(报税 §6694、法律工作成果、attestation) | **CRITICAL/LARGE**(监管) | Human-in-loop 强制;**2026 法律 sanctions 潮反而再度巩固**(W4.3)。Black Ore 全制表但 CPA 签字;Harvey 起草但律师签。 | Gate-movement 非模型;3–5 年,按辖区不均 |
| **G3 长时程多步可靠性**(pilot-to-production 鸿沟) | **LARGE**(软件的「物理」) | 80% 时程短;OSWorld 2.0 ~20.6%;0.8²⁰ 链式衰减。MIT NANDA 95% 零 P&L、S&P 42% 弃项(从 17%)、<15% 到生产、Gartner >40% agentic 项目 2027 底前取消、仅 ~130 家真 agentic 厂商。**这是自主运营卡住的根本原因。** | 良好界定可验证切片 12–24mo(METR 时程 4–7mo 翻倍);开放式真实运营远更久 |
| **G4 战略判断 & 新型例外**(「agent CEO」) | **LARGE**(信任) | V=2,H4,无干净成功单元;定价转向、招聘、危机、纠纷。Cowork/ChatGPT Work/Gemini 仍是 copilot。 | 结构性——增强而非替代,无确定跨越日 |
| **G5 物理履约腿**(拣/打/发、库存实操) | **MODERATE**(物理) | P>0,硬件门控(W5);bundle 甩给 3PL 而非自己做。 | 机器人时钟,3–7 年;与软件下注无关 |
| **G6 冷启动/数据-上下文整合** | **MODERATE**(数据/信任) | 新公司无专有数据,agent 继承通用先验(MIT「learning gap」)。 | 每次部署 12–24mo 随 ops-graph 积累——**这个 gap 同时是护城河** |

**约束的机械读法**:AO.1 卡住的绑定约束是 **G1(动钱/受托)+ G3(长时程可靠)+ G4(战略判断)**,不是模型智商。窗口内智商大涨(Fable 5 / Opus 4.8 / GPT-5.6 / Gemini 3 Deep Think),但这三条门几乎没动——**这正是 capability(~64%)与 realized capture(~0.02%)之间那道鸿沟没被 9 个月的模型进步填上的原因**。

---

## 六、投资读法

### 可下注的 wedge

**Lane (a) —— 公司即 API / agent 授权-薪资-身份 基元子层(护城河不迁移最干净的一层)**
- **阶段/估值**:种子 / pre-A,**~$3–6M @ ~$20–40M post**。
- **护城河为什么不迁移**:labs(Cowork/ChatGPT Work/Gemini Enterprise)拥有推理层,但**不会去供给受监管的金融/身份/电信轨道**——注册、KYC/受益人、收单账户、**agent 授权支付/支出控制、agent 原生工资授权**(给 <10 人的 AI 运营实体)。这是**合规+集成护城河,非模型护城河**,所以 lab-替代风险在这里最低。
- **但要点**:Naïve 已占住 ARR-已验证的版本(30k 开发者、6mo 10× ARR、$28.5M A)——**它的种子门正在关**。要猎的是它**还没吃下的未被加冕的基元**:**agent-授权/保证金轨道(正是 G1 的缺口)、agent-权限化、给微型 AI 实体的 agent-HR**(Warp/Sage/Gloat 偏企业,留出 <10 人 AI 运营实体的空白)。这也回应了第四节「假解锁 #2」——**谁把 agent-fiduciary-授权做成一条有保证金/保险的生产级轨道,谁就拿住 G1,这是窗口暴露出的最清晰的新白 space。**

**Lane (b) —— 单一 SMB 垂直的 ops-graph operator(留存数据复利)**
- **阶段/估值**:种子 / A,**~$4–8M @ ~$25–50M post**(Atomic One 模板:13 agents、Amazon 电商、€5.6M)。
- **护城河为什么不迁移**:横向 operator 和 labs 缺垂直 system-of-record 集成 + 结果数据;垂直 SaaS 巨头缺 agentic 执行层。类比 niche:Shopify 品牌运营、家政/现场服务运营、创作者/faceless-media 运营、专业事务所运营。
- **承保纪律**:按**留存净 ARR + NRR + 毛 logo churn <30%** 定价,**绝不**按注册用户/GMV/bookings。

### 该避开什么
1. **横向「agent 运营整家公司 / agent-CEO」operator——任何 pre-seed 以上价格都避开。** lab-替代(Cowork/ChatGPT Workspace/Gemini Enterprise 均 2026-04 出货)、OSS-通缩、agent-washing(**Builder.ai:$1.5B → 2025-05 破产,裁 80%,印度「concierge」人假扮 agent、round-tripping**)、pilot-to-production 鸿沟在这里全部汇合。
2. **任何按注册用户/GMV/bookings 定价的**——11x 的 tell($74M 融资、被指 70–80% churn、试用计入 ARR、伪造客户 logo)、Runable 的 $1.33/用户。
3. **已被巨头占住的后台切片**:记账→Intuit(~82.5%)、支出/AP→Ramp($1B ARR)、工资/HR→Sage/Warp/Gusto、电商→Shopify。横向 bundle 只是在**租**这些。

### 3 条带日期的证伪信号(到 2027Q4)

**FI-1 —— 留存-ARR 耐久性(主控解析器)。** 到 2027Q4,是否有 ≥1 家 AO.1 pure-play(Naïve/Runable 类)披露**审计后留存 ARR ≥$25M、NRR ≥100%、毛 logo churn <30%**?
→ **YES**:一个耐久的 SMB 劳动市场在形成,Net 向 Compression 倾斜,提高 conviction。
→ **NO,或 cohort 里出现 Builder.ai/11x 式的 churn/washing 爆雷**:卡在 pilot-to-production 鸿沟,维持 Net=Mixed,种子门是海市蜃楼。

**FI-2 —— 基元 vs operator 价值分裂(哪条 Lane 赢)。** 到 2027Q4,公司即 API 基元层是否**跑赢**横向 operator——即 **Naïve 越过 ≥$50M ARR、NRR >120%**,而纯「agent-operator」bundle(Runable 类)**停在 <$15M 留存或转型卖基础设施**?
→ **YES**:耐久价值在 bundle **之下的基元**(Lane a),集中火力。
→ **NO / operator 反超基元**:bundle 本身是耐久单元,上调 Lane (b)。

**FI-3 —— agent-fiduciary-授权轨道 + lab 替代(G1 与 L=4 双测,窗口新增)。** 到 2027Q4:(a) 是否有一条 **agent-授权/保证金/保险轨道达到生产级**(让 agent 能在有保证金背书下动受限公司资金、而非仅受限购买)?且 (b) 是否有 **model lab 出货原生「经营我的小公司」bundle**(Cowork/ChatGPT Work/Gemini 从注册→运营→财务延伸),**或**后台巨头(Intuit/Shopify/Ramp)出货让横向 operator 冗余的 agent-ops bundle?
→ (a)**YES**:G1 缺口被一条可承保的轨道填上——Lane (a) 里「agent-授权」子层被验证为真市场,是现在就该下种子的地方。
→ (b)**YES**:lab/巨头替代确认——横向 operator 不可投,只有受监管轨道基元(a)+垂直数据护城河(b)存活,把 L 提到 5。

---

## 附:与耦合纪律的合规声明
- ~$300–600B 分母是 W1/W2/W3 的再切分,**永不与母赛道相加**;
- realized 价值按 **capture-rate × 被替代人力(~0.02%)** 计,**从不 SW+Labor 相加**;
- `[L]` 需求-创造份额(~40–60%)明确排除在替代线外(Expansion,非 capture);
- 能力数字(~64%)经链式可靠性(0.8²⁰≈1.2%)与 pilot-to-production 鸿沟折到可靠自主(~15–25%)与 realized capture(~0.02%)两条线。

**核心时序判断(给 IC 一句话)**:这 9 个月里,AO.1 的价值**不是**均匀上升的——**基元层(Naïve)从无到有、拿到 $28.5M A,是最大的真解锁;而「agent 运营整家公司」和 agent 动钱权威是两个最大的假解锁**(链式可靠性 + fiduciary 底板都没塌)。模型智商大涨没有填平 capability↔capture 鸿沟,因为卡点是 G1/G3/G4 三条非模型门。HTC 的唯一活口是**基元层里 Naïve 还没吃下的 agent-授权/保证金轨道(填 G1 缺口)**,和**单垂直的 ops-graph operator(Atomic One 模板)**——两者都只在**留存-ARR/churn 承保、绝不用注册用户/GMV**的纪律下才过关。横向 operator 的种子门,在这同一个窗口里被 labs 和 Runable 关上了。

---

**主要信源(2026-09-03 web-verified)**:[Naïve $28.5M A — TechCrunch](https://techcrunch.com/2026/08/06/naive-raises-28-5m-to-automate-the-grunt-work-of-setting-up-and-running-a-company/) · [doola Formation API inside Naïve — Newswire](https://www.newswire.com/news/doola-powers-native-us-company-formation-inside-na-ves-ai-agent-22848579) · [Runable $21M A @ $65M(0→$2M ARR/3周、1.5M 用户/15 人)— TechCrunch](https://techcrunch.com/2026/08/26/runable-hits-21m-to-bet-ai-agents-can-go-from-building-businesses-to-growing-them/) · [Atomic One €5.6M(2026-07-31,创立 2021-12,Amazon 运营,「80% 运营任务」)— EU-Startups](https://www.eu-startups.com/2026/07/malaga-based-atomic-one-raises-e5-6-million-to-automate-e-commerce-operations-with-ai-agents) · [Anthropic Cowork:研究预览 2026-01-12 / GA 2026-04-09 / 移动+网页 2026-07-07 — TestingCatalog](https://www.testingcatalog.com/anthropic-launches-claude-cowork-in-general-availability/) · [Opus 4.8(2026-05-28,Dynamic Workflows)— TechCrunch](https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/) · [ChatGPT Workspace Agents & Gemini Enterprise Agent Platform 均 2026-04-22 — Pillitteri](https://pasqualepillitteri.it/en/news/1321/chatgpt-workspace-agents-openai-comparison-2026) · [Intuit Intelligence 2025-10-28 上线,Accounting/Payroll/Payments Agents — Self Employed](https://www.selfemployed.com/news/quickbooks-intuit-intelligence-ai-bookkeeping-2026/) · [Ramp 自主 AP + Agent Cards + $750M F@$44B/$1B ARR — Ramp](https://ramp.com/blog/ramp-ap-agents-announcement) · [Gusto Cofounder / Sage 2026-04 / Warp $60M B 2026-06 — The New Stack](https://thenewstack.io/gusto-cofounder-small-business-ai/) · [Black Ore Tax Autopilot GA 2026-04-29(75 firms、40% Top-20 CPA)— CPA Practice Advisor](https://www.cpapracticeadvisor.com/2026/04/29/black-ore-launches-tax-autopilot-for-broad-availability/182311/) · [agent 支付轨道:Visa TAP 2025-10-14 / Mastercard Agent Pay+AP2 / OpenAI ACP×Stripe / x402 — Medium(Masood)](https://medium.com/@adnanmasood/agentic-payments-101-2-2-payment-standards-and-protocols-acp-ucp-ap2-and-x402-26486e6d511f) · [OSWorld 原始 12%(2024-04)→85%(2026-06);OSWorld 2.0 长时程 ~20.6% — Medium(Masood)](https://medium.com/@adnanmasood/the-hardest-easy-problem-in-ai-the-state-of-computer-use-agents-a7e3aea7fa3a) · [端-2025 前沿模型:Opus 4.5 / Gemini 3 / GPT-5.2 — Vertu 时间线](https://vertu.com/lifestyle/the-ai-model-race-reaches-singularity-speed) · 语音生产级(Retell/Vapi/Bland,<800ms)· Builder.ai 崩盘 · MIT NANDA 95% · S&P 42% · Gartner 40%/130-real。内部:p0_foundation(耦合规则、pilot-to-production 折扣、能力前沿)、p3_frozen_taxonomy(E2 裁定、AO.1 行)、p5_deepdives(AO.1 静态底稿)。

---

**返回给调用方的要点摘要**:已完成 AO.1(HTC 猎场 #4)的时间维度机构级深研,全文如上(中文,公司/产品名英文)。核心增量是把工作拆解放到 2025年底→2026年9月 时间轴:(1)**真解锁**——Naïve 单一 API 基元层(2026-06,旗舰)、Ramp 自主 AP、Gusto/Sage/Warp 工资 agent、Black Ore 报税制表 GA、Atomic One 垂直电商 agent、前台语音生产级;(2)**假解锁**——「agent 运营整家公司」(链式可靠性 0.8²⁰≈1.2%、OSWorld 2.0 20.6%)、agent 动钱权威(支付轨道只解决受限购买、非受托权威、x402 真实 $41M vs $50B)、自主报税(制表≠§6694 签字);(3)**硬门槛** G1 动钱/受托 + G2 牌照签字 + G3 长时程可靠 + G4 战略判断仍撑住,模型智商大涨没填平 capability(~64%)↔capture(~0.02%)鸿沟。投资读法:Lane(a)公司即 API/agent-授权轨道基元(种子 $3–6M@$20–40M,猎 Naïve 未占的 agent-fiduciary-授权/保证金轨道即 G1 缺口)+ Lane(b)单垂直 ops-graph operator(Atomic One 模板,$4–8M@$25–50M,按留存 ARR/NRR/churn<30% 承保);避开横向 agent-CEO/operator(pre-seed 以上)、按注册用户/GMV 定价者、已被 Intuit/Ramp/Sage/Shopify 占的后台切片。已按耦合纪律(替代型:软件收入=capture×被替代人力,不相加)与 pilot-to-production 折扣校验全文。**未写新 .md 文件**(遵守 workflow 约束,报告作为文本返回;如需可另存为 `p5_AO1_timeline.md`)。