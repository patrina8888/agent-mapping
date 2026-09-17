# V3 证据包 · P8 — 机器人经济劳动（Robot-Economy Labor：teleop / fleet-supervision / commissioning / data-verify / sim）

HTC 内部 · 2026-09-16 · PhysicalAI 家族分区（partition id = **P**）里**唯一的净新增（net-new）叠加层**的完整证据包。
上游依据：`p0_foundation.md`（耦合规则、捕获率、pilot-to-production 断崖、W8 家族先验）、`p0b_capability_refresh_2026-09.md`（GPT-6 Astra 增量式、无量产 humanoid 车队、**数据/teleop/sim 层才是可投层**——本包所有能力主张以 p0b 为准，尤其 §C 机器人前沿与 §D 具身数据层）、`p3_frozen_taxonomy.md`（冻结 76 行、评分轴 V/H/P/R/L/D、**W8 intake 规则**、wage-bill denominator test）、`v3_physicalai_architecture.md`（P1–P8 分区架构，本包是 §5 里 P8 那一格的展开）、`v2_master.json`。

> **一句话定位**：P8 是 W8（数字智能体经济的净新增劳动）在**原子世界（物理机器人）里的孪生**。它不装任何"被机器人替代"的工资盘子——它装的是**机器人经济自己创造出来的、全新的人类工资盘子**：远程操作机器人采集数据的人（teleoperator）、盯着"自主"机器人车队救场的人（robot wrangler / 机器人调度员）、上门把机器人装好调好修好的人（physical FDE，物理前沿部署工程师）、把具身数据"逐帧核验"的人（frame-verifier）、以及给机器人写仿真场景的人（sim author）。**这一层是硬件解耦（hardware-decoupled）、按人和流程扩张（不是按芯片/资本扩张）、且尚未被现任巨头吃掉的——正是 p0b §D 和 HTC 机器人论点点名要占的那一层。CyberOrigin 就坐在这里。**

**读法纪律（贯穿全包,非谈判项）**:
1. **这是"创造"不是"替代"**：P8 = **additive / net-new creation**，没有被替代的分母，**永远不减、也不加进 P1–P7 的 $15T 物理工资盘**。它和 W8 一样，是 p0 说的"净新增抵消 + 领先指标（leading indicator）"——机器人部署跑得多快，P8 就长得多快。
2. **耦合纪律的退化情形**：因为没有被替代盘子，P8 **不适用 capture-rate × displaced-wage**；它的分母就是**这些新岗位自己的工资总额 `[W]`**。任何"机器人车队管理软件市场 $XXB""AV 远程操作市场 $XXB"都是 **`[$]` 软件/服务营收代理，只看方向、绝不当劳动线**（report-mill 数字，按 p0 R1–R9 一律降级）。
3. **硬件/算力划在门外（intake 规则，照抄 W8）**：机器人本体、GPU、云算力都是 `[$]`，**不进 P8**；只有**这些岗位隐含的人头工资**进 P8。一个具身数据基建供应商（Scale/Encord/Cosmos）是 `[$]` 台账条目；它**雇的人**（标注员、场景师、FDE）才是 P8。
4. **不迷信炒作**：**没有任何 humanoid 在受控、商业定价的量产环境里部署超过"低几百台"**（p0b §C.2）；Figure 03 在宝马 = **演示（demonstration），不是车队**；Unitree 公开市值 **~$9B（约 38× 销售额），不是 $50B**。所以 P8 今天真实是"小而真、增速极高"的一层，不是已经很大的一层。
5. **P8 独有的证伪风险不是"能不能替代人"，而是"合成数据会不会先把人类采集的活吃掉"**——见第三、六节。这是本包最重要的一条思考线。

---

## 一、这是什么 + 为什么值得看

### 1.1 定义与边界

**机器人经济劳动（robot-economy labor）** = 因为要**造出、喂养、部署、看管**机器人车队，而**新长出来的人类岗位**。它是 W8（数字智能体经济劳动）的物理孪生：W8 数的是"看管软件智能体的人"，P8 数的是"看管/喂养机器人的人"。P8 精确装五块（对应 v3 架构 §5 P8 的五个 scope）：

**① Teleoperation-as-a-Service + 具身数据采集（teleop / embodied-data collection）——最大、最投得进的一块**
- 大白话：一个人戴着 VR/手柄/动捕（motion-capture，动作捕捉）设备，**远程"钻进"机器人的身体**，替它做一遍任务（叠衣服、装配、拿杯子），机器人把"看到什么 + 做了什么"的**成对传感器-动作数据（action-paired sensorimotor data）**录下来，喂给 VLA（Vision-Language-Action，视觉-语言-动作大模型）去学。
- 为什么是人类活：**数据是 2026 年具身 AI 唯一真正的瓶颈**（p0b §D：*"action-paired 传感运动数据不存在互联网规模"*）。而 teleop 一个熟练操作员**一小时只能产 ~5–50 段（episodes）**，且会累、质量会掉——这是一个**按人头和流程扩张、和芯片解耦**的瓶颈，正是"可投层"的画像。
- CyberOrigin（HTC 组合锚）坐这里：自我定位 *"Ground Truth for Embodied Intelligence"*，做**逐帧核验（verified-to-the-frame）**的数据，卖给训练物理 AI 的实验室/世界模型团队；产品 CyberCode 让人"像查数据库一样查现实、用大白话组一个训练集、看它逐帧核验"。

**② 机器人车队远程监管与介入（fleet remote-supervision / "robot wrangler" 机器人调度员）**
- 大白话：机器人号称"自主"，但一旦卡壳（抓空了、迷路了、遇到没见过的情况），后台有个人**远程接管、把它救回来**，或者把异常丢进队列让人处理。这是"异常队列（exception queue）"的值守工。
- 为什么是人类活：**今天每一台出厂的家用/工厂 humanoid 都带人类兜底**——1X Neo 明确"专家模式（Expert Mode）"由**美国本土操作员**在你批准的时段远程驾驶；Figure、AV（自动驾驶车）都有远程协助后台。这是 W8.1（Agent Ops）在物理世界的孪生。

