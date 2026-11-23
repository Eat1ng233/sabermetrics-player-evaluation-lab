---
title: RPW（每勝得分）
type: concept
aliases: [Runs Per Win, RPW, R/W, 每勝得分]
domain: [value, method]
leagues: [MLB]
tags: [war, run-environment]
sources: ["[[src-2012-slowinski-fangraphs-war-position-players]]", "[[src-2012-slowinski-fangraphs-war-pitchers]]", "[[src-2016-weinberg-fangraphs-deriving-woba]]"]
source_count: 3
status: draft
created: 2026-11-23
updated: 2026-11-23
---

# RPW（每勝得分）

> 一句話定義：球隊平均要多得（或少失）幾分，才能多贏一場。用來把「得分」換成「勝場」。

## 定義與公式

$$
\text{RPW} = 9 \times \frac{\text{MLB Runs Scored}}{\text{MLB Innings Pitched}} \times 1.5 + 3
$$

也就是「聯盟每九局得分 × 1.5 + 3」。這是 Tom Tango 的簡化公式，和 Patriot 的 Pythagpat 每年相差約 0.02 分（[[src-2012-slowinski-fangraphs-war-position-players]]）。

直覺：一支 81 勝 81 敗、得失分差為 0 的球隊，要變成 82 勝 80 敗，得失分差需要多少？那就是 RPW。

## 各年數值（MLB）
| 球季 | R/W |
|---|---|
| 2015 | 9.421 |
| 2014 | 9.117 |
| 2013 | 9.264 |
| 2012 | 9.544 |
| 2011 | 9.454 |
| 2010 | 9.643 |

出處：Guts 頁節錄，引自 [[src-2016-weinberg-fangraphs-deriving-woba]]。

> [!info] 推論：從 RPW 反推得分環境
> 由公式可得 $\text{R/9} = (\text{RPW} - 3) / 1.5$。例如 2013 年：$(9.264 - 3)/1.5 \approx 4.18$ 分／九局。

## 「10 分 = 1 勝」
常見的經驗法則，但實際比例依當年得分環境而定，通常介於 9 到 10 之間（[[src-2012-slowinski-fangraphs-war-position-players]]）。得分環境越高，多贏一場需要的得分越多。

## 投手的動態 RPW
投手會改變自己出賽時的得分環境，所以投手 WAR 用專屬的 dRPW，見 [[war-pitchers#5. 投手專屬的動態 RPW]]。

## 相關頁面
[[war]]、[[war-position-players]]、[[war-pitchers]]、[[replacement-level]]

## 來源
- [[src-2012-slowinski-fangraphs-war-position-players]]：公式、9～10 的範圍
- [[src-2012-slowinski-fangraphs-war-pitchers]]：動態 RPW
- [[src-2016-weinberg-fangraphs-deriving-woba]]：2010–2015 年數值
