# v3 证据包 — P3：开放道路自动驾驶出行(Open-Road Autonomous Mobility / AV · Transport)

HTC internal · **2026-09-16** · PhysicalAI 家族分区 sub-family **P3** · 重归拢自 W9.1 / W9.2 / W9.3
框架纪律:coupling(耦合)· capability ≠ capture(能做 ≠ 抓到钱)· 物理捕获 <1.5%(此格 <1%)· 硬件/监管时间线 5–15 年 · 守 p0b 全部更正 · 用真实 2026 数据 · 大白话、术语首次出现即括注。

> **一句话定位**:P3 是整张物理地图里**唯一一个"身体动作本身几乎已经解决"的格子**——Waymo 到 2026 年 3 月已跑 **2.206 亿无人英里(rider-only miles,车里没有安全员)**,事故率显著低于人类。但它的**已实现劳动捕获仍 <1%**。原因不是"机器人手不够灵巧"(其他物理家族的卡点),而是 **R=5 的安全论证(safety case,向监管方证明"我足够安全"的一整套材料)+ 责任认定(liability)+ 保险 + 单车经济性(unit economics)+ 边缘长尾**。所以 P3 是"能力≠捕获"这条框架铁律最干净的实证案例:**大脑几乎到位,钱被制度和资本壁垒挡在门外,尾巴要拖十年。**

---

## 一、这是什么 + 为什么值得看(定义、边界、劳动盘子 labor TAM 及依据)

### 定义与边界
P3 = **在公共道路网络(public road)上完成"位移/运输"这件体力活**,physics(任务物理)本质就是"把车/货/人从 A 开到 B",即"just driving"。三条现有行拢进来:

- **W9.1 网约车 / 出租 / Robotaxi(无人出租车)** —— 载人。
- **W9.2 长途 + 区域卡车运输 / line-haul(干线运输,高速点到点的枢纽间运输)** —— 载货,重卡。
- **W9.3 最后一公里配送 / 快递(last-mile courier,人行道机器人 + 无人小车 + 无人机)** —— 载小件。

**边界(不重复计):**
- 仓库内搬运 / AMR(autonomous mobile robot,仓内自主移动机器人)、叉车 → 属 **W5.1 / W5.2**,不在 P3。P3 只算**上了公共道路**的。
- 派单/路由/呼叫中心里的**软件与语音坐席** → 是 W3.6 / W1.7 的数字劳动,不是 P3 的"开车"这块体力;但货运调度语音代理(freight dispatch voice agent)是 P3 的相邻猎场(见第六节),与 W3.6 交叉引用一次,不重复入盘。
- 国防/战场无人后勤 → 属 **W12.2**,主权捕获,单列。

### 劳动盘子(labor TAM)
按各行 [W](可替代工资盘子)口径,美国/发达经济体加权:

| 子行 | labor TAM `[W]` | 全球在岗(估) | 直接受威胁(估) | 近端"可耦合捕获"的真实切片 |
|---|---|---|---|---|
| W9.1 网约/出租/Robotaxi | **$0.3–0.5T** | ~47M | ~3.5M | 只有**已围栏运营域(ODD)内的城市按需出行**,远小于全盘 |
| W9.2 干线/区域卡车 | **$0.5–0.9T** | ~55M | ~5M | 只有 **~40% 的干线(line-haul)切片**近端可及;城配/末端派送(P&D)仍靠人 |
| W9.3 最后一公里配送 | **$0.3–0.6T** | ~30M | ~3.5M | 只有**适合人行道机器人/无人小车的短程稠密路线** |
| **P3 合计** | **~$1.1–2.0T `[W]`**(发达经济体加权;全球 ~2–2.5×) | ~130M | ~12M | **可耦合捕获切片 << 全盘**;当前已实现捕获 <1% |

依据:司机工资盘子用**低人均薪酬(low comp-per-head)× 巨大在岗数**,所以按"美元加权"看,P3 在整张图里被系统性**降权**(dollar-weighting de-emphasizes)——它头数吓人($1–2T 名义),但抓到的钱很少。W9.2 卡车里工资/福利约占大车队每一美元运营成本的 **~43 分**,是最诱人的成本项,但只有干线那 40% 近端可动。

### 为什么值得看(3 个理由)
1. **它是"能力≠捕获"的教科书案例。** 别的物理家族(W5/W6)是"大脑到位、身体做不到";P3 是"大脑和身体都基本到位、**制度和资本挡在门口**"。看懂 P3,就看懂了为什么"技术 demo 很炸"和"劳动被真实替代"之间隔着一条十年的河。
2. **2026 是它第一次出现"真·无安全员商业运营"的规模拐点信号**:Waymo $16B 融资 / $126B 估值、周付费单 50 万、NHTSA(美国高速公路安全管理局)**7 月发出史上首个 Robotaxi 商业豁免**、Zoox(亚马逊)拿到**无方向盘车联邦批准(最多 2,500 辆)**、Aurora 真·无人重卡上路。拐点在发生,但**捕获曲线仍是十年斜坡**。
3. **它在底下"长出一层净新增的机器人经济人力"**:远程操作员(teleoperator)、车队后勤、事件响应、道路救援——这层是硬件解耦、按人/流程扩张、尚未被现任吃掉的**可投层**,正对 HTC 机器人论文与 p0b 的"投数据/运营层、不投整车 OEM"立场。