**③ 机器人调试/集成/现场维护（commissioning / integration / field-maintenance = 物理 FDE）**
- 大白话：机器人运到现场后，有人去**装机、标定、接进产线、教它这个工位的活、坏了去修、要换活了去重配**。
- 为什么是人类活：**没有一家 OEM 披露 MTBF（mean time between failures，平均无故障时间）——这个"缺失的数字"本身就是信号**（p0b §C.2）。每部署一台机器人，就拖着一条又重又长的维护/集成人力。注意边界：这里修的是**机器人自己**，不是客户设备（客户设备的现场维修是 P4/W6.4，别重复计）。

**④ 具身数据逐帧核验与标注（embodied-data frame-verification & annotation）**
- 大白话：teleop 录进来的海量数据里，很多是废的（操作员手抖、任务失败、力反馈不对、时间戳错位），有人要**逐帧看、打分、对齐、剔坏**——把"量"变成"经核验的质"。
- 为什么单列：这和数字世界的 RLHF 文本/图像标注（W8.4）是**两种活、两类数据**（成对传感运动 episode vs 文本/图像标签），分开数、分开算（架构 §3.3 边界守则）。

**⑤ 仿真与合成环境/场景编写（sim / scenario authoring）**
- 大白话：真实数据太贵太慢，就在**仿真器（simulator）里造场景**——建 3D 场景、写任务变体、调物理、生成合成数据（synthetic data）去补真实数据的规模缺口。
- 为什么是人类活（**且带着最大的自我颠覆风险**）：仿真是每个机器人基础模型数据栈的**必备"规模层（scale layer）"**（p0b §D 的"三层栈：teleop 保真 + sim 规模 + 人类视频 多样"）。但——**仿真/合成数据越好，越可能反过来把 ① 的人类采集活吃掉**。这条张力是 P8 的核心投资问题（第六节证伪信号）。

> **明确装进 P8（intake，照抄 W8 的"人进、软硬件出"）**：teleoperator、robot wrangler、physical robot-FDE、frame-verifier、sim/scenario author 的**人头工资 `[W]`**。
> **明确不装进 P8（划出去，避免重复计）**：
> - **机器人本体 / GPU / 云算力 / teleop 硬件** → `[$]` 台账，不进劳动线。
> - **数字智能体的监管/集成/评测/标注** → W8.1/8.2/8.3/8.4（数字孪生）。边界：**看管软件智能体 → W8.1；远程操作或上门修机器人 → P8**。
> - **数字 RLHF 文本/图像标注** → W8.4；**具身逐帧核验** → P8.④。两种数据、两拨人，分开数。
> - **客户设备的现场维修**（不是修机器人本身）→ P4/W6.4。
> - **AV 硬件/算力/RaaS 资本开支**（Waymo/Aurora/Kodiak）→ `[$]`；只有 teleop-assist 操作员工资进 P8，被替代的司机工资盘在 P3。

### 1.2 为什么现在值得看（四个理由）

1. **它精确等于 HTC 机器人论点的可投层**。p0b §D 的结论是三句话：数据是所有前沿 VLA 的**共同瓶颈**；数据层**硬件解耦、按人/流程扩张、尚未被现任捕获**；所以**投数据/teleop/sim 层、不投 humanoid OEM**。P8 就是把这层做成了地图上的一个正式家族。CyberOrigin 的"逐帧核验/ground-truth"角度，是在原始 teleop 量泛滥时的一个**防御性子位**（数据的质，不只是量）。
2. **这个行业几乎是过去 18 个月凭空长出来的**——"采集专家（collection-specialist）整个梯队大致在 ~18 个月内成型"（Teahose，2026）。2026 的融资与产业化事件密度是元年级别：XDOF 带 $70M 出道、Mecka AI $60M（Framework Ventures 领）、Dyna Robotics $120M A、Encord 累计 $110M、Scale AI 联合 Universal Robots 在 GTC 2026 发 UR AI Trainer、AgiBot 开源 AGIBOT WORLD 2026 + CES 2026 发 Genie Sim 3.0、World Labs 融 **$1B** 并收购机器人仿真公司 SceniX。
3. **它是 P1–P7 全部物理行的"领先指标"**。物理捕获真实发生只在 P1（~1–1.5%），P4/P5/P6 被硬件时间线卡死在 ~0%（5–15 年）。但**不管哪一格未来会解锁，都得先经过 P8 这一层喂数据**——所以 P8 的增速，是整张物理地图部署速度的最干净的先行读数。
4. **GPT-6 Astra 没解锁任何物理格子，却直接推高了 P8 的需求**。p0b 的判定是 Astra 是"增量+降本"、没动任何物理捕获（§C.3 物理捕获仍 <1.5%）。但更强/更便宜的模型 = **更多团队去训 VLA = 更饥渴的数据需求**。模型层商品化（p0b §A.4"紧凑成团、无人独占护城河"）反而把价值往数据/部署/专有物理数据挤——这正是 P8 的顺风。

### 1.3 劳动盘子（labor TAM）及依据

P8 是**净新增 `[W]`**，坐在 P1–P7 的 $15T 分母**之外**（创造，不是替代）。今天很小、增速极高。自下而上拆（每块给发达+中国加权的人头 × comp 薄层，**低置信度，给区间不给点**）：

| 组成 | net-new labor TAM `[W]` | 依据（自下而上） |
|---|---|---|
| ① Teleop + 具身数据采集操作员 | **~$3–8B** | 最大一块。全球估 ~数万名操作员（中国权重高、comp 低）。单价锚点：teleop 采集 **~$72–145/hr（中国）/ $90–150/hr（美国 fully-loaded）**，egocentric 可穿戴 $25–60/hr（evsint/Teahose，2026，Tier-2）。折成年薪：中国 ~$15–40k、美/欧 ~$60–110k。CyberOrigin/AgiBot/1X/XDOF/Scale/Objectways 等在建产能 |
| ② 机器人车队远程监管（wrangler） | **~$0.5–2B** | 今天最小、增速最陡。AV 远程协助后台（Ottopia/Fernride/Vay）+ 早期 humanoid 兜底（1X Experts）。参照 Cruise 2024 "~1.5 人/AV"，随车队扩张线性长 |
| ③ 机器人调试/集成/现场维护（物理 FDE） | **~$1–4B** | 只算**机器人本身**的净新增集成/维护人力（不含 P4 客户设备维修）。系统集成/自主/AI-机器人复合技能"人才稀缺"（Deloitte：75% 制造商招不满关键岗）。每部署一台拖一条维护人力；MTBF 未披露=维护重 |
| ④ 具身数据逐帧核验/标注 | **~$0.5–2B** | 与数字 RLHF（W8.4）分开数。Encord/Objectways/Labelbox/Build AI 的物理 AI 标注产能 + 实验室内部核验团队（CyberOrigin 的"逐帧"是这块的高端） |
| ⑤ 仿真/场景编写 | **~$0.3–1B** | 头数最少、comp 最高的一块（NuRec/Cosmos/Genie Sim/Marble 场景师、real-to-sim 工程师）。带自我颠覆风险 |
| **P8 合计（净新增，不与别处重复计）** | **≈ $5–15B `[W]`,YoY >100%** | 与 W8（$10–20B）同量级、更早期。**低–中置信度**——头数与 comp 都是薄估，且中国权重大压低了金额加权 |

