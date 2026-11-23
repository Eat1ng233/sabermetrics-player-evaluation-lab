---
title: 投手 WAR 計算
type: metric
aliases: [Pitcher WAR, 投手 WAR, ifFIP, FIPR9]
domain: [value, pitching]
leagues: [MLB]
tags: [war, replacement-level, fip]
sources: ["[[src-2012-slowinski-fangraphs-war-pitchers]]", "[[src-2010-slowinski-fangraphs-fip]]", "[[src-2019-appelman-fangraphs-war-update-catcher-framing]]"]
source_count: 3
status: draft
full_name: Wins Above Replacement for Pitchers
scale: wins
upstream: ["[[fip]]", "[[park-factor]]", "[[replacement-level]]", "[[runs-per-win]]", "[[leverage-index]]"]
downstream: ["[[war]]"]
stabilization:
created: 2026-11-23
updated: 2026-11-24
---

# 投手 WAR 計算

> 一句話定義：以 FIP（把內野高飛球算成三振）衡量投手相對聯盟平均的失分預防，換成勝場、加上替補水準、依局數縮放。

> [!note] FIP 的定義與推導
> 一般 FIP 的公式、常數與 DIPS 理論見 [[fip]]。本頁使用的是把內野高飛球算成三振的 **ifFIP**，係數 13、3、2 的完整推導仍待補來源。

## 定義與公式

$$
\text{WAR} = \left[\left(\frac{\text{lgFIPR9} - \text{pFIPR9}}{\text{dRPW}} + \text{Replacement}\right) \times \frac{\text{IP}}{9}\right] \times \text{LI 係數} + \text{Correction}
$$

出處：[[src-2012-slowinski-fangraphs-war-pitchers]]。LI 係數只用於後援投手。

## 推導過程

### 1. ifFIP：把內野高飛球當作三振

$$
\text{ifFIP} = \frac{13\,\text{HR} + 3(\text{BB} + \text{HBP}) - 2(\text{K} + \text{IFFB})}{\text{IP}} + C_{\text{ifFIP}}
$$

$$
C_{\text{ifFIP}} = \text{lgERA} - \frac{13\,\text{lgHR} + 3(\text{lgBB} + \text{lgHBP}) - 2(\text{lgK} + \text{lgIFFB})}{\text{lgIP}}
$$

- IFFB：內野高飛球。和一般 FIP 不同，所以不能直接用球員頁的 FIP 或 Guts 頁的 cFIP。

> [!note] 2019 年起：捕手 framing 調整
> 投手受惠於捕手偷好球的部分要扣回：WAR 計算改用 $\text{FIP} + \dfrac{\text{Framing}}{9}$（每九局受惠的 framing 得分），動態 RPW 也一起調整；RA9-WAR 同樣調整。例：Greinke 2011 FIP 3.00，每九局受惠 0.31 → 改用 3.31（[[src-2019-appelman-fangraphs-war-update-catcher-framing]]）。

### 2. 轉成 RA9 尺度
FIP 的尺度和 ERA 相同，但 WAR 要用全部失分（RA9）：

$$
\text{FIPR9} = \text{ifFIP} + (\text{lgRA9} - \text{lgERA})
$$

### 3. 球場調整（乘法）
使用 FIP 專用的球場係數：

$$
\text{pFIPR9} = \frac{\text{FIPR9}}{\text{PF}/100}
$$

### 4. 與所屬聯盟比較

$$
\text{RAAP9} = \text{lgFIPR9}_{\text{AL/NL}} - \text{pFIPR9}
$$

每九局比聯盟平均少失幾分（RAAP9 是文章作者為說明而取的名稱）。

### 5. 投手專屬的動態 RPW
投手在場上時會改變比賽的得分環境，所以不用聯盟平均 RPW：

$$
\text{dRPW} = \left(\frac{(18 - \text{IP/G}) \times \text{lgFIPR9} + (\text{IP/G}) \times \text{pFIPR9}}{18} + 2\right) \times 1.5
$$

- 分子是加權平均：一場比賽兩隊共 18 局，投手在場上的局數用他的 pFIPR9，其餘用聯盟平均。
- 「+2 再 ×1.5」是把每場得分換成每勝得分的簡化法，和野手用的 [[runs-per-win|RPW]] 公式一致。

> [!info] 推論：與野手 RPW 公式的對應
> 野手的 $\text{RPW} = 1.5 \times \text{R/9} + 3$；而 $1.5 \times (x + 2) = 1.5x + 3$。所以投手公式只是把「R/9」換成「這位投手出賽時的得分環境」，兩者形式相同。

### 6. 換成每場勝場，加上替補水準

$$
\text{WPGAA} = \frac{\text{RAAP9}}{\text{dRPW}}, \qquad \text{WPGAR} = \text{WPGAA} + \text{Replacement}
$$

$$
\text{Replacement} = 0.03 \times \left(1 - \frac{\text{GS}}{\text{G}}\right) + 0.12 \times \frac{\text{GS}}{\text{G}}
$$

先發 0.12、後援 0.03。兩種角色都有時，來源建議分開計算再相加。

### 7. 依局數縮放

$$
\text{"WAR"} = \text{WPGAR} \times \frac{\text{IP}}{9}
$$

### 8. 後援投手的槓桿係數

$$
\text{LI 係數} = \frac{1 + \text{gmLI}}{2}
$$

把後援投手的平均登板槓桿（gmLI，見 [[leverage-index]]）向 1 迴歸一半。原因是「順位遞補」（chaining）：終結者受傷時，不是 3A 投手直接接手終結者，而是牛棚每個人往上遞補一格，3A 投手補最低的位置。

### 9. 全聯盟修正
讓 MLB 投手 WAR 合計為 430：

$$
\text{Correction} = \text{WARIP} \times \text{IP}
$$

2016 年 WARIP = −0.000682902；一般介於 −0.0007 到 −0.0012。

## 限制與常見誤用
- FIP 假設場內球結果為平均水準（見 [[war#限制與常見誤用]]）；FanGraphs 另提供 RA9-WAR。
- 球場係數假設一半比賽在主場、一半在中性球場，不考慮實際出賽球場分布。例如一位幾乎都在主場先發的洛磯投手，得到的調整會不夠。
- 不調整對手強度。

## 相關頁面
[[war]]、[[war-position-players]]、[[fip]]、[[park-factor]]、[[replacement-level]]、[[runs-per-win]]、[[leverage-index]]

## 來源
- [[src-2012-slowinski-fangraphs-war-pitchers]]
