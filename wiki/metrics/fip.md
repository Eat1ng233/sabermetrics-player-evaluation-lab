---
title: FIP（獨立於守備的投球）
type: metric
aliases: [FIP, Fielding Independent Pitching, 獨立於守備的投球]
domain: [pitching]
leagues: [MLB]
tags: [rate-stat, era-scale, dips]
sources: ["[[src-2010-slowinski-fangraphs-fip]]", "[[src-2012-slowinski-fangraphs-war-pitchers]]"]
source_count: 2
status: draft
full_name: Fielding Independent Pitching
scale: ERA（越低越好）
upstream: ["[[linear-weights]]"]
downstream: ["[[war-pitchers]]"]
stabilization:
created: 2026-11-24
updated: 2026-11-24
---

# FIP（獨立於守備的投球）

> 一句話定義：只用三振、保送、觸身球、全壘打估計投手的 ERA，假設場內球的結果、守備與事件順序都是聯盟平均。

## 定義與公式

$$
\text{FIP} = \dfrac{13\,\text{HR} + 3(\text{BB} + \text{HBP}) - 2\,\text{K}}{\text{IP}} + C
$$

變數說明：
- $\text{HR}$：被全壘打數；$\text{BB}$：保送數；$\text{HBP}$：觸身球數；$\text{K}$：三振數
- $\text{IP}$：投球局數
- $C$：FIP 常數，每年不同，一般約 3.10

出處：[[src-2010-slowinski-fangraphs-fip]]。

## 推導過程

### 1. 為什麼只用這四種事件
DIPS 理論（Voros McCracken）發現：投手被打成場內球後，變成安打的比例（BABIP）在不同球季之間幾乎不相關。換句話說，場內球的結果大多取決於守備與運氣，不是投手。

三振、保送、觸身球、全壘打都不需要守備員參與，所以被視為投手自己的結果（[[src-2010-slowinski-fangraphs-fip]]）。

### 2. 係數的意義
來源只說 13、3、2 來自「各事件對失分的相對價值」。

> [!info] 推論：係數為什麼這麼大
> FIP 的分子除以 IP 得到「每局」的值，而 ERA 是「每九局」的失分。所以係數約等於「每個事件比一般場內球多（或少）造成的失分 × 9」。
> 例如全壘打比一般場內球多約 1.4～1.5 分，乘以 9 約為 13；保送多約 0.3 分，乘以 9 約為 3；三振比場內球少約 0.2 分（多一個出局、沒有上壘機會），乘以 9 約為 2。這些近似值是依 [[linear-weights]] 的概念估計，來源沒有提供推導，待補來源確認。

### 3. 常數：讓 FIP 和 ERA 同尺度
四個事件算出的值不是失分，所以要加一個常數，讓**聯盟平均 FIP = 聯盟平均 ERA**：

$$
C = \text{lgERA} - \dfrac{13\,\text{lgHR} + 3(\text{lgBB} + \text{lgHBP}) - 2\,\text{lgK}}{\text{lgIP}}
$$

- $\text{lgERA}$：聯盟平均 ERA
- 其餘 $\text{lg}$ 開頭的變數：全聯盟的事件總數與總局數

> [!info] 推論：常數吸收了什麼
> 把聯盟數字代回 FIP 公式，會剛好得到 lgERA。也就是說，常數代表「場內球、守備、事件順序」在聯盟平均情況下造成的失分。投手的 FIP 等於「聯盟平均的場內球結果」加上「他自己的三振、保送、全壘打表現」。

### 4. 在投手 WAR 中的變形
[[war-pitchers]] 使用 **ifFIP**：把內野高飛球（IFFB）也算成三振，常數也要重新計算。所以不能直接用球員頁上的 FIP 算 WAR。

## 推導鏈：上游與下游
[[linear-weights]]（各事件失分價值）→ 係數 13、3、2 → FIP → ifFIP → FIPR9 → [[war-pitchers]]

## 聯盟與年份差異
- 常數每年、每個聯盟都不同，FanGraphs Guts 頁有各年數值。
- NPB／KBO／CPBL 要用各聯盟自己的 lgERA、lgHR 等重新計算常數（推論：係數本身也可能因得分環境而不同，來源未涵蓋）。

## 如何解讀
尺度和 ERA 相同，可以直接當 ERA 讀。評級表（[[src-2010-slowinski-fangraphs-fip]]，2016 年得分環境）：

| 評級 | FIP |
|---|---|
| 極佳 | 3.20 |
| 很好 | 3.50 |
| 高於平均 | 3.80 |
| 平均 | 4.20 |
| 低於平均 | 4.40 |
| 差 | 4.70 |
| 很差 | 5.00 |

聯盟平均 FIP 每年等於聯盟平均 ERA，所以門檻要隨年份調整。

## 限制與常見誤用
- **不是要取代 ERA**：FIP 只看投手結果的一部分。少數投手能長期優於 FIP，例如擅長牽制跑者、或能製造比較不容易變成安打的擊球類型。
- **樣本要夠大**：FIP 預測未來比描述當下更準；單場或少量局數波動很大，至少要一整季。
- **ERA 與 FIP 的差距**常被歸因於場內球運氣，但也可能來自上面提到的真實能力。

## 範例
_（尚無；需要投手資料）_

## 相關頁面
[[war-pitchers]]、[[war]]、[[linear-weights]]

## 來源
- [[src-2010-slowinski-fangraphs-fip]]：定義、公式、常數、DIPS、評級表
- [[src-2012-slowinski-fangraphs-war-pitchers]]：ifFIP 與投手 WAR 的用法
