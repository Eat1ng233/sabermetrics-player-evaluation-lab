---
title: wOBA（加權上壘率）
type: metric
aliases: [wOBA, weighted On-Base Average, 加權上壘率]
domain: [batting]
leagues: [MLB]
tags: [rate-stat, linear-weights]
sources: ["[[src-2010-slowinski-fangraphs-woba]]", "[[src-2016-weinberg-fangraphs-deriving-woba]]", "[[src-2010-slowinski-fangraphs-wrc]]"]
source_count: 3
status: stable
full_name: weighted On-Base Average
scale: OBP-scale
upstream: ["[[linear-weights]]", "[[run-expectancy-matrix]]"]
downstream: ["[[wraa]]", "[[wrc]]", "[[wrc-plus]]"]
stabilization:
created: 2026-11-23
updated: 2026-11-23
---

# wOBA（加權上壘率）

> 一句話定義：依每種進攻事件的**得分價值**給予不同權重，再縮放到上壘率尺度的綜合打擊指標。由 Tom Tango 提出，並在《The Book》中使用。

## 它在回答什麼問題
「這位打者每個打席平均替球隊創造多少進攻價值？」

傳統指標各有缺陷（[[src-2010-slowinski-fangraphs-woba]]）：
- **打擊率（AVG）**：一壘安打和全壘打等值，也忽略保送。
- **OBP**：所有上壘方式等值。
- **SLG**：用 1、2、3、4 的壘打數當權重，與實際得分價值不成比例。
- **OPS**：直接把 OBP 和 SLG 相加，等於假設兩者每一點價值相同。但文章估計 OBP 的價值約為 SLG 的 **1.8 倍**。

即使是同樣上壘的保送和一壘安打，對一局的影響也不同：保送一定讓每位跑者推進一個壘包，一壘安打的結果則依跑者位置和擊球方向而定（[[src-2016-weinberg-fangraphs-deriving-woba]]）。wOBA 的解法是讓權重直接反映得分價值，同時保留大家熟悉的上壘率尺度。

## 定義與公式
一般式：

$$
\text{wOBA} = \frac{w_{\text{BB}}\,\text{uBB} + w_{\text{HBP}}\,\text{HBP} + w_{\text{1B}}\,\text{1B} + w_{\text{2B}}\,\text{2B} + w_{\text{3B}}\,\text{3B} + w_{\text{HR}}\,\text{HR}}{\text{AB} + \text{BB} - \text{IBB} + \text{SF} + \text{HBP}}
$$

變數說明：
- $\text{uBB}$：非故意四壞（$\text{BB} - \text{IBB}$）
- $\text{HBP}$：觸身球
- $\text{1B}, \text{2B}, \text{3B}, \text{HR}$：一壘安打、二壘安打、三壘安打、全壘打
- $\text{AB}$：打數；$\text{BB}$：四壞（含故意）；$\text{IBB}$：故意四壞；$\text{SF}$：高飛犧牲打
- $w_{x}$：事件 $x$ 的權重，**隨聯盟與球季而變**，MLB 各年數值見 FanGraphs Guts 頁面（1871 年至今）

分母大致等於「扣除故意四壞與犧牲觸擊後的打席數」。

### MLB 2010–2015 年常數

| 球季 | lgwOBA | wOBA Scale | wBB | wHBP | w1B | w2B | w3B | wHR | lgR/PA |
|---|---|---|---|---|---|---|---|---|---|
| 2015 | .313 | 1.251 | .687 | .718 | .881 | 1.256 | 1.594 | 2.065 | .113 |
| 2014 | .310 | 1.304 | .689 | .722 | .892 | 1.283 | 1.635 | 2.135 | .108 |
| 2013 | .314 | 1.277 | .690 | .722 | .888 | 1.271 | 1.616 | 2.101 | .110 |
| 2012 | .315 | 1.245 | .691 | .722 | .884 | 1.257 | 1.593 | 2.058 | .114 |
| 2011 | .316 | 1.264 | .694 | .726 | .890 | 1.270 | 1.611 | 2.086 | .112 |
| 2010 | .321 | 1.251 | .701 | .732 | .895 | 1.270 | 1.608 | 2.072 | .115 |

