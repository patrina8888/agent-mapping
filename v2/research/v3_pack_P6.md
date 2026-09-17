# v3 Evidence Pack — P6 · Human-Contact Care & Physical Assistance
**（人体接触式照护与身体辅助）**

HTC internal · 2026-09-16 · Author: Agent Mapping v3 · **Re-homes W6.3** (Personal Care & ADL assistance)
Governed by: p0b_capability_refresh_2026-09（GPT-6 增量、无 humanoid 量产车队、数据层才是可投层)、p0_foundation（耦合规则 coupling、capture rates、pilot-to-production chasm)、p3_frozen_taxonomy（V/H/P/R/L/D 打分、W8-physical labor 层、猎场读法）。

> **术语速查（jargon）**：ADL = Activities of Daily Living（日常生活活动:吃饭/穿衣/如厕/移动/洗澡/如厕转移）。VLA = Vision-Language-Action model（视觉-语言-动作大模型,机器人的"大脑"）。teleop = teleoperation（远程遥操作,真人在后台替机器人接管难动作）。RaaS = Robot-as-a-Service（机器人即服务,按月订阅而非一次买断）。HHA/CNA/PCA = home health aide / certified nursing assistant / personal care aide（居家照护员/持证护理助理/生活照料员——本行当的三个主力工种)。METI = 日本经济产业省。MA = Medicare Advantage（美国联邦医保的商业托管版）。NDR/NRR = net dollar retention（净收入留存率,老客户续费+扩购的健康度指标)。

> **一句话定位**：这是全图里**最大的潜在劳动盘子**（~$11T 非正式照护 `[L]`）、**社会阻力最小**（劳动力短缺下社会许可 social-license 反转,几乎没有"抢饭碗"政治阻力)、但**物理捕获率几乎为 0**（硬件时间线 5–15 年 + 执照/责任门槛）的耦合扩张型（Coupled / Expansion）track。守纪律:**别赌照护 humanoid OEM(硬件资本坑),赌短缺授权下的照护数据/远程操作层与数字协调层。**

---

## 一、这是什么 + 为什么值得看

### 1.1 定义与边界

**P6 = 需要与人体直接、持续物理接触的精细操作类照护劳动。** 环境结构维度上它发生在"半结构化的家/护理院房间"里,但真正卡住它的不是导航或感知,而是**任务物理维度的另一头:直接作用在一个活人的身体上**——搀扶、翻身、转移(床↔轮椅)、喂食、穿衣、如厕/沐浴、康复训练。

判定这一族的门槛(gate)**不是灵巧度本身**,而是三件叠加的事:
- **人身安全(human-safety)**:对象是脆弱、会疼、会摔、会告你的真人,失败代价是伤害而非报废零件;
- **执照与责任(licensing + liability)**:护理、康复、给药都被执业执照和赔偿责任框住(R=4);
- **信任(trust)**:被照护者和家属要允许一台机器碰自己的身体。

**边界(与相邻 track 划清,不重复计)**:
- **纯陪伴/监测**(跌倒检测、生命体征、社交机器人 ElliQ)**不算 P6 的核心** ——它无人体接触、软件即可解、已量产;它是 P6 的"感知先行带",列入步骤但不构成灵巧度前沿。
- **居家日常打杂**(拿水、叠衣、递物)属 W14.1 消费级家务助理 / P 的非接触操作带,不是"照护"。
- **持证给药/配药**归 W4.9(药房,R=5 阻塞)。
- **康复设备的临床端**与本族重叠,但它是 P6 里**唯一已有报销代码**的子步骤,单列讨论。
- **P6 ≡ 冻结分类里的 W6.3**,本包即 W6.3 的完整重做与升维,不新增盘子。

### 1.2 劳动盘子(labor TAM)及依据

| 口径 | 数字 | 标签 | 依据 |
|---|---|---|---|
| **付费直接照护工资盘**(全球,comp-band 加权) | **$0.9–1.3T** | `[W]` | 居家照护员/CNA/生活照料员/护工/看护 的可置换工资总额。美国工种时薪低(HHA/PCA 中位数低于 $16/hr),所以**按美元加权会系统性低估这一族的人头**——它是全图**头数最大**的池子之一。 |
| **非正式/无偿照护的隐性劳动**(全球) | **~$11T** | `[L]` | **全图最大的潜在池**。美国仅家庭照护者就有 ~53M 人在做无偿照护(YC RFS S26 引用);全球把子女/配偶照护老人失能者的隐性工时按影子工资折算即 ~$11T 量级。这是**未被支付的需求**,是扩张(Expansion)的期权,**绝不与 `[W]` 相加**。 |

