# V3 证据包 · P1 — 结构化单元的操作与生产（Structured-Cell Manipulation & Production）

HTC 内部 · 2026-09-16 · PhysicalAI 家族分区（partition id = **P**）第一个子家族的完整证据包。
上游依据：`p0_foundation.md`（耦合规则、捕获率、pilot-to-production 断崖）、`p0b_capability_refresh_2026-09.md`（GPT-6 Astra 增量式、无量产 humanoid 车队、数据层才是可投层——本包所有能力主张以 p0b 为准）、`p3_frozen_taxonomy.md`（冻结 76 行分类、评分轴 V/H/P/R/L/D）、`v2_master.json`（结构化数据）。

> **一句话定位**：P1 是整张物理地图上**唯一已经真实"部署"、并把物理捕获率顶到 ~1–1.5% 天花板**的子家族。它对应的是**固定工位、刚性零件、在工程化/受控单元（cell）里做的操作**——机床上下料、抓取分拣码垛、结构化食品饮料产线、场外/预制建筑，外加两块**净新增（net-new）**的白地：实验室/药厂自动化、精密电子/微组装。这里"大脑（软件/VLA 模型）"进步是真的，但"身体（硬件/工装/集成）"仍是 5–15 年时间线的瓶颈——**capability ≠ capture 在这里体现得最干净**。

**读法纪律（贯穿全包，非谈判项）**：
1. **耦合（coupling）**：这些行都是 coupled——价值 = 捕获率 × 被替代的工资盘子（displaced wage bill），**绝不把软件 TAM 和劳动 TAM 相加**。
2. **capability ≠ capture**：物理捕获今天 <1.5%；部署落后能力约 10×（MIT 95% 零 P&L、S&P 42% 放弃率）。
3. **物理缺口是硬件时间线（5–15 年）**，很大程度**与模型 IQ 无关**——GPT-6 Astra 没有解锁任何一个此前 BLOCKED/TOO-EARLY 的物理单元。
4. **不迷信炒作估值**：Unitree 公开市值 **~$9B（约 38× 2025 销售额），不是 $50B**；**没有任何 humanoid 在受控、商业定价的量产环境里部署超过"低几百台"**；Figure 03 在宝马 = **演示（demonstration），不是车队**。

---

## 一、这是什么 + 为什么值得看

### 1.1 定义与边界

**结构化单元（structured cell）**指一个**被工程化过、可控、可重复**的作业空间：零件是刚性的（金属件、盒子、瓶罐、连接器、板卡），来料方式相对确定（料箱 bin、传送带 conveyor、料仓、夹具 fixture），环境光照/几何相对固定。P1 只装**固定工位的刚性操作（fixed-station rigid manipulation）**，它是两条正交轴的**"环境结构化高 × 任务物理难度中低"**那一格：

- **环境轴（environment-structure）**：单元是被搭建出来的、结构化的 → 感知/导航/安全这一半基本"解决"。
- **物理轴（task-physics = dexterity/contact，灵巧度/接触力）**：以**刚性抓放、上下料、码垛、对位插装**为主，接触力学相对可控（不是叠毛巾那种可变形、多层、滑溜的物体）。

**明确装进 P1 的（re-home 冻结行）**：
- **W5.2** 抓取分拣、装箱、码垛（piece-picking / packing / palletizing）
- **W5.3** 离散制造机床上下料（discrete manufacturing machine tending）
- **W5.6** 结构化建筑与场外预制（structured construction & offsite prefab）
- **W5.7** 结构化食品/饮料生产（structured food & beverage production）
- **净新增 1：实验室/药厂自动化**（wet-lab 液体处理、样本/板handling、细胞与基因治疗 GMP 生产）——原分类**没有单独的家**，散落在没被打分的白地。
- **净新增 2：精密电子/微组装**（precision electronics / micro-assembly，服务器/PCB/连接器亚毫米装配）——原分类同样无家。

**明确不装进 P1 的（划给 PhysicalAI 其他 band，避免重复计数）**：
- **W5.1** 仓库货物移动 & AMR 内部物流 → 这是**移动/导航**主导（mobile navigation），归 P0/移动感知 band，不归"固定工位操作"。
- **W5.4** 结构化视觉质检 → **感知先行（perception-ahead）** band，不是操作。
- **W5.5** 商业地面清洁 → 移动导航 band。
- W6.x（灵巧/非结构化）、W9（移动性/自动驾驶）、W6.3（个人照护）→ 物理轴难度更高的后续 band。

### 1.2 为什么现在值得看（三个理由）

