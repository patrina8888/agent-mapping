# v3 证据包 — 子家族 P2：有界空间移动 + 一线体力服务

**Bounded-Space Mobility & Frontline Service-Physical**

HTC internal · **2026-09-16** · Family P（PhysicalAI / 具身智能）第二个子家族的完整证据包。
上游依据：`v3_physicalai_architecture.md`（P 家族分区，P2 定义与不重复计数证明）、`p3_frozen_taxonomy.md`（冻结的 76 行、W5.1/W5.5/W10 原始行、评分轴、工资盘denominator 规则）、`p0_foundation.md`（耦合规则、捕获率、试点到量产的鸿沟）、`p0b_capability_refresh_2026-09.md`（**本包所有能力主张以 p0b 为准**：GPT-6 只是增量、没有量产 humanoid 车队、数据层才是可投层）。

> **三条非谈判纪律（贯穿全包，每个数字都受它约束）**
> 1. **耦合（coupling）。** 耦合赛道的厂商可实现 TAM = 捕获率 × 被替代的工资盘（displaced wage bill）。**永远不要把软件 TAM 和劳动 TAM 相加**——它们是同一笔钱的两个视角。叠加层（W10 零售/餐饮/配送的体力切片）是**非相加的重切（re-cut）**，绝不并入分区总额。
> 2. **能力 ≠ 捕获，且今天物理捕获 <1.5%。** 部署落后能力约 10 倍（MIT 95% 零 P&L、S&P 42% 试点弃用）。更强的机器人"大脑"（π0.7、Gemini Robotics 1.5、GR00T-N2、Skild）过去 6–9 个月在**软件**上提升了跨本体（cross-embodiment，一个大脑控多种机器人身体）和组合泛化——但**没有**移动 P2 的绑定闸门。
> 3. **物理缺口是硬件时间线问题（5–15 年），基本与模型 IQ 无关。** P2 的绑定闸门是**最后 10% 的边缘案例（edge cases）+ 单机经济学（unit economics）**，不是大语言模型的智商。

---

## 一、这是什么 + 为什么值得看

### 1.1 定义与边界

P2 = **在"已建图、有边界、且与人共享"的空间里做自主移动 + 轻操作（light manipulation，简单的抓放/牵引/对接，不是灵巧手作）的体力工作**。用大白话说：机器人在一个它大致认得、但有活人走来走去的场地里，把东西从 A 挪到 B，顺便做点简单动作。

**装进来的具体工种（scope）：**
- **仓库货物搬运 / AMR 内部物流**（AMR = Autonomous Mobile Robot，自主移动机器人；intralogistics = 仓库内部的搬运调度）——把货架、料箱（tote）、拖车里的货挪到拣货位、传送带、打包区。
- **商用地面清洁**——洗地机器人在商场、机场、写字楼大堂扫地拖地。
- **室内 / 人行道配送 + 前台接待机器人**——把外卖/包裹沿人行道送到门口，或在酒店/写字楼大堂送物、迎宾。
- **零售货架补货 / 盘点**——扫描货架缺货、错价（补货这一步下面会说其实还做不到）。
- **餐厅传菜 / 收台（food-running / bussing）**——把菜从后厨端到桌边、把脏盘收回。

**边界（不装进来的）：**
- **抓取灵巧作业**（piece-picking 单件拣选、码垛的精细抓放）→ 归 **P1**（结构化单元格操作）。P2 只做"移动 + 轻碰"。
- **开放道路的自动驾驶**（robotaxi、干线卡车、公路最后一公里）→ 归 **P3**，因为它的闸门是 R=5 的监管/安全论证/保险，不是边缘案例。
- **可变形/接触密集操作**（酒店铺床、洗衣、炒菜）→ 归 **P5**（灵巧前沿）。
- **零售/餐饮里的"数字/交易"切片**——收银、自助结账、语音点单——**留在它们的数字老家**（W1.7 后台 / W3 人际 / 自助结账算 `[$]` 资本），不进 P2。这是"叠加/重切 vs 分区"的老规矩：W10 那 $2.35T 的**全额永远不重复并入** PhysicalAI，只把它的**具身切片**盖一次章。