---

## 二、这份体力工作到底要做哪些步骤(拆成阶段与步骤,每步大白话说人在做什么)

把"一个司机/骑手把车货人从 A 送到 B"这件事,拆成 8 步。每步先说**人现在在干嘛**:

1. **看清路况(感知 perception)** —— 人用眼睛看:车道、红绿灯、行人、其他车、施工、天气。要在雨雾夜里也看得清。
2. **想好怎么走(预测+决策 prediction & planning)** —— 人在脑子里预判"那个行人会不会突然横穿""前车要不要变道",然后决定加速、刹车、变道、让行。
3. **动手开(控制/执行 control / actuation)** —— 人踩油门刹车、打方向。到了车上就是"线控(drive-by-wire,电信号直接控制转向刹车)"这层机械动作。
4. **应付罕见怪事(长尾边缘场景 long-tail edge cases)** —— 人遇到"倒下的电线""交警手势""婚礼堵路""逆行电动车",靠常识临场处理。这是**开车最难、最要命的最后 1%**。
5. **远程兜底(远程接管/协助 teleop / remote assist)** —— 无人车卡住时,远端有人**给建议或接管**(注意:多数是"给路径建议"而非实时方向盘)。这是无人车队特有的新工种。
6. **车队后勤(充电/加油、清洁、维修、抛锚救援 depot & recovery)** —— 有人负责把车充上电、擦干净(乘客吐了得有人擦)、坏了拖回来修、轮胎瘪了去换。**全是手上的活。**
7. **派单/路由/交接(dispatch / routing / handoff)** —— 有人/系统分配订单、规划路线;载货要**装卸、和收货人交接**;末端配送要**把包裹放到门口**。
8. **安全论证/合规/保险(safety-case / regulatory / insurance sign-off)** —— 有人写材料向监管方证明"这套系统够安全"、买够责任险、出事了走理赔和法律。**这步不在路上,却是真正的闸门。**

关键观察:**第 1–4 步是"开车的大脑",第 3 步是"开车的身体(已成熟机械)",第 5–8 步是"让一支无人车队真的能挣钱运营的制度与后勤"**。P3 的钱卡在哪里,下一节的表说清楚。

---

## 三、每一步 AI+机器人现在能不能做(核心表)

图例:**能** / **半能**(限定运营域 ODD 内、或需人兜底)/ **不能**。
诚实区分:**「软件/大脑」进步**(模型层) vs **「硬件/身体」瓶颈**(硬件/单车经济/制度时间线,非模型问题)。
> **P3 的特殊之处**:与人形家族不同,P3 的"身体硬件"(传感器、线控底盘)早已成熟——所以这里的**硬件瓶颈主要是"单车成本经济性"和"后勤的手上活"**,而**真正的闸门是制度(监管/责任/保险)和长尾可靠性**,不是模型 IQ。