> **纪律提醒（三条，都要盯死）**：
> - 这 $5–15B 是**人的工资盘**，不是软件/服务营收。市面上的"人形机器人车队管理服务市场 $0.6B(2026)→$45B(2036)"（Fact MR）、"AV teleoperation 服务 ~$0.55B(2026)"（Fact MR）、"机器人 teleop 云平台 $4.2B(2025)、managed service 占 44%"（Dataintelo）——**全是 `[$]` 服务营收代理，report-mill，只读方向，绝不当 P8 的 `[W]`**。
> - **不与 W8.4 重复**：数字文本/图像 RLHF 在 W8.4；具身逐帧核验在 P8.④。
> - **不与 P4 重复**：修客户设备是 P4；修机器人本体是 P8.③。

---

## 二、这份体力工作到底要做哪些步骤

P8 的"体力活"不是被机器人替代的活，而是**运营机器人经济这台机器**本身的活。按五块各自拆成阶段，大白话说人在做什么。

### ① Teleop + 数据采集（阶段 A→E）
- **A｜搭台子（rig 搭建）**：把 teleop 装备（VR 头显、力反馈手柄、外骨骼/动捕服）接上机器人或采集台，校准延迟（1X/Adamo 追求 **sub-40ms**，低于 40 毫秒，否则人操不动）。
- **B｜设计任务清单（task taxonomy）**：定今天要采什么技能、多少变体、什么难度分布（叠 T 恤 vs 多层滑布，抓刚性件 vs 抓软食物）。
- **C｜真人操作采集（teleop rollout）**：人远程/近端"钻进"机器人身体做一遍任务，系统录**成对的"看到+做了"数据**。AgiBot 用**自由式采集（free-form）+ BLOS 第一人称远程**（操作员共享机器人视角）+ 力控采集（含接触动力学）。
- **D｜egocentric 补采（第一人称人类视频）**：人戴手环/iPhone 直接做日常动作，采**第一人称人类视频**补多样性（Mecka 的路子）——比 teleop 便宜（$25–60/hr）。
- **E｜现场汇聚回传**：把多台、多本体、多场景的数据汇成集（OXE/RT-X 那种跨本体池化）。

### ② 车队远程监管（wrangler，阶段 A→D）
- **A｜盯盘（monitoring）**：一个人盯 N 台机器人的实况+遥测（telemetry），Formant/InOrbit 这类"机器人运维（RobOps）"台的看板。
- **B｜异常分诊（triage）**：报警来了判断——机器人能自己恢复？还是要人接管？（Cortex AI 的"human-in-the-loop rollouts，操作员在机器人失败时把它救回来"）。
- **C｜远程接管介入（remote intervention）**：低延迟 teleop 把卡住的机器人开出困境（1X Expert 在你家、Ottopia 在路上）。
- **D｜复盘喂回（feedback loop）**：把每次介入录下来、标注、喂回模型——**"救场"同时就是"采数据"**（1X Redwood 模型正是这么长的）。

### ③ 物理 FDE（阶段 A→E）
- **A｜现场勘测 + 装机（site survey / install）**：看工位、搭电搭网、把机器人固定/接进产线。
- **B｜标定（calibration）**：标坐标系、力/视觉、安全围栏、no-go 区。
- **C｜教活/配置（task teaching）**：把这个工位的具体活教给机器人（示教、微调策略）。
- **D｜现场维护/修（field maintenance）**：坏了去修、换件、软件升级（MTBF 未知=这步很重）。
- **E｜重配/退役（retask / decommission）**：产线换活了重新配置，或到寿退役。

### ④ 逐帧核验/标注（阶段 A→D）
- **A｜采集摄入（ingest）**：把 teleop/egocentric 原始数据入库。
- **B｜逐帧核验（frame-verify）**：人逐帧看——任务成没成功？力对不对？时间戳对齐没？剔废（CyberOrigin 的核心）。
- **C｜标注/结构化（annotate）**：打技能标签、语言指令对齐、分段。
- **D｜质量评分/出集（QA & release）**：给数据集打质量分、组成可训练集。

### ⑤ 仿真/场景编写（阶段 A→D）
- **A｜真转仿（real-to-sim）**：把真实传感数据重建成可交互仿真（NuRec 的 3D 高斯泼溅 Gaussian-splatting 渲染；World Labs 收 SceniX 就是补这条 real-to-sim gap）。
- **B｜场景编写（scenario authoring）**：造 3D 世界、写任务/难度变体（Marble、Cosmos Text2World/Video2World）。
- **C｜合成数据生成（synthetic generation）**：批量跑出带标签的合成 episode（NVIDIA Physical AI Data Factory Blueprint）。
- **D｜仿真-真实核验（sim-to-real check）**：验合成数据在真机上管不管用，闭环。

---

## 三、每一步 AI+机器人现在能不能做（核心表）

**这里的"能不能做"是一个和别的物理包不同的问题**：P8 是净新增的人类活，所以真正要问的是——**AI/自动化/合成数据现在能不能把这些人类活"自己吃掉"？** 能吃掉得越快，P8 的人类工资盘越短命（这正是 P8 的证伪风险，不是别的物理包的"能不能替代蓝领"）。区分**「软件/大脑」进步 vs「硬件/身体」瓶颈**，诚实标注。

