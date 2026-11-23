---
title: 計算範例：從得分期望值推導 MLB 2015 年 wOBA 權重
type: example
aliases: [wOBA 權重推導 2015]
domain: [batting, method]
leagues: [MLB]
tags: [worked-example, linear-weights, run-expectancy]
sources: ["[[src-2016-weinberg-fangraphs-deriving-woba]]"]
source_count: 1
status: draft
metric: ["[[woba]]"]
league: MLB
season: 2015
subject: 全聯盟
created: 2026-11-23
updated: 2026-11-23
---

# 計算範例：從得分期望值推導 MLB 2015 年 wOBA 權重

> [!warning] 部分無法重算
> 第 4 步的聯盟原始 wOBA（.250）需要 2015 年 MLB 全聯盟的事件總數才能重算，目前 `raw/data/` 沒有這份數據，所以這一步直接採用來源的數字。

## 目標
從[[run-expectancy-matrix|得分期望值矩陣]]出發，一步步得到 Guts 頁上的 2015 年 [[woba|wOBA]] 權重。

## 第 1 步：從矩陣算出單一打席的價值
例：一出局、一壘有人時選到保送 → 一出局、一二壘有人。

$$
\Delta\text{RE} = \text{RE}(\text{1B 2B, 1 out}) - \text{RE}(\text{1B, 1 out}) = 0.884 - 0.509 = +0.375
$$

矩陣數值：MLB 2010–2015（Tom Tango），見 [[run-expectancy-matrix]]。

## 第 2 步：同類事件取平均（線性權重）
把整季所有非故意四壞的 $\Delta\text{RE}$ 加總、除以次數，其他事件也一樣。2015 年的結果（比平均打席多創造的得分）：

| 事件 | BB | HBP | 1B | 2B | 3B | HR | 出局 |
|---|---|---|---|---|---|---|---|
| $\text{RV}_x$ | +0.29 | +0.31 | +0.44 | +0.74 | +1.01 | +1.39 | −0.26 |

出處：[[src-2016-weinberg-fangraphs-deriving-woba]]。保送的平均值（0.29）比第 1 步的單一例子（0.375）小。推論：很多保送發生在壘上無人時，價值比較低，拉低了平均。

## 第 3 步：平移讓出局 = 0

$$
\text{RV}^{*}_x = \text{RV}_x - (-0.26) = \text{RV}_x + 0.26
$$

| 事件 | BB | HBP | 1B | 2B | 3B | HR |
|---|---|---|---|---|---|---|
| $\text{RV}^{*}_x$ | 0.55 | 0.57 | 0.70 | 1.00 | 1.27 | 1.65 |

## 第 4 步：求 wOBA Scale
用第 3 步的權重算出全聯盟的 wOBA：

$$
\text{lgwOBA}_{\text{raw}} = \frac{\sum_x \text{RV}^{*}_x \times n_x^{\text{lg}}}{\text{AB} + \text{BB} - \text{IBB} + \text{SF} + \text{HBP}} = .250 \quad \text{（來源數字）}
$$

聯盟 OBP（扣除故意四壞）是 .313，所以：

$$
\text{wOBA Scale} = \frac{.313}{.250} = 1.252 \approx 1.251 \text{（Guts 表）}
$$

推論：Guts 表的 1.251 應該是用未四捨五入的原始 wOBA 算出的，所以和 $.313/.250$ 略有差異。

## 第 5 步：乘上 Scale 得到最終權重

$$
w_x = \text{RV}^{*}_x \times 1.251
$$

| 事件 | $\text{RV}^{*}_x$ | × 1.251 | Guts 表 | 差異 |
|---|---|---|---|---|
| BB | 0.55 | 0.688 | .687 | +0.001 |
| HBP | 0.57 | 0.713 | .718 | −0.005 |
| 1B | 0.70 | 0.876 | .881 | −0.005 |
| 2B | 1.00 | 1.251 | 1.256 | −0.005 |
| 3B | 1.27 | 1.589 | 1.594 | −0.005 |
| HR | 1.65 | 2.064 | 2.065 | −0.001 |

（已用程式驗算。）

## 結果與驗證
- 六個權重與 Guts 表的差異都在 ±0.005 以內。
- 誤差來源：$\text{RV}^{*}_x$ 只保留兩位小數，誤差最多 ±0.005，乘上 1.251 後最多約 ±0.006，所以這個差異範圍是合理的。

## 解讀
- 權重的「形狀」在第 2 步就決定了；第 3、4 步只是平移和縮放，讓數字看起來像 OBP。
- 出局的價值（−0.26）決定了平移量，也就是「上壘本身」的基本價值。這解釋了為什麼保送的權重（.687）遠大於它「高於平均」的價值（0.29）。

## 相關頁面
[[woba]]、[[linear-weights]]、[[run-expectancy-matrix]]