| 步骤 | 2025 年底(能/半能/不能 + 靠哪个模型×硬件) | 2026 年 9 月(+具体产品 / VLA / 机器人) | 这窗口是否新解锁 | 备注:软件大脑 vs 硬件/制度瓶颈 |
|---|---|---|---|---|
| **1. 感知路况** | **半能→能(域内)**。Waymo 多传感器(激光雷达 lidar + 摄像头 + 雷达)在测绘过的城市里稳;Tesla 纯视觉(camera-only)在 Austin 起步 | **能(域内)**。Waymo 到 3 月 **2.206 亿 rider-only 英里**;运营城市 10–14 个(9/1 新开 Denver/San Diego/Tampa) | **部分**(更多城市/天气,非质变) | **大脑到位、硬件到位**。传感器套件是成熟硬件,**不是**瓶颈;GPT-6 Astra 与此无关(AV 用专用驾驶栈,非通用 LLM) |
| **2. 预测+决策** | **半能(域内)**。规则+学习混合,靠高精地图兜底 | **半能→能(域内)**。端到端驾驶模型(end-to-end,像素直接出动作)成熟:Wayve、Waabi Driver 用"世界模型(world model,先在脑内模拟再动)";Waabi 6 月做到**驾驶栈迁移到 Volvo VNL 平台零重训** | **是**(泛化能力实打实前进) | **软件大脑真进步**,但仍是"域内可靠、域外掉链子";长尾未解(见第 4 行) |
| **3. 控制/执行(线控)** | **能**。线控底盘成熟数十年 | **能**。同 | 否 | **纯硬件、早解决**。**不是**任何瓶颈 |
| **4. 长尾边缘场景** | **不能**(罕见怪事仍是墙)。"最后 1% 可靠性"是硬约束 | **半能**(罕见场景仍需远程/保守停车)。这是 W1.7 里 OSWorld 2.0 那堵"长尾可靠性"墙的物理孪生 | **否** | **这是十年尾巴的根**。**模型 IQ 和 GPT-6 都解不了**——要的是海量真实驾驶数据 + 场景仿真 + 验证,是**数据/验证问题,不是大模型问题** |
| **5. 远程接管/协助** | **能但需人在环**。远端人给路径建议 | **能**。Waymo **~70 名远程操作员管 ~3,000 辆(约 1:43)**,一半在菲律宾;另设美国本土"事件响应队(Event Response Team)"处理撞后/急救协调 | 否(比例在改善) | **净新增人力层**。比例会压缩但多年内非零——这是可投的"机器人经济劳动层"(W8-physical) |
| **6. 车队后勤:充电/清洁/维修/救援** | **半能→不能**。充电桩自动化部分可,清洁/换胎/拖车全靠人(Transdev 等外包) | **不能(手上活)**。抛锚救援、车内清洁、轮胎更换无量产机器人 | **否** | **真·硬件时间线瓶颈**(与 W6 灵巧操作同源)。"擦掉乘客呕吐物 / 换爆胎的机器人"不存在——诚实标注:这块被硬件卡住,非模型问题 |
| **7. 派单/路由 + 装卸/门口交接** | **派单路由:能**(软件)。**装卸/交接:不能**(手上活) | **派单路由:能**(Uber 多模网络、车队管理软件)。**末端把包裹放到门口 / 重卡货物装卸:仍不能** | 否 | **分裂**:调度是已解决的软件;**物理交接是灵巧手瓶颈**(硬件时间线),这就是为什么 last-mile 的"最后 15 米"和卡车的 P&D 仍要人 |
| **8. 安全论证/监管/保险签核** | **半能**。工具在(Applied Intuition、Foretellix 场景仿真),但**签核是制度/法律** | **半能→机构级松动**。NHTSA **7 月发首个 Robotaxi 商业豁免**、streamline 豁免流程;Zoox 拿**无方向盘车联邦批准(≤2,500 辆/2 年)** | **是(制度侧,非模型侧)** | **真正的闸门,R=5**。**不是模型问题**,是监管/责任/保险的机构时间线。载人自驾运营强制 **$500 万/次商业伞险(commercial umbrella)= 人类车 5 倍** |

**读表结论**:P3 的进步几乎全在**第 1–2 步(大脑,域内)和第 8 步(制度侧松动)**;卡死的是**第 4 步(长尾,数据/验证问题)、第 6–7 步物理后勤(硬件时间线)、第 8 步的责任与保险(制度时间线)**。**没有一格是被"模型 IQ 不够"卡住的**——这正是 P3 与 W5/W6 的分野:它不是"造不出身体",是"制度/资本/长尾"这三样都要时间。

---

## 四、耦合与捕获(coupling 类型、当前 capture、net effect、conviction、denominator)

### 耦合类型
**Coupled / Mixed(耦合/混合)**。定价模型正好是耦合友好的:
- Robotaxi 走 **capex/RaaS(robot-as-a-service,按次/按里程/订阅计费)**——每一趟车费直接对标"本来要付司机的钱"。
- 卡车走 **per-mile / DaaS(Driver-as-a-Service,按里程卖"虚拟司机")**——Aurora、Kodiak 的模式,直接对标司机工资。
- Last-mile 走 **fee-per-delivery(按单计费)**——对标骑手每单成本。

所以**可以**用"capture-rate × displaced 司机工资盘子"来量。**但铁律不变:绝不把 SW 车费收入 + 司机工资两列相加**;车费本身就是司机工资的再分配视图。

### 当前 capture(守住 <1.5% 物理纪律 → 此格 <1%)
| 子行 | 2026 已实现车/货运收入(SW-TAM `[$]` 代理,**非**劳动捕获) | 对 labor 盘子的已实现捕获 |
|---|---|---|
| W9.1 Robotaxi | Waymo ~$355M 年化(2月)→ 冲 ~$1B(若达 1M 周单);Pony.ai Q2 robotaxi 收入 **$12.1M(+691%,基数极小)**;WeRide H1 收入 ~$51M;Apollo Go 累计 20M+ 单 | **<1%**(全盘 $0.3–0.5T)。**Waymo $126B 估值是估值,不是劳动捕获——不得换算成被替代司机数** |
| W9.2 卡车 | **<$100M** 商业自驾卡车收入(未规模化);Kodiak Q1 **$1.8M(+74%)**,28 辆无人车;Aurora 早期 per-mile | **~0%**(部署数百辆 vs ~200 万司机) |
| W9.3 Last-mile | ~$100–250M 全球配送机器人服务收入(多为试点补贴价);"$50B 末端机器人市场"是 **TAM 不是收入**,报告磨坊话术 | **<0.5%**(净骑手数仍在涨) |

