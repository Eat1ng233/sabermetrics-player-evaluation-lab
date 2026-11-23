---
title: wRAA（加權得分高於平均值）
type: metric
aliases: [wRAA, weighted Runs Above Average]
domain: [batting]
leagues: [MLB]
tags: [counting-stat, runs, linear-weights]
sources: ["[[src-2010-slowinski-fangraphs-woba]]", "[[src-2010-slowinski-fangraphs-wrc]]"]
source_count: 2
status: stable
full_name: weighted Runs Above Average
scale: runs
upstream: ["[[woba]]"]
downstream: ["[[wrc]]", "[[wrc-plus]]", "[[batting-runs]]"]
stabilization:
created: 2026-11-23
updated: 2026-11-23
---

# wRAA（加權得分高於平均值）

> 一句話定義：把打者的 [[woba|wOBA]] 與聯盟平均的差距換算成**得分**，再乘上打席數，得出這位打者比聯盟平均打者多創造多少分。

## 它在回答什麼問題
wOBA 是比率指標，只回答「每個打席打得多好」。wRAA 把它轉成累計值：「整季下來，比平均打者多貢獻幾分？」這樣同時反映了品質與上場量。

## 定義與公式

$$
\text{wRAA} = \frac{\text{wOBA} - \text{lgwOBA}}{\text{wOBA Scale}} \times \text{PA}
$$

變數說明：
- $\text{wOBA}$：打者的 wOBA
- $\text{lgwOBA}$：同聯盟、同球季的聯盟平均 wOBA（MLB 2013 年 = .314）
- $\text{wOBA Scale}$：同聯盟、同球季的縮放係數（MLB 2013 年 = 1.277）
- $\text{PA}$：打席數

出處：[[src-2010-slowinski-fangraphs-woba]]。各年常數見 [[woba#MLB 2010–2015 年常數]]。

## 推導過程
1. $\text{wOBA} - \text{lgwOBA}$：每個打席比聯盟平均高多少，單位是「OBP 尺度」。
2. 除以 $\text{wOBA Scale}$：wOBA 的權重是「相對出局的得分 × Scale」（見 [[woba#推導過程]]），除回去就變成**每打席多創造的得分**。
3. 乘上 $\text{PA}$：變成整季的累計得分。

定義上，聯盟平均打者的 wRAA = 0。

## 推導鏈：上游與下游
- 上游：[[woba]]
- 下游：
  - [[wrc]]：wRAA 加回聯盟平均得分，$\text{wRC} = \text{wRAA} + \frac{\text{lgR}}{\text{PA}} \times \text{PA}$
  - [[wrc-plus]]：wRAA/PA 是 wRC+ 公式的第一項
  - [[batting-runs]]：wRAA 經過球場與聯盟調整後就是 Batting Runs

兩份來源的說法一致：[[src-2010-slowinski-fangraphs-woba]] 說 wRAA 是未經球場調整的 Batting Runs；[[src-2010-slowinski-fangraphs-wrc]] 說 Batting Runs 是經過球場與聯盟調整的 wRAA。

## 聯盟與年份差異
$\text{lgwOBA}$ 與 $\text{wOBA Scale}$ 都是特定聯盟、特定球季的常數。NPB、KBO、CPBL 目前尚無來源。

## 如何解讀
- 0 = 聯盟平均
- 經驗法則（MLB）：每 600 PA 中，20 點 wOBA ≈ 10 分 wRAA。實際數值依當年 Scale 而定（2013 年約 9.4 分），見 [[woba#如何解讀]]。
- wRAA 和 wRC 是同一件事的不同表達：wRAA 以平均為 0，wRC 是絕對得分（[[src-2010-slowinski-fangraphs-wrc]]）。

## 限制與常見誤用
- 沒有球場調整，打者友善球場的球員會被高估。
- 以「平均」而不是「替補水準」為基準，所以上場時間多的平均打者 wRAA 仍是 0，不能反映他的耐操價值。替補水準的概念見 [[replacement-level]]。
- 繼承 wOBA 的所有限制（不考慮情境、不含跑壘）。

## 範例
- [[ex-woba-mlb-2013-trout]]：Trout 2013 年 wRAA = 61.1；FanGraphs Batting = 62.2，差距來自球場與聯盟調整
- [[ex-wrc-plus-mlb-2012-trout]]：Trout 2012 年 wRAA 48.2 代入 wRC+

## 相關頁面
[[woba]]、[[wrc]]、[[wrc-plus]]、[[batting-runs]]、[[park-factor]]

## 來源
- [[src-2010-slowinski-fangraphs-woba]]：公式、與 Batting Runs 的關係、Trout 範例
- [[src-2010-slowinski-fangraphs-wrc]]：與 wRC、Batting Runs 的關係
