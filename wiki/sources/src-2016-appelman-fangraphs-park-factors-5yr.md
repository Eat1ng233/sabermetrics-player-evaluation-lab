---
title: FanGraphs Library — Park Factors – 5 Year Regressed
type: source
aliases: [5 年迴歸球場係數, FanGraphs 球場係數計算方法]
domain: [method]
leagues: [MLB]
tags: [fangraphs-library, park-adjusted, regression]
sources: []
source_count: 0
status: stable
source_type: article
author: David Appelman（原文作者 Brandon Heipp）
publisher: FanGraphs Library
published: 2016-05-16
url: https://library.fangraphs.com/park-factors-5-year-regressed/
raw_path: raw/articles/2016-05-16_fangraphs_park-factors-5-year-regressed.pdf
ingest_mode: batch
created: 2026-11-23
updated: 2026-11-23
---

# FanGraphs Library — Park Factors – 5 Year Regressed

## 基本資訊
- 由 David Appelman 刊於 FanGraphs（2016-05-16）；原文由 Brandon Heipp 發表於 Buckeyes and Sabermetrics，文中範例年份為 2000–2004 年。
- FanGraphs 說明：這就是 FanGraphs 計算球場係數的方法。
- 原始檔：`raw/articles/2016-05-16_fangraphs_park-factors-5-year-regressed.pdf`；擷取日期：2026-11-23

## 核心論點
1. **為什麼需要**：衡量價值的單位是勝場（由得分與出局構成）。在 Coors Field 打出漂亮數字不代表替球隊贏更多球，所以要做球場調整。
2. **價值 vs 能力**：衡量「價值」時用**得分**球場係數，不分左右打；衡量「能力」時才適合用分項（一壘安打、二壘安打……）與左右打係數。
3. **分母用出局（或場數）**：每場出局數固定為 27，所以以 R/G 計算的係數可以直接套用到球員的得分總數。
4. **計算方法**（源自 Craig Wright，迴歸權重來自 MGL）：
   - 最多用 5 年資料（理想是前兩年、當年、後兩年）；新球場或大幅改建則用較短期間。
   - H = 主場每場得分、R = 客場每場得分、T = 聯盟球隊數：
     $$\text{原始 PF} = \frac{H \times T}{(T-1) \times R + H}$$
     這讓「客場環境」和聯盟一樣，包含 $(T-1)/T$ 的其他球場與 $1/T$ 的自家球場。
   - 減半，讓係數可以套用到整季數據：$\text{iPF} = (\text{原始 PF} + 1) / 2$
   - 迴歸：$\text{PF} = 1 - (1 - \text{iPF}) \times X$，$X$ = 0.6（1 年）、0.7（2 年）、0.8（3 年）、0.9（4 年以上）
   - 例：iPF = 1.25（類似 Coors）→ 1 年 1.15、2 年 1.175、3 年 1.20、4 年 1.225
5. **減半的例子**：主場 11 分／場、客場 10 分／場 → 1.10；但只有一半比賽在主場，所以套用到整季時是 $(1.10 + 1)/2 = 1.05$。
6. 多年資料的優點是樣本大；單年的優點是反映當年天氣、聯盟其他球場的變化。作者選擇多年加迴歸。

## 對 Wiki 的影響
- 更新：[[park-factor]]（計算方法；修正「顯示值換回原始值」的推論，加入迴歸）、[[ex-wrc-plus-mlb-2012-trout]]

## 本來源沒有涵蓋的部分
- 迴歸權重 X 的統計依據（作者表示權重來自 MGL 的建議，本身也覺得有些任意）
- 2016 年之後 FanGraphs 是否調整過方法