> **数据完整性更正(carry)**:这 ~$11T `[L]` 与 **W6.3、W14.1(消费级家庭照护)** 引用的是**同一个隐性照护池**,全图**只计一次**,是期权不是可加盘子。市场机构口径的"eldercare-assistive robots market ~$2.8B(2026)→~$11.86B(2035)、CAGR ~17.4%"[MarkWide/report-mill]属 **Tier-2 报告工厂**,只取方向不作锚;且该口径**把已量产的陪伴/监测**与**产量≈0 的物理 ADL**混在一起,不能当照护劳动捕获读。

### 1.3 为什么这一族值得单看(3 个结构性理由)

1. **盘子最大、阻力最小、捕获最低——三者同时成立**,这是全图独一份。劳动力短缺把通常的"机器抢人饭碗"政治**反转**成"求你快来补人":日本到 2040 年缺 ~57 万照护员、现在每 4.25 个岗位只有 1 个申请人[Stanford/HumansAreObsolete];美国十年内数百万照护岗空缺[YC RFS S26]。**社会许可反转 = 最省摩擦的物理落地路径**(p3 的 E6 情景轴)。
2. **门槛是"信任+执照+硬件时间线",不是模型 IQ**——GPT-6 Astra 这种"增量而非跃变"(p0b A.1)对它**零帮助**:让一个大模型更聪明,不会让一台机器更安全地把一位失能老人从床上抱起来。这正是框架"capability ≠ capture、物理缺口是硬件时间线问题"纪律的最纯样本。
3. **2026 年有一条真证据出现了**:斯坦福(Stanford FSI,2026-08)对日本护理院的研究显示,引入照护机器人后**照护员 +28%、护士 +39%、总雇佣 ~+26%**——即**增员而非减员**,机器人是协作(cobot)、补重体力活,人力反而更好招[Stanford Report / WEF / Automate.org]。这把 P6 的 Net 从"迟早替代"钉死成**Expansion(扩张)**,并且是**带审计级证据**的扩张。

---

## 二、这份体力工作到底要做哪些步骤

把"照护一位失能/半失能老人的一天"拆成阶段和步骤,每步用大白话说人到底在做什么、难在哪。按**环境轴上"感知先行 → 操作阶梯"**排列,越往下人体接触越深、越难。

**阶段 A — 感知与在场(不碰身体)**
1. **监测与预警**:盯着老人有没有摔倒、有没有下床、心率血氧对不对、夜里有没有异常——本质是"一双不睡觉的眼睛"。
2. **陪伴与认知激励**:陪聊天、提醒、放音乐、做认知游戏,缓解孤独和认知衰退——本质是"一个有耐心的说话对象"。

**阶段 B — 身体辅助(轻接触、以人为主、机器助力)**
3. **移动与步态辅助**:扶着走、防跌、上下楼、康复步行训练——人还是主体,机器给"托一把"的力。
4. **搬运与转移**:把人从床挪到轮椅、从轮椅挪到马桶/浴椅——**这一族的腰杆活**,照护员职业伤害(腰伤)的头号来源。

**阶段 C — 亲密照料(深接触、直接作用于人体)**
5. **喂食**:一勺一勺喂饭喂水,判断吞咽节奏、别呛着。
6. **穿衣/梳洗**:给穿脱衣服、洗脸梳头——涉及柔性织物 + 贴身接触,双重难。
7. **如厕与沐浴**:扶上马桶、清洁、洗澡——**最私密、最危险、最难**,湿滑环境 + 尊严 + 安全全叠加。

**阶段 D — 医疗与协调(数字为主)**
8. **用药管理**:按时提醒/发药、记录服没服——提醒是软件活,实际配发受药房执照管。
9. **康复训练**:中风/术后的步态、肢体功能重复训练——临床可量化、**有报销代码**。
10. **记录、排班与协调**:写照护记录、排班、和家属/医生/机构对接、应急调度——**纯数字活,可远程**。

