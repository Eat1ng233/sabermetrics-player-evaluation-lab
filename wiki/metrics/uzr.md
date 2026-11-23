---
title: UZR（終極區域評分）
type: metric
aliases: [UZR, Ultimate Zone Rating, UZR/150, 終極區域評分]
domain: [fielding]
leagues: [MLB]
tags: [counting-stat, runs, defense, contested]
sources: ["[[src-2010-slowinski-fangraphs-uzr]]", "[[src-2024-appelman-fangraphs-war-update]]", "[[src-2012-slowinski-fangraphs-war-position-players]]", "[[src-2010-slowinski-fangraphs-drs]]"]
source_count: 4
status: needs-review
full_name: Ultimate Zone Rating
scale: runs（0 = 同守位平均）
upstream: []
downstream: ["[[war-position-players]]"]
stabilization: 約 3 年（來源建議）
created: 2026-11-24
updated: 2026-11-24
---

# UZR（終極區域評分）

> 一句話定義：把每一顆擊球的處理結果換成得分，計算守備員比同守位平均多救（或多丟）了幾分。

## 定義與公式

$$
\text{UZR} = \text{ARM} + \text{DPR} + \text{RngR} + \text{ErrR}
$$

變數說明：
- $\text{ARM}$（Outfield Arm Runs）：外野手靠傳球阻止跑者推進所救的分數
- $\text{DPR}$（Double-Play Runs）：內野手完成雙殺的價值
- $\text{RngR}$（Range Runs）：守備範圍，接到的球比平均多或少
- $\text{ErrR}$（Error Runs）：失誤比同守位平均多或少

四項都是**相對同守位平均**的得分。出處：[[src-2010-slowinski-fangraphs-uzr]]。

## 推導過程

### 1. 每一顆擊球的價值
依擊球位置、速度等，把擊球分類。每一類擊球有兩個聯盟平均值：
- $v$：這類擊球如果沒被接到，平均造成的得分
- $p$：同守位平均守備員把它變成出局的機率

### 2. 接到球的得分
文章的例子：某顆球 $v = 0.8$ 分，平均左外野手接到的機率 $p = 40\%$。接到這顆球：

$$
\text{得分} = v \times (1 - p) = 0.8 \times (1 - 0.4) = 0.48
$$

越難接的球（$p$ 越小），接到的獎勵越大。

> [!info] 推論：沒接到的扣分，以及為什麼平均是 0
> 來源只給了接到球的算法。依同樣邏輯，沒接到應扣 $v \times p = 0.8 \times 0.4 = 0.32$ 分。
> 平均守備員接到的機率是 40%，期望值為
> $$0.4 \times 0.48 - 0.6 \times 0.32 = 0.192 - 0.192 = 0$$
> 這正是「相對平均」的意思：平均守備員的 UZR 是 0。

### 3. 加總與換算
- 一整季所有擊球的得分加總，得到 RngR 等各項，再相加成 UZR。
- **UZR/150**：把 UZR 換算成 150 場的尺度，用來比較出賽數不同的球員。

### 4. 接到 WAR
UZR 只和同守位比較，所以要加上 [[positional-adjustment|守位調整]]：

$$
\text{Def} = \text{UZR} + \text{Positional}
$$

在 [[war-position-players]] 中，UZR 是 Fielding 這一項（2016 年以前；見下方「不同觀點」）。

## 和 DRS 的比較
兩者目標相同、都用 BIS 資料、評級表相同，多數時候結論一致。主要差別：UZR 用多年資料判斷每一球的難度，DRS 用滾動的一年；DRS 另含投手與捕手的守備（[[src-2010-slowinski-fangraphs-drs]]）。詳見 [[drs#和 UZR 的比較]]。

## 推導鏈：上游與下游
擊球分類（位置、速度）→ 平均得分 $v$、平均接殺率 $p$ → 每顆球的得分 → RngR、ErrR、ARM、DPR → UZR → ＋守位調整 = Def → [[war-position-players]]

## 聯盟與年份差異
- 需要 BIS 人工記錄的擊球位置資料，只有 MLB；NPB／KBO／CPBL 沒有公開的 UZR（推論：日本有 DELTA 等機構自行計算的版本，待補來源）。
- FanGraphs 計算 UZR 到 2025 年球季結束（[[src-2024-appelman-fangraphs-war-update]]）。

## 如何解讀
單位是得分，+5 代表比同守位平均多救 5 分。評級表（[[src-2010-slowinski-fangraphs-uzr]]）：

| 守備能力 | UZR |
|---|---|
| 金手套級 | +15 |
| 很好 | +10 |
| 高於平均 | +5 |
| 平均 | 0 |
| 低於平均 | −5 |
| 差 | −10 |
| 很差 | −15 |

## 限制與常見誤用
- **樣本要大**：一兩個月的 UZR 參考價值很低；至少用 3 年資料判斷真實能力。
- **跨守位不能直接比**：+10 的一壘手不代表比 0 的游擊手好，要加守位調整。
- **人工記錄的誤差**：BIS 資料由人記錄擊球位置。
- **不考慮守備佈陣與站位**。
- UZR 已做球場調整。

## 不同觀點

> [!note] 觀點 A：FanGraphs WAR 的守備使用 UZR（非捕手）
> 依據：UZR 以得分為單位，能和打擊得分相加；捕手則用 DRS 的阻殺與防止捕逸。
> 來源：[[src-2010-slowinski-fangraphs-uzr]]、[[src-2012-slowinski-fangraphs-war-position-players]]

> [!note] 觀點 B：2016 年起，FanGraphs WAR 改用 Statcast 守備指標
> 依據：2022 年起守備範圍改用由 OAA 換算的 Fielding Runs Prevented；2024 年再把外野傳球、捕手阻殺換成 Statcast，新增捕手擋球，刪除雙殺得分，回溯到 2016 年。
> 來源：[[src-2024-appelman-fangraphs-war-update]]

**分歧所在**：時間先後不同，不是方法上的爭論。兩篇 2010、2012 年的文章描述改版前的做法；2024 年的文章說明改版後的做法。資料來源也不同：UZR 用 BIS 人工記錄，Statcast 用追蹤系統。看 2016 年以前的 WAR，守備仍是 UZR。

## 範例
_（尚無；Trout 2012、2013 的 Fielding 值見 [[ex-war-mlb-2012-trout]]）_

## 相關頁面
[[war-position-players]]、[[drs]]、[[positional-adjustment]]、[[war]]

## 來源
- [[src-2010-slowinski-fangraphs-uzr]]：定義、四個組成、計算例子、評級表、限制
- [[src-2024-appelman-fangraphs-war-update]]：2016 年起被 Statcast 取代的部分
- [[src-2012-slowinski-fangraphs-war-position-players]]：UZR 在野手 WAR 中的位置