1. **它是物理地图上唯一有"硬的、近乎审计级"部署证据的地方**。W5.3 机床上下料的捕获率**~1.1–1.7%（≈$30–40B 被真实替代 / $2.0–2.8T 工资盘）**是整包里唯一"复核确认、生产实测"的物理捕获数字（依据：约 90 万台机床上下料机器人 ≈ 460 万台工业机器人存量的 ~20%，替代约 130–150 万 FTE @ 混合 ~$25k）。别处物理行都还在 too-early/pilot。
2. **"净新增"两块（实验室/药厂、精密电子）是原分类的结构性盲点**，而 2026 恰好是这两块的融资与产业化元年（Automata $45M C、Multiply Labs×AstraZeneca、Bright Machines 转向 AI 服务器组装）。
3. **它精确演示了 HTC 论点里最重要的一条**：大脑（VLA 基础模型）在快速收敛且跨本体泛化（π0.7、GR00T、Gemini Robotics 都能一脑多身），所以**大脑不是护城河**；护城河迁移到"原子"——特定单元的专有抓取/任务数据、监管/无菌验证、部署车队的留存数据。这直接指向"投数据层、不投 humanoid OEM"。

### 1.3 劳动盘子（labor TAM）及依据

P1 的分母 = 被 re-home 的 partition 行工资盘（**MECE、不重复计**）+ 两块薄的净新增：

| 组成 | labor TAM `[W]` | 依据 |
|---|---|---|
| W5.3 机床上下料 | **$2.0–2.8T** | p0 W5 家族先验 + 再推导，冻结保留；发达经济体金额加权 |
| W5.2 抓取/装箱/码垛 | **$0.6–0.9T** | 冻结带 |
| W5.6 结构化/预制建筑 | **$0.5–0.8T** | 冻结带 |
| W5.7 结构化食品/饮料 | **$0.3–0.5T** | 冻结带 |
| 净新增 · 实验室/药厂手工操作 | **~$0.1–0.2T** | 实验室技师 + 药厂生产操作工的发达经济体加权手工盘子（美国医学/临床化验技师 ~33.5 万；加生物技师、药厂生产操作工；全球 wet-lab + 无菌灌装手工薄层）|
| 净新增 · 精密电子/微组装 | **~$0.2–0.4T** | 电子/电气装配工；亚洲头数巨大但 comp-per-head 低，发达加权后的薄层 |
| **P1 合计（非重复）** | **≈ $4–5T `[W]`**（下沿 ~$3.7T，上沿 ~$5.6T） | = W5 结构化家族（$5–7T）减去移动/感知的 W5.1/W5.4/W5.5（~$1.25T），再加两块净新增 |

> **纪律提醒**：这 $4–5T 是**分母（被暴露的工资盘）**，不是可捕获价值。今天真实被替代 ≈ $40–60B（机床上下料主导），即 **P1 整体已实现捕获 ~1–1.3%**——这正是"物理捕获天花板"的定义位置。机床上下料一行就占了盘子的一半以上，且它已经"70 年自动化史"里把 ROI 划算的活干完了，剩下的是高混合/低批量/发展中经济体里机器人回本失败的残余人。

---

## 二、这份体力工作到底要做哪些步骤

把"在结构化单元里操作与生产"拆成阶段，每步用大白话说人现在在做什么。P1 的活基本都是这 10 步的组合（不同行侧重不同步）：

**阶段 A：看清楚 + 抓起来（感知与抓取）**
1. **感知与定位（perception / pose estimation）**：人扫一眼料箱/传送带，认出零件是哪个、朝哪、在哪。
2. **抓取规划（grasp planning）**：决定用手/夹爪从哪个点、什么姿态抓——薄板从边缘、瓶子从颈部、乱堆的零件挑一个不打架的。
3. **抓取执行（grasp / pick）**：伸手、合爪/吸盘、稳稳提起来，不掉不压坏。

**阶段 B：搬过去 + 放/装进去（搬运与装配）**
4. **搬运与放置（transport & place）**：把件挪到机床/夹具/托盘，按公差放到位。
5. **机床上下料（machine load/unload）**：开安全门→把毛坯坐进卡盘/夹具→取出加工完的成品→关门启动。CNC、注塑、冲压、铸造边上那个"喂料的人"。
6. **精密装配/对位（precision assembly / alignment）**：两件对齐、拧螺丝、压装、插连接器——亚毫米级、要对准、要判断"到底了没"。服务器板卡、PCB、线束就是这步。

**阶段 C：换活 + 兜底（换线与异常）**
7. **编程/换线/调试（programming / changeover / commissioning）**：来了新零件/新产品，重新教机器人怎么抓怎么放、换工装、试跑。**这一步是今天真正吃人工的隐藏成本**——传统机器人每换一个 SKU 要工程师重编几天。
8. **单元内质检与异常处理（in-cell QC & exception recovery）**：抓空了、抓歪了、卡住了、来了个没见过的件——人立刻发现并纠正。