| 步骤 | 2025 年底（能/半能/不能 + 靠哪个模型×硬件） | 2026 年 9 月（+ 具体产品/VLA/机器人） | 这窗口是否新解锁 | 备注（软件大脑 vs 硬件身体；对 P8 人类活是"顺风"还是"自我颠覆"） |
|---|---|---|---|---|
| ①A 搭 teleop 台/降延迟 | 半能：teleop 延迟仍是痛点 | **半能↑**：Adamo sub-40ms teleop 软件、1X 消费级 rig 成熟 | 部分 | **硬件/软件双轨**。延迟下降是工程进步，**利好**采更多数据；不威胁人类活 |
| ①C 真人 teleop 采集本身 | **不能自动**：只能真人操作，~5–50 episodes/hr | **仍不能自动**：XDOF/AgiBot/1X/Scale 都还是真人在操 | 否 | **这是 P8 的命根**。teleop 采集**尚无法用 AI 替代真人**——正因如此才是可投的人类活。**风险来自旁路（⑤ 合成数据），不是来自把这步自动化** |
| ①D egocentric 补采 | 半能：可穿戴采人类视频 | **能↑**：Mecka（$60M A）body-sensor+iPhone 采第一人称 | 是（成本↓） | **利好且改变结构**：egocentric 比 teleop 便宜（$25–60 vs $90–150/hr），把一部分高价 teleop 人力挤成低价可穿戴人力——**P8 内部的降本，不是消灭 P8** |
| ②A/B 盯盘+异常分诊 | 半能：Formant/InOrbit 看板+告警 | **半能↑**：InOrbit 发 OpenRobOps（ISO 21423 参考实现）标准化运维 | 部分 | **软件大脑进步**：更好的自动分诊 = 一个 wrangler 盯更多机器人（杠杆↑），**压缩单位人力但扩大覆盖**——W1.8 SOC 同型（"压缩在岗+扩张到没人盯过的backlog"） |
| ②C 远程接管介入 | **不能自动**：卡壳就得真人接管 | **仍不能自动**：1X Expert、Cortex AI human-in-loop rollout 仍靠人救场 | 否 | **硬件/自主瓶颈**：正因自主可靠性没过 80% 门（p0b §C.1 长程二元完成仍是墙），兜底人**结构性存在**。自主越不达标，wrangler 越durable |
| ③ 物理 FDE（装机/标定/修） | **不能自动**：纯上门人力 | **仍不能自动**：Figure/BMW、Amazon/Agility 部署都靠人集成维护 | 否 | **硬件时间线**：MTBF 未披露=维护人力重且durable；这是"每部署一台就拖一条人力"的净新增，**5–15 年内不会被自动化吃掉** |
| ④B 逐帧核验 | 半能：可 AI 预筛，但质量把关靠人 | **半能↑**：Hebbian Robotics（YC S26）做"不训模型就能评 teleop 数据质量"的 API——**自动化了一部分核验** | 是（部分） | **软件大脑进步，双刃**：AI 预筛提效**利好**吞吐；但若"数据质量 API"足够好，会压缩人类逐帧核验的头数——**部分自我颠覆**。CyberOrigin 的"人+逐帧 ground-truth"是抗这一刀的高端定位 |
| ④C 标注/结构化 | 半能：AI 辅助标注 | **半能↑**：Encord（$110M）AI-assisted 多模态标注（LiDAR/雷达/视频/点云） | 是（部分） | 同数字标注史：**AI 辅助压单价、放大产能**；净效果通常是"标注总量涨得比单价降得快"，人类活先扩后缩 |
| ⑤A 真转仿 real-to-sim | 半能：仿真质量不够真 | **能↑（跳变）**：NuRec 3D 高斯泼溅、World Labs 收 SceniX 专补 real-to-sim gap | **是** | **软件大脑跳变**。**对 P8 是最大的自我颠覆源**：real-to-sim 越好，越能少采真实数据 |
| ⑤C 合成数据生成 | 半能：合成数据 sim-to-real 有 gap | **能↑（跳变）**：Cosmos WFM、Physical AI Data Factory Blueprint；**合成 1 万段 ~$10–15k GPU vs 真实 ~$50 万+** | **是** | **成本差 ~30–50×**。这是**悬在 ① teleop 人类工资盘头上的那把刀**：若合成数据能替真实数据做主，P8.① 的人类盘会先被压。**目前仍需真实数据兜底"多样性/接触物理"，合成补"规模"——三层栈并存，未坍缩**（p0b §D）|
| ⑤D sim-to-real 核验 | 半能 | 半能：仍需真机验合成 | 否 | **利好人类活**：只要合成不完全可信，就需要真人 teleop+核验来锚定 ground truth——这是 P8 存续的技术理由 |

**一句话总结第三节**：P8 里**真人 teleop 采集（①C）、远程接管（②C）、物理 FDE（③）三块，AI/机器人今天替代不了**——它们要么是硬件/自主时间线卡着（②C/③），要么本质是"人给机器人当身体"（①C）——所以是**结实的净新增人类活**。真正的威胁**不来自"把这些活自动化"，而来自旁路的合成数据/仿真（⑤A/⑤C）把"需要多少真实数据"这件事本身缩小**。GPT-6 级别的大模型进步**放大了对数据的总需求**（顺风），但仿真侧的进步**在悄悄侵蚀真实采集的份额**（逆风）——这场"数据饥渴 vs 合成替代"的赛跑，是 P8 的全部投资问题。

---

## 四、耦合与捕获：coupling / capture / net / conviction / denominator

**评分（照抄架构 §5，band 级重导出，不是行平均）：V3 / H3 / P1 / R2 / L3 / D3**
- **V=3**：数据质量/交付可部分核验（"这批数据能不能训出策略""异常队列清空没"），但"这批数据到底值多少训练价值"不干净可测——中等可验证。
- **H=3**：任务是中程的人-流程活（一次 teleop session、一次现场部署），不是秒级也不是月级。
- **P=1（关键）**：**这层劳动几乎硬件解耦**——屏幕、teleop rig、核验/仿真工具。**这正是它可投的全部理由**。（对比 P1–P7 的 P=3–5）。
- **R=2**：轻监管（隐私——1X 在家 teleop 的画面模糊/no-go 区/本土操作员是隐私合规，不是行业牌照）。
- **L=3**：实验室会自建数据运营（1X/PI/Figure 内部都有 teleop 团队），但这层**并非被实验室垄断**——独立的第三方数据/核验/仿真公司真实存在且在融资。L=3 是"部分实验室内化风险"，也是"仍有独立空间"的最强论据。
- **D=3**：护城河 = 专有的、经核验的具身数据集 + 操作员供给网络 + 客户/本体集成，中等且在积累（CyberOrigin 的"逐帧 ground-truth"是把 D 往上顶的动作）。

