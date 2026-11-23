---
title: FanGraphs Library — WAR for Position Players
type: source
aliases: [野手 WAR 計算]
domain: [value, batting, fielding, baserunning]
leagues: [MLB]
tags: [fangraphs-library, war]
sources: []
source_count: 0
status: stable
source_type: article
author: Piper Slowinski
publisher: FanGraphs Library
published: 2012-04-02
url: https://library.fangraphs.com/war/war-position-players/
raw_path: raw/articles/2012-04-02_fangraphs_war-position-players.pdf
ingest_mode: discussed
created: 2026-11-23
updated: 2026-11-23
---

# FanGraphs Library — WAR for Position Players

## 基本資訊
- 作者：Piper Slowinski；發表：2012-04-02
- 原始檔：`raw/articles/2012-04-02_fangraphs_war-position-players.pdf`；擷取日期：2026-11-12

## 核心論點
1. 總公式：$\text{WAR} = \text{RAR} / \text{RPW}$，其中 RAR = Batting + Base Running + Fielding + 守位調整 + 聯盟調整 + 替補水準。網站上的 Off = Batting + Base Running，Def = Fielding + 守位調整。
2. [[batting-runs|Batting Runs]] = wRAA + 球場調整 + 聯盟調整（以 AL 或 NL 野手 wRC/PA 為基準）。
3. [[bsr|BsR]] = UBR + wSB + wGDP；文章附 wSB 公式，盜壘價值固定 0.2 分。
4. 守備：非捕手用 UZR；捕手用 rSB + RPP，不含 framing。守備得分相對於「同守位平均」。
5. [[positional-adjustment|守位調整]]：每 162 場（每場 = 9 局）的固定值；數值來自多年前的實證比較，可能隨時間改變。
6. 聯盟調整：讓每個聯盟的「高於平均得分」總和為 0，每季影響約 0～5 分。
7. [[replacement-level|替補水準得分]]：1,000 WAR／2,430 場，野手占 57%（570 WAR）。
8. [[runs-per-win|RPW]] = 9 × (MLB 得分 ÷ 投球局數) × 1.5 + 3，與 Pythagpat 相差約 0.02。
9. 手算結果與網站可能差一點，因為網站的球場係數、R/PA 保留更多位數。

## 對 Wiki 的影響
- 新建：[[war-position-players]]、[[batting-runs]]、[[bsr]]、[[positional-adjustment]]、[[runs-per-win]]、[[ex-war-mlb-2012-trout]]
- 更新：[[wraa]]、[[replacement-level]]

## 本來源沒有涵蓋的部分
- UZR、UBR、wGDP 的計算（只附連結；UBR 需要 BIS 影像資料，無法自算）
- 守位調整數值的推導