**纪律**:Waymo $126B、Pony/WeRide 上市市值、"某某市场 $XXB" 全是**估值/TAM,不是被替代工资**。套 Unitree 规则:**永不把 Robotaxi 估值或"完成多少单"的头条换算成已部署劳动。**

### Net effect(净效应):**Mixed(混合,偏 Expansion 于近端)**
三股力量叠加,**不是**干净的"司机被裁":
1. **压缩(Compression)**:在围栏运营域内,机器替代了司机工时——真实但很小(<1%),且司机净头数**仍在涨**(gig 增长、卡车司机长期短缺 ~8.2 万缺口)。
2. **扩张(Expansion / 诱导需求)**:更便宜的出行会**诱导新需求**(以前不打车的人现在打),把盘子做大而非纯替代;卡车的干线自驾是**填短缺**而非净裁(短缺给了政治掩护,像 SOC/RCM,低反弹)。
3. **净新增(underneath)**:每支无人车队底下**长出**远程操作员、后勤、事件响应、救援——W8-physical 层的净新增工资盘子。Waymo 1:43 的远程操作比、Transdev 后勤外包、Uber **$100M 投 Robotaxi 基础设施**,都是这层在成形。

### Conviction / Denominator
- **Conviction:Medium**。能力侧证据强(Waymo 2.2 亿无人英里 + 保险级安全数据);但捕获侧被制度/资本/长尾压在 <1%,且是**十年斜坡**,不是 2026 事件。
- **Denominator(工资盘子,不与别处重复计)**:P3 = 司机工资盘子 ~$1.1–2.0T `[W]`(发达加权),**只算上了公共道路的位移劳动**;仓内 AMR 归 W5、国防无人后勤归 W12、货运调度语音归 W3.6——**各计一次,不重复**。W9.2 的干线切片与城配 P&D 要分开,只有 ~40% 干线近端可动。

---

## 五、竞争格局(具体到公司名)

### 5.1 巨头 / OEM / 现任(硬件与平台)—— 车辆层已被资本雄厚方占据
- **Alphabet / Waymo**:绝对领跑。2026 年 2 月 **$16B 融资 @ $126B 估值**;周付费单 **50 万**(2024/5 的 5 万 ×10),运营 10–14 城,9/1 新开 Denver/San Diego/Tampa;2026 目标 **周 100 万单(~$1B 年化;Q4 中位预测 ~71.3 万,大概率略欠)**;首次海外(伦敦、后东京)。**安全数据是它的护城河**:25.3M 无人英里仅 9 起财损 + 2 起人伤索赔;财损 -88% / 人伤 -92% vs 人类。
- **Tesla**:Austin 无安全员运营(54 车、两周 170 单全无车内安全员,但仍远程监督);上半年扩 Dallas/Houston/Phoenix/Miami/Orlando/Tampa/Vegas。Musk"年底全美铺开"**照例打折**——车少、仍远程兜底。纯视觉 + 量产车成本是它的赌注。
- **Amazon / Zoox**:7 月底拿 **NHTSA 无方向盘车联邦豁免(≤2,500 辆/2 年)**;8/10 起 **Vegas 付费**;SF/Austin/Miami 免费;累计近 100 万乘客。自研专用车,不是改装。
- **Baidu Apollo Go**:中国领跑,累计 **20M+ 单**,1,000+ 辆级车队,多城。
- **Uber**:**平台/需求聚合的关键现任**——不造车,but 把 Waymo、Waabi(robotaxi)、Serve、Nuro、Cartken、Avride、Coco 全接入,**$100M 投 Robotaxi 基础设施**。谁赢技术,Uber 都可能收需求端的过路费。
- **卡车 OEM**:Volvo Autonomous Solutions(与 Waabi 合造 VNL Autonomous,New River Valley 建厂)、International/Navistar(Aurora 用其 LT 平台)。**芯片/栈**:Nvidia(DRIVE)、Mobileye。**保险巨头**:传统车险正被"谁负责"重构(见下)。

