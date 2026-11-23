---
title: WAR（勝場貢獻值）
type: metric
aliases: [WAR, Wins Above Replacement, fWAR, 勝場貢獻值, 替補水準以上勝場]
domain: [value]
leagues: [MLB]
tags: [counting-stat, wins, replacement-level]
sources: ["[[src-2010-slowinski-fangraphs-what-is-war]]", "[[src-2012-slowinski-fangraphs-war-misconceptions]]", "[[src-2012-slowinski-fangraphs-war-position-players]]", "[[src-2012-slowinski-fangraphs-war-pitchers]]", "[[src-2013-cameron-fangraphs-unifying-replacement-level]]", "[[src-2019-appelman-fangraphs-war-update-catcher-framing]]", "[[src-2024-appelman-fangraphs-war-update]]"]
source_count: 7
status: draft
full_name: Wins Above Replacement
scale: wins
upstream: ["[[batting-runs]]", "[[bsr]]", "[[positional-adjustment]]", "[[replacement-level]]", "[[runs-per-win]]", "[[fip]]"]
downstream: []
stabilization:
created: 2026-11-23
updated: 2026-11-24
---

# WAR（勝場貢獻值）

> 一句話定義：估計一位球員比「隨手可得的替補球員」多替球隊贏了幾場球，把打擊、跑壘、守備、投球的貢獻合成一個以**勝場**為單位的數字。

## 它在回答什麼問題
「如果這位球員受傷，球隊只能找小聯盟或板凳邊緣球員替補，會損失多少勝場？」（[[src-2010-slowinski-fangraphs-what-is-war]]）

它讓技能組合完全不同的球員可以互相比較，例如強打一壘手和頂級守備游擊手誰比較有價值。

## 定義與公式

野手（細節見 [[war-position-players]]）：

$$
\text{WAR} = \frac{\text{Batting} + \text{Base Running} + \text{Fielding} + \text{Positional} + \text{League} + \text{Replacement}}{\text{RPW}} = \frac{\text{RAR}}{\text{RPW}}
$$

投手（細節見 [[war-pitchers]]）：

$$
\text{WAR} = \left[\left(\frac{\text{lgFIPR9} - \text{pFIPR9}}{\text{dRPW}} + \text{Replacement}\right) \times \frac{\text{IP}}{9}\right] \times \text{LI 係數（後援）} + \text{Correction}
$$

變數說明：
- RAR：Runs Above Replacement，高於替補水準的得分
- RPW：每勝場需要的得分，見 [[runs-per-win]]
- 投手公式各項見 [[war-pitchers]]

出處：[[src-2012-slowinski-fangraphs-war-position-players]]、[[src-2012-slowinski-fangraphs-war-pitchers]]。

## 推導過程：為什麼是這樣組成
1. **先算「相對平均」的得分**：打擊、跑壘、守備都以聯盟平均（守備以同守位平均）為 0。
2. **把不同守位放到同一尺度**：守備得分只跟同守位比，所以要加上[[positional-adjustment|守位調整]]，反映「當平均游擊手比當平均一壘手難」。
3. **聯盟調整**：讓各聯盟「高於平均」的總和為 0。
4. **改成相對替補水準**：以平均為基準時，600 打席的平均球員和 1 打席的球員都是 0，無法反映上場量的價值。加上[[replacement-level|替補水準得分]]後就能區分。
5. **得分換成勝場**：除以 [[runs-per-win|RPW]]。

## 推導鏈：上游與下游
- 打擊：[[woba]] → [[wraa]] → [[batting-runs]] → WAR
- 跑壘：[[bsr]]（UBR + wSB + wGDP）
- 守備：UZR（捕手：rSB + RPP）＋ [[positional-adjustment]]
- 投手：[[fip]] → ifFIP → FIPR9 → … → WAR