**耦合类型（coupling）**：**Additive / net-new creation**。这是耦合规则的**退化情形**——没有被替代的工资盘子，所以**不做 capture × displaced**。它像 W8：**永不从 $15T 物理分母里减，也永不加进去**。

**当前 capture**：**n/a（不适用）**——没有被替代池，就没有"捕获率"。守物理纪律的方式在 P8 是另一句话：**别把 `[$]` 服务营收（Fact MR/Dataintelo 的市场数字）当成 `[W]` 劳动线**，也别把它当"捕获"。（P8 不违反"物理捕获 <1.5%"——那条纪律管的是 P1–P7 的被替代盘；P8 根本不在那个分母里。）

**Net effect**：**Expansion（扩张）**。纯创造：机器人经济越铺，这五块人类活越多。**内部有结构迁移**——高价 teleop 被 egocentric/AI 辅助核验/合成数据部分挤压（第三节），但**整层仍在净扩张**（采集专家梯队 18 个月成型、2026 融资密集）。

**Conviction（置信度）**：**Medium**。
- 往上：产业事件密度高、真实融资多、CyberOrigin 是 HTC 已验证的锚、边界清晰。
- 往下：**金额是薄估**（头数/comp 都低置信度，中国权重大压低金额加权）；且**服务营收数字全是 report-mill**，不能用来锚 `[W]`；且**合成数据的自我颠覆风险真实**（⑤A/C 是跳变项）。

**Denominator（分母，不与别处重复计）**：
- P8 分母 = **teleoperator + wrangler + physical robot-FDE + frame-verifier + sim author 的净新增人头工资 `[W]`**（$5–15B）。
- **坐在 P1–P7 的 $15T 之外**（创造，不是替代）。
- **不含**：机器人本体/GPU/云（`[$]`）；数字智能体运营（W8.1）；数字 RLHF（W8.4）；客户设备维修（P4）；被替代的司机盘（P3）。
- **W8 ↔ P8 边界**（架构 §3.3）：看管软件智能体→W8.1；远程操作/上门修机器人→P8。数字文本标注→W8.4；具身逐帧核验→P8.④。

---

## 五、竞争格局（分三块，具体到公司名）

> 纪律：下列一切"市场规模/估值"数字按 p0 R1–R9 处理——**融资额 ≠ 营收 ≠ 劳动盘**；report-mill 只读方向。P8 的真问题不是"谁市值大"，而是"谁拥有**经核验的专有具身数据 + 操作员供给网络**这条真护城河，且不被实验室内化"。

### 5.1 巨头 / OEM / 现任（硬件与平台）——多数是 `[$]` 层，不是 P8 的可投人类活，但定义了 P8 的需求侧和挤压面

- **NVIDIA**——具身数据/仿真的事实基建层。**Cosmos**（世界基础模型 WFM，Text2World/Image2World/Video2World 合成数据）、**Isaac Sim/GR00T**（N1.7 GA、N2 DreamZero）、**Omniverse NuRec**（3D 高斯泼溅把真实传感数据变可交互仿真）、GTC 2026 发 **Physical AI Data Factory Blueprint**。**它把 ⑤ 仿真/合成这块的底座商品化了——既是 P8 sim 层的顺风工具，也是 P8.① teleop 人类盘的最大结构性挤压源**（合成 1 万段 ~$10–15k vs 真实 $50 万+）。
- **Scale AI**——从数字标注霸主横切物理。**scale.com/physical-ai**；GTC 2026 与 **Universal Robots** 合发 **UR AI Trainer**（"lab-to-factory"模仿学习系统），年内发 UR 机器人上采的大规模工业数据集。**这是"数字标注巨头把 W8.4 能力平移到 P8"的最直接威胁**——独立 P8 数据公司要防的就是 Scale/Labelbox 的平移。
- **Google DeepMind**——**OXE / RT-X**（1M+ episodes、22+ 本体的池化跨本体数据集，是"公共数据层"的标杆）；Gemini Robotics 1.5 + ER 1.5 的数据栈。定义了"跨本体池化 > 单本体"的数据范式。
- **humanoid OEM（自建 teleop 数据运营，L 风险来源）**：**1X**（Neo + **1X Experts** 美国本土操作员 + **Redwood** 模型，teleop-first 明说"teleop 不是自主才是路径"）、**Figure**（Helix VLA + 自采）、**Tesla Optimus**（Fremont 自采）、**Physical Intelligence**（π0.7，多机器人+人类视频+自主次优数据）、**Skild**（human video + 海量 sim）。**这些都在内部做 teleop/数据——是 P8 独立公司的 L=3 内化风险的具体来源**，也是他们的客户（对外买核验数据/仿真）。
- **机器人车队运维平台（RobOps `[$]` 层）**：**Formant**（低延迟 teleop + 遥测 + 告警 + 分析）、**InOrbit.AI**（RobOps 平台 + **OpenRobOps ISO 21423** 参考实现 + tele-assistance）、**Freedom Robotics**、**AWS IoT RoboRunner**（多品牌异构车队）。**这些是软件 `[$]`；P8 是它们平台上"坐着的那个 wrangler 的工资"**。
- **工业自动化现任（P8.③ 集成/维护的现任雇主）**：FANUC/ABB/KUKA/Siemens 及其集成商网络——传统"上门集成维护"的现任，humanoid 时代的物理 FDE 需求会外溢出他们的产能（Deloitte：75% 制造商招不满关键岗）。

### 5.2 独立 startup（名字 + 阶段 + 融资 + 一句话）——P8 的真正可投面