### 5.2 独立 startup(名字 + 阶段 + 融资 + 一句话)
**机器人卡车(载货):**
- **Aurora Innovation**(上市 AUR):gen-2 无人重卡(International LT,造价约一代一半、100 万英里设计寿命)已**真·无人上路**;Sun Belt 10 条无人线路(含 FTW–El Paso 600 英里);**年底目标 200 辆无人车**;DaaS 模式面向 2027+;一客户拟购 500 辆。**最接近规模化的干线玩家。**
- **Kodiak AI**(上市,经 Ares SPAC,$2.5B 估值):Q1 收入 **$1.8M(+74%)**,28 辆无人车、23,500+ 付费小时、15,600+ 累计货运;近期 **$100M 融资但折价严重、股价一度 -37%**;长途干线无人年底冲。**规模真实但极小、二级市场已在打折。**
- **Waabi**(私有):1 月 **$1B 融资 + 借 Uber 拓 robotaxi**;世界模型驱动的 Waabi Driver,6 月做到零重训迁移 Volvo 平台;真·无人上路**延后几个季度**,现为德州带员试点。**技术叙事最性感、商业化最晚。**
- **Wayve**(私有):2 月 **$1.2B D 轮 @ $8.6B 估值**;端到端具身驾驶基础模型,主攻可迁移到量产车的 L2→L4。

**Robotaxi(载人):**
- **Pony.ai**(上市):车队 1,975 →目标 **3,500**;Q2 robotaxi 收入 $12.1M(+691%,小基数);H1 总收入 $70.47M。
- **WeRide**(上市):L4 车队 **3,400**(略大于 Pony);H1 收入 ~$51M(+73.3%),Q2 毛利 37.5%,单车日均 >21 单。
- **Nuro**(私有,~$6B):从造车**转型"Nuro Driver"授权**(把自驾栈卖给 OEM/车队),轻资产化。

**Last-mile(载小件):**
- **Serve Robotics**(上市):Uber 剥离;签 **Uber Eats 最多 2,000 台**部署;7-Eleven;数万单。
- **Coco Robotics**(私有):**$80M 融资**(Altman 兄弟等);50 万+ 零排放配送(LA/Chicago/Miami/Helsinki);**万台目标 2026(未证实)**。
- **Zipline**(私有,$1.75B):无人机配送;**Starship**(人行道机器人);Cartken、Avride、Ottonomy(尾部)。

**相邻"卖铲子"层(硬件解耦,真正可投处——见第六节):**
- **Applied Intuition**(私有,**$15B 估值**,$600M F 轮 2025/6,较 2024 E 轮 $6B 翻倍):AV 仿真 + 正扩向**安全论证自动化(safety-case automation)**。核心已太贵。
- **Foretellix**(私有,总融 $135M,$85M C 轮):**场景化安全验证 V&V**;Volvo 合作;与 Inverted AI 做混合仿真。
- **Oxa**(英,geofenced 场景)、**FERNRIDE**(码头/堆场无人牵引车,teleop 兜底)、**Clevon / GetUgo**(远程操作硬件+软件,一人管多车)、**driveblocks / Turing Drive**(off-road/园区)。

### 5.3 YC(重点 Summer 2026 / S26 及近批,联网搜)
S26 整批 230+ 家,**明显向工业/机器人/国防倾斜**,但"开放道路 AV"本身**极薄**(因为核心是资本密集+监管密集,不是 YC 甜点):
- **Teleo**(S26):把推土机、卡车、装载机等**重型设备改成"有人监督的自主机器人"**——采矿/工地为主,属"围栏 off-road",是 AV 能力向低监管场景的溢出,**监督-自主(supervised autonomy)= teleop 的商业化模板**。
- **Hypermile**(S26):卡车 **AI 辅助驾驶(ADAS)**做能效/安全/油耗——不是全无人,是"给现有车队省钱"的软件楔子。
- **Shotwell AI**(S26):为**灵巧机器人做数据 QA 层**(给 teleop + 第一视角数据做密集语义标注)——虽偏具身数据,但正是"teleop/数据层"这条 HTC 主线的 YC 苗子。
- **Salem Robotics**(S26):核环境自主巡检——高危 off-road。

读法:**S26 里没有一家在正面做"开放道路 Robotaxi/干线卡车"**(门槛太高)。所有苗子都落在**监督-自主(teleop)、车队能效软件、具身数据 QA**——恰好印证第六节:**可投的从来不是整车,是解耦的软件/数据/运营层。**

---

## 六、HTC 猎场读法

### 大局判断(先说结论)
**整车/AV-开发层:PASS。** capex 数十亿、大厂/OEM 捕获(Alphabet、Tesla、Amazon、Baidu、Volvo、Nvidia)、上市玩家已late-stage(Aurora/Kodiak/Wayve/Pony/WeRide)。**这不是种子/A 的软件问题,是资本 + 监管 + 时间的问题。** 别碰。

**可下注处 = 硬件解耦的"卖铲子/运营/制度"层**——护城河**不迁移**到整车 OEM 手里,因为数据不同、买家不同、能力不同:

