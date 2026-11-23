---
title: Linear Weights（線性權重）
type: concept
aliases: [Linear Weights, 線性權重, run values]
domain: [method, batting]
leagues: [general]
tags: [linear-weights, run-value]
sources: ["[[src-2010-slowinski-fangraphs-woba]]", "[[src-2016-weinberg-fangraphs-deriving-woba]]", "[[src-2014-weinberg-fangraphs-re24]]"]
source_count: 3
status: draft
created: 2026-11-23
updated: 2026-11-23
---

# Linear Weights（線性權重）

> 一句話定義：給每一種比賽事件一個固定的**平均得分價值**，用「次數 × 權重」加總來估計創造的得分。

## 詳細說明
計算方式（[[src-2016-weinberg-fangraphs-deriving-woba]]）：
1. 用[[run-expectancy-matrix|得分期望值矩陣]]算出每個打席造成的得分期望值變化 $\Delta\text{RE}$。
2. 把同一類事件（例如所有非故意四壞）的 $\Delta\text{RE}$ 加總，再除以該事件次數：

$$
\text{RV}_{x} = \frac{\sum_{i \in x} \Delta \text{RE}_i}{n_x}
$$

變數說明：
- $x$：事件類型（uBB、HBP、1B、2B、3B、HR、出局等）
- $n_x$：該類事件在整季中的次數
- $\text{RV}_x$：事件 $x$ 的平均得分價值

### 為什麼是「高於平均」
來源把 $\text{RV}_x$ 稱為各事件「高於平均」的得分，出局則是「比平均打席少 0.26 分」。例如 MLB 2015 年：保送 +0.29、全壘打 +1.39、出局 −0.26（[[src-2016-weinberg-fangraphs-deriving-woba]]）。

> [!info] 推論：為什麼平均打席的價值是 0
> 一局中所有打席的 $\Delta\text{RE}$（含直接得分）加總，等於「該局實際得分 − 開局時的得分期望值（0 出局無人）」。因為開局期望值就是平均每局得分，整季平均下來這個差距約為 0。所以 $\Delta\text{RE}$ 天生就是「相對平均打席」的尺度。

### 「線性」的意思
不管事件發生在什麼情境，都用同一個平均值，所以總價值可以直接相加。

## 和 RE24 的差別
同樣從 ΔRE 出發：[[re24|RE24]] 把每次的 ΔRE 原樣加總（考慮情境），線性權重則把同類事件**取平均**（不考慮情境）。所以線性權重衡量「做了什麼」，RE24 衡量「在當時情境下造成多少影響」（[[src-2014-weinberg-fangraphs-re24]]）。

## 在球員評估中的用途
- [[woba|wOBA]] 權重的來源（[[src-2010-slowinski-fangraphs-woba]]）
- [[wraa|wRAA]]、[[wrc|wRC]]、[[batting-runs|Batting Runs]] 的基礎

## 不同的實作方式
同樣以線性權重為基礎，可以縮放成不同尺度：FanGraphs 的 wOBA 縮放到 OBP 尺度；Baseball Prospectus 的 [[true-average|True Average]] 用不同方式實作。縮放尺度只是為了好理解，不影響事件之間的相對價值（[[src-2016-weinberg-fangraphs-deriving-woba]]）。

## 限制
- **不考慮情境**：適合評估球員本身的能力，但不能衡量「關鍵時刻」的價值。
- 權重取決於得分環境，不同聯盟、年份要重新計算。

## 相關頁面
[[run-expectancy-matrix]]、[[woba]]、[[wraa]]、[[ex-woba-mlb-2015-derivation]]

## 來源
- [[src-2010-slowinski-fangraphs-woba]]：wOBA 權重來自線性權重
- [[src-2016-weinberg-fangraphs-deriving-woba]]：計算方式、2015 年數值、不同實作