### 1.2 劳动盘子（labor TAM）与依据

**分区口径（partition，每一冻结美元只算一次）：约 $1.05T `[W]`**
- **W5.1 仓库货物搬运 & AMR**：**$0.7–1.0T `[W]`**（冻结值，中枢 ~$0.85T，在 4–5× 发达经济体薪酬带上）。依据：搬运/理货/叉车/手工搬运类工种（BLS "Laborers & Freight, Stock, and Material Movers" 美国约 280 万人 × ~$37K，加上 stockers/理货），按发达经济体薪酬加权。
- **W5.5 商用地面清洁（结构化切片）**：**$150–250B `[W]`**。依据：清洁工（janitors/cleaners）里"结构化硬地面"这一可机器人化的子切片。

**叠加口径（overlay，只盖章、不并入上面的 $1.05T）：**
- W10.1 零售的**货架/盘点体力切片**、W10.3 餐饮的**传菜/收台体力切片**、W10.2 酒店的**配送/接待机器人切片**——按各自 W10 母行（$0.5–1.2T 级）里的体力比例盖章到 P2，**非相加**。收银/点单/前台语音留数字老家。

> **为什么这一段口径要写死**：这是 v2 反复出错的地方——把 $2.35T 的整个"零售劳动"当成机器人可捕获盘子会高估一个数量级。P2 真正的分区分母是 ~$1.05T，其余是重切。

### 1.3 为什么值得看（三点，都很反直觉）

1. **这是全物理地图里"生产级替代证据最硬"的一带。** 别的物理赛道都是 demo，P2 是**已经在量产环境里跑、且有近乎审计级替代证据**的一带——亚马逊 100 万+ 台机器人（下面详述）。
2. **但捕获率仍 <1%，而且钱不以 SaaS 形式落账。** 最大的替代者（亚马逊）把机器人**内部化**了，替代以"少雇人"而非厂商 ARR 的形式出现——这让"用厂商收入算捕获"的方法**结构性低估** P2 约 3–5 倍。即便如此，慷慨修正后捕获仍 <1.5%（守住纪律）。
3. **它是"能力成熟但价值不可投"的教科书案例。** 机器人是能干活的；问题是硬件在商品化（中国洗地机 ASP 压到 ~$8K）、价值归了 OEM 和买方的 opex 节省。**可投的不是底盘，是软件/数据/远程运维层**——这正是第六节要讲的猎场。

---

## 二、这份体力工作到底要做哪些步骤

把 P2 这一带的活拆成八步（对仓库 AMR、洗地、配送、传菜、盘点是通用骨架，各工种只是权重不同）：

| 步骤 | 大白话：人（或机器人）在做什么 |
|---|---|
| **S1 建图 + 定位** | 先把场地"记下来"：走一圈生成地图，之后随时知道自己在哪。（SLAM = 同步定位与建图） |
| **S2 自主导航 + 避障** | 从 A 走到 B，路上绕开货架、叉车、以及**活人**——人是会乱走的，这是难点。 |
| **S3 移动/牵引载荷** | 驮着料箱、拉着货架、托着菜盘、拖着洗地刷盘往前走。 |
| **S4 对接 / 装卸 / 交接** | 到位后把货**接上/放下**：从货架取箱、放上传送带、把菜盘停到桌边、把包裹放到门口、（拆拖车卸货最难）。 |
| **S5 轻操作** | 按电梯、开门、把商品**摆上货架**、扫描条码、贴标——简单动作，不是灵巧手作。 |
| **S6 边缘案例处理（最后 10%）** | 地上有水渍、过道被堵、卡住了、有人挡路或逗它、货掉了——**处理这些"意外"才是绑定闸门**。 |
| **S7 单机经济 + 机队调度** | 一台机器人一小时挣不挣得回成本；一群机器人怎么排队不打架、正常运行时间（uptime）够不够。 |
| **S8 远程接管 / 异常队列** | 机器人搞不定时，**远处一个人**接管把它解困——这是今天能跑的关键（也是 P8 数据/远程运维层的接口）。 |