> 关键结构洞察:**步骤 1–2、8(提醒)、10 是"数字/大脑"活,今天就能做;步骤 3–4 是"人穿戴外骨骼、机器助力"活,正在真落地;步骤 5–7 是"机器自主碰人体"活,基本没影;步骤 9 康复是唯一有报销通道的临床子步骤。** 越往下,卡点越是**身体(硬件+责任)**而非**大脑(模型)**。

---

## 三、每一步 AI+机器人现在能不能做(核心表)

能/半能/不能 + 靠哪个模型×硬件。**诚实区分「软件/大脑」进步 vs「硬件/身体」瓶颈**;凡卡在硬件/责任时间线的,明确标注"非模型问题"。

| 步骤 | 2025 年底(能/半能/不能 + 模型×硬件) | 2026 年 9 月(+具体产品/VLA/机器人) | 本窗口新解锁? | 备注(大脑 vs 身体) |
|---|---|---|---|---|
| **1 监测预警** | **能**。摄像头+传感器跌倒检测/生命体征已量产(护理院普及)。 | **能**,LLM 让告警更少误报、能语音解释。ElliQ、床垫/雷达传感器、护理院监控。 | 否(早已解锁) | **软件已解**。感知先行带,P6 最成熟层,但无人体接触、非灵巧度前沿。 |
| **2 陪伴认知** | **半能**。ElliQ(Intuition Robotics)脚本化陪伴已卖多年。 | **能↑**。GPT-6/Gemini 级语音让对话自然度真提升;Twolabs 明确在建"社交智能层"。 | 半(语音大脑升级,真实增量) | **软件进步**,身体不涉及。会被模型厂语音(Alexa+ 等)商品化,毛利薄。 |
| **3 移动/步态辅助** | **半能**。康复外骨骼(Ekso EksoNR、Lifeward ReStore)临床在用;可穿戴助行。 | **半能↑**。**报销打通是关键增量**(见步骤 9)。German Bionic Exia(CES 2026)可穿戴、AI 自适应助力。 | 是(报销/硬件增量,非能力跃变) | **人为主体、机器助力**,不是机器自主。真落地但资本重。 |
| **4 搬运/转移** | **半能(仅助力式)**。护理员**穿**外骨骼抬人(German Bionic Apogee+),减腰伤;机器**自主**抱人=不能。 | **半能↑**。German Bionic **Exia**:单次动作 38kg/84lb 动态助力,专为转移/翻身设计。但**机器自主转移一个真人仍为 0 量产**。 | 否(自主转移未过闸) | **身体+责任双卡**。助力外骨骼真用;自主抱人是 P=5+R=4,硬件时间线问题,**非模型问题**。 |
| **5 喂食** | **半能(被动器械)**。Obi(FDA Class I / 510(k) 豁免)、Bestic 是**用户自己操控**的喂食臂,不是自主判断。 | **半能**。Obi Gen 3 在做临床可用性研究(NCT07151950);Twolabs 把"喂食"列为首发任务,**在训 VLA,未量产**。 | 否 | **窄任务器械已解,自主喂食未解**。报销覆盖薄。 |
| **6 穿衣/梳洗** | **不能**。柔性织物操作(deformable manipulation)本身未攻克。 | **不能**。π0 只在"已知衣物折叠">80%(p0b C.1),**给活人穿衣=未演示**;Twolabs 列为目标,无产品。 | 否 | **身体硬卡**。织物 + 贴身接触双重难,10 年+。**非模型能勉强的**。 |
| **7 如厕/沐浴** | **不能**。 | **不能**。日本 AIREC(Moonshot/早稻田)原型演示换尿布/助浴/喂食,**仍是原型,目标 ~2030+**。 | 否 | **全族最难**。湿滑+私密+安全+尊严,硬件时间线最长。 |
| **8 用药管理** | **能(提醒)/ 不能(实际配发)**。提醒是软件;实际发药受药房执照管(W4.9)。 | 同左,LLM 让提醒更个性化。 | 否 | **提醒=软件已解;物理配发=执照阻塞**,归 W4.9。 |
| **9 康复训练** | **半能**。Ekso EksoNR(FDA 清中风/脊髓损伤/脑损伤/MS,500+ 康复中心)、Lifeward ReStore(中风软外骨骼)。 | **半能↑↑**。**报销真突破**:2026-03 Lifeward 宣布 Aetna/Humana/UnitedHealthcare 把 ReWalk 个人外骨骼纳入 MA 覆盖,~1600 万参保可及,近半 MA 参保人已在覆盖计划内;美国建立个人外骨骼 Medicare 报销通道。 | **是(报销门槛松动=真解锁,R 轴)** | **临床+硬件,资本重**。是 P6 唯一有代码/报销的子步骤;但主要是上市公司(Ekso/Lifeward)地盘。 |
| **10 记录/排班/协调** | **能**。纯数字,可远程。 | **能↑**。Sage Care(YC S26)用 AI 撮合家庭与 HHA/CNA/陪护;居家照护机构运营自动化。 | 半(数字 wedge 成型) | **软件已解,可投的数字楔子在这**。远程照护调度/机构运营/语音对接。 |