## 不同版本
| 版本 | 提供者 | 投手基礎 | 備註 |
|---|---|---|---|
| fWAR | FanGraphs | FIP（含內野高飛球） | 另提供 RA9-WAR |
| rWAR／bWAR | Baseball-Reference | 失分，並嘗試修正球隊守備 | 替補水準與 fWAR 相同 |
| WARP | Baseball Prospectus | — | 概念相同、名稱不同 |

三者框架相同，但打擊、守備、投球的估算方法不同，所以結果可能有差異（[[src-2010-slowinski-fangraphs-what-is-war]]）。

## 聯盟與年份差異
- 每季總共 1,000 WAR，對應替補勝率 .294；野手 570、投手 430（57%／43%）。
- WAR 經過球場與聯盟調整、不考慮情境，所以可以跨年、跨聯盟、跨球隊比較。
- NPB、KBO、CPBL 目前尚無來源。

## 如何解讀
先發野手與先發投手的經驗法則（[[src-2010-slowinski-fangraphs-what-is-war]]）：

| WAR | 等級 |
|---|---|
| 0–1 | 邊緣球員（Scrub） |
| 1–2 | 角色球員（Role Player） |
| 2–3 | 穩定先發（Solid Starter） |
| 3–4 | 好球員（Good Player） |
| 4–5 | 明星（All-Star） |
| 5–6 | 超級明星（Superstar） |
| 6+ | MVP |

- 全職先發野手、先發投手平均約 2 WAR；板凳球員通常 0～1；後援投手超過 1 就很出色。
- WAR 可以是負值。

## 限制與常見誤用
綜合 [[src-2010-slowinski-fangraphs-what-is-war]]、[[src-2012-slowinski-fangraphs-war-misconceptions]]：

1. **不是精確值**：6 WAR 可能介於 5 到 7；6.4 和 6.1 無法區分，6.4 和 4.1 才能。
2. **球隊 WAR 總和 ≠ 實際勝場**：要加回全替補球隊的基準勝場（見 [[replacement-level]]）。
3. **衡量過去，不是真實實力**：估計真實實力時，用近三年 WAR 依 **5/3/1** 加權平均。
4. **守備的不確定性最大**：守備數據由 BIS 人工輸入，守位調整也是估計值；靠守備拿到大量價值的球員，WAR 的不確定性也較大。捕手 WAR 最不精確。
5. **投手的場內球**：FIP 假設場內球結果是平均水準，會低估善於壓制場內球安打的投手。可以搭配 RA9-WAR 參考。
6. **環境交互作用**：球場調整無法消除球員技能與環境的交互影響。
7. **不考慮情境**：關鍵安打、高槓桿後援沒有額外加分（後援投手 WAR 有槓桿係數，但只是部分反映）；情境價值看 [[wpa|WPA]]。

> [!note] 方法的更新（已由來源確認）
> - **2013**：FanGraphs 與 Baseball-Reference 統一替補水準為 .294（之前 FanGraphs .265）（[[src-2013-cameron-fangraphs-unifying-replacement-level]]）
> - **2019**：捕手 framing 納入 WAR，資料從 2008 年起；投手依搭配捕手扣回（[[src-2019-appelman-fangraphs-war-update-catcher-framing]]）
> - **2024**：守備與跑壘改用 Statcast（OAA、XBR 等），回溯至 2016 年（[[src-2024-appelman-fangraphs-war-update]]）
> 比較不同年代、或不同時間抓下來的 WAR 時，要注意這些版本差異。

## 範例
- [[ex-war-mlb-2012-trout]]：Trout 2012 年野手 WAR 完整拆解

## 相關頁面
[[war-position-players]]、[[war-pitchers]]、[[replacement-level]]、[[runs-per-win]]、[[batting-runs]]、[[bsr]]、[[positional-adjustment]]

## 來源
- [[src-2010-slowinski-fangraphs-what-is-war]]：定義、版本、解讀、1,000 WAR
- [[src-2012-slowinski-fangraphs-war-misconceptions]]：常見誤用
- [[src-2012-slowinski-fangraphs-war-position-players]]：野手公式
- [[src-2012-slowinski-fangraphs-war-pitchers]]：投手公式
