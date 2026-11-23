---
title: "WAR Update: Catcher Framing!"
type: source
aliases: [捕手 framing 加入 WAR]
domain: [value, fielding, pitching]
leagues: [MLB]
tags: [fangraphs, war, framing, catcher]
sources: []
source_count: 0
status: stable
source_type: article
author: David Appelman
publisher: FanGraphs
published: 2019-03-20
url: https://blogs.fangraphs.com/war-update-catcher-framing/
raw_path: raw/articles/2019-03-20_fangraphs_war-update-catcher-framing.pdf
ingest_mode: discussed
created: 2026-11-24
updated: 2026-11-24
---

# WAR Update: Catcher Framing!

## 基本資訊
- 作者：David Appelman；發表：2019-03-20（後來修正過一個影響投手 WAR 的錯誤）
- 原始檔：`raw/articles/2019-03-20_fangraphs_war-update-catcher-framing.pdf`；擷取日期：2026-11-24

## 核心論點
1. FanGraphs 加入捕手 framing（偷好球）數據，由 Jared Cross（Steamer 預測系統共同作者）提供，並納入 WAR。文中的比較表涵蓋 2008–2018 年。
2. 爭議點一直不是捕手，而是投手：捕手多拿的 framing 得分，要從投手那邊扣回來。
3. 扣回的方式不是平均分攤，而是看每位投手實際和哪位捕手搭配。例：2011 年釀酒人整體 framing 約 +40 分，多數投手受惠於 Lucroy，但 Randy Wolf 多半搭配 Kottaras，反而略受拖累。
4. 捕手：framing 得分除以每勝得分，加進原本的 WAR。
5. 投手：FIP 加上「每九局 framing 得分」再算 WAR（受惠越多，調整後 FIP 越高），動態每勝得分也一起調整；RA9-WAR 同樣調整。
6. 影響很大：生涯（2008–2018）McCann +18.8、Russell Martin +17.2；Doumit −16.1。單季最大 Lucroy 2011 +4.5。

## 關鍵數據與公式
捕手（本文的簡化寫法）：

$$
\text{WAR} = \dfrac{\text{Batting} + \text{Base Running} + \text{Fielding} + \text{Catcher Framing} + \text{Replacement}}{\text{RPW}}
$$

投手：

$$
\text{WAR} = \left(\dfrac{\text{lgFIP} - \left(\text{FIP} + \dfrac{\text{Framing}}{9}\right)}{\text{dRPW}} + \text{Replacement}\right) \times \dfrac{\text{IP}}{9} \times \text{LI 係數}
$$

例：Greinke 2011 FIP 3.00，每九局受惠 0.31 分 → WAR 計算改用 3.31。

## 對 Wiki 的影響
- 更新頁面：[[war-position-players]]：捕手守備加入 framing；[[war-pitchers]]：FIP 的 framing 調整
- 解決的問題：[[src-2024-appelman-fangraphs-war-update]] 沒有提到的 framing，其實 2019 年就已加入

## 待追問的問題
- framing 回溯的起始年份：文中表格從 2008 年開始，推論資料從 2008 年起
- 捕手公式省略了守位與聯盟調整，只是簡化寫法（推論）；framing 是否也計入聯盟調整的總和，本文沒有說明