**A. Teleop / 具身数据采集（P8.①，最密集）**
- **CyberOrigin**（HTC 组合锚）——*"Ground Truth for Embodied Intelligence"*，**逐帧核验**数据 + CyberCode（"像查数据库一样查现实"）。**定位在"质/ground-truth"而非"量"，是抗合成数据与抗 Scale 平移的防御性子位**（公开融资数字未在本轮联网中检索到确认——**不臆造**，按 p0 标"未验证/待补"）。
- **XDOF**——**出道即 $70M**（2026-06）。三层"数据金字塔"：定制 teleop / 通用 teleop / egocentric。低成本 teleop 系统采训练数据。
- **Mecka AI**——**$60M**（$25M A + $35M 跟投，Framework Ventures 领，2026）。**egocentric**：body-sensor + iPhone 采第一人称人类动作数据（比 teleop 便宜的那条路）。
- **Adamo**——2025 出 stealth，**managed teleoperation 服务** + **sub-40ms** teleop 软件，卖给机器人公司。
- **Telexistence**（日）——2026-01 起商用**机器人动作数据集生成服务**（2025-09 开预订）。
- **AgiBot / 智元（Zhiyuan）**（中）——**AGIBOT WORLD 2026** 开源数据集（100% 真实场景、自由式采集、BLOS 第一人称远程、力控采集，五阶段发布）；**Genie Sim 3.0**（CES 2026，首个建在真实机器人操作上的开源仿真平台）。**中国"数据+仿真"一体化的头部**。
- **Genesis AI**——**$105M 种子**（Khosla 领）；**Dyna Robotics**——**$120M A**——两家是"基础模型+数据引擎全栈"（严格说跨 P8/OEM，列此作数据侧参照）。

**B. 逐帧核验 / 标注（P8.④）**
- **Encord**——累计 **$110M**，物理 AI 数据服务 + AI 辅助多模态标注（LiDAR/雷达/视频/3D 点云）全栈。
- **Objectways**——托管定制采集 + robotics-grade 标注（robot-matched FOV、逐关节手姿、多模态同步）。
- **Labelbox / Labellerr / Build AI / Unidata / truelabel**——物理 AI 标注/egocentric 数据供给梯队（多为服务型，投资性偏薄，但定义了单价与产能）。

**C. 车队远程监管 / wrangler（P8.②）——多脱胎自 AV teleop**
- **Ottopia**（以）——混合 AI teleop，最大化"每操作员管多少车"。
- **Fernride**（德）——**€75M+**、150+ 人，"human-assisted autonomy"码头/堆场卡车，teleop 中心处理边缘案例。
- **Vay**（德）——teledriving（真人远程把车开到客户处）。
- **参照系**：Cruise 2024 曾 ~1.5 人/AV（远程操作含在内）——**wrangler 头数随车队线性长**；AV 侧的 RA（remote assistance）/RD（remote driving）二分法，会平移到 humanoid 车队。

**D. 仿真 / 场景编写（P8.⑤）——带自我颠覆的双刃层**
- **World Labs**（Fei-Fei Li）——**融 $1B**（2026-02-18；AMD/Autodesk $200M/NVIDIA/Fidelity/Sea/Emerson）；**Marble**（文/图/视频生成持久 3D 世界）；**2026-07-21 收购 SceniX**（机器人仿真，专补 real-to-sim gap）。**空间智能→机器人仿真的最重注**。
- **AgiBot Genie Sim 3.0**（见上）、**NVIDIA Cosmos/NuRec**（`[$]` 底座）。

### 5.3 YC（重点 Summer 2026 / S26 及近批，联网核）

- **Hebbian Robotics（YC S26）**——**Physical AI 数据的"质量 API"**：不训模型就能评估机器人训练数据（含 teleop session）的质量，补"具身数据集缺可复现质量指标"这个洞。团队 Columbia + NUS，履历 Jane Street / Verkada / DeepMind / OpenAI。**这正是 P8.④ 核验层的"卖铲子"打法，也是最直接的"自动化一部分人类核验"的力量——既是 P8 玩家又是 P8 人类活的部分颠覆者**。
- **Cortex AI（YC S26）**——**真实职场机器人 + egocentric 数据集** + **human-in-the-loop rollouts（远程操作员在机器人失败时救场）**。**一家公司同时覆盖 P8.① 采集 + P8.② wrangler**——是把"救场"和"采数据"合一（1X 同型）的早期纯玩家。
- **读法**：S26 里 P8 相关的是**"数据质量/基础设施"角度（Hebbian）+ "真实场景采集+人在环"角度（Cortex）**，而不是又一个 humanoid 本体——这与 HTC"投数据层不投 OEM"完全一致。种子门在**数据质量/核验/垂直采集**这一侧仍开着；在 humanoid 本体侧早已关到实验室估值。

---

## 六、HTC 猎场读法

### 6.1 可下注的种子 / A wedge（具体细分 + 为什么护城河不迁移）

**这是整张物理地图上 HTC 论点最集中、种子门最开的一层**——因为它硬件解耦（P=1）、按人/流程扩张、尚未被现任吃掉（L=3 而非 5）。三个具体 wedge：

1. **"经核验的 ground-truth 数据"层（CyberOrigin 型），不是"原始 teleop 量"层。**
   - 为什么护城河不迁移：当 XDOF/AgiBot/Scale 把**原始 teleop 量**打成商品（单价被压、Scale 平移威胁大），**"质/逐帧核验/可组合的可信数据集"**是价值上浮的地方。护城河 = 专有核验流程 + 操作员供给网络 + 客户信任（实验室愿意为"能训出策略的干净数据"付溢价）。**GPT-6 级模型商品化只会加剧对好数据的争夺**（p0b §A.4）。
   - 反共识点：市场把"谁采得多"当赢家；真赢家是"谁的数据经得起逐帧核验、能复现地训出策略"。Hebbian 的"质量 API"证明"质量"正在成为独立品类。

2. **垂直场景的 teleop-数据-核验一体化（vertical embodied-data ops），不是水平通用采集。**
   - 为什么不迁移：通用水平采集会被 Scale/大 OEM 内化；但**某个垂直**（如无菌药厂操作、精密电子、特定食品处理）的 teleop+核验，护城河是**该垂直的专有任务数据 + 合规/无菌流程知识 + 留存的客户本体集成**——这些不跟着模型走。对标 P1 里"投数据/commissioning 层不投臂"的同一逻辑。

