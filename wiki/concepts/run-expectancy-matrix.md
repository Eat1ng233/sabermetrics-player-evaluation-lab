---
title: 得分期望值矩陣（Run Expectancy Matrix）
type: concept
aliases: [Run Expectancy, RE24 matrix, 得分期望值, RE matrix]
domain: [method]
leagues: [MLB]
tags: [run-expectancy, base-out-state]
sources: ["[[src-2016-weinberg-fangraphs-deriving-woba]]"]
source_count: 1
status: draft
created: 2026-11-23
updated: 2026-11-23
---

# 得分期望值矩陣（Run Expectancy Matrix）

> 一句話定義：在特定的「壘包 × 出局數」狀態下，從那一刻到該局結束，平均會再得幾分。

## 詳細說明
- **壘包出局狀態（base-out state）**：出局數有 3 種（0、1、2），壘包狀態有 8 種（無人、一壘、二壘……滿壘），共 **24 種**狀態。每個打席開始時都處於其中一種。
- **計算方式**：找出一整季（或多季）中所有處於某狀態的時刻，加總每次從那一刻到該局結束的得分，再除以次數。

$$
\text{RE}(s) = \frac{\sum_{i \in s} \text{從第 } i \text{ 次出現到該局結束的得分}}{n_s}
$$

變數說明：
- $s$：某一種壘包出局狀態
- $n_s$：該狀態在樣本中出現的次數

### MLB 2010–2015 年矩陣

| 壘上跑者 | 0 出局 | 1 出局 | 2 出局 |
|---|---|---|---|
| 無人 | 0.481 | 0.254 | 0.098 |
| 一壘 | 0.859 | 0.509 | 0.224 |
| 二壘 | 1.100 | 0.664 | 0.319 |
| 一、二壘 | 1.437 | 0.884 | 0.429 |
| 三壘 | 1.350 | 0.950 | 0.353 |
| 一、三壘 | 1.784 | 1.130 | 0.478 |
| 二、三壘 | 1.964 | 1.376 | 0.580 |
| 滿壘 | 2.292 | 1.541 | 0.752 |

出處：Tom Tango 計算，引自 [[src-2016-weinberg-fangraphs-deriving-woba]]。FanGraphs 實際使用的是每場經過球場調整的矩陣，數值會略有不同。

## 在球員評估中的用途
每個打席都會讓狀態從 $s_{\text{before}}$ 變成 $s_{\text{after}}$，這次打席的得分價值為：

$$
\Delta \text{RE} = \text{RE}(s_{\text{after}}) - \text{RE}(s_{\text{before}}) + \text{該打席直接得分}
$$

例如一出局、一壘有人時選到保送，狀態變成一出局、一二壘有人：

$$
\Delta \text{RE} = 0.884 - 0.509 + 0 = +0.375
$$

把同一類事件的 $\Delta \text{RE}$ 取平均，就得到該事件的[[linear-weights|線性權重]]，也就是 [[woba|wOBA]] 權重的基礎。

> [!info] 推論：$\Delta\text{RE}$ 公式中的「直接得分」項
> 來源的保送範例沒有得分，所以沒有寫出這一項。但全壘打等事件會直接得分，必須加回去，否則得分事件的價值會被低估。這是常見的定義方式，待其他來源確認。

## 相關指標
[[linear-weights]]、[[woba]]、[[re24]]

## 限制
- 矩陣取決於得分環境，不同聯盟、年代需要各自計算。NPB、KBO、CPBL 目前沒有來源。
- 矩陣只記錄平均值，不考慮打者、投手、比分等因素。

## 來源
- [[src-2016-weinberg-fangraphs-deriving-woba]]：定義、24 種狀態、2010–2015 年矩陣、保送範例