出處：FanGraphs Guts 頁節錄，引自 [[src-2016-weinberg-fangraphs-deriving-woba]]。2013 年的權重與 [[src-2010-slowinski-fangraphs-woba]] 一致。

觀察：
- 全壘打權重約為一壘安打的 2.4 倍（$2.101 / 0.888 \approx 2.37$，2013），而 SLG 給的是 4 倍。
- 保送權重約為一壘安打的 78%（$0.690 / 0.888 \approx 0.78$，2013），而 OBP 視兩者相同。
- 六年間權重變動不大，但 Scale 從 1.245 到 1.304 都有，所以跨年比較原始 wOBA 時要小心。

## 推導過程
以 MLB 2015 年為例（[[src-2016-weinberg-fangraphs-deriving-woba]]），完整計算見 [[ex-woba-mlb-2015-derivation]]。

**步驟 1：建立得分期望值矩陣。** 計算 24 種壘包出局狀態下，到該局結束的平均得分（見 [[run-expectancy-matrix]]）。

**步驟 2：算出每種事件的平均得分價值（線性權重）。** 每個打席讓狀態改變，得分期望值的變化就是這個打席的價值。把同一類事件取平均：

$$
\text{RV}_{x} = \frac{\sum_{i \in x} \Delta \text{RE}_i}{n_x}
$$

得到的是「比平均打席多創造幾分」。2015 年：BB +0.29、HBP +0.31、1B +0.44、2B +0.74、3B +1.01、HR +1.39，出局 −0.26。

**步驟 3：改成相對出局的價值。** OBP 尺度中出局記為 0，所以每個值都減去出局的價值（也就是加 0.26）：

$$
\text{RV}^{*}_{x} = \text{RV}_{x} - \text{RV}_{\text{out}}
$$

2015 年：BB 0.55、HBP 0.57、1B 0.70、2B 1.00、3B 1.27、HR 1.65。

**步驟 4：縮放到 OBP 尺度。** 用步驟 3 的權重算出全聯盟的「原始 wOBA」，得到 .250；但聯盟 OBP（**扣除故意四壞**）是 .313。兩者的比值就是 wOBA Scale，最終權重等於步驟 3 的值乘上 Scale：

$$
\text{wOBA Scale} = \frac{\text{lgOBP}_{\text{no IBB}}}{\text{lgwOBA}_{\text{raw}}} = \frac{.313}{.250} \approx 1.251, \qquad w_x = \text{RV}^{*}_x \times \text{wOBA Scale}
$$

驗算：$0.55 \times 1.251 = 0.688$，Guts 表為 .687；$1.65 \times 1.251 = 2.064$，Guts 表為 2.065。差異來自 $\text{RV}^{*}$ 只保留兩位小數。

> [!note] 縮放只是為了好理解
> 縮放到 OBP 是一種美觀上的選擇，也可以縮放到打擊率，或完全不縮放。重點是事件之間的相對價值（[[src-2016-weinberg-fangraphs-deriving-woba]]）。

### wOBA Scale 為什麼有兩種用途
步驟 4 是把「相對出局的得分」**乘上** Scale 變成 OBP 尺度，所以反過來**除以** Scale，就能把 wOBA 的差距換回「每打席得分」：

$$
\frac{\text{wOBA} - \text{lgwOBA}}{\text{wOBA Scale}} = \frac{\text{wRAA}}{\text{PA}}
$$

這就是 wOBA 接到 [[wraa|wRAA]] 的關鍵。

> [!info] 推論：為什麼兩個 wOBA 相減後，出局的平移會抵銷
> 步驟 3 讓每個事件都加上同一個常數，但每個打席（包括出局）都加了這個常數，所以兩個 wOBA 相減後，常數項抵銷，剩下的就是相對平均的差距。這也是為什麼 wRAA 可以直接用 wOBA 的差距計算。

## 推導鏈：上游與下游
- 上游：[[run-expectancy-matrix]] → [[linear-weights]] → wOBA
- 下游：wOBA → [[wraa]] → [[wrc]] → [[wrc-plus]]

