---
title: 替補水準（Replacement Level）
type: concept
aliases: [Replacement Level, 替補水準, Replacement Runs]
domain: [value, method]
leagues: [MLB]
tags: [war, replacement-level]
sources: ["[[src-2010-slowinski-fangraphs-what-is-war]]", "[[src-2012-slowinski-fangraphs-war-misconceptions]]", "[[src-2012-slowinski-fangraphs-war-position-players]]", "[[src-2012-slowinski-fangraphs-war-pitchers]]", "[[src-2013-cameron-fangraphs-unifying-replacement-level]]"]
source_count: 5
status: draft
created: 2026-11-23
updated: 2026-11-24
---

# 替補水準（Replacement Level）

> 一句話定義：球隊不花代價就能找到的球員（小聯盟自由球員、板凳邊緣球員）的表現水準。WAR 以它為 0。

## 為什麼不用「平均」當基準
1. 平均球員本身就有價值，能穩定提供平均表現的球員並不容易取得。
2. 以平均為基準時，1 打席和 600 打席的平均球員都是 0，無法區分上場量的價值（[[src-2012-slowinski-fangraphs-war-position-players]]）。

## 定義與公式
- FanGraphs 和 Baseball-Reference 使用相同的替補水準：每季 **1,000 WAR**（2,430 場），對應替補勝率 **.294**；野手占 57%（570 WAR）、投手占 43%（430 WAR）（[[src-2010-slowinski-fangraphs-what-is-war]]）。

> [!info] 推論：.294 與 1,000 WAR 的對應
> 每季共 2,430 勝。如果全部由替補球員組成，總勝場 = 2,430 − 1,000 = 1,430，每隊 $1430 / 30 \approx 47.7$ 勝，勝率 $47.7 / 162 \approx .294$。

### 野手的替補水準得分

$$
\text{Replacement} = 570 \times \frac{\text{MLB Games}}{2430} \times \frac{\text{RPW}}{\text{lgPA}} \times \text{PA}
$$

- $\frac{\text{MLB Games}}{2430}$：季中計算時，依已進行的場次比例縮放
- $\frac{\text{RPW}}{\text{lgPA}}$：把勝場換成每打席得分

出處：[[src-2012-slowinski-fangraphs-war-position-players]]。

### 投手的替補水準（每場勝場）

$$
\text{Replacement} = 0.03 \times \left(1 - \frac{\text{GS}}{\text{G}}\right) + 0.12 \times \frac{\text{GS}}{\text{G}}
$$

先發 0.12、後援 0.03（[[src-2012-slowinski-fangraphs-war-pitchers]]）。

## 不同觀點

> [!note] 觀點 A（2013 年以前的 FanGraphs）：全替補球隊約 43 勝
> 依據：球隊 WAR 總和加上約 43 勝才是預估勝場。43 勝約等於 .265 勝率，正是 FanGraphs 統一前的基準。
> 來源：[[src-2012-slowinski-fangraphs-war-misconceptions]]（2012-03-23）；[[src-2013-cameron-fangraphs-unifying-replacement-level]]

> [!note] 觀點 B（2013 年起）：替補勝率 .294（約 47.7 勝）
> 依據：2013 年 FanGraphs 與 Baseball-Reference 統一替補水準，每季 1,000 WAR。
> 來源：[[src-2013-cameron-fangraphs-unifying-replacement-level]]（2013-03-28）；[[src-2010-slowinski-fangraphs-what-is-war]]（內容含後來的更新）

**分歧所在**：時間先後不同，已由來源證實。2013 年 3 月以前，FanGraphs 的替補勝率是 .265、Baseball-Reference 是 .320；2013 年起兩站統一為 .294（Tango 2008 年原始模型是 .292）。〈WAR Misconceptions〉寫於統一之前，所以是 43 勝。

| 時期／網站 | 替補勝率 | 每隊勝場 |
|---|---|---|
| FanGraphs（2013 年以前） | .265 | 約 43 |
| Baseball-Reference（2013 年以前） | .320 | 約 52（推論） |
| Tango 原始模型（2008） | .292 | 約 47（推論） |
| 統一後（2013 起） | .294 | 47.7 |

## 替補水準設在哪裡才合理
- Tango 的定義：在自由市場上只需支付最低薪資、或在交易中以極小代價就能取得的能力。
- 檢驗一：以小聯盟合約或讓渡取得的 24 名野手，兩季約 10,000 打席累積約 0 WAR。
- 檢驗二：用 .294 計算，生涯 6,000 打席以上的 628 位球員中只有 1 人低於 0（Alfredo Griffin，−1.0）。
- 統一的影響：單季幾乎看不出（Trout 當時生涯 10.8 → 10.7）；長生涯球員降最多（Aparicio −14.2）。
（[[src-2013-cameron-fangraphs-unifying-replacement-level]]）

## 在球員評估中的用途
- 估計球隊勝場：$\text{預估勝場} \approx \text{全替補球隊勝場} + \sum \text{WAR}$
- 讓上場量成為價值的一部分

## 相關頁面
[[war]]、[[war-position-players]]、[[war-pitchers]]、[[runs-per-win]]

## 來源
- [[src-2010-slowinski-fangraphs-what-is-war]]：1,000 WAR、.294、57/43
- [[src-2012-slowinski-fangraphs-war-misconceptions]]：約 43 勝
- [[src-2012-slowinski-fangraphs-war-position-players]]：野手公式
- [[src-2012-slowinski-fangraphs-war-pitchers]]：投手公式
- [[src-2013-cameron-fangraphs-unifying-replacement-level]]：2013 年統一替補水準、舊基準 .265／.320
