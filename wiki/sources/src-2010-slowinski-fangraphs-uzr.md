---
title: FanGraphs Library — UZR
type: source
aliases: [UZR 說明頁]
domain: [fielding]
leagues: [MLB]
tags: [fangraphs-library, uzr, defense]
sources: []
source_count: 0
status: stable
source_type: article
author: Piper Slowinski
publisher: FanGraphs Library
published: 2010-02-15
url: https://library.fangraphs.com/defense/uzr/
raw_path: raw/articles/2010-02-15_fangraphs_uzr.pdf
ingest_mode: discussed
created: 2026-11-24
updated: 2026-11-24
---

# FanGraphs Library — UZR

## 基本資訊
- 作者：Piper Slowinski；發表：2010-02-15
- 原始檔：`raw/articles/2010-02-15_fangraphs_uzr.pdf`；擷取日期：2026-11-23

## 核心論點
1. UZR 用「得分」衡量守備：球員靠守備比同守位平均多救（或多丟）幾分。
2. 由四個部分組成：外野傳球（ARM）、雙殺（DPR）、守備範圍（RngR）、失誤（ErrR）。
3. 基本邏輯：每顆擊球依位置、速度等有平均得分價值與平均被接殺機率，球員的處理結果和平均比較。
4. 以得分為單位，所以能直接和 wRAA 等打擊得分相加。文中說 FanGraphs 的 WAR 對非捕手使用 UZR。
5. UZR 是相對**同守位**平均；不同守位難度不同，要加上守位調整，得到 Def。
6. 樣本要大：至少 3 年資料再判斷真實能力；UZR/150 把 UZR 換算成 150 場的尺度，方便比較出賽數不同的球員。
7. 使用 BIS 人工記錄的資料，有人為誤差；不考慮守備佈陣與站位；已做球場調整。

## 關鍵數據與公式

$$
\text{UZR} = \text{ARM} + \text{DPR} + \text{RngR} + \text{ErrR}
$$

文章的例子：平均左外野手接到某顆球的機率為 40%，這顆球平均價值 0.8 分；接到就得 $0.8 \times (1-0.4) = 0.48$ 分。

評級表：金手套級 +15、很好 +10、高於平均 +5、平均 0、低於平均 −5、差 −10、很差 −15。

## 對 Wiki 的影響
- 新建頁面：[[uzr]]
- 更新頁面：[[war-position-players]]：守備組成連到 [[uzr]]
- 與既有內容的矛盾：本文說 WAR 使用 UZR，[[src-2024-appelman-fangraphs-war-update]] 說 2016 年起已改用 Statcast（見 [[uzr#不同觀點]]）

## 待追問的問題
- 完整計算細節（文章指向 UZR Primer）
- DRS 的計算方式 → 見 [[drs]]、[[src-2010-slowinski-fangraphs-drs]]
