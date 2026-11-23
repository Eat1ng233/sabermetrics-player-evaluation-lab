---
title: 野手 WAR 計算
type: metric
aliases: [Position Player WAR, 野手 WAR, RAR]
domain: [value, batting, baserunning, fielding]
leagues: [MLB]
tags: [war, replacement-level]
sources: ["[[src-2012-slowinski-fangraphs-war-position-players]]"]
source_count: 1
status: draft
full_name: Wins Above Replacement for Position Players
scale: wins
upstream: ["[[batting-runs]]", "[[bsr]]", "[[positional-adjustment]]", "[[replacement-level]]", "[[runs-per-win]]"]
downstream: ["[[war]]"]
stabilization:
created: 2026-11-23
updated: 2026-11-23
---

# 野手 WAR 計算

> 一句話定義：把野手的打擊、跑壘、守備得分加上守位、聯盟、替補水準調整，得到 RAR，再除以每勝得分換成勝場。

## 定義與公式

$$
\text{WAR} = \frac{\text{Batting} + \text{Base Running} + \text{Fielding} + \text{Positional} + \text{League} + \text{Replacement}}{\text{RPW}}
$$

FanGraphs 網站上的彙總欄位：

$$
\text{Off} = \text{Batting} + \text{Base Running}, \qquad \text{Def} = \text{Fielding} + \text{Positional}
$$

出處：[[src-2012-slowinski-fangraphs-war-position-players]]。

## 推導過程：六個組成

### 1. Batting Runs（相對平均）
見 [[batting-runs]]：

$$
\text{Batting} = \text{wRAA} + \left(\frac{\text{lgR}}{\text{PA}} - \text{PF} \times \frac{\text{lgR}}{\text{PA}}\right)\text{PA} + \left(\frac{\text{lgR}}{\text{PA}} - \frac{\text{wRC}_{\text{AL/NL 野手}}}{\text{PA}_{\text{AL/NL 野手}}}\right)\text{PA}
$$

### 2. Base Running Runs（相對平均）
見 [[bsr]]：$\text{BsR} = \text{UBR} + \text{wSB} + \text{wGDP}$

### 3. Fielding Runs（相對同守位平均）
- 非捕手：UZR（BIS 影像資料，由 Mitchel Lichtman 開發）
- 捕手：DRS 中的 rSB（阻殺盜壘）+ RPP（防止捕逸、暴投），**不含** framing（來源時間：2012–2016，待確認是否已更新）
- 守多個位置時，各位置的守備得分直接相加
- +10 的一壘手代表比平均一壘手多 10 分，不代表比平均游擊手好

### 4. Positional Adjustment
見 [[positional-adjustment]]：

$$
\text{Positional} = \frac{\text{Inn}/9}{162} \times \text{守位得分值}
$$

### 5. League Adjustment
讓每個聯盟「高於平均」的得分總和為 0：

$$
\text{League} = \frac{-(\text{lgBatting} + \text{lgBaseRunning} + \text{lgFielding} + \text{lgPositional})}{\text{lgPA}} \times \text{PA}
$$

各項都是該球員所屬聯盟（AL 或 NL）的總和。每季約影響 0～5 分。

### 6. Replacement Runs
見 [[replacement-level]]：

$$
\text{Replacement} = 570 \times \frac{\text{MLB Games}}{2430} \times \frac{\text{RPW}}{\text{lgPA}} \times \text{PA}
$$

### 換成勝場
除以 [[runs-per-win|RPW]]：$\text{RPW} = 9 \times \dfrac{\text{MLB R}}{\text{MLB IP}} \times 1.5 + 3$

## 推導鏈：上游與下游
- [[woba]] → [[wraa]] → [[batting-runs]] ┐
- [[bsr]] ─────────────────────┤
- UZR ＋ [[positional-adjustment]] ──┼→ RAR → ÷ RPW → [[war]]
- 聯盟調整、[[replacement-level]] ────┘

## 限制與常見誤用
- 手算結果可能和網站差一點：網站的球場係數、R/PA 保留更多位數；正確計算的誤差通常不超過 1 分（[[src-2012-slowinski-fangraphs-war-position-players]]）。
- 守位調整的數值來自多年前的實證比較，可能已不符合現況。
- 其他限制見 [[war#限制與常見誤用]]。

## 範例
- [[ex-war-mlb-2012-trout]]

## 相關頁面
[[war]]、[[war-pitchers]]、[[batting-runs]]、[[bsr]]、[[positional-adjustment]]、[[replacement-level]]、[[runs-per-win]]

## 來源
- [[src-2012-slowinski-fangraphs-war-position-players]]