**表读法(核心结论)**:
- **本窗口(2025 末→2026 年 9 月)真正的新解锁全在"非能力"轴上**:①**报销/监管松动**(康复外骨骼进 MA;日本 METI 把照护机器人安全验证从 18 个月压到 <6 个月)——这是 **R 轴门槛在动**;②**证据出现**(斯坦福日本研究把 Net 钉成 Expansion);③**数据/大脑在训**(Twolabs 训 VLA、1X Neo teleop 攒数据)——是软件/数据进步,**不是部署解锁**。
- **没有任何一个"机器自主碰人体"的物理 ADL 步骤(4 自主/5 自主/6/7)过闸**。这是硬件时间线 + 责任门槛,**GPT-6 增量、任何模型 IQ 都推不动**(p0b B/C 纪律)。
- **无照护 humanoid 量产车队**:Twolabs 有首款设计 Tobi 但在训练/演示态;1X Neo(见五)~60–70% 自主、难动作靠 teleop——是"远程操作的木偶在攒训练数据",不是自主照护劳动(p0b D 的 staged-vs-paid 纪律)。

---

## 四、耦合与捕获(coupling & capture)

| 维度 | 判定 | 说明 |
|---|---|---|
| **Coupling 类型** | **Coupled(耦合)** | 若真发生置换,计价按"每次照护/每小时看护"对标真人工资,而非软件预算。**永远用 capture-rate × 被置换工资盘,绝不 SW+labor 相加。** |
| **当前 capture** | **≈ 0(物理 ADL);<0.5% 全族** | 守物理纪律(<1.5%)。物理 ADL(转移/喂食/如厕)**生产环境置换≈0**;已实现收入几乎全在陪伴/监测(软件,<$100M)与助力外骨骼(增量工具,不是置换)。照护 humanoid 无付费车队。 |
| **Net effect** | **Expansion(扩张)** | 斯坦福证据:机器人进护理院 → **总雇佣 +26%**,人力增员;机器补重体力活、扩服务覆盖、填短缺,而非砍人头。短缺授权把 Compression 反转为 Expansion。 |
| **Conviction** | **Low–Med** | 盘子和短缺方向高置信;但"何时/是否有机器自主碰人体的付费部署"极不确定,capture-expansion 是**未证的赌注**。 |
| **Denominator(工资盘,只计一次)** | **$0.9–1.3T `[W]`** 付费直接照护 + **~$11T `[L]`** 非正式照护(期权,与 W6.3/W14.1 同池,**不重复计,不与 [W] 相加**) | 康复设备的软件/器械收入是**增量(additive)**,不进耦合置换线。 |

> **耦合纪律小结**:P6 今天几乎没有可耦合的置换在发生——它的价值是**扩张进那 ~$11T 从没被支付过的照护缺口**,外加**服务稀缺人力的工具/数据层**。把"eldercare robot 市场 $2.8B→$11.86B"当劳动捕获读,是把**部署成本速度**误当**捕获**(p3 Reality-Ladder Tier-D 错误)。

---

## 五、竞争格局(具体到公司名)

### 5.1 巨头 / OEM / 现任(硬件与平台)

