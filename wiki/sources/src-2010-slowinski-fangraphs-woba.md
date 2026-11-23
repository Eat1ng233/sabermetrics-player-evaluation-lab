---
title: FanGraphs Library — wOBA
type: source
aliases: [FanGraphs wOBA 說明頁, Slowinski wOBA]
domain: [batting]
leagues: [MLB]
tags: [fangraphs-library, linear-weights]
sources: []
source_count: 0
status: stable
source_type: article
author: Piper Slowinski
publisher: FanGraphs Library
published: 2010-02-15
url: https://library.fangraphs.com/offense/woba/
raw_path: raw/articles/2010-02-15_fangraphs_woba.pdf
ingest_mode: discussed
created: 2026-11-23
updated: 2026-11-23
---

# FanGraphs Library — wOBA

## 基本資訊
- 作者：Piper Slowinski
- 出處：FanGraphs Library（Offense 分類）
- 發表：2010-02-15；頁面最後修改：2017-05-08
- 網址：https://library.fangraphs.com/offense/woba/
- 原始檔：`raw/articles/2010-02-15_fangraphs_woba.pdf`
- 擷取日期：2026-11-23

## 核心論點
1. [[woba|wOBA]] 由 Tom Tango 提出，並在《The Book》中使用。它是綜合性的進攻指標，依各進攻事件的相對價值給予不同權重。
2. 傳統指標的缺陷：打擊率把所有安打視為等值；OBP 同樣不分上壘方式；SLG 給安打的權重不準確；OPS 隱含「1 點 SLG = 1 點 OBP」的假設。文章估計 OBP 的價值約為 SLG 的 1.8 倍。
3. 權重由 [[linear-weights|線性權重]]（各事件的得分價值）決定，接著縮放成聯盟平均 wOBA ≈ 聯盟平均 OBP。
4. 權重每年不同。FanGraphs Guts 頁面提供 1871 年至今各年的權重。
5. wOBA Scale 把 wOBA 與聯盟平均的差距換算成得分，並用來計算 [[wraa|wRAA]]。文章把 wRAA 定義為未經球場調整的 [[batting-runs|Batting Runs]]。
6. 限制：不計入故意四壞；盜壘相關價值已移出，改由 [[ubr|UBR]] 與 [[wsb|wSB]] 處理；不考慮情境（壘包、出局數、槓桿）；沒有[[park-factor|球場調整]]。

## 關鍵數據與公式
MLB 2013 年的 wOBA 公式：

$$
\text{wOBA}_{2013} = \frac{0.690\,\text{uBB} + 0.722\,\text{HBP} + 0.888\,\text{1B} + 1.271\,\text{2B} + 1.616\,\text{3B} + 2.101\,\text{HR}}{\text{AB} + \text{BB} - \text{IBB} + \text{SF} + \text{HBP}}
$$

- MLB 2013 年 wOBA Scale = 1.277；聯盟 wOBA = .314
- 平均打者約 .320
- 經驗法則：每 600 PA 中，20 點 wOBA ≈ 10 分（相對平均）
- 解讀門檻表見 [[woba#如何解讀]]

範例：Mike Trout 2013 年 wOBA .423、wRAA ≈ 61.1，見 [[ex-woba-mlb-2013-trout]]。

## 對 Wiki 的影響
- 新建頁面：[[woba]]、[[wraa]]、[[linear-weights]]、[[ex-woba-mlb-2013-trout]]
- 更新頁面：[[overview]]
- 與既有內容的矛盾：無（第一份來源）

## 本來源沒有涵蓋的部分
- 權重的具體推導步驟（得分期望值矩陣 → 事件得分價值 → 相對出局價值 → 乘上 Scale）。
- [[wrc|wRC]] 與 [[wrc-plus|wRC+]] 的計算，內文沒有提到，只出現在導覽連結中。
- 為什麼排除故意四壞。
- MLB 以外聯盟的權重。

## 待追問的問題
- wOBA Scale 實際上怎麼算？為什麼它同時是「縮放到 OBP」的乘數，又是「換算成得分」的除數？
- 經驗法則「20 點 ≈ 10 分」依賴 Scale 的數值；用 2013 年的 1.277 驗算，$0.020 / 1.277 \times 600 \approx 9.4$ 分，大致吻合。
- 建議下一份來源：文章延伸閱讀中的 FanGraphs〈deriving wOBA〉、FanGraphs Library 的 wRC+ 頁面。