**阶段 D：出货（后段）**
9. **码垛/装箱/打包（palletize / pack / case-pack）**：把成品堆托盘、装箱、封口、贴标。相对最"解决"的一步。

**阶段 E：受控/无菌环境专有（实验室/药厂净新增）**
10. **无菌/受控环境操作（aseptic / controlled-environment ops）**：移液（pipetting）、96 孔板搬运、离心、细胞传代、无菌连接——动作本身不难，难在**无菌、可追溯、GMP 合规、不能出错**。

---

## 三、每一步 AI+机器人现在能不能做（核心表）

**判定口径**：能 = 在真实付费部署里稳定跑；半能 = 结构化窄场景能跑但泛化/可靠性不够、或仍需人兜底；不能 = 仅 demo 或未证明。**关键区分**：🧠=软件/大脑进步（模型问题）；🔩=硬件/身体瓶颈（工装/接触力学/集成/成本/安全，**非模型问题、5–15 年时间线**）。

| 步骤 | 2025 年底（能/半能/不能 + 靠哪个模型×硬件） | 2026 年 9 月（+ 具体产品/VLA/机器人） | 本窗口新解锁？ | 备注（🧠软件 vs 🔩硬件 瓶颈） |
|---|---|---|---|---|
| 1 感知/定位 | **能**（结构化）。3D 视觉 + 学习位姿估计成熟。Cognex/Keyence + 视觉基础模型 | **能**。视觉基础模型继续从下方商品化；结构化单元里近乎已解决 | 否（早已解决） | 🧠已解决。这是环境轴"结构化高→感知半自动解决"那一半的兑现 |
| 2 抓取规划 | **半能**。均匀 SKU 能，混合/乱堆料箱靠 grasp 模型；Dexterity/RightHand/Covariant 系 | **半能↑**。π0.7 组合泛化、GR00T N1.7/N2、Gemini Robotics 1.5 跨本体迁移让"抓没见过的件"更稳 | 部分（🧠软件真进步） | 🧠VLA 泛化是真的；但"最后 10% 可靠性"仍卡在长尾抓取，capture 仍 <2%（W5.2） |
| 3 抓取执行 | **能**（刚性件）。夹爪/吸盘 + 力控成熟 | **能**（刚性件） | 否 | 🔩刚性件已解决；可变形/滑溜件（薄板、软包）仍难——见步骤 6/食品线 |
| 4 搬运/放置 | **能**。固定工位放置公差可控 | **能** | 否 | 🔩机械问题，早解决 |
| 5 机床上下料 | **能**（这是 P1 的成熟核心）。FANUC/ABB/UR 臂 + RaaS（Formic/Standard Bots） | **能**。~90 万台在役，捕获 ~1.1–1.7%；Formic 累计 40 万+机器人小时 | 否（增量 +~6%/年） | 🔩瓶颈是**集成/工装/回本**不是模型——高混合/小批量场景机器人回本失败，这是硬件+经济学时间线 |
| 6 精密装配/对位 | **半能**。刚性亚毫米对位可做（Bright Machines 微工厂）；柔性/线束仍难 | **半能↑**。Bright Machines 转做 AI 数据中心服务器组装（NVIDIA/微软/Jabil 背书），刚性板卡装配放量 | 部分（应用面扩张，🧠+🔩） | 🔩接触力学 + 亚毫米对位仍是身体瓶颈；模型帮了对位判断，但线束/柔性连接器仍未解决 |
| 7 编程/换线/调试 | **半能**。传统机器人换 SKU 要工程师重编数天——最大隐藏人工 | **半能↑↑**（本窗口最亮）。**一次示教学习**：YC S26 **Shiraz AI**"工厂里一次人类演示就学新任务"；π0.7 语言跟随 + 技能重组 | **是**（🧠软件真解锁） | 🧠这是 VLA 对 P1 最实际的价值——把"换线重编程"从工程师数天压到示教分钟级；直接改善机床上下料/装配单元的部署经济学 |
| 8 单元内质检/异常 | **半能**。抓空/抓歪能检测；未见异常靠人兜底 | **半能**。Embodied reasoning（GR-ER 1.5"想后再动"）改善异常判断，但长时程自主可靠性仍是墙 | 否（增量） | 🧠改善；🔩长时程端到端可靠性（对应 OSWorld 2.0 二值 ~31% 的物理孪生）仍未过生产线 |
| 9 码垛/装箱/打包 | **能**。最成熟；混合码垛稍难 | **能**。Dexterity Mech 等做混合卸货/码垛 | 否 | 🔩已解决；价值归垂直整合运营商（Amazon/Symbotic）自建资产负债表，不是独立 ARR |
| 10 无菌/受控操作（实验室/药厂） | **半能**。液体处理成熟（Opentrons/Automata/Tecan）；细胞治疗仍手工 | **半能↑**。Multiply Labs 多臂集群自动化细胞治疗（AstraZeneca/CPC Biotech）；Automata LINQ + Beckman；Neuromorphic（YC S26）操作现有实验设备 | 部分（🧠+🔩，净新增放量） | 🔩瓶颈是 **GMP 验证 + 无菌 + 可追溯**（监管时间线），不是模型能力；这也正是护城河所在 |

