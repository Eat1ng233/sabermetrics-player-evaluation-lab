---
title: FanGraphs Library — WAR for Pitchers
type: source
aliases: [投手 WAR 計算]
domain: [value, pitching]
leagues: [MLB]
tags: [fangraphs-library, war, fip]
sources: []
source_count: 0
status: stable
source_type: article
author: Piper Slowinski（Neil Weinberg 更新）
publisher: FanGraphs Library
published: 2012-03-28
url: https://library.fangraphs.com/war/calculating-war-pitchers/
raw_path: raw/articles/2012-03-28_fangraphs_war-pitchers.pdf
ingest_mode: discussed
created: 2026-11-23
updated: 2026-11-23
---

# FanGraphs Library — WAR for Pitchers

## 基本資訊
- 作者：Piper Slowinski；內文由 Neil Weinberg 更新（含 2016 年數值）；發表：2012-03-28
- 原始檔：`raw/articles/2012-03-28_fangraphs_war-pitchers.pdf`；擷取日期：2026-11-12

## 核心論點
1. 先選一個衡量投手相對平均的指標。FanGraphs 用 [[fip|FIP]]，也可以用 RA9 或 DRA；本文不討論選 FIP 的理由。
2. ifFIP：把內野高飛球（IFFB）當作三振，並使用專屬常數（不能直接用 Guts 頁的 cFIP）。
3. 轉成 RA9 尺度 → 用 FIP 專用球場係數調整 → 與 AL 或 NL 平均比較（RAAP9）。
4. 投手會影響自己出賽時的得分環境，所以用**投手專屬的動態 RPW**，而不是聯盟平均 RPW。
5. 替補水準：先發 0.12、後援 0.03（每場勝場）。
6. 乘以 IP/9 得到總量；後援投手乘上槓桿係數 (1 + gmLI) / 2，反映「牛棚順位遞補」（chaining）。
7. 最後每局做統一修正（2016 年為每局 −0.000682902），讓全聯盟投手 WAR 合計 430。
8. 限制：球場係數假設一半比賽在主場；不調整對手強度。

## 對 Wiki 的影響
- 新建：[[war-pitchers]]
- 待補：[[fip]]、[[leverage-index]]

## 本來源沒有涵蓋的部分
- FIP 本身的推導、FIP 球場係數的計算
- 各年度的 WARIP 修正值