**照护/家庭 humanoid OEM(都在定位,无一有照护车队)**:
- **1X Technologies** — **Neo** 家用 humanoid,$20K 一次买断或 $499/月订阅,2026 开始交付;明确瞄准**独居老人/失能者"就地养老"(aging-in-place)**。**关键纪律**:独立评测约 **60–70% 自主,难动作由远程操作员(teleop)接管**;The Robot Report 直接标题"**teleop 而非自主才是 Neo 的路径**"。= 远程木偶攒数据,非自主照护。
- **Figure**(~$39B,OpenAI 领投)家用有野心但当前是汽车厂试点;**Tesla Optimus**(目标激进、产量落后,别当已部署劳动读——p0b C.2);**Apptronik**(~$5.5B)、**Agility**(物流为主)、**Sanctuary AI**、**Neura Robotics**、**Unitree**(IPO ~$9B,主要是研究铁,非部署劳动)。**全部:无照护量产车队。**
- **韩国财阀捕获(chaebol-captive,p3 E6)**:**Hyundai**(收 Boston Dynamics Atlas)、**Samsung**(Bot Fit 可穿戴/RX 机器人)——短缺授权下的近水楼台,但捕获归大集团,非可投 startup。

**助力外骨骼 / 转移辅助(现任,资本重、已有装机)**:
- **German Bionic**(德国,欧洲外骨骼技术领头羊)——**Exia**(CES 2026,38kg 动态助力,专攻护理转移/翻身)、**Apogee+**(北美护理版)。**但 2025-11-17 在满手订单下申请破产**(承诺投资突然撤回造成流动性缺口),累计融资 ~$65M,已被 Archimedes Partners 收购。**这是 P6 硬件资本坑的活教材(见六)。**
- **Cyberdyne**(日本,HAL 外骨骼)、**Ekso Bionics**(EksoNR,500+ 康复中心,FDA 清中风/SCI/TBI/MS)、**Lifeward/ReWalk**(个人外骨骼,2026 进 MA 报销)、**Panasonic**(Resyone 床-轮椅一体)、**RIKEN**(Robear 抱人原型的学术传承)、日本 **AIREC / Moonshot**(早稻田,换尿布/助浴原型,~2030+)。

**陪伴/监测 + 平台现任(软件已解,毛利薄)**:Intuition Robotics(**ElliQ**,陪伴非 ADL)、Amazon(Alexa+ / Astro)、护理院监控/雷达传感器厂。

**日本国家层**:**METI**($6.3B AI/机器人承诺,把照护机器人安全验证 18mo→<6mo);SoftBank/ABB 相关短缺补人计划(p3 E6)。

### 5.2 独立 startup(名字 + 阶段 + 融资 + 一句话)

- **Twolabs**(YC 2026 批,SF)— **种子** — 为护理院造照护 humanoid,首款设计 **Tobi**,首发任务喂食/穿衣/给药/日常/陪伴,**在训 VLA + 建社交智能层**;创始人 Sardor Rahmatulloev(前 Meta Superintelligence Labs)、Danyal Ahmad(前 Salesforce,GT AI 硕士)。**唯一一家把照护 humanoid 当纯种子在打的**——但产品在演示/训练态,守"无车队"纪律。
- **Sage Care**(YC S26)— **种子** — AI 撮合家庭与背调过的 HHA/CNA/陪护,自动化居家照护机构运营。**不是机器人,是数字协调/用工层**——恰是可投楔子(见六)。
- **Diligent Robotics**(**Moxi**,创始人含 Vivian Chu)— 中后期 — 医院内物流/递送协作机器人。**注意:是医院后勤(W5 邻族),非人体接触照护**,列此以划清边界。
- **康复硬件**:**Fourier Intelligence**(中国,康复外骨骼)、**Harmonic Bionics**(Harmony 上肢康复)、**Hocoma**(Lokomat)——多为器械/临床、资本重。
- **喂食器械**:**Obi**(Desin LLC)、**Bestic/Camanio**——FDA 合规的被动喂食臂,小众、报销薄。
- **陪伴**:**Hyodol**(韩国,陪伴娃娃)、**ElliQ** 之外的社交机器人一众——正在商品化。
- **读法**:**独立、可投、软件/数据规模化的照护 startup 稀薄**——价值要么在硬件(资本坑),要么在数字协调/数据层(下节)。这与 p3"物理族是硬件时间线、真钱在数据/teleop 层"完全一致。

