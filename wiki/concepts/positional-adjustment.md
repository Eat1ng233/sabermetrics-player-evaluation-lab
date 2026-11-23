---
title: 守位調整（Positional Adjustment）
type: concept
aliases: [Positional Adjustment, Positional, 守位調整]
domain: [fielding, value]
leagues: [MLB]
tags: [war]
sources: ["[[src-2012-slowinski-fangraphs-war-position-players]]"]
source_count: 1
status: draft
created: 2026-11-23
updated: 2026-11-23
---

# 守位調整（Positional Adjustment）

> 一句話定義：把不同守位的球員放到同一個尺度上的調整。守備得分只和「同守位平均」比較，但當平均游擊手比當平均一壘手困難得多。

## 數值（每 162 場防守出賽）

| 守位 | 得分 |
|---|---|
| 捕手 C | +12.5 |
| 游擊 SS | +7.5 |
| 二壘 2B | +2.5 |
| 三壘 3B | +2.5 |
| 中外野 CF | +2.5 |
| 左外野 LF | −7.5 |
| 右外野 RF | −7.5 |
| 一壘 1B | −12.5 |
| 指定打擊 DH | −17.5 |

出處：[[src-2012-slowinski-fangraphs-war-position-players]]。數值來自多年前的實證比較，可能隨時間改變。

## 公式
一場防守出賽 = 守備 9 局：

$$
\text{Positional} = \frac{\text{Inn} / 9}{162} \times \text{守位得分值}
$$

守多個位置時，分別計算再相加。

## 範例：Trout 2012 年

$$
\begin{aligned}
\text{LF} &: \frac{328.0/9}{162} \times (-7.5) = -1.69 \\
\text{CF} &: \frac{885\tfrac{2}{3}/9}{162} \times 2.5 = +1.52 \\
\text{RF} &: \frac{12.0/9}{162} \times (-7.5) = -0.06 \\
\hline
\text{合計} &= -0.23
\end{aligned}
$$

FanGraphs 為 −0.2，一致。守備局數來自使用者提供的 Trout 球員頁 PDF（`raw/data/fangraphs_mlb_2026-11-23_trout-player-page.pdf`）；局數中的 .2 代表 2/3 局。

> [!warning] 待查證：Trout 2013 年
> 只用 LF（356.0 局）和 CF（952⅔ 局）算出 −0.20，但 FanGraphs 為 −1.2，差約 1.0 分。推論：可能有指定打擊出賽（每 9 局 DH 約 −0.108 分，約 9 場可以補足差距），需要 Trout 2013 年的 DH 出賽數據確認。

## 解讀
- 正值守位（C、SS）代表就算守備只是平均，也比較有價值。
- 指定打擊的負值最大，因為完全不提供守備價值。

## 相關頁面
[[war-position-players]]、[[war]]

## 來源
- [[src-2012-slowinski-fangraphs-war-position-players]]