$$
\begin{aligned}
\text{wRAA} &= \frac{\text{wOBA} - \text{lgwOBA}}{\text{wOBA Scale}} \times \text{PA} \\
\text{wRC} &= \text{wRAA} + \frac{\text{lgR}}{\text{PA}} \times \text{PA} \\
\text{wRC+} &= \frac{\dfrac{\text{wRC}}{\text{PA}} + \dfrac{\text{lgR}}{\text{PA}}(1 - \text{PF})}{\text{聯盟野手的 wRC/PA}} \times 100
\end{aligned}
$$

每一步加入了什麼：
| 指標 | 單位 | 新加入的東西 |
|---|---|---|
| wOBA | OBP 尺度（比率） | 依得分價值加權 |
| wRAA | 得分（累計，平均 = 0） | 除以 Scale 換回得分、乘上 PA |
| wRC | 得分（累計，絕對值） | 加回聯盟平均得分 |
| wRC+ | 指數（平均 = 100） | 球場調整、除以聯盟野手平均 |

出處：[[src-2010-slowinski-fangraphs-woba]]、[[src-2010-slowinski-fangraphs-wrc]]。

## 聯盟與年份差異
- **MLB**：權重與 Scale 每年重算，FanGraphs Guts 頁面提供 1871 年至今的數值。FanGraphs 實際計算時，每場比賽使用經過球場調整的得分期望值矩陣（[[src-2016-weinberg-fangraphs-deriving-woba]]）。
- **NPB / KBO / CPBL**：尚無來源。這些聯盟的得分環境不同，權重必須用各聯盟自己的得分期望值矩陣重新推導，**不能直接套用 MLB 權重**。

## 如何解讀
MLB 參考門檻（來源標註為估計值，且聯盟平均每年不同）：

| 評等 | wOBA |
|---|---|
| Excellent（頂尖） | .400 |
| Great（優秀） | .370 |
| Above Average（中上） | .340 |
| Average（平均） | .320 |
| Below Average（中下） | .310 |
| Poor（差） | .300 |
| Awful（極差） | .290 |

出處：[[src-2010-slowinski-fangraphs-woba]]。

經驗法則：每 600 PA 中，**20 點 wOBA ≈ 10 分**（相對平均）。以 MLB 2013 年 Scale 驗算：

$$
\frac{0.020}{1.277} \times 600 \approx 9.4 \text{ 分}
$$

所以這個法則的實際數值會隨當年的 Scale 變動。

## 限制與常見誤用
- **故意四壞**不計入分子，並從分母扣除；縮放目標也是扣除故意四壞的 OBP。來源沒有說明排除的理由。
- **跑壘不在內**：盜壘與盜壘失敗已從 wOBA 移出，改由 [[ubr|UBR]] 與 [[wsb|wSB]] 處理。
- **不考慮情境**：同樣是一壘安打，滿壘和壘上無人時權重相同，也不考慮比賽槓桿。
- **沒有球場、聯盟、對手強度調整**：需要跨球隊或跨年代比較時，改用 [[wrc-plus|wRC+]]。
- 原始 wOBA 只適合在同聯盟、同年份內比較。

## 不同的實作方式
wOBA 只是以線性權重為基礎的進攻指標之一。Baseball Prospectus 的 [[true-average|True Average]] 建立在相同的原理上，但實作方式不同（[[src-2016-weinberg-fangraphs-deriving-woba]]）。

## 範例
- [[ex-woba-mlb-2015-derivation]]：從得分期望值推導出 2015 年權重
- [[ex-woba-mlb-2013-trout]]：Mike Trout 2013 年的 wOBA、wRAA、wRC

## 相關頁面
[[run-expectancy-matrix]]、[[linear-weights]]、[[wraa]]、[[wrc]]、[[wrc-plus]]、[[park-factor]]

## 來源
- [[src-2010-slowinski-fangraphs-woba]]：定義、動機、2013 年公式、門檻、限制
- [[src-2016-weinberg-fangraphs-deriving-woba]]：完整推導過程、2010–2015 年常數表
- [[src-2010-slowinski-fangraphs-wrc]]：往 wRC、wRC+ 的推導鏈
