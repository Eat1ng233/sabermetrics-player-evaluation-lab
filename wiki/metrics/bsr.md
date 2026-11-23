---
title: BsR（跑壘得分）
type: metric
aliases: [BsR, Base Running Runs, Base Running, 跑壘得分]
domain: [baserunning, value]
leagues: [MLB]
tags: [counting-stat, runs, linear-weights]
sources: ["[[src-2012-slowinski-fangraphs-war-position-players]]", "[[src-2024-appelman-fangraphs-war-update]]"]
source_count: 2
status: draft
full_name: Base Running Runs
scale: runs
upstream: ["[[ubr]]", "[[wsb]]", "[[wgdp]]"]
downstream: ["[[war-position-players]]"]
stabilization:
created: 2026-11-23
updated: 2026-11-24
---

# BsR（跑壘得分）

> 一句話定義：球員在壘包上（含盜壘與避免雙殺）比聯盟平均多創造的得分。

## 定義與公式

$$
\text{BsR} = \text{UBR} + \text{wSB} + \text{wGDP}
$$

- **UBR**（Ultimate Base Running）：盜壘以外的跑壘價值，例如多推進一個壘包。由 Mitchel Lichtman 開發，需要 BIS 影像資料，**無法自行計算**。
- **wSB**（Weighted Stolen Base Runs）：盜壘與盜壘失敗的價值，可以自行計算（見下）。
- **wGDP**（Weighted GIDP Runs）：實際雙殺打次數與預期次數的差距，換算成得分。由 Lichtman 開發。

出處：[[src-2012-slowinski-fangraphs-war-position-players]]。

> [!note] 2016 年起的版本
> FanGraphs 在 2024 年把 UBR 與 wGDP 換成 Statcast 的跑壘指標 **XBR**，回溯到 2016 年（[[src-2024-appelman-fangraphs-war-update]]）。文章沒有提到 wSB，推論 wSB 仍保留，待確認。2016 年以前（例如 Trout 2012、2013）仍是上面的公式。

## wSB 的推導

$$
\text{wSB} = \text{SB} \times \text{runSB} + \text{CS} \times \text{runCS} - \text{lgwSB} \times (\text{1B} + \text{BB} + \text{HBP} - \text{IBB})
$$

$$
\text{lgwSB} = \frac{\text{lgSB} \times \text{runSB} + \text{lgCS} \times \text{runCS}}{\text{lg1B} + \text{lgBB} + \text{lgHBP} - \text{lgIBB}}
$$

$$
\text{runSB} = 0.2, \qquad \text{runCS} = 2 \times \text{RunsPerOut} + 0.075
$$

變數說明：
- $\text{runSB}$：盜壘成功的得分價值，所有球季固定 0.2
- $\text{runCS}$：盜壘失敗的得分價值，隨每年的得分與出局價值變動；$\text{RunsPerOut}$ = 該季總得分 ÷ 總出局數
- $\text{1B} + \text{BB} + \text{HBP} - \text{IBB}$：上到一壘的機會數（盜壘機會的近似值）
- $\text{lgwSB}$：聯盟平均每次上一壘的盜壘得分
- 各年常數在 Guts 頁（runSB、runCS 欄位），例如 MLB 2013 年 runCS = −0.384（見 [[woba#MLB 2010–2015 年常數]] 的來源表）

> [!info] 推論：runCS 的正負號
> 來源寫的是 $\text{runCS} = 2 \times \text{RunsPerOut} + 0.075$，但 Guts 頁的 runCS 是負值（2013 年 −0.384）。以 2013 年約 4.18 分／九局、每九局 27 個出局估算：$\text{RunsPerOut} \approx 0.155$，$2 \times 0.155 + 0.075 \approx 0.384$，正好等於 Guts 頁數值的絕對值。所以實際使用時應為 $\text{runCS} = -(2 \times \text{RunsPerOut} + 0.075)$：盜壘失敗多一個出局、少一名跑者。

> [!info] 推論：為什麼要減去 lgwSB 那一項
> 前兩項是球員盜壘的總價值；第三項是「平均球員在同樣上壘次數下的盜壘價值」。相減後得到**相對平均**的盜壘得分，和 wRAA 一樣以平均為 0，才能和其他 WAR 組成相加。

## 推導鏈：上游與下游
- 下游：[[war-position-players]]（Off = Batting + BsR）

## 限制
- UBR、wGDP 無法自算，只能使用 FanGraphs 提供的數值。
- 盜壘價值是線性權重的估計值（[[src-2012-slowinski-fangraphs-war-position-players]]）。

## 資料
- Trout 的 UBR、wGDP、XBR、wSB 子欄位因 PDF 對齊問題未收錄在 `raw/data/`；跑壘總值見 `fangraphs_mlb_2011-2026_trout-value.csv` 的 `Base Running`。

## 相關頁面
[[war-position-players]]、[[linear-weights]]

## 來源
- [[src-2012-slowinski-fangraphs-war-position-players]]
