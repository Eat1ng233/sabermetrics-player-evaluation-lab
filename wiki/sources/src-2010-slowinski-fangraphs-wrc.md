---
title: FanGraphs Library — wRC and wRC+
type: source
aliases: [FanGraphs wRC+ 說明頁, Slowinski wRC]
domain: [batting]
leagues: [MLB]
tags: [fangraphs-library, park-adjusted]
sources: []
source_count: 0
status: stable
source_type: article
author: Piper Slowinski
publisher: FanGraphs Library
published: 2010-02-16
url: https://library.fangraphs.com/offense/wrc/
raw_path: raw/articles/2010-02-16_fangraphs_wrc-and-wrc-plus.pdf
ingest_mode: discussed
created: 2026-11-23
updated: 2026-11-23
---

# FanGraphs Library — wRC and wRC+

## 基本資訊
- 作者：Piper Slowinski
- 出處：FanGraphs Library（Offense 分類）
- 發表：2010-02-16
- 網址：https://library.fangraphs.com/offense/wrc/
- 原始檔：`raw/articles/2010-02-16_fangraphs_wrc-and-wrc-plus.pdf`
- 擷取日期：2026-11-23

## 核心論點
1. [[wrc|wRC]] 是 Bill James Runs Created 的改良版，由 Tom Tango 以 [[woba|wOBA]] 為基礎提出，用「得分」表示打者的總進攻價值。
2. 三者的關係：[[wraa|wRAA]] 是把聯盟平均設為 0 的 wRC；[[batting-runs|Batting Runs]] 是經過球場與聯盟調整的 wRAA。
3. [[wrc-plus|wRC+]] 是控制球場與聯盟後的比率指標，100 是平均，每一分代表高於或低於平均一個百分點。因此可以跨年份、跨球場、跨聯盟比較。
4. wRC+ 是衡量打擊表現最完整的比率指標；應該用它取代 OPS+。
5. 限制：兩者都不考慮情境，也都沒有守位調整；wRC 沒有球場與聯盟調整。

## 關鍵數據與公式

$$
\text{wRC} = \left(\frac{\text{wOBA} - \text{lgwOBA}}{\text{wOBA Scale}} + \frac{\text{lgR}}{\text{PA}}\right) \times \text{PA}
$$

$$
\text{wRC+} = \frac{\left(\dfrac{\text{wRAA}}{\text{PA}} + \dfrac{\text{lgR}}{\text{PA}}\right) + \left(\dfrac{\text{lgR}}{\text{PA}} - \text{PF} \times \dfrac{\text{lgR}}{\text{PA}}\right)}{\text{AL 或 NL 的 wRC/PA（不含投手）}} \times 100
$$

- 範例：Miguel Cabrera 2013 年 wRC = 143.7；Mike Trout 2012 年 wRC+ = 167
- 評等門檻表：見 [[wrc#如何解讀]]、[[wrc-plus#如何解讀]]

## 對 Wiki 的影響
- 新建頁面：[[wrc]]、[[wrc-plus]]、[[park-factor]]（stub）、[[ex-wrc-plus-mlb-2012-trout]]
- 更新頁面：[[woba]]（推導鏈）、[[wraa]]（與 wRC、Batting Runs 的關係）、[[ex-woba-mlb-2013-trout]]（加入 wRC）
- 與既有內容的矛盾：無。「wRAA 是未經球場調整的 Batting Runs」與 [[src-2010-slowinski-fangraphs-woba]] 一致

## 本來源沒有涵蓋的部分
- 球場係數本身怎麼計算
- 「AL 或 NL」分開計算的做法，在 2022 年起兩聯盟都採用指定打擊後是否改變
- Batting Runs 中「聯盟調整」的具體算法
