---
title: The Beginner's Guide To Deriving wOBA
type: source
aliases: [Deriving wOBA, Weinberg wOBA 推導]
domain: [batting, method]
leagues: [MLB]
tags: [fangraphs-library, linear-weights, run-expectancy]
sources: []
source_count: 0
status: stable
source_type: article
author: Neil Weinberg
publisher: FanGraphs Library
published: 2016-04-11
url: https://library.fangraphs.com/the-beginners-guide-to-deriving-woba/
raw_path: raw/articles/2016-04-11_fangraphs_deriving-woba.pdf
ingest_mode: discussed
created: 2026-11-23
updated: 2026-11-23
---

# The Beginner's Guide To Deriving wOBA

## 基本資訊
- 作者：Neil Weinberg（FanGraphs Site Educator）
- 出處：FanGraphs Library
- 發表：2016-04-11
- 網址：https://library.fangraphs.com/the-beginners-guide-to-deriving-woba/
- 原始檔：`raw/articles/2016-04-11_fangraphs_deriving-woba.pdf`
- 擷取日期：2026-11-23

## 核心論點
1. [[woba|wOBA]] 的目標是衡量每種進攻結果對得分的**情境中立**貢獻。例如保送一定讓每位跑者推進一個壘包，一壘安打的結果則依跑者位置和擊球方向而不同，兩者的價值不同。
2. 推導分三步：用[[run-expectancy-matrix|得分期望值矩陣]]算出各事件的平均得分變化（[[linear-weights|線性權重]]）→ 平移讓出局 = 0 → 乘上 wOBA Scale，讓聯盟 wOBA 等於聯盟 OBP（扣除故意四壞）。
3. 權重每年依得分環境變動，但幅度不大。
4. 縮放到 OBP 只是為了好理解，也可以縮放到打擊率或完全不縮放。Baseball Prospectus 的 True Average 是同一個概念的另一種做法。
5. FanGraphs 實際計算時，每場比賽都用經過球場調整的矩陣，所以和文章中的整體矩陣會略有差異。
6. wOBA 本身不考慮球場、聯盟、對手強度等因素，是後續調整的基礎。

## 關鍵數據與公式
- 2010–2015 年 MLB 得分期望值矩陣（Tom Tango 計算）：見 [[run-expectancy-matrix]]
- 2015 年各事件高於平均的得分值，以及相對出局的得分值：見 [[ex-woba-mlb-2015-derivation]]
- 2010–2015 年 Guts 常數表（lgwOBA、Scale、權重、R/PA 等）：見 [[woba#MLB 2010–2015 年常數]]

關鍵式：

$$
\text{wOBA Scale} = \frac{\text{lgOBP}_{\text{no IBB}}}{\text{lgwOBA}_{\text{raw}}} = \frac{.313}{.250} \approx 1.251 \quad \text{(MLB 2015)}
$$

## 對 Wiki 的影響
- 新建頁面：[[run-expectancy-matrix]]、[[ex-woba-mlb-2015-derivation]]
- 更新頁面：[[woba]]（推導過程從「推論」改為有來源的版本，並修正縮放目標為扣除 IBB 的 OBP）、[[linear-weights]]
- 與既有內容的矛盾：無。先前 [[woba]] 的推論骨架三個步驟都得到確認

## 本來源沒有涵蓋的部分
- 用來算出 .250 的 2015 年全聯盟事件總數
- 出局的線性權重如何精確計算（文章只說「用同樣方法」，給出約 −0.26）
- 為什麼縮放目標要扣除故意四壞（只說明是為了配合 OBP 扣除 IBB）
