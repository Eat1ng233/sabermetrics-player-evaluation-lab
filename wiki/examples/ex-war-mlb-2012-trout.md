---
title: 計算範例：Mike Trout 2012 年的野手 WAR
type: example
aliases: [Trout 2012 WAR]
domain: [value, batting, fielding, baserunning]
leagues: [MLB]
tags: [worked-example, war]
sources: ["[[src-2012-slowinski-fangraphs-war-position-players]]", "[[src-2010-slowinski-fangraphs-wrc]]", "[[src-2016-weinberg-fangraphs-deriving-woba]]"]
source_count: 3
status: draft
metric: ["[[war-position-players]]", "[[batting-runs]]", "[[positional-adjustment]]"]
league: MLB
season: 2012
subject: Mike Trout
data: ["raw/data/fangraphs_mlb_2011-2026_trout-advanced.csv", "raw/data/fangraphs_mlb_2011-2026_trout-value.csv", "raw/data/fangraphs_mlb_2026-11-23_trout-player-page.pdf"]
created: 2026-11-23
updated: 2026-11-23
---

# 計算範例：Mike Trout 2012 年的野手 WAR

## 目標
依 [[war-position-players]] 的公式拆解 Trout 2012 年的 WAR，盡可能自己算出每個組成，再和 FanGraphs 的 Value 表對照。

## FanGraphs 的數值（`value.csv`）

| Batting | Base Running | Fielding | Positional | League | Replacement | RAR | WAR |
|---|---|---|---|---|---|---|---|
| 50.1 | 14.3 | 10.4 | −0.2 | 2.7 | 18.9 | 96.1 | 10.1 |

## 逐步計算

### 第 1 步：Batting Runs（可完整重算）
依 [[batting-runs]]，輸入：wRAA 48.2、PA 639（`advanced.csv`）；lgR/PA .114、PF 0.95、美聯野手 wRC/PA = 10032 / 85797（[[src-2010-slowinski-fangraphs-wrc]]）。

$$
\begin{aligned}
\text{球場調整} &= (0.114 - 0.95 \times 0.114) \times 639 = 0.0057 \times 639 = +3.64 \\
\text{聯盟調整} &= \left(0.114 - \frac{10032}{85797}\right) \times 639 = (0.114 - 0.11693) \times 639 = -1.87 \\
\text{Batting} &= 48.2 + 3.64 - 1.87 = 49.97
\end{aligned}
$$

FanGraphs：50.1。差 0.13，來自常數的四捨五入。來源說明手算誤差通常不超過 1 分。

### 第 2 步：Base Running（無法重算）
BsR = UBR + wSB + wGDP。UBR、wGDP 需要 BIS 資料，所以採用 FanGraphs 的 14.3（見 [[bsr]]）。

### 第 3 步：Fielding（無法重算）
UZR 需要 BIS 資料，採用 FanGraphs 的 10.4。

### 第 4 步：Positional（可完整重算）
守備局數：LF 328.0、CF 885⅔、RF 12.0（球員頁 PDF 的 Fielding 表）。依 [[positional-adjustment]]：

$$
\frac{328.0/9}{162}(-7.5) + \frac{885.67/9}{162}(+2.5) + \frac{12.0/9}{162}(-7.5) = -1.69 + 1.52 - 0.06 = -0.23
$$

FanGraphs：−0.2，一致。

### 第 5 步：League（無法重算）
需要美聯全體的 Batting、Base Running、Fielding、Positional 總和與 PA，採用 FanGraphs 的 2.7。

### 第 6 步：Replacement（部分驗證）
需要 2012 年 MLB 總 PA。

> [!info] 推論：反推 MLB 總 PA
> $$\text{lgPA} = \frac{570 \times 9.544 \times 639}{18.9} \approx 183{,}900$$
> 這是合理的 MLB 單季總打席數量級，可以在取得聯盟數據後核對。

### 第 7 步：RAR

$$
\text{RAR} = 50.1 + 14.3 + 10.4 - 0.2 + 2.7 + 18.9 = 96.2
$$

FanGraphs：96.1，差 0.1，來自各組成的四捨五入。

### 第 8 步：WAR
2012 年 RPW = 9.544（[[runs-per-win]]）：

$$
\text{WAR} = \frac{96.1}{9.544} = 10.07 \approx 10.1
$$

（以上數字都已用程式驗算。）

## 結果與驗證

| 組成 | 自己算 | FanGraphs | 狀態 |
|---|---|---|---|
| Batting | 49.97 | 50.1 | ✓ 重算 |
| Base Running | — | 14.3 | 需 BIS 資料 |
| Fielding | — | 10.4 | 需 BIS 資料 |
| Positional | −0.23 | −0.2 | ✓ 重算 |
| League | — | 2.7 | 需聯盟總和 |
| Replacement | — | 18.9 | 需 MLB 總 PA |
| RAR | 96.2（加總） | 96.1 | ✓ |
| WAR | 10.07 | 10.1 | ✓ |

## 解讀
- 10.1 WAR 遠高於 6 WAR 的 MVP 門檻（見 [[war#如何解讀]]）。
- 價值來源：打擊約 50 分、跑壘 14 分、守備 10 分。跑壘與守備合計約 24 分，約 2.5 勝，在野手中相當罕見。
- 守備是 WAR 中不確定性最大的部分（[[war#限制與常見誤用]]），所以這 10 分守備價值的誤差範圍也比較大。

## 相關頁面
[[war]]、[[war-position-players]]、[[batting-runs]]、[[positional-adjustment]]、[[ex-wrc-plus-mlb-2012-trout]]