3. **机器人车队"wrangler + 现场 FDE"的 managed-service 层（人+流程，不是软件）。**
   - 为什么不迁移：Formant/InOrbit 卖的是 `[$]` 软件平台；但**"坐在平台前救场的操作员团队"和"上门装机维护的 FDE 团队"是人力 managed service**，随每台部署线性长、且被 MTBF 未披露/自主未达 80% 结构性锁死（第三节 ②C/③）。这是最"无聊但结实"的净新增人类盘，且几乎不被合成数据颠覆（合成数据颠覆的是采集①，不是救场②/维护③）。

### 6.2 该避开什么（OEM / 硬件资本坑）

- **避开 humanoid 本体 OEM**：Figure ~$39B、1X ~$10B、Skild >$14B、PI $5.6B（→$11B）——**资本重、估值已到实验室级、且"没有任何 humanoid 量产车队 >低几百台"**（p0b §C.2）。买本体 = 买一个 5–15 年硬件时间线的 `[$]` 资本故事，不是买 P8 的可投人类层。
- **避开把 `[$]` 服务市场当劳动盘**：Fact MR"人形车队管理 $45B(2036)"、"AV teleop $0.55B"、Dataintelo"teleop 云 $4.2B"——**全 report-mill，只读方向**。别用它们给 P8 的 `[W]` 定价，更别当"捕获"。
- **避开水平通用数据采集的红海**：XDOF/Mecka/AgiBot/Scale 已在水平采集堆资本；再进一个"通用 teleop 农场"是往被商品化的量里跳。要么上浮到质/核验，要么下沉到垂直。
- **避开"合成数据会赢者通吃"的乐观**同时也**别忽视它**：⑤A/⑤C 是跳变项。**纯 teleop 采集的独立公司**（无核验/无垂直护城河）最暴露于合成数据挤压——这类恰恰要避。
- **避开被 Scale/Labelbox 平移吃掉的水平标注**：数字标注巨头正横切物理（scale.com/physical-ai、UR AI Trainer）。独立标注/核验要有"具身特有的、非 Scale 能平移"的东西（逐关节手姿、力控、垂直合规），否则是给巨头的收购标的、不是独立公司。

### 6.3 三条带日期的证伪信号（到 2027Q4）

**证伪信号 = 会让"P8 是可投净新增层"这一判断翻掉的、可观测的事件。**

1. **【合成数据坍缩人类采集盘 — P8 最致命的自我颠覆】到 2027Q4：是否有 ≥1 家前沿 VLA 团队（PI/DeepMind/Figure/1X 级）公开宣称其量产策略"主要靠合成/仿真数据训练、真实 teleop 数据占比 <20%"，且被独立复现？**
   - **YES → 看空 P8.①/④**：真实 teleop 的人类工资盘会先被压，$5–15B 的最大一块（①$3–8B）缩水；P8 价值向 ⑤ 仿真（少数高 comp 头）和 ③ FDE 集中。CyberOrigin 型"ground-truth"仍可能作为"合成数据的锚点核验"存活，但盘子变薄。
   - **NO（三层栈 teleop+sim+人类视频 并存、真实数据仍是多样性/接触物理的必需）→ 维持 Medium、P8.① 继续 >100% YoY**。（当前状态：p0b §D 明确"三层并存、数据仍是共同瓶颈"——尚未坍缩。）

2. **【现任平移吃掉独立数据层 — L 从 3 升向 5】到 2027Q4：Scale AI（scale.com/physical-ai + UR AI Trainer 路线）或某大 OEM，是否推出"端到端具身数据+核验+仿真"的托管栈，并签下 ≥2 家前沿实验室的量产数据合同？**
   - **YES → 独立第三方数据公司（含 CyberOrigin 型）估值坍向"被收购/被平移"**；水平层归巨头，独立价值只剩"垂直+合规"的窄缝。L 上修至 4–5。
   - **NO（实验室继续多源采购、独立核验公司保住前沿客户）→ 维持 L=3、独立层可投**。

3. **【净新增劳动盘是否真的兑现 — 增速证实】到 2027Q4：具身数据/teleop 的采集专家梯队（CyberOrigin/AgiBot/1X/XDOF/Mecka 级）合计**经核验的**（非融资额、非 report-mill 服务市场）真实营收/在岗操作员头数，是否仍保持 >100% YoY？**
   - **YES → P8 从 Medium 升 Medium-High**，确认"机器人经济净新增劳动"是真实、在扩张的领先指标；HTC 可加注 6.1 的三个 wedge。
   - **NO（增速掉到 <50% YoY，或出现 11x/Builder.ai 型的"agent-washing"暴雷——即某数据公司被曝营收注水/操作员头数造假）→ 下修至 Low**，按"过早、盘子薄"处理，退回观察位。
   - **纪律**：兑现只认**经核验营收 / 在岗头数**——不认融资额（XDOF $70M、Mecka $60M 是部署资本速度，不是劳动兑现），不认 Fact MR/Dataintelo 的服务市场数字。

---

## Sources

**内部**：`p0_foundation.md`（耦合规则、capture、pilot-to-production 断崖、W8 家族先验）、`p0b_capability_refresh_2026-09.md`（§C 机器人前沿、§C.2 无量产 humanoid 车队/Unitree ~$9B、§D 具身数据/teleop 层 = 可投层、§F 缺失垂直扫描——**governs all capability claims**）、`p3_frozen_taxonomy.md`（W8 intake 规则、wage-bill denominator test、`[W]/[L]/[$]` 标签）、`v3_physicalai_architecture.md`（P1–P8 分区、§3.3 P8↔W8/P4 边界守则、§5 P8 block）、`v2_master.json`。