> **关键认知**：S1–S3 十年前就基本解决了（经典 SLAM + 路径规划）；**S6 才是墙**。P2 不是"等大脑变聪明"的问题，是"边缘案例 + 单机账"的问题。

---

## 三、每一步 AI + 机器人现在能不能做（核心表）

**读法：**「软件/大脑」= 感知/规划/VLA 模型进步；「硬件/身体」= 底盘/机械臂/传感器/成本时间线。**诚实标注哪些是硬件卡住（非模型问题）。**
（VLA = Vision-Language-Action model，视觉-语言-动作模型，机器人的"大脑"。）

| 步骤 | 2025 年底（能/半能/不能 + 靠哪个模型×硬件） | 2026 年 9 月（+具体产品/VLA/机器人） | 这窗口新解锁? | 备注（大脑 vs 身体） |
|---|---|---|---|---|
| **S1 建图+定位** | **能**。经典 SLAM 成熟，AMR/洗地机/送餐机标配。 | **能**。无实质变化。 | 否 | 早就解决，**非闸门**。 |
| **S2 导航+避障（有人环境）** | **半能→能**。有界空间稳；拥挤/动态人流仍有边缘案例。靠经典规划 + 局部 CV（计算机视觉）。 | **能（有界内）**。VLA 感知（Gemini Robotics 1.5、GR00T-N1.7）在"读懂场景"上边际帮忙；但绑定的是几何避障，非语义。 | 否（渐进） | **大脑进步 ≠ 闸门移动**。P2 移动早已由经典栈解决，VLA 帮的是长尾感知，不是核心能力。 |
| **S3 移动/牵引载荷** | **能**。AMR 驮箱/牵引货架、洗地刷盘、送餐托盘均成熟。 | **能**。Locus Array（2026-04）把"货到人"升级到"机器人到货"的移动搬运。 | 否 | 纯**硬件已成熟**。 |
| **S4 对接/装卸/交接** | **半能**。结构化交接（料箱上传送带、菜盘到桌、包裹落门口）能；**拆拖车卸散货**很难。 | **半能→改善**。YC S26 **Manifold** 做自主拆拖车/卸货/码垛"按次计价"、已在仓库跑——但这偏 P1 灵巧边界。 | 部分（卸货） | 卸拖车是**硬件+灵巧**卡点，非模型；结构化交接靠夹具工程。 |
| **S5 轻操作（摆货架/按电梯/扫描）** | **半能**。扫描/盘点能（Simbe Tally 98–99% 准）；**把商品摆上货架做不到**；电梯/门靠 IoT API 打通，非机械臂。 | **半能，无实质突破**。Simbe 反而加**固定传感器（Spot）**去补机器人——承认纯移动机器人做不全。 | 否 | **补货这一步是硬件/灵巧墙**：这正是零售盘点机器人只"看"不"补"的原因。 |
| **S6 边缘案例（最后 10%）** | **不能→半能**。溢洒/堵路/卡死/人际意外仍需人接管。这是**绑定闸门**。 | **半能**。Serve 上半年**暂停铺新机**，转去抠利用率/整合——等于承认这道墙还在。 | 否（仍是墙） | **既是硬件也是长尾数据问题**；不是 GPT-6 能解的。**GPT-6 Astra 对 P2 零贡献**（纯数字模型，不碰移动）。 |
| **S7 单机经济+机队调度** | **半能**。单机账在补贴下勉强；多厂商机队各说各话、互不相通。 | **改善（本窗口最实动作）**。VDA 5050 v3.0（2026-03）多厂商互通标准落地；亚马逊 DeepFleet AI 调度 −10% 行驶时间。 | **是（部署/经济，非能力）** | **这是本窗口 P2 真正移动的地方**——但它是**运营/经济学解锁，不是能力步变**。 |
| **S8 远程接管/异常队列** | **能，但人在环**。每支"自主"车队背后有人兜底。 | **能，人在环（且这是可投层）**。远程运维/teleop 托管服务在成形（AV 远程协助最成熟）。 | 否 | **这是特性不是缺陷**：人在环正是今天能跑的原因，也是 **P8 数据/远程运维**的商业入口。 |

