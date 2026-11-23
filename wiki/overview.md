---
title: 知識庫綜述
type: overview
aliases: [Overview, 綜述]
domain: [method]
leagues: [general]
tags: [overview]
sources: ["[[src-2010-slowinski-fangraphs-woba]]", "[[src-2016-weinberg-fangraphs-deriving-woba]]", "[[src-2010-slowinski-fangraphs-wrc]]"]
source_count: 3
status: draft
created: 2026-11-23
updated: 2026-11-23
---

# 知識庫綜述

> 本頁由 LLM 維護，概述知識庫目前涵蓋的範圍、核心觀點與尚待研究的問題。隨著來源增加而更新。

## 範圍
賽伯計量學中的球員評估，涵蓋 MLB、NPB、KBO、CPBL。優先領域為打擊與投球、守備與跑壘、Statcast 追蹤數據、新秀評等與合約價值。

## 目前涵蓋
- **打擊指標推導鏈（MLB）**：[[run-expectancy-matrix|得分期望值矩陣]] → [[linear-weights|線性權重]] → [[woba|wOBA]] → [[wraa|wRAA]] → [[wrc|wRC]] → [[wrc-plus|wRC+]]，每一步都有來源與計算範例。
- **方法**：[[park-factor|球場係數]]（stub，只有 wRC+ 中的用法）。
- **範例**：[[ex-woba-mlb-2015-derivation]]、[[ex-woba-mlb-2013-trout]]、[[ex-wrc-plus-mlb-2012-trout]]。
- **數據**：Mike Trout 2011–2026 年 FanGraphs 數據（`raw/data/`）。
- 目前只有 MLB 資料，NPB、KBO、CPBL 尚無來源。

## 核心觀點與綜合結論
- 現代打擊評估的核心是「用得分價值當權重」。線性權重來自得分期望值的變化，wOBA 把它平移（出局 = 0）、縮放（聯盟 wOBA = 聯盟 OBP）成大家熟悉的尺度。
- wOBA Scale 是整條推導鏈的樞紐：乘上它進入 OBP 尺度，除以它回到得分。之後每一步只加入一個新東西：乘 PA（wRAA）→ 加回聯盟平均（wRC）→ 球場與聯盟調整後除以野手平均（wRC+）。
- 縮放到 OBP 是為了好理解，不影響事件之間的相對價值。

## 主要分歧
_（待來源累積後撰寫，詳見各頁「不同觀點」段落）_

## 待研究的問題
- 球場係數怎麼計算？2015 年以前的球場調整要用什麼來源？
- wRC+ 分 AL、NL 計算的做法，在 2022 年兩聯盟都採用指定打擊後是否改變？
- Batting Runs 的「聯盟調整」具體怎麼算？如何接到 WAR？
- 各聯盟（NPB、KBO、CPBL）的進階數據來源與可取得程度為何？
- 跨聯盟成績換算（MLE）的方法與可靠度？
