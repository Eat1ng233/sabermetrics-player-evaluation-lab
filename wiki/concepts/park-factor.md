---
title: Park Factor（球場係數）
type: concept
aliases: [Park Factor, PF, 球場係數, 球場因子]
domain: [method]
leagues: [MLB]
tags: [park-adjusted]
sources: ["[[src-2010-slowinski-fangraphs-wrc]]"]
source_count: 1
status: stub
created: 2026-11-23
updated: 2026-11-23
---

# Park Factor（球場係數）

> 一句話定義：衡量一座球場相對於聯盟平均，讓得分變多或變少的程度。100 代表中性。

## 詳細說明
目前的來源只說明了它在 [[wrc-plus|wRC+]] 中的用法（[[src-2010-slowinski-fangraphs-wrc]]）：
- FanGraphs 球場係數頁上的數字要先除以 100 再使用，例如 98 → 0.98。
- wRC+ 用**加法**調整：每個打席加上 $\text{lgR/PA} - \text{PF} \times \text{lgR/PA}$。

$$
\text{球場調整（每打席）} = \frac{\text{lgR}}{\text{PA}} \times (1 - \text{PF})
$$

- $\text{PF} < 1$（投手球場）：調整值為正，補回被球場壓低的得分
- $\text{PF} > 1$（打者球場）：調整值為負

例如 PF = 0.95、lgR/PA = .114 時，每打席加上 $0.114 \times 0.05 = 0.0057$ 分（見 [[ex-wrc-plus-mlb-2012-trout]]）。

## 資料可取得性
- 使用者提供（2026-11-23）：FanGraphs 目前只提供 **2016 年以後**的球場係數。2015 年以前的球場調整需要其他來源。

## 待補
- 球場係數本身怎麼計算（樣本年數、是否只算一半主場效應等）
- 各聯盟（NPB、KBO、CPBL）的球場係數來源

## 相關頁面
[[wrc-plus]]、[[woba]]、[[batting-runs]]

## 來源
- [[src-2010-slowinski-fangraphs-wrc]]：在 wRC+ 中的加法調整方式
