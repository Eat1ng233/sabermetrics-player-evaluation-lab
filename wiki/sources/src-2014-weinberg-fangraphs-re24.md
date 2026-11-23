---
title: FanGraphs Library — RE24
type: source
aliases: [RE24 說明頁]
domain: [method, batting, pitching]
leagues: [MLB]
tags: [fangraphs-library, run-expectancy, context-dependent]
sources: []
source_count: 0
status: stable
source_type: article
author: Neil Weinberg
publisher: FanGraphs Library
published: 2014-07-30
url: https://library.fangraphs.com/misc/re24/
raw_path: raw/articles/2014-07-30_fangraphs_re24.pdf
ingest_mode: batch
created: 2026-11-23
updated: 2026-11-23
---

# FanGraphs Library — RE24

## 基本資訊
- 作者：Neil Weinberg；發表：2014-07-30
- 原始檔：`raw/articles/2014-07-30_fangraphs_re24.pdf`；擷取日期：2026-11-12

## 核心論點
1. **得分期望值（run expectancy）**：在目前的出局數與跑者配置下，到該局結束平均會得幾分。「24」指 3 種出局數 × 8 種跑者配置。
2. **得分期望值矩陣**依整體得分環境、出局數、跑者配置而定；每個球場、每一年都有自己的矩陣。文章附一張得分環境 4.15 分／場、約為 2014 年中性環境的矩陣（例如無人出局一壘有人 = 0.831）。
3. **單一打席的 RE24** = 結果狀態的 RE − 開始狀態的 RE + 這次打席的得分。
   - 例：無人出局一壘有人，一壘安打後變成一三壘有人：$1.798 - 0.831 + 0 = 0.967$
   - 例：無人出局一三壘有人，一壘安打得 1 分、變成一二壘有人：$1.373 - 1.798 + 1 = 0.575$
4. 打者得到的值，投手得到相反數；盜壘、暴投、捕逸的推進算給跑者，投手扣分。
5. **球季 RE24** = 每個打席 RE24 的總和，聯盟平均為 0，數值大小和 wRAA 相近。
6. **考慮情境**：和 wRAA、wRC、Batting Runs 不同，RE24 對壘上有人時的安打給較多分。例：兩出局無人的二壘安打約 +0.2 分，滿壘二壘安打約 +2.5 分。沒有證據顯示「壘上有人時的打擊」是獨立技能，所以 RE24 的預測力不如 wRAA，但適合用來評價已經發生的貢獻。
7. RE24 只控制出局數與跑者配置，不考慮比分、局數，也不含守備價值；除以 RPW 得到 REW，但不等於 WAR。
8. 後援投手特別適用：例如滿壘無人出局上場，全部留在壘上 = +2.282，全部失分後才結束這局 = −0.72。

## 關鍵數據
- 經驗法則（打者）：45 頂尖、30 優秀、15 中上、0 平均、−5 中下、−10 差、−20 極差。先發投手、後援投手另有門檻。
- 比較情境與否：RE24 對照 Batting Runs + wSB（或 Off − UBR）。

## 對 Wiki 的影響
- 新建：[[re24]]
- 更新：[[run-expectancy-matrix]]（定義、計算方式；「直接得分」一項由推論改為有來源）、[[linear-weights]]

## 本來源沒有涵蓋的部分
- 得分期望值矩陣如何依得分環境調整（文章只附互動工具連結）
