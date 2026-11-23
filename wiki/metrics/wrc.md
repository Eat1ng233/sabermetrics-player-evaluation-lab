---
title: wRC（加權得分創造）
type: metric
aliases: [wRC, weighted Runs Created, 加權得分創造]
domain: [batting]
leagues: [MLB]
tags: [counting-stat, runs, linear-weights]
sources: ["[[src-2010-slowinski-fangraphs-wrc]]"]
source_count: 1
status: draft
full_name: weighted Runs Created
scale: runs
upstream: ["[[woba]]", "[[wraa]]"]
downstream: ["[[wrc-plus]]"]
stabilization:
created: 2026-11-23
updated: 2026-11-23
---

# wRC（加權得分創造）

> 一句話定義：以 [[woba|wOBA]] 為基礎，估計一位打者替球隊創造的**總得分**。是 Bill James Runs Created 的改良版，由 Tom Tango 提出。

## 它在回答什麼問題
「這位打者整季總共替球隊創造了幾分？」和 [[wraa|wRAA]] 是同一件事的不同表達方式：wRAA 以聯盟平均為 0，wRC 則是絕對的得分數（[[src-2010-slowinski-fangraphs-wrc]]）。

## 定義與公式

$$
\text{wRC} = \left(\frac{\text{wOBA} - \text{lgwOBA}}{\text{wOBA Scale}} + \frac{\text{lgR}}{\text{PA}}\right) \times \text{PA}
$$

變數說明：
- $\text{wOBA}$：打者的 wOBA
- $\text{lgwOBA}$、$\text{wOBA Scale}$：同聯盟、同球季的常數（MLB 2013 年 = .314、1.277）
- $\dfrac{\text{lgR}}{\text{PA}}$：聯盟每打席平均得分 = MLB 總得分 ÷ 總打席（MLB 2013 年 = .110；Guts 頁四捨五入到小數三位，所以手算可能有微小誤差）
- $\text{PA}$：打席數

出處：[[src-2010-slowinski-fangraphs-wrc]]；2013 年常數見 [[woba#MLB 2010–2015 年常數]]。

## 推導過程
括號內第一項就是每打席的 wRAA（見 [[wraa]]），所以：

$$
\text{wRC} = \left(\frac{\text{wRAA}}{\text{PA}} + \frac{\text{lgR}}{\text{PA}}\right) \times \text{PA} = \text{wRAA} + \frac{\text{lgR}}{\text{PA}} \times \text{PA}
$$

意思是：**wRC = 比平均多創造的得分 + 平均打者在同樣打席數會創造的得分**。把「相對平均」的 wRAA 加回聯盟平均，就變成絕對得分。

## 推導鏈：上游與下游
- 上游：[[woba]] → [[wraa]] → wRC
- 下游：wRC → [[wrc-plus]]（加入球場與聯盟調整後，除以聯盟平均）

## 聯盟與年份差異
$\text{lgR/PA}$ 隨得分環境每年變動。wRC 本身**沒有**球場與聯盟調整。NPB、KBO、CPBL 目前尚無來源。

## 如何解讀
wRC 是累計值，一定要搭配打席數看：50 PA 打出 10 wRC 很好，200 PA 打出 10 wRC 就很差（[[src-2010-slowinski-fangraphs-wrc]]）。

MLB 參考門檻（每 600 PA，來源標註為估計值）：

| 評等 | wRC |
|---|---|
| Excellent（頂尖） | 105 |
| Great（優秀） | 90 |
| Above Average（中上） | 75 |
| Average（平均） | 65 |
| Below Average（中下） | 60 |
| Poor（差） | 50 |
| Awful（極差） | 40 |

## 限制與常見誤用
- 沒有球場、聯盟、守位調整。
- 不考慮情境（[[src-2010-slowinski-fangraphs-wrc]]）。

## 範例
- 來源範例：Miguel Cabrera 2013 年 wOBA .455、652 PA：$\left(\frac{.455 - .314}{1.277} + .110\right) \times 652 = 143.7$（已驗算）
- [[ex-woba-mlb-2013-trout]]：Trout 2013 年 wRC ≈ 140

## 相關頁面
[[woba]]、[[wraa]]、[[wrc-plus]]、[[batting-runs]]

## 來源
- [[src-2010-slowinski-fangraphs-wrc]]：定義、公式、Cabrera 範例、門檻