**本表三句话总结**：
- **🧠软件解锁只有一个真的、且它很实用**：**换线/示教（步骤 7）**——VLA 的语言跟随 + 一次示教学习，把部署经济学从"每 SKU 重编数天"改善到分钟级。这改的是**成本曲线**，不是能力天花板。
- **其余"半能→能"的移动几乎全是硬件/集成/监管时间线（🔩）**：机床上下料的瓶颈是回本，精密装配是接触力学，实验室/药厂是 GMP 验证。**GPT-6 Astra 这一代对这些一格没动**（p0b §B/§C 已确认）。
- **可变形物体仍是墙**：π0 达到已知衣物折叠 >80%，但**通用可变形操作未解决**——这限制了食品线里软包/散料/生鲜的处理（W5.7 的天花板）。

---

## 四、耦合与捕获

**耦合类型**：全部 **coupled**（价值 = 捕获率 × 被替代工资，绝不 SW+labor 相加）。

**当前捕获（守住 <1.5% 物理纪律）**：

| 行 | 已实现捕获 | 依据 | Net 净效应 | Conviction |
|---|---|---|---|---|
| W5.3 机床上下料 | **~1.1–1.7%** | ~$30–40B 真实替代 / $2.0–2.8T；生产实测（Formic 40 万+机器人小时、BotQ ~1 机器人/小时） | **压缩（Compression）**，但增量缓慢（装机 +~6%/年） | **High**（唯一近审计级物理捕获） |
| W5.2 抓取/码垛 | **<2%** | grasp 多样性（P=4）仍限可靠自主；缩放红利归垂直整合运营商 | 混合（Mixed） | Medium |
| W5.7 食品/饮料 | **<1.5%** | Chef 100M+ 份，但仅 >12 设施；RaaS 递归收入结构是首个可信"经常性"物理收入 | 混合 | Medium |
| W5.6 结构化/预制建筑 | 极低（早期） | 劳动力短缺 → **扩张（Expansion）**、低替代反弹；startup 主导、无 incumbent 锁 | **扩张** | Medium |
| 净新增 实验室/药厂 | ~0（起步） | 净新增自动化 + 部分替代化验/生产手工；GMP 时间线限速 | 混合（替代 + [L] 潜在需求扩张） | Medium |
| 净新增 精密电子/微组装 | 低 | Bright Machines 等；AI 服务器组装是 2026 需求拉动 | 混合 | Medium |

**net effect（子家族整体）**：**压缩为主 + 一处扩张（预制建筑）+ 净新增的潜在需求扩张（实验室/药厂）**。综合读作 **Coupled / Compression 主导，Conv High**（对应任务书定位"deployed frontier, physical capture at ~1–1.5% ceiling"）。

**denominator（工资盘，不与别处重复计）**：$4–5T `[W]`（见 §1.3 表）。**边界守卫**：
- 不含 W5.1 仓库移动（$0.85T，归移动 band）、不含 W5.4 视觉质检、不含 W5.5 地面清洁——这三块的移动/感知盘子**不在 P1**。
- 机床上下料 $2.0–2.8T 是发达加权、且大部分早已被固定自动化/cobot 吃掉，**剩余可捕获 << 分母**。
- 实验室/药厂、精密电子的净新增薄层与 W5.7 有极小重叠，已按净新增薄计，不重复 W5.3/W5.7。

**关键结论（capture-expansion 才是赌注）**：P1 已实现捕获 ~1–1.3%，**赌的是捕获率扩张**，不是把两个大数相加。而且——**物理捕获的"扩张速度"是硬件/回本/监管时间线决定的，不是模型 IQ**。这与 W1.1 编码（软件、seat-ARR 巨大但耦合捕获 0.1–0.2%）形成镜像：编码是"revenue 领先 value"，P1 是"capability 领先 capture"，但两者的赌注都是**capture-expansion 的可信度**。

---

## 五、竞争格局（具体到公司名）

