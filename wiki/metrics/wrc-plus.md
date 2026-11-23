---
title: wRC+（加權得分創造指數）
type: metric
aliases: [wRC+, weighted Runs Created Plus, 加權得分創造指數]
domain: [batting]
leagues: [MLB]
tags: [rate-stat, park-adjusted, league-adjusted, index-100]
sources: ["[[src-2010-slowinski-fangraphs-wrc]]"]
source_count: 1
status: draft
full_name: weighted Runs Created Plus
scale: 100=avg
upstream: ["[[wrc]]", "[[wraa]]", "[[park-factor]]"]
downstream: []
stabilization:
created: 2026-11-23
updated: 2026-11-23
---

# wRC+（加權得分創造指數）

> 一句話定義：經過**球場與聯盟調整**後，打者每打席創造的得分相對聯盟平均的比例，以 100 為平均。

## 它在回答什麼問題
「排除球場和年代的影響後，這位打者比平均打者好多少？」

[[woba|wOBA]] 和 [[wrc|wRC]] 都沒有調整球場與得分環境：在打者天堂打出 .400 wOBA，不如在投手球場打出同樣數字；2000 年的 .400 也不如 2014 年的 .400。wRC+ 把這兩件事都調整掉，所以可以跨年份、跨球場、跨聯盟比較，例如比較 Ted Williams 和 Albert Pujols（[[src-2010-slowinski-fangraphs-wrc]]）。

## 定義與公式

$$
\text{wRC+} = \frac{\left(\dfrac{\text{wRAA}}{\text{PA}} + \dfrac{\text{lgR}}{\text{PA}}\right) + \left(\dfrac{\text{lgR}}{\text{PA}} - \text{PF} \times \dfrac{\text{lgR}}{\text{PA}}\right)}{\dfrac{\text{wRC}_{\text{lg}}}{\text{PA}_{\text{lg}}}\ \text{（AL 或 NL，不含投手）}} \times 100
$$

變數說明：
- $\dfrac{\text{wRAA}}{\text{PA}}$：打者每打席高於平均的得分，也可以直接算成 $\dfrac{\text{wOBA} - \text{lgwOBA}}{\text{wOBA Scale}}$，兩種算法結果相同
- $\dfrac{\text{lgR}}{\text{PA}}$：**MLB** 每打席平均得分（Guts 頁）
- $\text{PF}$：球場係數，FanGraphs 頁面上的數字除以 100（例如 95 → 0.95），見 [[park-factor]]
- 分母：打者所屬聯盟（AL 或 NL）**扣除投手**後的 wRC 總和 ÷ PA 總和，要從 Leaders 頁面取得

出處：[[src-2010-slowinski-fangraphs-wrc]]。

## 推導過程
把公式拆成三塊（[[src-2010-slowinski-fangraphs-wrc]]）：

**1. 分子第一個括號 = 打者每打席的 wRC。** 依 [[wrc#推導過程]]，$\dfrac{\text{wRAA}}{\text{PA}} + \dfrac{\text{lgR}}{\text{PA}} = \dfrac{\text{wRC}}{\text{PA}}$。

**2. 分子第二個括號 = 球場調整（加法）。**

$$
\frac{\text{lgR}}{\text{PA}} - \text{PF} \times \frac{\text{lgR}}{\text{PA}} = \frac{\text{lgR}}{\text{PA}} \times (1 - \text{PF})
$$

投手球場（$\text{PF} < 1$）加分，打者球場（$\text{PF} > 1$）扣分。

**3. 除以聯盟（不含投手）的 wRC/PA，再乘以 100。** 這一步完成**聯盟調整**：比較的基準是同聯盟的野手平均，所以平均野手 = 100。

整理後可以寫成：

$$
\text{wRC+} = \frac{\dfrac{\text{wRC}}{\text{PA}} + \text{球場調整}}{\text{聯盟野手的 wRC/PA}} \times 100
$$

> [!info] 推論：為什麼結果可以讀成「百分比」
> 因為分子和分母的單位都是「每打席得分」，比值就是「這位打者每打席創造的得分是聯盟野手平均的幾倍」。乘以 100 後，125 就代表多 25%。

## 推導鏈：上游與下游
- 上游：[[run-expectancy-matrix]] → [[linear-weights]] → [[woba]] → [[wraa]] → [[wrc]] → wRC+
- 調整項：[[park-factor]]、聯盟（AL / NL）野手平均

## 聯盟與年份差異
- 平均永遠是 100，所以 2000 年的 140 和 2014 年的 140 意義相同（[[src-2010-slowinski-fangraphs-wrc]]）。
- 分母分 AL、NL 計算。2022 年起兩聯盟都採用指定打擊，這個做法是否改變，目前沒有來源。
- 球場係數：使用者指出 FanGraphs 目前只提供 2016 年以後的球場係數（見 [[park-factor]]）。
- NPB、KBO、CPBL 目前尚無來源。

## 如何解讀
MLB 參考門檻（來源標註為估計值）：

| 評等 | wRC+ |
|---|---|
| Excellent（頂尖） | 160 |
| Great（優秀） | 140 |
| Above Average（中上） | 115 |
| Average（平均） | 100 |
| Below Average（中下） | 80 |
| Poor（差） | 75 |
| Awful（極差） | 60 |

出處：[[src-2010-slowinski-fangraphs-wrc]]。

## 限制與常見誤用
- **沒有守位調整**：同樣 120 的捕手和一壘手，價值並不相同。
- **不考慮情境**：有人在壘和壘上無人的安打權重相同。
- 手算時因為常數四捨五入，可能和 FanGraphs 的數字差 1 分。
- 應該用 wRC+ 取代 OPS+：兩者結論通常相似，但 wRC+ 以 wOBA 為基礎，更準確（[[src-2010-slowinski-fangraphs-wrc]]）。

## 範例
- [[ex-wrc-plus-mlb-2012-trout]]：Trout 2012 年 wRC+ = 167

## 相關頁面
[[wrc]]、[[wraa]]、[[woba]]、[[park-factor]]、[[ops-plus]]

## 來源
- [[src-2010-slowinski-fangraphs-wrc]]：定義、公式、各項說明、Trout 2012 範例、門檻