### 5.3 YC(重点 Summer 2026 / S26 及近批)

- **YC RFS(Requests for Startups)Summer 2026 明确点名"AI for elderly care"**:①能真对话的语音接口;②让老人安全独立的监测;③**帮做家里体力活的机器人**;④帮家庭照护者协调照护/预约/急救的软件[YC RFS; UrbanGeekz; Forbes]。
- **批次趋势**:Industrials 已占 S26 批 **23%(第二大类,仅次 B2B)**,humanoid/家用机器人是重头[neweconomies.co]。
- **具体公司**:**Twolabs**(照护 humanoid,批次标签在 Spring/Summer 2026 之间,官方页记 caregiving)、**Sage Care**(S26,居家照护用工/运营)。
- **HTC 提示**:YC 在把照护当明确主题推,但其"robotics for physical tasks"绝大多数会撞上本包步骤 4–7 的硬件墙——**S26 里真正可下注的更可能是 Sage Care 这类"数字协调/用工/语音"侧,而非 Tobi 这类"机器碰人体"侧。**

---

## 六、HTC 猎场读法

### 6.1 可下注的种子 / A wedge(具体细分 + 为什么护城河不迁移)

**核心判断:别赌照护 humanoid OEM,别赌外骨骼硬件——赌短缺授权下的照护"数据/远程操作层"与"数字协调层"。** 这是 p0b D + p3 猎场 #6 在 P6 的落地。

1. **照护专用 embodied 数据 / teleop / sim 层(CyberOrigin-adjacent,最高置信)。** 每个照护 VLA(Twolabs、1X、Physical Intelligence)都被同一件事卡死:**人体接触的照护动作数据不存在于互联网规模**,而且是**安全攸关、需帧级验证(frame-verified)、需受控护理环境准入**的最难采集的一类数据。
   - **为什么护城河不迁移**:护城河 = **受控照护场景的准入 + 信任/安全标注 + 帧级 ground-truth**,不是模型 IQ;模型再强也拿不到"合规地在真护理院采集真人转移/喂食数据"的权限。这**独立于任何单一 humanoid OEM**,坐在整条捕获重资本机器人栈的**上游**。日本/韩国短缺授权(METI <6mo 验证)是**最省摩擦的合规采集入口**。
   - 形态:照护场景 teleop-as-a-service + 帧验证标注;喂食/转移/步态这类安全攸关动作的专用数据集。

2. **数字照护协调 / 用工 / 文档 / 远程督导层(software wedge,真 NDR 可期)。** = Sage Care 剖面(机构运营/用工撮合)+ **"照护机器人管家(robot wrangler)"** 远程督导/介入(每个 1X Neo/Twolabs 都需真人后台接管——W8-physical labor)+ **居家照护机构的语音对接**(W3.6 ∩ 照护,HappyRobot 类,坐在被加冕 CX 巨头之下)。
   - **为什么护城河不迁移**:护城河 = **机构/家属/照护员工作流嵌入 + 系统-of-record 集成深度**,不是模型;可用 retained-ARR/NDR 检验,种子门未关。

3. **康复(rehab)——唯一有报销代码的子步骤,但谨慎。** 2026 MA 把个人外骨骼纳入报销是真 R 轴解锁,但这块是**器械+临床、资本重、且主要是上市公司(Ekso/Lifeward)地盘**——**只在有软件/数据/依从性(adherence)角度时才碰**,别做又一家硬件厂。

**下注纪律**:目标 ~$8–20M 进 ≤$40–80M post,押数据/协调/督导层;underwrite **retained-ARR + NDR + 受控场景准入**,不要 underwrite 出货量/装机/市场规模报告。

### 6.2 该避开什么(OEM / 硬件资本坑)