### 5.1 巨头 / OEM / 现任（硬件与平台层——多为 incumbent-captured）

- **工业机械臂四大家（Big-4 arm OEM）**：**FANUC、ABB、KUKA、Yaskawa** + **Universal Robots（Teradyne，cobot 协作臂）**。机床上下料/码垛/装配的硬件底座，装机基础与集成渠道锁死；+~6%/年增量曲线的主体。**W5.3/W5.2 的 incumbent verdict 主因。**
- **机器视觉现任**：**Cognex、Keyence**——数十年装机 + 现已自带深度学习，从上方夹住视觉质检/定位（W5.4 是最 incumbent 的一格，但其感知能力外溢到 P1 的步骤 1）。
- **VLA / 机器人基础模型（"大脑"平台层——收敛中、跨本体泛化）**：
  - **NVIDIA Isaac GR00T N1.7 / N2（DreamZero 世界-动作模型）**——开放 3B 推理 VLA，"商业可部署"，N2 新任务成功率约 2× 领先 VLA；**外加 Jetson/Isaac Sim 生态**，是最像"卖铲子"的平台巨头。
  - **Google DeepMind Gemini Robotics 1.5 + ER 1.5**——"具身思考"（想后再动）、Motion Transfer 跨本体（ALOHA/双臂 Franka/Apollo humanoid，无需按机型重训）。
  - **Physical Intelligence π0.5 → π0.7**——组合泛化步进、跨机器人技能迁移、语言跟随；估值 $5.6B，传闻融向 $11B。
  - **Skild AI**——"全身型（omni-bodied）"基础模型，$1.4B C（>$14B 估值，2026-01，最大机器人 AI 轮，软银/NVIDIA/Bezos/三星/LG）。
  > **纪律**：这些是"大脑"平台，**收敛且跨本体泛化 → 大脑不是独立创业公司的护城河**（p0b §C/§E5）。它们提高步骤 2/7/8 的能力，但**不移动 P1 的 Net/capture**（硬件/部署门控）。
- **微组装/软件定义工厂现任-挑战者**：**Bright Machines**——$126M C（$106M 股权 BlackRock 领投 + $20M JPM 债，2024；累计 $279M），投资方含 **NVIDIA、微软、Jabil**；2026 明确**转向 AI 数据中心服务器 / AI 硬件组装**，与 Azure GTM 绑定。Brightware OS 编排机器人+传送+检测的模块化 cell。**这是"精密电子/微组装"净新增里最像巨头的一家，但它的拉动是 AI capex（服务器需求），不是劳动替代论。**
- **humanoid OEM（资本坑，务必守纪律）**：Figure（~$39B，OpenAI 领投）、1X（~$10B，Neo）、Apptronik（~$5.5B）、Tesla Optimus（Musk 称 Fremont 1,000+ Gen-3，**公开承认落后进度、不可当已部署劳动**）、Unitree（**上交所 STAR 2026-08-06 IPO ~$9.04B，非 $50B**；$235M 2025 营收、5,500+ 台）。**没有任何 humanoid 在受控商业量产做机床上下料 > 低几百台**；Dexterity "Mech superhumanoid MMR" 是**卡车装卸/码垛的双臂移动操作 demo/早期**，不是机床上下料车队。

### 5.2 独立 startup（名字 + 阶段 + 融资 + 一句话）

**机床上下料 / RaaS（多已过种子，且 incumbent-adjacent）**
- **Formic Technologies**（Series A 累计 ~$52M；Lux/Blackhorn）——机床上下料/焊接/码垛的 RaaS（按小时订阅，客户免 capex）；40 万+机器人小时。
- **Standard Bots**（Series B+）——RO1 六轴臂 + RaaS，机床上下料/装配定位平价化。

**抓取 / 分拣 / 码垛（水平层已到晚期）**
- **Dexterity**（$1.65B 独角兽，2025-03；2026-05 有 $5M B 补充轮）——Mech 移动双臂操作，卡车装卸/码垛/拣选；Sumitomo 日本部署合同。
- **RightHand Robotics**（Series C，累计 ~$66M）、**Ambi Robotics**（累计 ~$66.7M）、**Mujin**、**Pickle Robot**（卡车卸货）——单元级拣选/装箱。**Covariant** 已被 Amazon acqui-hire（2024）、**Berkshire Grey** 被软银收——**"独立抓取 startup 被垂直整合运营商吸走"是本格的基准命运。**

