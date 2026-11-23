---
title: 野手 WAR 計算
type: metric
aliases: [Position Player WAR, 野手 WAR, RAR]
domain: [value, batting, baserunning, fielding]
leagues: [MLB]
tags: [war, replacement-level]
sources: ["[[src-2012-slowinski-fangraphs-war-position-players]]", "[[src-2024-appelman-fangraphs-war-update]]", "[[src-2010-slowinski-fangraphs-uzr]]", "[[src-2019-appelman-fangraphs-war-update-catcher-framing]]", "[[src-2010-slowinski-fangraphs-drs]]"]
source_count: 5
status: needs-review
full_name: Wins Above Replacement for Position Players
scale: wins
upstream: ["[[batting-runs]]", "[[bsr]]", "[[uzr]]", "[[positional-adjustment]]", "[[replacement-level]]", "[[runs-per-win]]"]
downstream: ["[[war]]"]
stabilization:
created: 2026-11-23
updated: 2026-11-24
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

2016 年起，UBR 與 wGDP 改用 Statcast 跑壘指標 XBR（[[src-2024-appelman-fangraphs-war-update]]）。

### 3. Fielding Runs（相對同守位平均）
- 非捕手：[[uzr|UZR]]（BIS 影像資料，由 Mitchel Lichtman 開發）
- 捕手：[[drs|DRS]] 中的 rSB（阻殺盜壘）+ RPP（防止捕逸、暴投）
- **捕手 framing**：2019 年起加入 WAR（資料從 2008 年起），framing 得分 ÷ RPW 加進捕手 WAR；同樣的得分依搭配捕手從投手 WAR 扣回（[[src-2019-appelman-fangraphs-war-update-catcher-framing]]）
- **2016 年起改用 Statcast**：守備範圍改用由 OAA 換算的得分；外野傳球、捕手阻殺改用 Statcast；新增捕手擋球；刪除雙殺得分（[[src-2024-appelman-fangraphs-war-update]]，見下方「不同觀點」）
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

## 不同觀點

> [!note] 觀點 A：守備用 UZR＋DRS，跑壘用 UBR＋wSB＋wGDP
> 依據：本頁六個組成的原始說明。
> 來源：[[src-2012-slowinski-fangraphs-war-position-players]]、[[src-2010-slowinski-fangraphs-uzr]]

> [!note] 觀點 B：2016 年起守備與跑壘改用 Statcast
> 依據：守備範圍（2022 年起）、外野傳球、捕手阻殺與擋球改用 Statcast Fielding Run Value；UBR 與 wGDP 改用 XBR；UZR 的雙殺得分刪除。2016–2023 年大部分球員的 WAR 變動在 1 以內。
> 來源：[[src-2024-appelman-fangraphs-war-update]]

**分歧所在**：時間先後不同。2016 年以前的 WAR（例如 [[ex-war-mlb-2012-trout]]）仍依觀點 A 計算；2016 年以後依觀點 B。六個組成的架構與 RPW 換算沒有改變。

## 範例
- [[ex-war-mlb-2012-trout]]（2012 年，不在 2024 更新的回溯範圍內）

## 相關頁面
[[war]]、[[uzr]]、[[drs]]、[[war-pitchers]]、[[batting-runs]]、[[bsr]]、[[positional-adjustment]]、[[replacement-level]]、[[runs-per-win]]

## 來源
- [[src-2012-slowinski-fangraphs-war-position-players]]
- [[src-2024-appelman-fangraphs-war-update]]：2016 年起的 Statcast 替換
- [[src-2010-slowinski-fangraphs-uzr]]：UZR 的定義
- [[src-2019-appelman-fangraphs-war-update-catcher-framing]]：捕手 framing
- [[src-2010-slowinski-fangraphs-drs]]：DRS 的定義