- **照护 humanoid OEM 直投**:P=5 亲密灵巧 + R=4 责任,**5–15 年硬件/信任时间线**,无付费车队;把 humanoid 估值/出货当部署劳动读是 p3 标准物理误判。
- **外骨骼/照护硬件厂**:**German Bionic 就是活教材**——欧洲技术领头羊、满手订单、CES 2026 旗舰机,却在 2025-11 因一轮融资撤资直接资金链断裂破产、被贱卖收购。**硬件公司现金流对资本市场情绪的脆弱性,是"满订单也会死"的资本坑。**
- **陪伴硬件(ElliQ 类)**:被模型厂语音(Alexa+/GPT-6 语音)商品化,毛利薄。
- **直接自主 ADL 机器人**(自主转移/喂食/如厕):步骤 4 自主/5 自主/6/7 全部未过闸,是硬件时间线,不是种子软件问题。
- **消费订阅照护 humanoid**(Neo $499/mo 面向 C 端):teleop 成本 + 隐私 + 信任,离规模化远。

### 6.3 三条带日期的证伪信号(到 2027Q4)

1. **物理 ADL 过闸信号(去伪最硬)**:**到 2027Q4,是否有任何机器人在生产型养老照护中,自主完成一项"被报销/付费"的物理 ADL(转移或喂食),规模 >100 家机构、含经常性 RaaS 收入?**
   - 是 → 物理 capture-expansion 真启动,P6 Net 向"混合"移,提物理置换置信;
   - 否(仍只有陪伴/监测/teleop)→ 物理 ADL 维持 `[L]` 期权,capture≈0,守纪律。(承 W6.3 falsi,收紧)

2. **可投层验证信号**:**到 2027Q4,照护专用 embodied-数据/teleop 平台是否拿到真经常性收入(向 VLA 实验室卖帧验证的人体接触照护数据),或有 Twolabs 级照护 humanoid 拿到超越试点的付费护理院部署?**
   - 数据层先拿到经常性收入 → "投数据层不投 OEM"的 HTC 命题在 P6 印证;
   - 只有 OEM 试点、数据层没起来 → 说明照护数据还太早,继续观望而非追 OEM。

3. **RaaS 耐久性 vs 硬件资本坑信号**:**到 2027Q4,日本/韩国短缺授权部署(METI <6mo 验证、ReWalk 式报销)是否转成护理院**持续 RaaS/软件订阅收入 >30% 占比**,还是重演 German-Bionic 式(满订单 + 资本缺口 → 破产/被并购)?**
   - RaaS 攀升 → 出现耐久的照护机器人劳动捕获,可下注;
   - 重演资本坑 → 照护机器人是商品化硬件竞赛、startup 价值捕获≈0,只碰数据/协调层。

---

## 附:关键 2026 数据与来源(web-verified 2026-09-16)

