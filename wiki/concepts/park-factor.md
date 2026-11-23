---
title: Park Factor（球場係數）
type: concept
aliases: [Park Factor, PF, 球場係數, 球場因子]
domain: [method]
leagues: [MLB]
tags: [park-adjusted]
sources: ["[[src-2016-appelman-fangraphs-park-factors-5yr]]", "[[src-2010-slowinski-fangraphs-park-factors]]", "[[src-2010-slowinski-fangraphs-wrc]]", "[[src-2012-slowinski-fangraphs-war-position-players]]", "[[src-2012-slowinski-fangraphs-war-pitchers]]"]
source_count: 5
status: draft
created: 2026-11-23
updated: 2026-11-23
---

# Park Factor（球場係數）

> 一句話定義：衡量一座球場相對於平均球場，讓得分變多或變少的程度。100 代表中性。

## 為什麼需要
棒球場的尺寸各不相同，而且影響不只來自尺寸：天氣、溫度、空氣密度、周邊地形、看台配置都會改變擊球的飛行。例如 Petco Park 有海霧，Coors Field 位於高海拔、空氣稀薄。所以「大球場」不等於「投手球場」（[[src-2010-slowinski-fangraphs-park-factors]]）。

理想上要知道每個打席在 30 座球場各會變成什麼結果，但資料不足，只能用近似值。

## FanGraphs 的球場係數
- 使用 **5 年迴歸**的球場係數（計算細節待補）。
- 網站上顯示的數字**已經減半**：球員只有一半比賽在主場，其餘假設在中性球場。
  - 平均 = 100；顯示 **105** 代表主場得分其實多 **10%**。
- 另外有各種安打、擊球類型、左右打的分項係數，但球場調整只用總體係數。
- 不同網站（Baseball-Reference、StatCorner 等）的球場係數各不相同。

出處：[[src-2010-slowinski-fangraphs-park-factors]]。

## 計算方法（FanGraphs）
出處：[[src-2016-appelman-fangraphs-park-factors-5yr]]。方法源自 Craig Wright，迴歸權重來自 MGL。

**步驟 1：原始球場係數。** H = 主場每場得分（兩隊合計）、R = 客場每場得分、T = 聯盟球隊數：

$$
\text{原始 PF} = \frac{H \times T}{(T-1) \times R + H}
$$

分母讓「比較基準」和聯盟一樣：$(T-1)/T$ 是其他球場，$1/T$ 是自家球場。

**步驟 2：減半。** 只有一半比賽在主場，客場假設為中性：

$$
\text{iPF} = \frac{\text{原始 PF} + 1}{2}
$$

例：主場 11 分／場、客場 10 分／場 → 約 1.10 → $(1.10+1)/2 = 1.05$。

**步驟 3：迴歸。** 觀察值含有隨機誤差，向 1 迴歸以免過度調整：

$$
\text{PF} = 1 - (1 - \text{iPF}) \times X, \qquad X = \begin{cases} 0.6 & \text{1 年} \\ 0.7 & \text{2 年} \\ 0.8 & \text{3 年} \\ 0.9 & \text{4 年以上} \end{cases}
$$

例：iPF = 1.25（類似 Coors）→ 1 年 1.15、2 年 1.175、3 年 1.20、4 年以上 1.225。

**資料期間**：最多 5 年，理想是前兩年、當年、後兩年；新球場或大幅改建時用較短期間。

**為什麼用得分係數**：衡量價值時只看得分與出局，所以用單一的得分係數；分項（各種安打）與左右打係數適合衡量能力，不適合衡量價值。

> [!info] 推論：從顯示值換回原始係數
> 顯示值經過減半與迴歸。假設用 4 年以上資料（X = 0.9）：
> $$\text{iPF} = 1 - \frac{1 - \text{PF}}{0.9}, \qquad \text{原始 PF} = 2 \times \text{iPF} - 1$$
> 例：顯示 95 → iPF ≈ 0.944 → 原始 ≈ 0.889，也就是主場得分約比平均少 11%。在 wRC+、Batting Runs 公式中**直接使用顯示值**即可，減半與迴歸都已經包含在內。

## 調整方式

### 打者：加法（wRC+、Batting Runs）

$$
\text{球場調整（每打席）} = \frac{\text{lgR}}{\text{PA}} \times (1 - \text{PF})
$$

PF 使用顯示值 ÷ 100（例如 95 → 0.95）。投手球場（PF < 1）加分，打者球場（PF > 1）扣分（[[src-2010-slowinski-fangraphs-wrc]]、[[src-2012-slowinski-fangraphs-war-position-players]]）。

例：PF = 0.95、lgR/PA = .114 時，每打席加 $0.114 \times 0.05 = 0.0057$ 分（見 [[ex-wrc-plus-mlb-2012-trout]]）。

### 投手：乘法（投手 WAR）
投手 WAR 使用依 FIP 組成計算的專用球場係數：

$$
\text{pFIPR9} = \frac{\text{FIPR9}}{\text{PF}_{\text{FIP}}/100}
$$

出處：[[src-2012-slowinski-fangraphs-war-pitchers]]。

### 哪些指標有球場調整
FanGraphs 不計算 wOBA+，而是用 [[wrc-plus|wRC+]] 作為經球場調整的打擊指標。ERA− 等帶 +/− 的指標都有球場調整（[[src-2010-slowinski-fangraphs-park-factors]]）。

## 限制
- **單一數字無法反映不同球員**：左右打、滾地球或飛球型、快腿或慢腿，受球場影響的程度都不同。例如 Target Field 整體略偏打者，和 Yankee Stadium 相近，但對左打全壘打非常不利，Yankee Stadium 則非常有利。
- **方向性的誤差**：例如在 PNC Park 打球的右打者，如果是反方向長打型，球場係數反而會過度修正。
- **只考慮主客各半**：不考慮實際在哪些球場出賽。例如幾乎都在主場先發的洛磯投手，得到的調整會不夠（[[src-2012-slowinski-fangraphs-war-pitchers]]）。
- 儘管不完美，仍然比假設 30 座球場都一樣好得多。

## 資料可取得性
- 使用者提供（2026-11-23）：FanGraphs 目前只提供 **2016 年以後**的球場係數。2015 年以前的球場調整需要其他來源。

## 待補
- 迴歸權重 X 的統計依據；2016 年後 FanGraphs 是否調整過方法
- 各聯盟（NPB、KBO、CPBL）的球場係數來源

## 相關頁面
[[wrc-plus]]、[[batting-runs]]、[[war-pitchers]]、[[woba]]

## 來源
- [[src-2016-appelman-fangraphs-park-factors-5yr]]：計算方法（原始 PF、減半、迴歸）
- [[src-2010-slowinski-fangraphs-park-factors]]：成因、5 年迴歸、減半、限制
- [[src-2010-slowinski-fangraphs-wrc]]：wRC+ 中的加法調整
- [[src-2012-slowinski-fangraphs-war-position-players]]：Batting Runs 中的用法
- [[src-2012-slowinski-fangraphs-war-pitchers]]：FIP 專用係數、乘法調整
