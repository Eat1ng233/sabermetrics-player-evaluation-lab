---
title: Batting Runs（打擊得分）
type: metric
aliases: [Batting Runs, Batting, 打擊得分]
domain: [batting, value]
leagues: [MLB]
tags: [counting-stat, runs, park-adjusted, league-adjusted]
sources: ["[[src-2012-slowinski-fangraphs-war-position-players]]", "[[src-2010-slowinski-fangraphs-woba]]", "[[src-2010-slowinski-fangraphs-wrc]]"]
source_count: 3
status: stable
full_name: Batting Runs Above Average
scale: runs
upstream: ["[[wraa]]", "[[park-factor]]"]
downstream: ["[[war-position-players]]", "[[war]]"]
stabilization:
created: 2026-11-23
updated: 2026-11-23
---

# Batting Runs（打擊得分）

> 一句話定義：經過**球場與聯盟調整**的 [[wraa|wRAA]]，也就是打者比聯盟平均多創造的得分。是 WAR 打擊部分的輸入。

## 定義與公式

$$
\text{Batting} = \text{wRAA} + \underbrace{\left(\frac{\text{lgR}}{\text{PA}} - \text{PF} \times \frac{\text{lgR}}{\text{PA}}\right) \times \text{PA}}_{\text{球場調整}} + \underbrace{\left(\frac{\text{lgR}}{\text{PA}} - \frac{\text{wRC}_{\text{lg}}}{\text{PA}_{\text{lg}}}\right) \times \text{PA}}_{\text{聯盟調整}}
$$

變數說明：
- $\text{wRAA}$：見 [[wraa]]
- $\frac{\text{lgR}}{\text{PA}}$：MLB 每打席平均得分（Guts 頁）
- $\text{PF}$：球場係數 ÷ 100（例如 95 → 0.95），使用網站上已減半的數字，見 [[park-factor]]
- $\frac{\text{wRC}_{\text{lg}}}{\text{PA}_{\text{lg}}}$：打者所屬聯盟（AL 或 NL）**不含投手**的 wRC/PA

出處：[[src-2012-slowinski-fangraphs-war-position-players]]。

## 推導過程
- **球場調整**：和 [[wrc-plus|wRC+]] 用的加法調整完全相同，只是乘上 PA 變成總得分。
- **聯盟調整**：wRAA 的基準是 MLB 平均（lgwOBA），這一項把基準換成打者所屬聯盟（AL 或 NL）的**野手**平均：每打席加上「MLB 平均 R/PA − 所屬聯盟野手 wRC/PA」。

> [!info] 推論：聯盟調整的直覺
> 聯盟野手的 wRC/PA 通常高於 MLB 整體 R/PA（因為 MLB 整體包含投手打擊），所以這一項多半是負值。例如 2012 年美聯：$0.114 - 10032/85797 = -0.0029$ 分／打席。

## 和 wRC+ 的關係
兩者使用**相同的球場與聯盟基準**：

$$
\frac{\text{Batting}}{\text{PA}} = \frac{\text{wRC}}{\text{PA}} + \text{球場調整} - \frac{\text{wRC}_{\text{lg}}}{\text{PA}_{\text{lg}}}
$$

> [!info] 推論：同一件事的兩種表達
> wRC+ 是把「打者每打席的 wRC + 球場調整」**除以**聯盟野手的 wRC/PA；Batting Runs/PA 則是**減去**它。所以 Batting Runs 是「相差多少分」，wRC+ 是「相差多少比例」。由上式可推得：
> $$\text{wRC+} = \left(1 + \frac{\text{Batting}/\text{PA}}{\text{wRC}_{\text{lg}}/\text{PA}_{\text{lg}}}\right) \times 100$$
> 用 Trout 2012 年驗算：$\left(1 + \frac{50.1/639}{0.11693}\right) \times 100 = 167.1$，與 FanGraphs 的 167 一致。

## 推導鏈：上游與下游
- 上游：[[woba]] → [[wraa]] → Batting Runs
- 下游：[[war-position-players]]

兩份來源都說明 wRAA 是未調整的 Batting Runs（[[src-2010-slowinski-fangraphs-woba]]、[[src-2010-slowinski-fangraphs-wrc]]）。

## 範例
- [[ex-war-mlb-2012-trout]]：48.2 + 3.64 − 1.87 = 49.97，FanGraphs 為 50.1

## 相關頁面
[[wraa]]、[[wrc-plus]]、[[park-factor]]、[[war-position-players]]

## 來源
- [[src-2012-slowinski-fangraphs-war-position-players]]：公式
- [[src-2010-slowinski-fangraphs-woba]]、[[src-2010-slowinski-fangraphs-wrc]]：與 wRAA 的關係