- **斯坦福日本护理院研究(增员非减员的审计级证据)**:机器人采用 → 照护员 +28%、护士 +39%、总雇佣 ~+26%;cobot 协作、补重体力活,增员多为灵活合同工。[Stanford Report 2026-08](https://news.stanford.edu/stories/2026/08/care-robots-japan-employment-labor-shortage-research) · [Stanford FSI](https://fsi.stanford.edu/news/robots-ease-elder-care-shortages-without-displacing-workers-or-diminishing-care-quality-study) · [WEF](https://www.weforum.org/stories/technological-innovation/study-robots-service-sector-japan/) · [Automate.org](https://www.automate.org/robotics/industry-insights/robots-were-supposed-to-replace-workers-in-japans-nursing-homes-the-opposite-happened)
- **日本短缺 + METI 提速**:2040 缺 ~57 万照护员、每 4.25 岗 1 申请人;METI 安全验证 18mo→<6mo;Takaichi 政府 ~$6.3B。[HumansAreObsolete 2026-02](https://humansareobsolete.com/articles/japan-aging-workforce-robotics-crisis-570000-care-worker-shortage-2040-february-3-2026) · [METI 照护机器人优先领域](https://www.meti.go.jp/english/press/2024/0628_004.html) · [Metaintro](https://www.metaintro.com/blog/japan-robot-workforce-filling-jobs-no-one-wants-2026)
- **German Bionic(硬件资本坑教材)**:Exia @ CES 2026(38kg 助力,护理转移);Apogee+ 北美护理版;**2025-11-17 满订单下申请破产,累计融资 ~$65M,被 Archimedes Partners 收购**。[German Bionic CES 2026](https://www.germanbionic.com/news/ai-to-wear-german-bionic-presents-the-exia-robotic-exoskeleton-at-ces-2026) · [破产公告](https://www.germanbionic.com/news/filed-regular-insolvency-proceedings-open-the-door-for-strategic-realignment) · [VC Magazin 2025-11](https://www.vc-magazin.de/blog/2025/11/20/german-bionic-insolvenz-geplatzte-finanzierungsrunde/) · [xpert.digital](https://xpert.digital/en/exoskeleton-star-german-bionic/)
- **1X Neo(teleop 非自主)**:$20K / $499/mo,2026 交付,~60–70% 自主难动作靠远程操作员,瞄准就地养老。[The Robot Report — teleop 才是路径](https://www.therobotreport.com/teleop-not-autonomy-the-path-for-1x-neo-humanoid/) · [eWeek](https://www.eweek.com/news/1x-neo-humanoid-home-robot-2026/) · [1x.tech](https://www.1x.tech/discover/neo-home-robot)
- **康复报销解锁**:2026-03 Lifeward — Aetna/Humana/UnitedHealthcare 把 ReWalk 个人外骨骼纳入 MA,~1600 万可及;个人外骨骼 Medicare 报销通道建立。Ekso EksoNR 500+ 康复中心,FDA 清中风/SCI/TBI/MS。[Exoskeleton Report 2026-02](https://exoskeletonreport.com/2026/02/2026-exoskeleton-news-depot-trials-for-hypershell-rewalk-insurance-momentum-and-real-world-clinical-adoption-signals/) · [ReWalk/Medicare 2026](https://momentarylab.com/blog/healthcare-devices/rewalk-exoskeleton) · [New Mobility](https://newmobility.com/medicare-to-cover-personal-exoskeletons/) · [Ekso Health](https://eksobionics.com/eksohealth/)
- **喂食器械**:Obi FDA Class I / 510(k) 豁免(product code ILC),Gen 3 临床可用性研究 NCT07151950。[School Health — Obi](https://www.schoolhealth.com/obi-feeding-device) · [ClinicalTrials NCT07151950](https://clinicaltrials.gov/study/NCT07151950)
- **YC S26 照护**:RFS 点名 elderly-care AI(语音/监测/家用机器人/照护者协调);Industrials 占批 23%。**Twolabs**(照护 humanoid Tobi,喂食/穿衣/给药,训 VLA)、**Sage Care**(照护用工/机构运营)。[YC RFS](https://www.ycombinator.com/rfs) · [Twolabs YC](https://www.ycombinator.com/companies/twolabs) · [Sage Care YC](https://www.ycombinator.com/companies/sagecare) · [neweconomies.co S26](https://www.neweconomies.co/p/y-combinator-summer-26-batch) · [UrbanGeekz RFS](https://urbangeekz.com/2026/05/y-combinator-reveals-15-startup-ideas-it-wants-founders-to-build-in-summer-2026/)
- **日本 AIREC / Moonshot(物理 ADL 仍原型)**:换尿布/助浴/喂食演示,目标 ~2030+。[RoboZaps 眼镜级综述](https://blog.robozaps.com/b/humanoid-robots-in-elderly-care) · MIT Tech Review 综述(历史背景)
- **市场口径(Tier-2,只取方向)**:eldercare-assistive robots ~$2.8B(2026)→~$11.86B(2035),CAGR ~17.4%——报告工厂口径,混淆已量产陪伴/监测与产量≈0 的物理 ADL,**不作劳动捕获锚**。[MarkWide Research](https://markwideresearch.com/eldercare-assistive-robots-market)

**Sourcing caveats(守 p0 R1–R9 + p0b 更正)**:①无照护 humanoid 量产车队,Twolabs/1X 为演示/teleop 态,守"出货≠部署劳动";②物理 ADL 生产置换≈0,capture 守 <1.5%;③~$11T `[L]` 与 W6.3/W14.1 同池,只计一次,不与 `[W]` 相加;④市场规模数字为 Tier-2 报告工厂,仅方向;⑤GPT-6 Astra 为增量(p0b A.1),对 P6 的身体/责任门槛零推动——本族卡点是硬件时间线,非模型 IQ。