**三句话总结这张表：**
- **能力早已够，闸门在别处。** S1–S3 十年前就成；S6（最后 10%）和 S7（单机账）才是墙——**都不是模型 IQ 问题**。
- **本窗口的进步是"部署/经济学"不是"能力步变"。** VDA5050 v3.0、DeepFleet、RaaS 收入过规模——这些让机器人**更好卖、更好管**，不是让它**更会干**。
- **大脑（VLA）进步真实但对 P2 边际。** π0.7/GR00T/Gemini Robotics 1.5 的跨本体泛化，主要利好 P1/P4/P5 的**操作**，P2 的**移动**早就不缺大脑。**GPT-6 Astra 明确没动 P2。**

---

## 四、耦合与捕获

**耦合类型：Coupled / Mixed（耦合，混合净效应）。**

- **定价即耦合证据。** P2 的主流商业模式是 RaaS（Robots-as-a-Service，机器人即服务）——按台/月（Locus 每台每月订阅、Bear ~$999/月）、按次拣选（Manifold "priced by the pick"）、按次配送（Serve/Coco）。这些**计量的是"被替代工人的产出对标人的工资"**，所以是耦合——软件收入和劳动替代是同一笔钱的两个视角，**不相加**。

- **当前捕获（守 <1.5% 纪律）：<1%。**
  - 以厂商可归因收入除以工资盘：仓库搬运可归因厂商收入约 $2–4B ÷ ~$0.85T ≈ **0.3–0.5%**。清洁、配送、传菜同样 <1%（配送机器人仍在**试点补贴**下跑，实捕获 <0.5%）。
  - **结构性低估警告：** 最大替代者亚马逊把机器人内部化了（100 万+台、ex-Kiva、DeepFleet 自研），替代以**"避免招聘"**而非厂商 ARR 出现——泄露内部文件（NYT，2025-10）：到 **2027 年避免招 16 万+ 人**、到 2033 年最多 60 万；Shreveport 模板厂 ~1000 台机器人、少雇 ~25% 工人、每件省 ~30¢、计划 2027 年底复制到 ~40 个厂。**按"避免招聘 + 单件人工"口径，P2 被低估 ~3–5 倍；但即便如此，修正后捕获仍 <1.5%**（守住 p3 物理纪律）。

- **净效应（net）：Mixed（混合）。** = 搬运/传菜/清洁劳动的压缩 + 吞吐扩张 + 亚马逊式避免招聘（不落厂商账）。**不是清洁替代**：酒店/餐饮在用工荒下"用机器人补填不满的岗"，偏 Expansion 味；仓库偏 Compression。

- **Conviction（信念度）：替代清晰度 High，可投性 Low。**
  - **替代 High**：W5.1 是全物理地图**唯一有硬、近审计级生产替代证据**的赛道——真实且在复利，只是不以 SaaS 落账。
  - **可投 Low / incumbent-captured**：底盘商品化、价值归 OEM 和买方 opex。把 W5.5（洗地）当作"物理劳动可捕获"的**概念验证经济学**看，别当种子部署地。

- **Denominator（分母，不与别处重复计）：**
  - 分区 `[W]` = **~$1.05T**（W5.1 $0.85T + W5.5 $0.2T），发达经济体加权，**只算一次**。
  - W10 零售/餐饮/酒店的体力切片是**叠加盖章、非相加**，不进这 $1.05T。
  - 机器人硬件/算力资本是 `[$]`（2026 年仓储机器人厂商+系统收入 ~$5–7B、清洁机器人市场 ~$1.8–3.1B、配送机器人服务收入 ~$0.1–0.25B），**永不与 `[W]` 相加**。

---

## 五、竞争格局（具体到公司名）

### 5.1 巨头 / OEM / 现任（硬件与平台）——这一层已被现任占住

