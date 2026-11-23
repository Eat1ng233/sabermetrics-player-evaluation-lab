---
title: FanGraphs Library — Park Factors
type: source
aliases: [Park Factors 說明頁]
domain: [method]
leagues: [MLB]
tags: [fangraphs-library, park-adjusted]
sources: []
source_count: 0
status: stable
source_type: article
author: Piper Slowinski
publisher: FanGraphs Library
published: 2010-02-27
url: https://library.fangraphs.com/principles/park-factors/
raw_path: raw/articles/2010-02-27_fangraphs_park-factors.pdf
ingest_mode: discussed
created: 2026-11-23
updated: 2026-11-23
---

# FanGraphs Library — Park Factors

## 基本資訊
- 作者：Piper Slowinski；發表：2010-02-27（內容提到 5 年迴歸球場係數，應為後來更新的版本）
- 原始檔：`raw/articles/2010-02-27_fangraphs_park-factors.pdf`；擷取日期：2026-11-23

## 核心論點
1. 每座球場的尺寸都不同，而且球場效應不只來自尺寸，天氣、空氣密度、周邊地形、看台配置都會影響擊球飛行。例如 Petco Park 的海霧、Coors Field 的稀薄空氣。「大球場」不等於「投手球場」。
2. 理想做法是知道每個打席在 30 座球場各會變成什麼結果，但資料不足，只能用近似值。
3. FanGraphs 使用 **5 年迴歸**的球場係數。網站上顯示的數字**已經減半**，因為球員只有一半比賽在主場，其餘假設在中性環境。平均 = 100；顯示 105 代表主場得分多 10%。
4. 另外也提供各種安打、擊球類型、左右打的係數，但球場調整只用總體係數。
5. 採用**加法**調整。FanGraphs 不算 wOBA+，而是用 [[wrc-plus|wRC+]] 作為經球場調整的打擊指標；ERA− 等 +/− 指標也都有球場調整。
6. 限制：單一數字無法反映球場對不同球員的不同影響。例如 Target Field 整體略偏打者、與 Yankee Stadium 相近，但對左打全壘打非常不利。

## 對 Wiki 的影響
- 更新：[[park-factor]]（stub → draft）、[[wrc-plus]]、[[ex-wrc-plus-mlb-2012-trout]]（PF 0.95 是減半後的數字）

## 本來源沒有涵蓋的部分
- 5 年迴歸球場係數的計算細節（文章只附連結）
