---
title: Unifying Replacement Level
type: source
aliases: [替補水準統一公告]
domain: [value]
leagues: [MLB]
tags: [fangraphs, war, replacement-level]
sources: []
source_count: 0
status: stable
source_type: article
author: Dave Cameron
publisher: FanGraphs
published: 2013-03-28
url: https://blogs.fangraphs.com/unifying-replacement-level/
raw_path: raw/articles/2013-03-28_fangraphs_unifying-replacement-level.pdf
ingest_mode: discussed
created: 2026-11-24
updated: 2026-11-24
---

# Unifying Replacement Level

## 基本資訊
- 作者：Dave Cameron（FanGraphs 總編輯）；發表：2013-03-28
- 原始檔：`raw/articles/2013-03-28_fangraphs_unifying-replacement-level.pdf`；擷取日期：2026-11-24

## 核心論點
1. FanGraphs 與 Baseball-Reference 的 WAR 常被拿來比較，差距被用來質疑整個模型；很多差距其實只是替補水準不同。
2. 例子：Jack Morris 兩站相差 17.6 WAR，但他的 ERA（3.90）與 FIP（3.94）幾乎相同，兩站對他表現的評價也一致，差距來自 FanGraphs 的基準比較低。
3. 2013 年兩站統一替補水準：每 2,430 場分配 **1,000 WAR**，等於 **.294** 勝率、每隊 **47.7 勝**。
4. 統一前：FanGraphs 用 **.265**、Baseball-Reference 用 **.320**；.294 約在兩者中間，但不只是折衷。Tango 2008 年的原始模型是 1,009 勝（.292），所以這也是回到原點。
5. Tango 的定義：替補水準是「在自由市場上只需支付最低薪資、或在交易中以極小代價就能取得的能力」。
6. 檢驗：生涯 6,000 打席以上的 628 位球員中，用 .294 計算只有 1 人（Alfredo Griffin，−1.0 WAR）低於 0；以小聯盟合約或讓渡取得的 24 名野手，兩季約 10,000 打席累積約 0 WAR。
7. 影響：FanGraphs 球員每季 WAR 略降，單季幾乎看不出（Trout 生涯 10.8 → 10.7）；長生涯球員降幅最大（Aparicio −14.2）。

## 關鍵數據與公式

$$
\frac{2430 - 1000}{30} = 47.7 \text{ 勝}, \qquad \frac{47.7}{162} = .294
$$

| 時期／網站 | 替補勝率 | 每隊勝場（推論） |
|---|---|---|
| FanGraphs（2013 年以前） | .265 | 約 43 |
| Baseball-Reference（2013 年以前） | .320 | 約 52 |
| Tango 原始模型（2008） | .292 | 約 47 |
| 統一後（2013 起） | .294 | 47.7 |

## 對 Wiki 的影響
- 更新頁面：[[replacement-level]]：「43 勝 vs .294」改為依時間先後說明，移除 needs-review
- 與既有內容的矛盾：解決 [[src-2012-slowinski-fangraphs-war-misconceptions]] 的「約 43 勝」：那是 2013 年統一前 FanGraphs 的基準

## 待追問的問題
- 文章說統一後野手、投手的分配；57／43 的比例是否也是此時決定，本文沒有說明