- **Amazon Robotics（现任之王）**：100 万+ 台部署机器人（2025-07）；**DeepFleet** 自研调度 AI（−10% 行驶时间）；Shreveport 下一代模板厂。**关键**：它把机器人栈**垂直内部化**了，捕获以避免招聘（16 万/2027、60 万/2033）而非厂商 ARR 出现——**它不是你能投的，它是你要绕开的护城河（DeepFleet 的自有数据优势）**。
- **Symbotic（SYM，已上市）**：backlog **$22.5B**、57 套系统部署中；**沃尔玛占 FY25 收入 85%**（客户集中风险）；2025 年初收购沃尔玛机器人部门、合同到 2037。系统集成 + 资本重、**沃尔玛captive**。
- **Geekplus（Geek+，2025 港交所上市）**、**Exotec（~$2B）**、**Zebra/Fetch**：横向 AMR OEM，均已晚期/上市。
- **服务/清洁侧现任**：**LG**（控股 Bear Robotics 51%）、**SoftBank Robotics**（联合开发 + Whiz 洗地）、**Brain Corp**（BrainOS 平台驱动 Tennant/Whiz）、**Tennant/Nilfisk**（清洁设备现任）、**NCR/Toshiba**（自助结账现任，属数字切片）、**Oracle Opera/Cloudbeds**（酒店 PMS 现任）。

### 5.2 独立 startup（名字 + 阶段 + 融资 + 一句话）

- **Locus Robotics** — 晚期，**$180M ARR（2026-06，Sacra）**（较 2025 年底 $165M 增长）、~$2B 估值（2022 F 轮）、2026 又加 Series G $41.6M；纯 RaaS 每台每月订阅。仓库 AMR 的独立龙头，2026-04 推 Locus Array 移动搬运、5 月收购 Nexera。**种子门已关**。
- **Serve Robotics** — **已上市（NASDAQ: SERV）**，~2000 台机器人、44 城/14 州；FY26 指引 **$26M**、Q2 收入同比 +400%、经常性收入过 50%、现金 $240M+；**上半年主动暂停铺新机**去抠利用率——诚实的"最后 10% 墙"信号。
- **Coco Robotics** — 成长期，累计 **$123M**（2025 年 $80M 轮，Sam/Max Altman 投）、1300 台→目标 2026 年 1 万台、50 万+次配送（迈阿密/LA/芝加哥/赫尔辛基）、接 Uber/DoorDash、与 OpenAI 合作（用其模型、回传数据）。**仍靠试点补贴，单机账未证。**
- **Bear Robotics** — **LG 控股（51%）**，Servi Q（2026-05，联合 SoftBank Robotics，紧凑型）、Servi Plus（88 磅载重传菜/收台）、2026-07 起加自主清洁。传菜机龙头但已被 LG 收编。
- **Simbe Robotics** — Tally 3 货架扫描/盘点，数千门店、98–99% 准、$30–50K/店/年、Harmons 17 店；2026 加固定传感器 Spot 补机器人。**只"看"不"补"**（补货是硬件墙）。
- **Gausium（高仙）** — 中国洗地价格领导者，Mira/Marvel 2026 系列、机场/地铁规模部署、50+ 型号从 $8K 起。**把 ASP 压到 ~$8K，商品化底盘。**
- **Avidbots** — $70M Series C，Neo/Kas 洗地机。
- **Pudu（普渡）/ Keenon（擎朗）** — 中国传菜/服务机器人，BellaBot/送餐；智能服务机器人市场传 2033 年 $6.6B。
- **Starship（$339M，人行道配送）、Nuro（$6B，已转"Nuro Driver"授权）** — 配送侧，多已资本重或转授权。

### 5.3 YC（重点 Summer 2026 / S26 及近批，联网核实）

**批次背景（2026-09-10 Demo Day，史上最大批，235–245 家，~1500 投资人）：** **Industrials（机器人/制造/硬件/能源/国防/物流）占 23%**（上批 12.8%、五年均值仅 6.6%）——被称"Return of the Atoms（原子的回归）"，硬科技/国防明显抬头。P2 相关：