**食品/饮料生产（startup 主导、RaaS 递归收入是新意）**
- **Chef Robotics**（Series A $43.1M，累计 ~$97.8M 含设备债；Avataar 领投）——**category 锚**；100M+ 份、>12 设施、RaaS 按份计价；**2026 从食材扩到二次包装/kitting（酱包、餐具包）**，同硬件同软件复用。**"经常性 RaaS + 留存数据飞轮"是它的护城河，不是机器人本身。**
- **Hyphen、Nala Robotics、Cala**——邻近结构化食品制造；**Miso Robotics（Flippy）**= QSR 前场翻车的警示墓碑。

**结构化 / 预制建筑（唯一 startup 可拥有 category 的 W5 格）**
- **Monumental**（$32M B，2026，Khosla 领投）——~150 台砌砖机器人车队（英国/欧洲）。
- **Dusty Robotics**（~$16.5M 近轮；FieldPrinter 放样，9,100 万+平方英尺已打印）、**Built Robotics**（累计 $112M；挖机自主，走 Cat/Komatsu 渠道）、**Canvas**（石膏板）、**Toggle**（钢筋）。

**实验室 / 药厂自动化（净新增——2026 是产业化元年）**
- **Automata**（**$45M Series C，2026-01-29**，Dimension 领投 + **Danaher Ventures**；累计 $177M）——自主 wet-lab 参考架构（模块机器人 + 编排软件 + 统一数据）；**2026-01 与 Beckman Coulter 合作**整合液体处理/基因组/细胞分析。
- **Opentrons**（累计 $200M+，独角兽）——Flex 液体处理机器人 + OpentronsAI；**2026-02 与 HighRes 合作** agent-to-agent 实验室工作流。
- **Multiply Labs**（旧金山）——**多臂机器人集群（四臂并行）自动化细胞与基因治疗 GMP 生产**；**2026-02 与 AstraZeneca** 评估商业规模细胞治疗、**2026-05 与 CPC Biotech** 做无菌机器人连接器。
- **Lila Sciences**（累计 ~$550M，含 $350M A @ >$1.3B；Flagship Pioneering）——"科学超智能"自主实验室工厂（材料/生命/化学），已跑数十万实验。**注意**：Lila 偏 **R&D 自动化（W15 邻域、净新增 [L] 潜在需求、L=5 lab-captured）**，不是 P1 的"生产线替代"——列此以划界。**Periodic Labs**（Fedus/Cubuk）同类、更早期。

### 5.3 YC 重点（Summer 2026 / S26 及近批——联网核实）

**S26 批"工业（Industrials）占比升到 23%**（上一批 12.8%），第二大板块，含 humanoid/家用、仓储/数据中心机器人、机器人评测/训练基础设施"——这是本次 demo day 最明显的结构性转向。与 P1 直接相关的 S26 公司：

- **Shiraz AI** — "工厂里**一次人类演示就学新任务**的机器人"。**直击 P1 步骤 7（换线/示教）——本窗口唯一软件解锁的商业化。**
- **Neuromorphic** — "自主 wet-lab 机器人，**操作现有科学设备**执行实验"。**净新增实验室自动化的种子级代表**（对标 Automata 的轻资产打法）。
- **Manifold** — "自主仓库机器人做拣选/装载/码垛，**按任务计价（priced by task）**"。**按任务计价 = 天然 coupled/结果定价**，值得盯留存。
- **Grip** — 废弃物/回收的学习型操作 + 定制硬件（结构化度较低的操作边缘）。
- **Neuron Industries** — "为 AI 打造的工业控制器，替代老旧 PLC"。**"软件定义单元"的大脑/控制层**——注意这偏 [$] 基础设施，不是劳动分母。
- **Hebbian Robotics** — "给机器人数据团队的 API，**验证训练数据质量**"。**这是 P1 的"数据/验证层"种子**——CyberOrigin 逻辑在结构化操作里的孪生。
- **Moving Atoms**（用预训练物理模型训策略、免手工采数）、**Enact / Robocurve**（真实世界机器人评测基准）——**数据/仿真/评测层**，与 HTC 论点同源。
- **Tensr**（机器人化工厂造机器人零件/空间应用）、**Salem Robotics**（危险环境自主巡检——偏感知）、**Aktoria**（任意机器人远程操作——teleop 层）、**Libra**（太阳能场/数据中心协作机器人 crew）、**Nori**（<$2000 双臂移动操作，家庭/小商业）。

> **YC 读法**：S26 把机器人 startup 的重心从"造本体/humanoid"往下推到了**数据质量验证（Hebbian）、仿真/评测（Moving Atoms/Enact/Robocurve）、一次示教（Shiraz）、按任务计价的操作（Manifold）、软件定义控制（Neuron）**——**这正是 HTC 该猎的层**（见 §六）。而 humanoid/本体那一半仍是资本密集、估值≠部署的坑。

---

## 六、HTC 猎场读法

