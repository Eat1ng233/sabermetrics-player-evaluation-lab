---
title: FanGraphs Library — FIP
type: source
aliases: [FIP 說明頁]
domain: [pitching]
leagues: [MLB]
tags: [fangraphs-library, fip, dips]
sources: []
source_count: 0
status: stable
source_type: article
author: Piper Slowinski
publisher: FanGraphs Library
published: 2010-02-15
url: https://library.fangraphs.com/pitching/fip/
raw_path: raw/articles/2010-02-15_fangraphs_fip.pdf
ingest_mode: discussed
created: 2026-11-24
updated: 2026-11-24
---

# FanGraphs Library — FIP

## 基本資訊
- 作者：Piper Slowinski；發表：2010-02-15（評級表標示「2016 年得分環境」，應為後來更新的版本）
- 原始檔：`raw/articles/2010-02-15_fangraphs_fip.pdf`；擷取日期：2026-11-23

## 核心論點
1. FIP 估計：如果投手遇到聯盟平均的場內球結果與事件順序，他的 ERA 會是多少。
2. 理論基礎是 Voros McCracken 的 DIPS 理論：場內球變成安打的比例（BABIP）在不同球季之間相關性很低，投手對它的控制力有限。
3. 因此只用投手能直接控制的事件：三振、保送、觸身球、全壘打。這樣能去除守備、運氣與**事件順序**（sequencing）的影響。
4. 常數只是用來把 FIP 拉到 ERA 的尺度，讓聯盟平均 FIP = 聯盟平均 ERA；常數一般約 3.10。
5. FanGraphs 的投手 WAR 以 FIP 為基礎，而不是 ERA。
6. 少數投手能長期優於 FIP（例如擅長牽制跑者、製造較易被接殺的擊球類型），所以 FIP 應視為分析的起點。
7. FIP 預測未來的能力比描述當下更好；單場比較不適用，至少需要一整季的局數。

## 關鍵數據與公式

$$
\text{FIP} = \dfrac{13\,\text{HR} + 3(\text{BB} + \text{HBP}) - 2\,\text{K}}{\text{IP}} + C
$$

$$
C = \text{lgERA} - \dfrac{13\,\text{lgHR} + 3(\text{lgBB} + \text{lgHBP}) - 2\,\text{lgK}}{\text{lgIP}}
$$

評級表（2016 年得分環境）：極佳 3.20、很好 3.50、高於平均 3.80、平均 4.20、低於平均 4.40、差 4.70、很差 5.00。

## 對 Wiki 的影響
- 新建頁面：[[fip]]
- 更新頁面：[[war-pitchers]]：移除「FIP 沒有來源」警示，改連到 [[fip]]

## 待追問的問題
- 13、3、2 三個係數的完整推導（文章只說它們來自各事件對失分的相對價值）
- 各年 FIP 常數（文章指向 FanGraphs Guts 頁）