- **Manifold Industries（S26）** — 自主仓库机器人：单件拣选、拆拖车装卸、码垛，**"按次拣选"计价、已在仓库跑**；团队含 Caltech/Penn 研究者 + 仓库运营者 + Balyasny/Starwood 校友。**注意**：拣选偏 P1 灵巧边界，但仓库物流 P2 邻接、且是"按产出计价"的干净耦合样本——**S26 里最贴 P1/P2 的一家**。
- **Proprio Robotics（S26）** — 机器人**运维数据中心**：组装服务器、7×24 维护在役机房、回收上代部件。有界设施内移动+操作，偏 P1/P4，但"有界人共享空间"属性与 P2 同源，**且踩中 AI 算力 capex 顺风**。
- **Salem Robotics（S26）** — 机器人方向，细节尚薄，待跟踪。
- **读法**：S26 的 P2 相关标的集中在**仓库/数据中心的按产出计价服务**，而非横向底盘——这与第六节"投软件/数据层、别投 OEM"的结论一致。横向 AMR/送餐/洗地的种子门在 YC 层面也已基本关闭（龙头已上市或被 LG/沃尔玛/亚马逊收编）。

---

## 六、HTC 猎场读法

### 6.1 可下注的种子/A wedge（具体细分 + 为什么护城河不迁移）

横向 AMR/OEM 的**种子门已关**（Locus 晚期、Symbotic/Serve/Geekplus 上市、Bear 被 LG 收、Amazon 内部化）。可投的是**硬件解耦**的软件/数据/运维层——三条：

1. **厂商中立的多机队编排 / 仓库执行中间件（WES middleware）。** 顺风是 **VDA 5050 v3.0（2026-03）** 多厂商互通标准 + "2026 年 >50% 内部物流机器人用户上多智能体编排平台"。为**非亚马逊长尾**（沃尔玛以外的仓、混合品牌机队）做统一调度/执行层，正面对抗 DeepFleet 的**自有数据优势**。**护城河为何不迁移**：价值归于**谁拥有跨厂商集成 + 运营异常数据**——这份数据随部署复利、且单个 OEM 拿不走（OEM 只想锁自己的机队）。现有玩家（KINEXON、Goat Robotics、SVT SOFTBOT）仍浅，种子有位。
2. **远程运维 / 异常队列托管服务（→ P8，本命 thesis 车道）。** 每支部署车队都需要 S8 的"机器人 wrangler（解困员）"——把它做成托管服务，就是 **CyberOrigin 邻接的具身数据/远程操作价值层**。**护城河为何不迁移**：它硬件解耦、按人和流程扩（非 capex）、且**尚未被现任占领**——正是 p0b §D 和 HTC 机器人 thesis 点名的层。人在环不是缺陷，是今天唯一能跑的形态，且顺带产出训练 VLA 的帧级验证数据。
3. **单一有界细分的"最后 10%"垂直自治（S6 攻坚）。** 挑一个窄场景（某类仓/某类零售/某类园区配送），把边缘案例数据攒成复利护城河。**护城河为何不迁移**：长尾边缘案例数据是场景专属的，横向大脑（VLA）给不了。

**诊断非负商量：** 只认**审计级留存 ARR + 毛/净流失**，不认部署台数或 run-rate（11x/Builder.ai 是前车之鉴）。

### 6.2 该避开什么（OEM / 硬件资本坑）

- **横向 AMR / 送餐 / 洗地底盘 OEM。** 底盘在商品化（高仙把洗地 ASP 压到 ~$8K；配送机器人试点补贴、捕获 <0.5%），价值归买方 opex，**风险投资无回报**。
- **任何按"机器人市场 TAM 报告"定价的标的**（$50B 最后一公里、$6.6B 服务机器人 2033）——那是 TAM 不是部署劳动捕获。
- **亚马逊 / 沃尔玛 captive 供应链**（DeepFleet 内部化、Symbotic 85% 靠沃尔玛）——客户集中 + 现任占位。
- **humanoid（人形）OEM。** 与 P2 无关且不可投：估值 ≠ 部署劳动，**没有任何 humanoid 在持续商用价位下部署超过低百台**（p0b：Unitree 公开市值 ~$9B 非 $50B 谣传；Figure 03 是 demo 非车队）。
- **纯硬件卖断、ASP <$10K、无软件 attach 的清洁/配送**——那是商品化硬件竞赛，~0 startup 价值捕获（W5.5 冻结信念度 High 是替代**清晰度**，不是可投性）。

