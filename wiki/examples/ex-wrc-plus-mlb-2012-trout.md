---
title: 計算範例：Mike Trout 2012 年的 wRC+
type: example
aliases: [Trout 2012 wRC+]
domain: [batting]
leagues: [MLB]
tags: [worked-example, park-adjusted]
sources: ["[[src-2010-slowinski-fangraphs-wrc]]", "[[src-2010-slowinski-fangraphs-park-factors]]"]
source_count: 2
status: stable
metric: ["[[wrc-plus]]"]
league: MLB
season: 2012
subject: Mike Trout
data: ["raw/data/fangraphs_mlb_2011-2026_trout-standard.csv", "raw/data/fangraphs_mlb_2011-2026_trout-advanced.csv"]
created: 2026-11-23
updated: 2026-11-23
---

# 計算範例：Mike Trout 2012 年的 wRC+

## 目標
依 [[wrc-plus|wRC+]] 公式，逐步算出 Mike Trout 2012 年的 wRC+。

## 輸入資料

| 項目 | 數值 | 出處 |
|---|---|---|
| wRAA | 48.2 | [[src-2010-slowinski-fangraphs-wrc]]；與 `advanced.csv` 一致 |
| PA | 639 | 同上；與 `standard.csv` 一致 |

## 使用的常數

| 常數 | 數值 | 說明 |
|---|---|---|
| $\text{lgR/PA}$ | .114 | MLB 2012（也與 [[woba#MLB 2010–2015 年常數]] 一致） |
| $\text{PF}$ | 0.95 | 天使隊主場，FanGraphs 網站顯示的球場係數 95 ÷ 100（顯示值已減半，見 [[park-factor]]） |
| AL 野手 wRC 總和 | 10032 | 美聯 2012 年，不含投手 |
| AL 野手 PA 總和 | 85797 | 同上 |

出處：[[src-2010-slowinski-fangraphs-wrc]]。

## 逐步計算

### 第 1 步：每打席的 wRAA

$$
\frac{\text{wRAA}}{\text{PA}} = \frac{48.2}{639} = 0.07543
$$

### 第 2 步：加回聯盟平均，得到每打席的 wRC

$$
\frac{\text{wRC}}{\text{PA}} = 0.07543 + 0.114 = 0.18943
$$

### 第 3 步：球場調整（加法）

$$
\frac{\text{lgR}}{\text{PA}} \times (1 - \text{PF}) = 0.114 \times (1 - 0.95) = 0.00570
$$

PF < 1 代表天使主場在 2012 年偏向投手，所以每打席加回 0.0057 分。

> [!info] 推論：原始球場係數
> 顯示值 95 已減半。依 [[park-factor]]，原始係數約為 $2 \times 95 - 100 = 90$，也就是天使主場的得分約比平均少 10%。

### 第 4 步：聯盟野手平均

$$
\frac{\text{wRC}_{\text{AL}}}{\text{PA}_{\text{AL}}} = \frac{10032}{85797} = 0.11693
$$

### 第 5 步：wRC+

$$
\text{wRC+} = \frac{0.18943 + 0.00570}{0.11693} \times 100 = \frac{0.19513}{0.11693} \times 100 = 166.9 \approx 167
$$

（已用程式驗算。）

## 結果與驗證
- 166.9 ≈ **167**，與來源及 FanGraphs 頁面（`advanced.csv` 2012 年 wRC+ = 167）一致。

## 解讀
- Trout 每打席創造的得分（經球場調整）是美聯野手平均的 1.67 倍，高於 160 的「頂尖」門檻（見 [[wrc-plus#如何解讀]]）。
- 球場調整的影響：如果不做球場調整，結果是 $0.18943 / 0.11693 \times 100 = 162.0$。球場調整讓他多了約 5 分。

## 相關頁面
[[wrc-plus]]、[[wrc]]、[[wraa]]、[[park-factor]]、[[ex-war-mlb-2012-trout]]
