---
title: 知識庫綜述
type: overview
aliases: [Overview, 綜述]
domain: [method]
leagues: [general]
tags: [overview]
sources: ["[[src-2010-slowinski-fangraphs-woba]]", "[[src-2016-weinberg-fangraphs-deriving-woba]]", "[[src-2010-slowinski-fangraphs-wrc]]", "[[src-2010-slowinski-fangraphs-park-factors]]", "[[src-2010-slowinski-fangraphs-what-is-war]]", "[[src-2012-slowinski-fangraphs-war-misconceptions]]", "[[src-2012-slowinski-fangraphs-war-position-players]]", "[[src-2012-slowinski-fangraphs-war-pitchers]]"]
source_count: 8
status: draft
created: 2026-11-23
updated: 2026-11-23
---

# 知識庫綜述

> 本頁由 LLM 維護，概述知識庫目前涵蓋的範圍、核心觀點與尚待研究的問題。隨著來源增加而更新。

## 範圍
賽伯計量學中的球員評估，涵蓋 MLB、NPB、KBO、CPBL。優先領域為打擊與投球、守備與跑壘、Statcast 追蹤數據、新秀評等與合約價值。

## 目前涵蓋
- **打擊推導鏈（MLB）**：[[run-expectancy-matrix|得分期望值矩陣]] → [[linear-weights|線性權重]] → [[woba|wOBA]] → [[wraa|wRAA]] → [[wrc|wRC]] → [[wrc-plus|wRC+]]；以及平行的 [[batting-runs|Batting Runs]]。
- **綜合價值**：[[war|WAR]]（[[war-position-players|野手]]、[[war-pitchers|投手]]），以及組成概念：[[bsr|BsR]]、[[positional-adjustment|守位調整]]、[[replacement-level|替補水準]]、[[runs-per-win|RPW]]。
- **方法**：[[park-factor|球場係數]]。
- **範例**：[[ex-woba-mlb-2015-derivation]]、[[ex-woba-mlb-2013-trout]]、[[ex-wrc-plus-mlb-2012-trout]]、[[ex-war-mlb-2012-trout]]。
- **數據**：Mike Trout 2011–2026 年 FanGraphs 數據（`raw/data/`）。
- 目前只有 MLB 資料；投球（FIP）、守備（UZR、OAA）尚無獨立來源；NPB、KBO、CPBL 尚無來源。

## 核心觀點與綜合結論
- 現代打擊評估的核心是「用得分價值當權重」。線性權重來自得分期望值的變化，wOBA 把它平移（出局 = 0）、縮放（聯盟 wOBA = 聯盟 OBP）成熟悉的尺度。
- wOBA Scale 是打擊推導鏈的樞紐：乘上它進入 OBP 尺度，除以它回到得分。之後每一步只加入一個新東西：乘 PA（wRAA）→ 加回聯盟平均（wRC）→ 球場與聯盟調整（wRC+ 用相除、Batting Runs 用相減）。
- WAR 延續同樣的邏輯：各組成先算「相對平均」的得分，再用守位、聯盟、替補水準調整基準，最後用 RPW 換成勝場。
- 所有指標都不考慮情境，而且都是估計值：守備與投手場內球是最大的不確定性來源。

## 主要分歧
- **替補水準球隊的勝場**：約 43 勝（2012）vs .294 勝率（約 47.7 勝），見 [[replacement-level#不同觀點]]。

## 待研究的問題
- 球場係數怎麼計算（5 年迴歸）？2015 年以前的球場調整要用什麼來源？
- FanGraphs 現行 WAR 是否已加入捕手 framing、是否改用 OAA／FRV 計算守備？
- FIP 的推導（投手 WAR 的基礎）？
- wRC+ 分 AL、NL 計算的做法，在 2022 年兩聯盟都採用指定打擊後是否改變？
- 各聯盟（NPB、KBO、CPBL）的進階數據來源與可取得程度為何？
- 跨聯盟成績換算（MLE）的方法與可靠度？