### 6.1 可下注的种子 / A wedge（具体细分 + 为什么护城河不迁移）

**核心命题**：P1 的大脑（VLA）在收敛且跨本体泛化 → **不投大脑、不投本体、不投水平 RaaS 转售**。护城河迁移到"原子"——**特定单元的专有物理数据、监管/无菌验证、结果定价的留存客户**。可下注三条 wedge：

1. **结构化操作的数据 / 示教 / 仿真 / 验证层（CyberOrigin 逻辑的工厂孪生）——最高确信、最贴 HTC 论点**。
   - 细分：为结构化单元 VLA 供给**帧级验证的抓取/装配/上下料动作数据**、一次示教工具、以及**数据质量验证**（YC S26 **Hebbian** 就是这个）。
   - 为什么护城河不迁移：数据是每个 VLA（π0.7/GR00T/Gemini Robotics）的**共同绑定约束**，且**硬件解耦、按人/流程扩张不按芯片扩张**（teleop 仅 ~5–50 episodes/hr）；水平模型 lab 拿不走"特定垂直单元里帧级验证的专有数据"。这比 humanoid 家用 teleop 更窄、更高保真、更贴近可付费的工业客户。

2. **净新增实验室/药厂自动化——单元天生受控、替代的是买方自己的劳动、且有监管护城河**。
   - 细分：**Neuromorphic 式"操作现有实验设备"的轻资产 wet-lab 自动化**、**细胞与基因治疗 GMP 生产自动化**（Multiply Labs 已证明产业需求：AstraZeneca/CPC Biotech）。
   - 为什么护城河不迁移：这里的墙是 **GMP 验证 + 无菌 + 可追溯（监管时间线）**，不是模型能力——**监管/验证护城河不会因为下一代 VLA 变强而蒸发**，反而随部署加深。且买方替代的是自己的化验/生产工，displacement 政治阻力低（短缺行业）。
   - 种子进入点：轻资产、操作既有设备（不自造大型硬件）、按结果/通量定价、垂直（细胞治疗 / 特定化验）里数据复利。避开 Lila 式 $550M 重资产"科学工厂"（那是 R&D/W15、L=5 lab-captured、不可投种子）。

3. **结果/任务定价的垂直操作运营商，在未服务的窄垂直里、靠留存数据 + 递归 RaaS 建护城河**。
   - 细分：复制 **Chef 的食品制造 RaaS 飞轮**到未服务垂直（烘焙、蛋白分割、饮料/共包装 co-packing）；或 **Manifold 式"按任务计价"的拣选/码垛**在中端 3PL/混箱卡车装卸。
   - 为什么护城河不迁移：**递归 RaaS + 每单元留存的任务数据**是护城河（不是机器人本身）；水平 OEM/lab 拿不走"某个垂直产线里回本验证过的部署 + 留存数据 + 客户流程集成"。
   - 非谈判尽调：审计**留存 ARR / 净收入留存（NRR）/ 毛净流失**，不看装机数或 run-rate（11x/Builder.ai 的教训）。

### 6.2 该避开什么（OEM / 硬件资本坑）

- **humanoid OEM**：Figure $39B、Unitree（公开 ~$9B）、1X、Apptronik、Tesla Optimus——**估值 ≠ 部署劳动**；无任何量产机床上下料车队；种子投资人进不去（$200M+ 轮）。**把 humanoid 当"已部署劳动"是 p3 Reality-Ladder Tier-D 错误。**
- **水平机床上下料 / 抓取 RaaS 转售**：Formic、Standard Bots、Dexterity（$1.65B）、RightHand、Ambi——**要么过种子、要么 incumbent-adjacent、要么会被 Amazon/Symbotic 式垂直整合运营商吸走**（Covariant→Amazon、Berkshire Grey→软银的基准命运）。
- **视觉质检 AI-native 水平层**：被 Cognex/Keyence（自带深度学习）+ 视觉基础模型（从下商品化）两头夹（W5.4 verdict = incumbent）。
- **软件定义控制/PLC 替代（Neuron 式）**：真需求，但**分母是软件/IT 预算 = [$] 基础设施台账，不是劳动 TAM**；且易被工业自动化巨头 feature 化。可作 [$] 观察，不当劳动行下注。
- **大脑/VLA 基础模型本身**：收敛、跨本体、model-lab/NVIDIA 捕获，独立 startup 无护城河。

### 6.3 三条带日期的证伪信号（到 2027Q4）

