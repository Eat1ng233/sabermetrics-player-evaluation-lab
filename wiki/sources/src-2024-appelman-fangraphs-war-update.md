---
title: 2024 FanGraphs WAR Update
type: source
aliases: [2024 WAR 更新]
domain: [value, fielding, baserunning]
leagues: [MLB]
tags: [fangraphs, war, statcast, oaa]
sources: []
source_count: 0
status: stable
source_type: article
author: David Appelman
publisher: FanGraphs
published: 2024-04-05
url: https://blogs.fangraphs.com/2024-fangraphs-war-update/
raw_path: raw/articles/2024-04-05_fangraphs_war-update-2024.pdf
ingest_mode: discussed
created: 2026-11-24
updated: 2026-11-24
---

# 2024 FanGraphs WAR Update

## 基本資訊
- 作者：David Appelman（FanGraphs 創辦人）；發表：2024-04-05
- 原始檔：`raw/articles/2024-04-05_fangraphs_war-update-2024.pdf`；擷取日期：2026-11-24

## 核心論點
1. 這次更新完成了 FanGraphs WAR 從 UZR 轉向 Statcast 守備指標的過程。
2. 轉換始於 2022 年：UZR 的守備範圍改用 Statcast 的 Fielding Runs Prevented（由 OAA 換算成相對平均的得分）。
3. 本次變更**回溯到 2016 年球季**：
   - 新增：Statcast Fielding Run Value 的捕手擋球（blocking）
   - 取代：UZR 的 ARM → Statcast 外野傳球；DRS 的阻殺盜壘 → Statcast 捕手阻殺
   - 取代：UBR 與 wGDP → Statcast 跑壘指標（XBR）
   - 刪除：UZR 的雙殺得分（DPR）
4. UZR 會繼續計算到 2025 年球季結束。
5. 幾乎所有球員 2016–2023 的 WAR 總和變動都在 1 以內；變動最大的例子：Yadier Molina +3.0、Mookie Betts −3.0。改版前的數值以 Legacy WAR（L-WAR）保留。

## 關鍵數據與公式
2016 年起的野手 WAR 組成（推論，依本文整理）：

$$
\text{Fielding}_{2016+} \approx \text{FRP（範圍）} + \text{ARM}_{\text{Statcast}} + \text{Blocking} + \text{Throwing}_{\text{捕手}} + \text{ErrR}?
$$

$$
\text{BsR}_{2016+} \approx \text{XBR} + \text{wSB}?
$$

帶問號的項目本文沒有提到，見下方待追問。

## 對 Wiki 的影響
- 更新頁面：[[war-position-players]]、[[bsr]]、[[uzr]]：加入 2016 年起的版本差異與「不同觀點」
- 與既有內容的矛盾：[[src-2010-slowinski-fangraphs-uzr]]、[[src-2012-slowinski-fangraphs-war-position-players]] 描述的是改版前的做法（時間先後，不是方法爭議）
- 對既有範例的影響：[[ex-war-mlb-2012-trout]] 的 2012 年不在回溯範圍內，不受影響

## 待追問的問題
- 2022 年的守備範圍替換是否也回溯到 2016 年？本文沒有明說
- UZR 的失誤得分（ErrR）、wSB 是否保留？本文沒有提到
- 捕手 framing 是否計入 WAR？本文沒有提到 → 已由 [[src-2019-appelman-fangraphs-war-update-catcher-framing]] 回答：2019 年起計入