**联网核验 2026-09-16（Tier-2 除非另注；report-mill 服务市场数字一律"只读方向"，按 p0 R1–R9 降级，绝不当 `[W]`）**：
- CyberOrigin 定位/CyberCode 逐帧核验 — [cyberorigin.ai](https://cyberorigin.ai/)（公开融资数字未检索到确认，标"待补/未验证"，未臆造）
- 具身数据/teleop 融资与经济学 — [evsint 具身数据采集 teleop 指南 2026](https://www.evsint.com/embodied-ai-data-collection-teleoperation-sim-to-real-2026/)、[Teahose 机器人训练数据公司 2026](https://www.teahose.com/guides/robotics-training-data)（teleop $72–145/hr 中国、$90–150/hr 美、egocentric $25–60/hr；采集专家梯队 ~18 月成型）、[New Market Pitch 具身 AI 融资 2026](https://newmarketpitch.com/blogs/news/embodied-ai-funding-trends)（$5.6B YTD、RFM ~$2.28B/41%）
- XDOF $70M 出道 / 三层数据金字塔 — [SiliconANGLE](https://siliconangle.com/2026/06/17/robotic-teleoperation-data-startup-xdof-launches-70m-funding/)
- Mecka AI $60M（$25M A + $35M；Framework Ventures）egocentric — [Fortune](https://fortune.com/2026/06/01/mecka-ai-series-a-60-million-robotics-data-training/)
- Adamo managed teleop / sub-40ms、Telexistence 数据集服务 — [Labellerr teleop 服务商 2026](https://www.labellerr.com/blog/top-teleoperation-companies-humanoid-robotics/)、[Businesswire Telexistence](https://businesswire.com/news/home/20250825662344/en/)
- AgiBot WORLD 2026 数据集（自由式/BLOS/力控/五阶段）、Genie Sim 3.0（CES 2026） — [The Robot Report](https://www.therobotreport.com/agibot-world-2026-dataset-open-source-accelerate-embodied-ai-development/)、[PRNewswire Genie Sim 3.0](https://www.prnewswire.com/news-releases/agibot-unveils-genie-sim-3-0-at-ces-2026--the-first-open-source-simulation-platform-built-on-real-world-robot-operations-302653656.html)
- 1X Neo teleop-first / 1X Experts / Redwood 数据飞轮 — [The Robot Report — teleop not autonomy for Neo](https://www.therobotreport.com/teleop-not-autonomy-the-path-for-1x-neo-humanoid/)
- 车队运维（RobOps）：Formant / InOrbit OpenRobOps ISO 21423 / Freedom / AWS RoboRunner；humanoid 车队管理服务市场 $0.6B(2026)→$45B(2036)（report-mill，只读方向）— [Standard Bots 车队软件 2026](https://standardbots.com/blog/robot-fleet-management-software)、[The Robot Report InOrbit OpenRobOps](https://www.therobotreport.com/inorbit-ai-releases-openrobops-iso-21423-reference-implementation/)、[Fact MR humanoid 车队管理](https://www.factmr.com/report/humanoid-robot-fleet-management-services-market)
- AV teleop 参照（Ottopia/Fernride €75M/Vay；Cruise ~1.5 人/AV；RA vs RD） — [EE Times teleoperation & AVs](https://www.eetimes.com/teleoperation-how-will-it-impact-avs/)、[Ottopia](https://www.ottopia.tech/)
- Scale AI 物理 AI 横切 / UR AI Trainer（GTC 2026，Universal Robots） — [Scale Physical AI](https://scale.com/physical-ai)、[Universal Robots × Scale AI Trainer](https://www.universal-robots.com/news-and-media/news-center/universal-robots-scale-ai-launch-imitation-learning-system-accelerate-ai-training-lab-to-factory/)
- 仿真/合成数据：NVIDIA Cosmos/NuRec 3D 高斯泼溅/Physical AI Data Factory Blueprint（合成 1 万段 ~$10–15k vs 真实 $50 万+） — [NVIDIA Newsroom Omniverse/Cosmos](https://nvidianews.nvidia.com/news/nvidia-opens-portals-to-world-of-robotics-with-new-omniverse-libraries-cosmos-physical-ai-models-and-ai-computing-infrastructure)、[Spheron Cosmos 合成数据经济学](https://www.spheron.network/blog/deploy-nvidia-cosmos-gpu-cloud-synthetic-data/)
- World Labs $1B / Marble / 收购 SceniX（real-to-sim） — [World Labs 融资 2026](https://www.worldlabs.ai/blog/funding-2026)、[explainx World Labs 收 SceniX](https://explainx.ai/blog/world-labs-acquires-scenix-robotics-simulation-2026)
- 数据核验/标注：Encord $110M / Objectways / Build AI — [Encord 物理 AI 数据服务](https://encord.com/physical-ai-data-services/)、[Labellerr 机器人标注公司 2026](https://www.labellerr.com/blog/top-robotics-annotation-platforms/)
- 集成/维护人力缺口（物理 FDE）：Deloitte 75% 制造商招不满 / 新岗位（fleet manager、AI trainer、maintenance tech） — [Propellence 机器人趋势 2026](https://propellence.com/blog/robotics-industry-trends-2026.html)、[RoboZaps humanoid at work 2026](https://blog.robozaps.com/b/humanoid-robots-in-workplace)
- YC S26：Hebbian Robotics（数据质量 API）、Cortex AI（真实场景采集 + human-in-loop rollout） — [Dealroom — Hebbian Robotics YC S26](https://app.dealroom.co/news/note/hebbian-robotics-launches-from-yc-s26-with-data-quality-apis-for-robotics)、[YC 制造与机器人公司](https://www.ycombinator.com/companies/industry/manufacturing-and-robotics)
- Genesis AI $105M 种子 / Dyna Robotics $120M A（数据侧参照） — [TechFundingNews Genesis AI](https://techfundingnews.com/genesis-ai-105m-seed-funding/)、[New Market Pitch 具身 AI 融资榜](https://newmarketpitch.com/blogs/news/embodied-ai-top-startups-fundraising)

**Sourcing caveats（p0 R1–R9）**：P8 的**金额（$5–15B `[W]`）是自下而上的薄估**，头数与 comp 均低置信度，中国权重压低金额加权——标 **Medium conviction**。一切"服务/软件市场规模"（Fact MR、Dataintelo）为 **`[$]` report-mill，只读方向、绝不当劳动线或捕获**。融资额（XDOF $70M、Mecka $60M、World Labs $1B、Genesis $105M、Dyna $120M、Encord $110M）为**部署资本速度，不是营收、更不是劳动兑现**（p0 R2、ARR Reality Ladder Tier-D）。CyberOrigin 具体融资数字**未在本轮联网中检索到确认，标待补，未臆造**。所有能力主张（无量产 humanoid 车队、合成数据 vs 真实数据三层栈并存、GPT-6 未解锁物理）严格以 **p0b** 为准。