### 6.3 三条带日期的证伪信号（到 2027Q4）

1. **【替代是否真实·仓库】到 2027Q4：** 亚马逊是否运营 **≥40 个 Shreveport 设计的配送中心、且单件人工持续低 ≥25%，同时美国履约岗位持平或下降而发货量上升**（核对 BLS + 10-K）？
   - **是 → 避免招聘式替代真实且在复利**，P2 的 Compression 坐实、把 W5.1 按"避免招聘 + 单件人工"重算（捕获仍 <1.5% 但结构性上修）。
   - **否**（避免招聘停滞、Symbotic 把 $22.5B backlog 转成部署系统 <25%、单厂人均岗位回升）**→ 撞上可靠性/ROI 墙**，增量-仅/现任占位读法确认。

2. **【单机经济·配送/服务】到 2027Q4：** 是否有人行道/室内配送运营商（Coco 目标 1 万台 / Serve 过 2 千台）在**非补贴、≥1 万台持续商用**下公布**优于人工快递员的单次经济账**？或某餐饮连锁报告**可归因于服务机器人的前厅工时下降**（而非把点单员挪去后厨）？
   - **是 → 最后 10% + 单机账墙被突破**，配送/服务切片开始真替代。
   - **否 / 持续试点补贴到 2027 → 墙仍在**，替代递延；这是最可能的基线。

3. **【可投层是否成立·编排/运维】到 2027Q4：** 是否有**厂商中立的多机队编排 或 机器人远程运维托管服务**，在**非亚马逊长尾**上做到 **>$25–50M 留存 ARR、净收入留存（NRR）>100%**？
   - **是 → 硬件解耦的软件/数据 wedge 成立**，HTC 车道（6.1 之 1、2）验证，加仓。
   - **否**（DeepFleet 式 captive 平台 + OEM 原生机队软件占住这层）**→ 中间件 wedge 被现任压缩**，撤回纯数据/远程操作层（P8）——即"投数据层、别投编排应用层"。

---

## 来源（Web-verified 2026-09-16；Tier-2 aggregator 标注，仅取方向；估值/台数不折算部署劳动）

