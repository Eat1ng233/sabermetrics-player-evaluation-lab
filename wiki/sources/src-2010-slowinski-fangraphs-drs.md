---
title: FanGraphs Library — DRS
type: source
aliases: [DRS 說明頁]
domain: [fielding]
leagues: [MLB]
tags: [fangraphs-library, drs, defense]
sources: []
source_count: 0
status: stable
source_type: article
author: Piper Slowinski
publisher: FanGraphs Library
published: 2010-02-15
url: https://library.fangraphs.com/defense/drs/
raw_path: raw/articles/2010-02-15_fangraphs_drs.pdf
ingest_mode: discussed
created: 2026-11-24
updated: 2026-11-24
---

# FanGraphs Library — DRS

## 基本資訊
- 作者：Piper Slowinski；發表：2010-02-15
- 原始檔：`raw/articles/2010-02-15_fangraphs_drs.pdf`；擷取日期：2026-11-24

## 核心論點
1. DRS（Defensive Runs Saved）由 John Dewan 的 The Fielding Bible 計算，衡量球員比同守位平均多救幾分；和 UZR 一樣用 BIS 資料、以得分為單位。
2. 組成：rSB（阻殺盜壘，捕手／投手）、rBU（處理觸擊，一壘／三壘）、rGDP（雙殺，二壘／游擊）、rARM（外野傳球）、rHR（沒收全壘打，每次 1.6 分）、rPM（Plus/Minus，守備範圍與把擊球變出局的能力）。
3. 讀法和 UZR 相同：+5 的三壘手比平均三壘手多救 5 分；評級表也相同（+15 金手套級 … −15 很差）。
4. 跨守位比較要加守位調整；可以用 DRS 加守位調整，得到以 DRS 為基礎的 Def。
5. 限制：小樣本不可靠、人工記錄的誤差、不考慮佈陣與站位。
6. 和 UZR 的差別：DRS 用滾動的**一年**資料判斷每一球的難度，UZR 用**多年**資料；DRS 也包含投手與捕手的守備。兩者多數時候結論一致。

## 關鍵數據與公式

$$
\text{DRS} = \text{rSB} + \text{rBU} + \text{rGDP} + \text{rARM} + \text{rHR} + \text{rPM}
$$

（推論：來源列出各組成並說 DRS 是總和，沒有寫成公式；Fielding Bible 可能還有本文未列出的組成。）

## 對 Wiki 的影響
- 新建頁面：[[drs]]
- 更新頁面：[[uzr]]：加入和 DRS 的比較；[[war-position-players]]：捕手的 rSB 連到 [[drs]]

## 待追問的問題
- 完整計算方式（文章指向 Fielding Bible 的 FAQ）
- RPP（防止捕逸、暴投）在本文沒有列出，但 [[src-2012-slowinski-fangraphs-war-position-players]] 說捕手守備用 rSB + RPP