1. **机床上下料 capture-expansion 拐点（W5.3）**：**到 2027Q4**，IFR World Robotics 显示机床上下料应用装机加速 **>15%/年**（对比 ~6% 基线）**且** ≥1 家 humanoid 厂商披露 **≥5,000 台在"付费制造业机床上下料生产"**（非仓储/pilot）@ ≤$30/机器人-小时全负荷 → **物理捕获扩张真正开始，L 轴需上调（价值从 incumbent 迁向 model-lab）**。若装机仍 ~6%/年 且 humanoid 生产上下料 <2,000 台 → **增量-only / incumbent-captured 读法确认，capture 守 <2%。**
2. **净新增实验室/药厂验证信号**：**到 2027Q4**，≥1 家自主 wet-lab 或细胞治疗自动化 startup（Automata / Multiply Labs / Neuromorphic 类）披露 **≥$50M 留存收入 且拿到 GMP 商业生产（非评估/pilot）合同** → **净新增自动化是真可投 category、监管护城河成立**。若都停在评估/pilot 或被 Danaher/Thermo/Beckman 式仪器巨头收编 <$100M → **incumbent 吸收、种子门关闭。**
3. **结果定价 / RaaS 留存证伪（W5.7 食品 + Manifold 式按任务）**：**到 2027Q4**，Chef（或同类）跨 **~$50M 经常性 RaaS、>30 生产设施、NRR >120%**；或 ≥1 家"按任务计价"操作运营商披露留存 ARR ≥$25M、毛流失 <30% → **可持续物理劳动捕获 + 递归护城河成立**。若食品停 <15 设施靠硬件收入、或按任务计价者流失 >50% 回退混合 → **capture 卡 <1.5%，本 band 的"结果定价护城河"证伪。**

---

## 附：来源（2026-09-16 联网核实；Tier 标注承 p0 R1–R9）

**能力 / VLA / 硬件（承 p0b）**：NVIDIA Isaac GR00T N1.7/N2（HF/NVIDIA dev）；DeepMind Gemini Robotics 1.5（arXiv 2510.03342）；Physical Intelligence π0.7（arXiv 2604.15483）；Skild AI $1.4B（The Robot Report）；Unitree IPO ~$9.04B（ValueAdd VC）；Figure 03 = demo（BMW press）；humanoid 出货 19,100 台 H1 2026（Standard Bots）——**均为 p0b 已核实，Tier-2 聚合器慎当方向**。

**P1 具体公司（本包新核实）**：
- Automata $45M C（analytica-world / automata.tech，2026-01-29；Dimension + Danaher Ventures；累计 $177M）；Beckman Coulter 合作（2026-01）。
- Opentrons（Crunchbase；$200M+；Flex）；HighRes 合作（2026-02）。
- Multiply Labs × AstraZeneca（BioSpace / Contract Pharma / roboticsandautomationnews，2026-02）；× CPC Biotech（MarketScale，2026-05）。
- Bright Machines $126M C（The Robot Report / PRNewswire；BlackRock/NVIDIA/微软/Jabil；累计 $279M；AI 服务器组装转向）。
- Chef Robotics $43.1M A / 累计 ~$97.8M（The Robot Report / Robotics 24/7 / chefrobotics.ai；100M+ 份；2026 扩二次包装/kitting）。
- Dexterity $1.65B（Robotics 24/7，2025-03）+ $5M B（2026-05）；Mech MMR；Sumitomo 日本部署。
- Formic ~$52M+ A（MMH / BusinessWire；机床上下料 RaaS）。
- 结构化建筑：Monumental $32M B（Khosla，2026）、Dusty ~$16.5M、Built $112M cum（v2_master.json 已核）。
- Lila Sciences ~$550M（含 $350M A @ >$1.3B；Flagship）、Periodic Labs（C&EN / MIT Tech Review）——**划界为 R&D 自动化，非 P1 生产线**。
- YC S26：Industrials 占 23%（neweconomies.co / foundevo）；公司名与一句话（ycombinator.com/companies manufacturing-and-robotics S26）：Shiraz AI、Neuromorphic、Manifold、Hebbian Robotics、Neuron Industries、Grip、Moving Atoms、Enact、Robocurve、Tensr、Salem、Aktoria、Libra、Nori、Lambda、Most Robotic。

**内部**：p0_foundation.md、p0b_capability_refresh_2026-09.md、p3_frozen_taxonomy.md、v2_master.json（W5.1–W5.7 行、耦合规则、捕获纪律、猎场清单）。

**Sourcing caveats（承 p0）**：机器人/实验室融资多为 Crunchbase/press-tier（Tier-2，融资=事件可用、估值≠劳动分母）；humanoid 部署数与 Musk 目标为运营方声明、未审计——守 p3"出货台数 ≠ 已部署劳动"纪律；GPT-6 Astra 基准为 Tier-2 聚合器、方向性——且 p0b 已确认其对物理一格未动。
