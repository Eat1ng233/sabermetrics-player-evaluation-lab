---
title: 計算範例：Mike Trout 2013 年的 wOBA、wRAA 與 wRC
type: example
aliases: [Trout 2013 wOBA]
domain: [batting]
leagues: [MLB]
tags: [worked-example]
sources: ["[[src-2010-slowinski-fangraphs-woba]]", "[[src-2010-slowinski-fangraphs-wrc]]"]
source_count: 2
status: stable
data: ["raw/data/fangraphs_mlb_2011-2026_trout-standard.csv", "raw/data/fangraphs_mlb_2011-2026_trout-advanced.csv"]
metric: ["[[woba]]", "[[wraa]]", "[[wrc]]"]
league: MLB
season: 2013
subject: Mike Trout
created: 2026-11-23
updated: 2026-11-23
---

# 計算範例：Mike Trout 2013 年的 wOBA、wRAA 與 wRC

## 目標
用 MLB 2013 年的權重，算出 Mike Trout 的 [[woba|wOBA]]，再換算成 [[wraa|wRAA]] 與 [[wrc|wRC]]。

## 輸入資料

| 項目 | 數值 | 出處 |
|---|---|---|
| uBB | 100 | [[src-2010-slowinski-fangraphs-woba]] |
| HBP | 9 | 同上 |
| 1B | 115 | 同上 |
| 2B | 39 | 同上 |
| 3B | 9 | 同上 |
| HR | 27 | 同上 |
| PA | 716 | 同上 |
| AB | 589 | `raw/data/fangraphs_mlb_2011-2026_trout-standard.csv` |
| BB | 110 | 同上 |
| IBB | 10 | 同上（uBB = 110 − 10 = 100，與來源一致） |
| SF | 8 | 同上 |

## 使用的常數（MLB 2013）

| 常數 | 數值 |
|---|---|
| $w_{\text{BB}}, w_{\text{HBP}}, w_{\text{1B}}, w_{\text{2B}}, w_{\text{3B}}, w_{\text{HR}}$ | 0.690, 0.722, 0.888, 1.271, 1.616, 2.101 |
| $\text{lgwOBA}$ | .314 |
| $\text{wOBA Scale}$ | 1.277 |
| $\text{lgR/PA}$ | .110 |

出處：[[src-2010-slowinski-fangraphs-woba]]；lgR/PA 見 [[woba#MLB 2010–2015 年常數]]。

## 逐步計算

### 第 1 步：分子（加權後的進攻事件）

$$
\begin{aligned}
0.690 \times 100 &= 69.000 \\
0.722 \times 9 &= 6.498 \\
0.888 \times 115 &= 102.120 \\
1.271 \times 39 &= 49.569 \\
1.616 \times 9 &= 14.544 \\
2.101 \times 27 &= 56.727 \\
\hline
\text{分子} &= 298.458
\end{aligned}
$$

（已用程式驗算。）

各事件的貢獻占比：一壘安打約 34%，保送約 23%，全壘打約 19%。

### 第 2 步：分母

$$
\text{分母} = \text{AB} + \text{BB} - \text{IBB} + \text{SF} + \text{HBP} = 589 + 110 - 10 + 8 + 9 = 706
$$

> [!info] 驗證：與反推結果一致
> 在拿到數據前，曾從 wOBA = .423 反推分母（真實值介於 .4225 和 .4235 之間）：
> $$
> \frac{298.458}{0.4235} \approx 704.7 \quad \text{到} \quad \frac{298.458}{0.4225} \approx 706.4
> $$
> 也就是 705 或 706。實際數據為 706，落在範圍內。

### 第 3 步：wOBA

$$
\text{wOBA} = \frac{298.458}{706} = 0.42275 \approx .423
$$

### 第 4 步：wRAA

$$
\begin{aligned}
\text{wRAA} &= \frac{\text{wOBA} - \text{lgwOBA}}{\text{wOBA Scale}} \times \text{PA} \\
&= \frac{0.423 - 0.314}{1.277} \times 716 \\
&= 0.08536 \times 716 \\
&\approx 61.1
\end{aligned}
$$

### 第 5 步：wRC
依 [[wrc]]，把 wRAA 加回聯盟平均打者在同樣打席數會創造的得分：

$$
\begin{aligned}
\text{wRC} &= \text{wRAA} + \frac{\text{lgR}}{\text{PA}} \times \text{PA} \\
&= 61.1 + 0.110 \times 716 \\
&= 61.1 + 78.8 \\
&\approx 139.9
\end{aligned}
$$

## 結果與驗證
- wOBA = .42275 ≈ .423：與來源及 FanGraphs 頁面（`advanced.csv`）一致。
- wRAA ≈ 61.1：與來源及 FanGraphs 頁面一致（程式驗算 61.12）。
- wRC ≈ 139.9，與 FanGraphs 頁面的 140 一致（`advanced.csv`）。
- FanGraphs 頁面的 2013 年 wRC+ 為 176，但無法驗算：需要 2013 年天使主場的球場係數，而 FanGraphs 目前只提供 2016 年以後的數值（見 [[park-factor]]）。
- 對照 FanGraphs Value 表：Batting = 62.2，比 wRAA 多 1.1 分。依 [[src-2010-slowinski-fangraphs-woba]]，wRAA 是未經球場調整的 Batting Runs，差距即來自球場與聯盟調整（`value.csv`）。

## 解讀
- .423 高於 .400 的「頂尖」門檻（見 [[woba#如何解讀]]）。
- 每打席比聯盟平均多創造約 0.085 分，整季累計約 61 分。照「每 10 分 ≈ 1 勝」的常見換算，大約是 6 勝。這個換算還沒有來源，見 [[runs-per-win]]。
- 這個數字沒有球場調整。要和其他球隊的打者比較，需要依主場的[[park-factor|球場係數]]調整，或改用 [[wrc-plus|wRC+]]（兩者都待補來源）。

## 相關頁面
[[woba]]、[[wraa]]、[[wrc]]、[[linear-weights]]