1. **远程操作 / 车队远程运营 SaaS(teleop / remote-ops)——最对 HTC 主线。**
   - **为什么**:Waymo 1:43 的操作员比 = 一个**随车队规模线性扩张、按人/流程计价、硬件解耦、尚未被现任吃掉**的净新增劳动市场(W8-physical / p0b 候选 #2"机器人车队远程监督")。每一支上路的无人车队——不只 Robotaxi,还有卡车、末端、堆场、矿区——都需要这层。
   - **护城河为何不迁移**:整车厂的护城河是**专有驾驶数据 + capex**;teleop 平台的护城河是**低延迟通信栈 + 跨车队调度 + 异常处理 SOP + 操作员劳动网络**——两者数据和买家都不同。Waymo 自建,但**区域运营商、卡车队、堆场、Teleo 式 off-road 客户不会各自造 teleop**。
   - **标的画像**:种子/A,~$10–40M post;押"低延迟 + 一人管更多车 + 跨品牌"的中立平台(Clevon/GetUgo/FERNRIDE 是模板但多在欧洲/垂直);underwrite **retained ARR + 每操作员管车数的爬坡**,不是部署补贴速度。

2. **安全论证 / 场景仿真 / 验证工具(safety-case / scenario-sim / V&V)——闸门即生意。**
   - **为什么**:第 8 步那道 R=5 闸门,本身就是一门"卖给所有 AV 玩家和监管方"的中立生意。全球监管正转向**场景化虚拟验证(scenario-based virtual validation)**,谁能自动化"生成边缘场景 + 证明覆盖度 + 出可签核报告",谁就收所有人的过路费。
   - **现状**:核心已贵(Applied Intuition $15B、Foretellix $135M)——**正面 PASS**。种子楔子在**垂直/受监管细分**:卡车专用 V&V、off-road/矿区/堆场安全案、或"给监管方用"的第三方审计/覆盖度验证层(对标 W8.3 eval 的物理孪生 = 反-C1 对冲:只要长尾价值缺口存在,验证需求就涨,不管谁赢整车)。

3. **自驾车道保险 / 责任与精算(autonomous-lane insurance / actuarial)——制度闸门的金融化。**
   - **为什么**:载人自驾强制 **$500 万/次商业伞险(人类车 5 倍)**,责任在 Waymo/Alphabet/第三方之间**极其复杂**。传统车险精算模型不适配"无司机、责任归制造商/软件"的新范式。谁掌握**无人英里的真实事故/理赔数据 + 新责任模型**,谁能给中小 AV 运营商、卡车队、末端车队做承保。
   - **护城河**:专有事故数据 + 监管关系;买家是运营商而非整车厂。**冷门但真实**(与 W8.5 agent 保险、SA.2 collections 同属"被资金忽视的合规成本→生意"逻辑)。

4. **货运调度语音代理(freight dispatch voice agent)——与 W3.6 交叉引用一次。**
   - **模板**:HappyRobot($150M C 轮,NDR >150%,货运调度)证明在被加冕的 CX 巨头**之下**,货运/现场服务/物流协调有种子空间。语音已是生产级(19% 呼入量)。**押载体数据 + 承运人集成**,不是又一个横向 CX。

5. **区域运营商的车队编排 / 后勤 RaaS orchestration。**
   - 给"买了 Nuro Driver 授权 / Aurora DaaS"的区域车队做**调度、充电排程、后勤外包编排**的软件层——Nuro/Aurora 转授权模式,恰好**留出中间运营层**给独立方。

### 该避开什么
- **整车 / AV 栈自研**:capex 坑,OEM/大厂/主权资本已占,种子无法竞争。
- **任何按"完成多少单 / 估值 / $XXB 市场"定价的标的**:Waymo $126B、Pony/WeRide 市值、"$50B 末端市场"全是估值/TAM,**不是被替代工资**(套 Unitree 纪律)。
- **横向英语 Robotaxi/末端配送**:门已关,大厂+上市玩家占满。
- **纯硬件末端机器人 OEM**:Coco/Serve/Nuro 已过种子且资本重;做"配送机器人本体"是硬件资本坑,做"其上的运营/teleop/保险软件"才对。
- **p0b 纪律再强调**:GPT-6 Astra 的增量**不移动 P3**(AV 用专用驾驶栈,非通用 LLM);**没有量产人形车队**在开车;**可投层是数据/运营/制度层,不是整车 OEM**——与机器人论文、CyberOrigin 数据层立场一致。

### 3 条带日期的证伪信号(到 2027 Q4)
1. **【捕获是否真上斜坡】Waymo 是否在 2026 Q4 达成"周 100 万付费单(~$10 亿年化)"?** 达成 → 城市 Robotaxi 商业化拐点确立,可上调 W9.1 conviction、Net 偏向 Compression;**若明显落在 ~71 万(中位预测)以下 → 证实"多年 capex 苦役、非 2026 事件"的读法,维持 Medium。**(附:任一美国大都会在 2027 中前 BLS/市政数据出现**可测的出租/网约司机净头数下降** = 位移转真。)
2. **【卡车干线是否真·无员规模化】2027 Q4 前,是否有运营商达到"真·无安全观察员、>500 辆商业规模"?**(Aurora 年底目标 200、Kodiak 年底干线无人目标)。达到 → 干线切片位移变结构性;**若 ATA 卡车司机短缺 2026 全年仍 >8 万(→2028 冲 17.5 万)→ 位移仍是"填短缺"而非"净裁",coupled 捕获停在 <1%。**
3. **【制度闸门是否松动 + 独立层是否成形】2027 Q4 前:(a) NHTSA 7月商业豁免是否从"逐案豁免"走向"可规模化的联邦框架/规则"**(而非停滞的自愿 AV STEP);**(b) 是否有独立 teleop / 自驾保险 / 安全论证 startup 披露 ≥$50M retained ARR 且保持独立**(未被 Waymo/OEM/大保险收编)。两者皆是 → 解耦运营/制度层是真可投猎场;**若豁免仍碎片化("permissive fragmentation,许可式割裂"、10 年无联邦 AV 法)且独立层被现任收编(NHI 式 pre-maturity 被并购)→ 价值仍归大厂/整车,独立种子层坍塌。**

---

## 附:数据出处(web-verified 2026-09-16)

**Robotaxi:**
- Waymo $16B/$126B 估值、20+ 城扩张:[Electrek 2026-02-02](https://electrek.co/2026/02/02/waymo-raises-16-billion-round-at-126-billion-valuation-plans-expansion/) · [eWeek](https://www.eweek.com/news/waymo-16-billion-robotaxi-expansion-2026/);50 万周单 / 1M 目标:[Automotive World](https://www.automotiveworld.com/news/waymos-metric-for-2026-success-one-million-weekly-rides/) · [TechCrunch 2026-03-27](https://techcrunch.com/2026/03/27/waymo-skyrocketing-ridership-in-one-chart/);9/1 新开 3 城 + 14 城足迹:[Road to Autonomy](https://www.roadtoautonomy.com/waymo-accelerates-multi-city-rollout/)
- Waymo 安全数据(2.206 亿英里、25.3M 英里 9+2 索赔、-88%/-92%):[Waymo Safety Impact](https://waymo.com/safety/impact/);NHTSA 累计事故(1,429/117 伤/2 亡 2021–2025):[christensenhymas](https://christensenhymas.com/articles/waymo-accident-2026-statistics-and-what-it-means-for-injury-claims/)
- Waymo 远程操作员 70/3000(1:43)、菲律宾、事件响应队、Transdev、Uber $100M:[Futurism](https://futurism.com/advanced-transport/waymo-remote-operators) · [AV Market Strategist](https://avmarketstrategist.substack.com/p/waymos-shocking-data-release-uber)
- Tesla Austin 无安全员 / 扩城:[Teslarati](https://www.teslarati.com/tesla-launches-robotaxi-rides-in-austin-with-no-safety-monitor/) · [Electrek 2026-03-31](https://electrek.co/2026/03/31/tesla-expands-unsupervised-robotaxi-service-area-still-only-handful-vehicles/) · [CNBC 2026-01-22](https://www.cnbc.com/2026/01/22/musk-tesla-robotaxis-us-expansion.html)(Musk 年底铺开——打折)
- Zoox NHTSA 无方向盘豁免(≤2,500 辆)+ Vegas 付费 8/10:[Al Jazeera 2026-07-30](https://www.aljazeera.com/economy/2026/7/30/amazons-zoox-secures-us-federal-approval-for-steering-wheel-free-robotaxis) · [TechCrunch 2026-08-05](https://techcrunch.com/2026/08/05/zoox-to-start-charging-for-robotaxi-rides-in-las-vegas/)
- 中国三强(Pony 1,975→3,500/Q2 $12.1M/H1 $70.47M;WeRide 3,400/H1 $51M/GM 37.5%;Apollo Go 20M+):[Bloomberg](https://www.bloomberg.com/news/articles/2026-05-26/pony-ai-lifts-2026-robotaxi-fleet-goal-to-3-500-on-fast-growth) · [TechTimes 2026-08-19](https://www.techtimes.com/articles/325005/20260819/ponyai-robotaxi-revenue-691-q2-ponyworld-scales-global-deployments.htm) · [Bamboo Works](https://thebambooworks.com/its-revenue-surging-can-co-built-fleets-help-pony-ai-drive-to-profits/) · [China Daily](https://global.chinadaily.com.cn/a/202601/26/WS6976c4b4a310d6866eb35b32.html)

**卡车:**
- Aurora gen-2 无人上路 / 200 辆目标 / 10 路线 / DaaS / 500 辆采购:[Aurora 26Q2 8-K](https://www.sec.gov/Archives/edgar/data/0001828108/000182810826000075/aurora26q2shareholderlet.htm) · [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/aurora-innovation-targets-200-driverless-180310190.html) · [Trucking Info](https://www.truckinginfo.com/news/aurora-rolls-out-next-generation-of-driverless-trucks-for-commercial-freight) · [Aurora IR — FTW-El Paso](https://ir.aurora.tech/news-events/press-releases/detail/128/)
- Kodiak $2.5B SPAC / Q1 $1.8M+74% / 28 车 / 23.5k 时 / $100M 折价 -37%:[FreightWaves](https://www.freightwaves.com/news/kodiak-ai-q1-2026-earnings-28-driverless-trucks) · [TT News](https://www.ttnews.com/articles/autonomous-kodiak-goes-public) · [TechCrunch 2026-05-07](https://techcrunch.com/2026/05/07/kodiak-ai-raises-100m-at-a-steep-discount-sending-its-stock-tumbling-37/)
- Waabi $1B + Uber robotaxi / Volvo VNL 零重训迁移 / 延后:[TechCrunch 2026-01-28](https://techcrunch.com/2026/01/28/waabi-raises-1b-and-expands-into-robotaxis-with-uber/) · [FreightWaves — generalization](https://www.freightwaves.com/news/autonomous-truck-generalization) · [Volvo Autonomous Solutions](https://www.volvoautonomoussolutions.com/en-en/news-and-insights/stories/2025/oct/waabi-and-volvo-demonstrate-the-future-of-autonomous-trucking.html)
- Wayve $1.2B D @ $8.6B;AV 融资 2026 破纪录 $21.4B / 大额化:[New Market Pitch](https://newmarketpitch.com/blogs/news/autonomous-vehicle-funding-analysis) · [Fifth Level Consulting](https://fifthlevelconsulting.com/autonomous-vehicle-funding-more-than-triples-in-2026/)

**Last-mile:**
- Coco $80M / 50万单 / 万台目标:[The Robot Report](https://www.therobotreport.com/coco-robotics-raises-80m-to-scale-sidewalk-delivery-robots/) · [PRNewswire](https://www.prnewswire.com/news-releases/coco-robotics-raises-80m-to-expand-autonomous-delivery-and-ai-platform-302478405.html);Serve 2,000 台 Uber Eats、Nuro Driver 授权、Uber 多模网:[Thomasnet](https://www.thomasnet.com/insights/top-delivery-robot-companies/)

**监管/保险 + 相邻层 + YC:**
- NHTSA 7 月首个 Robotaxi 商业豁免 / AV STEP 停滞 / permissive fragmentation / $500 万伞险:[Hunton](https://www.hunton.com/hunton-retail-law-resource/nhtsa-takes-major-steps-in-establishing-autonomous-vehicle-framework) · [thetechtrends](https://thetechtrends.tech/autonomous-vehicle-regulations/) · [uberaccidentlawyers 2026](https://www.uberaccidentlawyers.net/robotaxi-vs-human-rideshare-accidents-in-2026/)
- Applied Intuition $15B / safety-case automation:[Contrary Research](https://research.contrary.com/company/applied-intuition) · [Sacra](https://sacra.com/c/applied-intuition/);Foretellix $135M V&V:[Foretellix](https://www.foretellix.com/foretellix-accelerates-ai-powered-autonomous-vehicles/);teleop 玩家(GetUgo/Clevon/FERNRIDE)+ AV 融资结构:[StartUs Insights](https://www.startus-insights.com/innovators-guide/autonomous-vehicle-startups-and-companies/) · [New Market Pitch — systems](https://newmarketpitch.com/blogs/news/autonomous-systems-funding-analysis)
- YC S26(Teleo / Hypermile / Shotwell AI / Salem):[YC Summer 2026](https://www.ycombinator.com/companies?batch=Summer+2026) · [YC autonomous-trucking](https://www.ycombinator.com/companies/industry/autonomous-trucking)

**Sourcing caveats(守 p0 R1–R9)**:Robotaxi/卡车营收多为运营商自报或早期年化,标 `[$]` 代理、**非**劳动捕获;Pony/Kodiak 小基数高增速(+691%/+74%)属"小分母把戏",看绝对额;Coco 万台目标、Musk 年底铺开、"$50B 末端市场"均为**未证实/目标/报告磨坊话术**,已按 p3 "shipped ≠ deployed labor" 纪律降权;Waymo 安全数据源自公司自披露(第三方保险数据研究在同行评审中),方向可信、量级需 P4 复核。