**仓库 AMR / 货物搬运：**
- [Sacra — Locus Robotics revenue](https://sacra.com/c/locus-robotics/)（$180M ARR 2026-06，纯 RaaS）· [Robotics247 — Locus Series F ~$2B](https://www.robotics247.com/article/locus_robotics_raises_117m_series_f_round_bringing_valuation_nearly_2b/warehouse) · [TechCompanyNews — Locus Series G $41.6M / Array / Nexera](https://www.techcompanynews.com/locus-robotics-raises-41-6-million-in-series-g-funding/)
- [Motley Fool — Symbotic $22.5B backlog, 57 systems, Walmart 85%](https://www.fool.com/investing/2026/09/01/symbotics-backlog-sits-at-x-billion-heres-the-cust/) · [StockTitan — SYM 10-K](https://www.stocktitan.net/sec-filings/SYM/10-k-symbotic-inc-files-annual-report-b238fde66e2e.html)
- [TechCrunch — Amazon 1M robots + DeepFleet](https://techcrunch.com/2025/07/01/amazon-deploys-its-1-millionth-robot-releases-generative-ai-model/) · [AboutAmazon — 1M robots, foundation model](https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model)
- [Gizmodo — Amazon 避免招聘 60 万（泄露文件）](https://gizmodo.com/leaked-amazon-plans-say-robots-will-help-it-avoid-hiring-600000-workers-2000674920) · [Washington Times — 16 万/2027、60 万/2033、Shreveport 少雇 25%](https://www.washingtontimes.com/news/2025/oct/22/amazon-robots-could-replace-160000-new-jobs-2027-600000-2033/)

**清洁 / 服务 / 配送 / 零售：**
- [Gausium — 2026 商用清洁机器人部署](https://gausium.com/2026/08/26/cleaning-robots-large-commercial-facilities/) · [GrabaRobot — 2026 清洁机器人 50+ 型号从 $8K](https://www.grabarobot.com/robots/cleaning-robot/) · [Avidbots](https://avidbots.com/)（$70M Series C，Neo/Kas）
- [GlobeNewswire — Serve Robotics Q2 2026（+400% YoY、经常性 >50%、$240M 现金）](https://www.globenewswire.com/news-release/2026/08/06/3340828/0/en/serve-robotics-announces-second-quarter-2026-results.html) · [Seeking Alpha — Serve $26M 指引、暂停铺新机、~2000 台/44 城](https://seekingalpha.com/news/4590013-serve-robotics-reiterates-26m-2026-revenue-guidance-as-it-pauses-new-sidewalk-robot)
- [The Robot Report — Coco Robotics $80M / 1300→10000 台](https://www.therobotreport.com/coco-robotics-raises-80m-to-scale-sidewalk-delivery-robots/) · [Bloomberg — Altman-backed Coco $80M](https://www.bloomberg.com/news/articles/2025-06-11/altman-backed-delivery-startup-coco-robotics-raises-80-million)
- [RestaurantTechnologyNews — Bear Robotics Servi Q/Plus + 清洁（2026-07）](https://restauranttechnologynews.com/2026/07/bear-robotics-brings-physical-ai-service-robots-and-autonomous-cleaning-to-restaurants-and-hotels/) · [RestaurantTechnologyNews — LG 控股 Bear](https://restauranttechnologynews.com/2025/01/lg-bets-on-bear-robotics-to-serve-up-profitable-growth-in-the-autonomous-restaurant-waiter-market/)
- [Grocery Dive — Simbe 加固定传感器补机器人](https://www.grocerydive.com/news/simbe-spot-robotics-inventory-computer-vision-retail-grocery/736662/) · [Simbe — Tally](https://www.simberobotics.com/store-intelligence/tally)

**编排 / 互通 / YC：**
- [GoInvest — VDA 5050 v3.0.0（2026-03）多品牌机队互通](https://goinvest.com/2026/09/15/multi-brand-robot-integration-vda-5050-fleet-management-and-open-intralogistics/) · [Robotomated — 2026 AMR 机队管理软件](https://robotomated.com/learn/warehouse/amr-fleet-management-software)
- [Whalesbook — YC S26 转硬科技/国防、industrials 23%](https://www.whalesbook.com/news/English/startupsvc/Y-Combinator-S26-Demo-Day-Shifts-Toward-Hard-Tech-and-Defense/6aa70afb75fe79b492e5d068) · [Jared Heyman — On the YC S26 batch: Return of the Atoms](https://jaredheyman.medium.com/on-the-yc-s26-batch-return-of-the-atoms-2f6f47fd295a) · [Extruct — YC S26 full list](https://www.extruct.ai/data-room/ycombinator-companies-s26/)（Manifold、Proprio Robotics、Salem Robotics）

**内部依据：** `v3_physicalai_architecture.md`（P2 定义 §2/§5、straddler 盖章 §3.2）、`p3_frozen_taxonomy.md`（W5.1/W5.5/W10 冻结行、denominator 规则）、`p0_foundation.md`（耦合 §3、捕获率）、`p0b_capability_refresh_2026-09.md`（§C 机器人前沿、§D 具身数据/远程操作层——**治理本包所有能力主张**）、`v2_master.json`（冻结评分）。

**纪律声明（守 p0b + p0 R1–R9）：** GPT-6 Astra 对 P2 零贡献（数字模型）。VLA 大脑进步真实但对 P2 移动边际；P2 闸门是最后 10% 边缘案例 + 单机经济，**非模型 IQ、非硬件时间线以外的东西**。物理捕获守 <1.5%；亚马逊避免招聘让厂商-收入口径低估 ~3–5 倍，但修正后仍 <1.5%。台数/估值**永不折算为部署劳动**；配送/服务机器人 ARR 多为试点补贴、单机账未证——按 ARR Reality Ladder 折价。
