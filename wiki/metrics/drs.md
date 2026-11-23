---
title: DRS（守備救分）
type: metric
aliases: [DRS, Defensive Runs Saved, 守備救分, rSB, rPM]
domain: [fielding]
leagues: [MLB]
tags: [counting-stat, runs, defense]
sources: ["[[src-2010-slowinski-fangraphs-drs]]", "[[src-2012-slowinski-fangraphs-war-position-players]]", "[[src-2024-appelman-fangraphs-war-update]]"]
source_count: 3
status: draft
full_name: Defensive Runs Saved
scale: runs（0 = 同守位平均）
upstream: []
downstream: ["[[war-position-players]]"]
stabilization: 1～3 年（來源建議）
created: 2026-11-24
updated: 2026-11-24
---

# DRS（守備救分）

> 一句話定義：The Fielding Bible 計算的守備指標，衡量球員比同守位平均多救幾分；和 UZR 目標相同、方法略有不同。

## 定義與公式

$$
\text{DRS} = \text{rSB} + \text{rBU} + \text{rGDP} + \text{rARM} + \text{rHR} + \text{rPM}
$$

| 組成 | 適用守位 | 衡量什麼 |
|---|---|---|
| rSB | 捕手、投手 | 阻殺盜壘、讓跑者不敢盜 |
| rBU | 一壘、三壘 | 處理觸擊 |
| rGDP | 二壘、游擊 | 完成雙殺（而不是只拿一個出局） |
| rARM | 外野 | 傳球阻止跑者推進、多推進時觸殺 |
| rHR | 外野 | 沒收全壘打，每次 1.6 分 |
| rPM | 全部 | Plus/Minus：守備範圍、把擊球變成出局 |

出處：[[src-2010-slowinski-fangraphs-drs]]。

> [!info] 推論
> 來源列出各組成並說 DRS 代表總守備價值，但沒有寫成加總公式；Fielding Bible 可能還有其他組成。另外，野手 WAR 文章說捕手守備用 rSB + **RPP**（防止捕逸、暴投），RPP 不在本文的列表中。

## 推導過程
完整計算在 Fielding Bible 的 FAQ，來源沒有收錄。基本邏輯和 [[uzr]] 相同：依擊球位置與類型判斷難度，和同守位平均比較，換成得分。

## 和 UZR 的比較

| | DRS | UZR |
|---|---|---|
| 計算者 | The Fielding Bible（John Dewan） | Mitchel Lichtman |
| 資料 | BIS | BIS |
| 判斷難度用的資料 | 滾動的一年 | 多年 |
| 投手、捕手守備 | 有 | 沒有（捕手另計） |
| 評級表 | 相同（+15 … −15） | 相同 |

兩者多數時候結論一致，差別在調整方式（[[src-2010-slowinski-fangraphs-drs]]）。

## 推導鏈：上游與下游
BIS 擊球位置與類型 → 各組成的救分 → DRS →（捕手的 rSB 進入 2016 年以前的 [[war-position-players]]）

## 聯盟與年份差異
- 只有 MLB 有公開的 DRS。
- FanGraphs WAR 的捕手阻殺：2016 年以前用 DRS 的 rSB；2016 年起改用 Statcast（[[src-2024-appelman-fangraphs-war-update]]）。

## 如何解讀
單位是得分；+5 的三壘手比平均三壘手多救 5 分。評級表同 [[uzr#如何解讀]]。

## 限制與常見誤用
- 小樣本不可靠，至少用 1～3 年。
- 人工記錄的誤差；不考慮佈陣與站位。
- 跨守位比較要加 [[positional-adjustment|守位調整]]。

## 範例
_（尚無）_

## 相關頁面
[[uzr]]、[[war-position-players]]、[[positional-adjustment]]

## 來源
- [[src-2010-slowinski-fangraphs-drs]]：定義、組成、和 UZR 的比較
- [[src-2012-slowinski-fangraphs-war-position-players]]：捕手 rSB + RPP
- [[src-2024-appelman-fangraphs-war-update]]：2016 年起捕手阻殺改用 Statcast
