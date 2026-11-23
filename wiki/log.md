# Log

只追加的時間紀錄。查詢最近 5 筆：`grep "^## \[" wiki/log.md | tail -5`

---

## [2026-11-23] setup | 建立知識庫架構
- 建立 `AGENTS.md`（schema）與資料夾結構：`raw/`、`wiki/`、`outputs/`、`scripts/`
- 建立 `wiki/index.md`、`wiki/log.md`、`wiki/overview.md`、`wiki/dashboard.md`
- 主要規則：繁體中文內文、英文 kebab-case 檔名、Obsidian wikilink、Dataview frontmatter、公式一律用 LaTeX、多聯盟（MLB/NPB/KBO/CPBL）、矛盾並列呈現、依來源類型選擇 ingest 模式

## [2026-11-23] ingest | FanGraphs Library — wOBA
- 模式：discussed
- 新建：[[src-2010-slowinski-fangraphs-woba]]、[[woba]]、[[wraa]]、[[linear-weights]]（stub）、[[ex-woba-mlb-2013-trout]]（needs-review）
- 更新：[[index]]、[[overview]]
- 紅連結：run-expectancy-matrix、wrc、wrc-plus、batting-runs、park-factor、ubr、wsb、replacement-level、runs-per-win
- 備註：來源沒有給出權重的具體推導步驟與 wRC+，woba.md 的推導過程以「推論」標示並等待補來源；Trout 範例分母待使用者提供 FanGraphs 數據；原文 PDF 待使用者存入 raw/articles/2010-02-15_fangraphs_woba.pdf

## [2026-11-23] schema | 新增網頁來源存檔與數據提醒規則
- AGENTS.md 第 11.1 節：網頁來源一律存成 PDF 放入 raw/articles/
- AGENTS.md 第 15 節：範例或分析需要的數據不在 raw/ 時，主動提醒使用者提供，並轉成 CSV 存入 raw/data/

## [2026-11-23] ingest | Mike Trout FanGraphs 球員頁數據
- 模式：batch
- 新增數據：`raw/data/fangraphs_mlb_2011-2026_trout-{standard,advanced,value}.csv`（含 .meta.md），原檔 `fangraphs_mlb_2026-11-23_trout-player-page.pdf`
- 更新：[[ex-woba-mlb-2013-trout]]（補上分母 706，status → stable）、[[src-2010-slowinski-fangraphs-woba]]（raw_path 改為實際檔名）、[[index]]
- 備註：advanced 表的 UBR、wGDP、XBR、wSB 因 PDF 版面對齊有歧義而未收錄

## [2026-11-23] schema | raw 檔名規則與缺失清單
- AGENTS.md：raw/ 改為「內容唯讀」，檔名不符合規則時可依規則改名
- AGENTS.md 11.1：每次匯入的報告都要附一次列完的「缺失清單」，標註必要或選擇性
- 改名：`wOBA _ Sabermetrics Library.pdf` → `2010-02-15_fangraphs_woba.pdf`；`The Beginner’s Guide To Deriving wOBA _ Sabermetrics Library.pdf` → `2016-04-11_fangraphs_deriving-woba.pdf`；`wRC and wRC+ _ Sabermetrics Library.pdf` → `2010-02-16_fangraphs_wrc-and-wrc-plus.pdf`

## [2026-11-23] ingest | The Beginner's Guide To Deriving wOBA
- 模式：discussed
- 新建：[[src-2016-weinberg-fangraphs-deriving-woba]]、[[run-expectancy-matrix]]、[[ex-woba-mlb-2015-derivation]]
- 更新：[[woba]]（推導過程改為有來源版本，status → stable）、[[linear-weights]]（stub → draft）
- 備註：確認先前推論骨架正確；修正縮放目標為扣除 IBB 的 OBP

## [2026-11-23] ingest | FanGraphs Library — wRC and wRC+
- 模式：discussed
- 新建：[[src-2010-slowinski-fangraphs-wrc]]、[[wrc]]、[[wrc-plus]]、[[park-factor]]（stub）、[[ex-wrc-plus-mlb-2012-trout]]
- 更新：[[wraa]]（status → stable）、[[ex-woba-mlb-2013-trout]]（加入 wRC）、[[index]]、[[overview]]
- 備註：使用者指出 FanGraphs 只提供 2016 年以後的球場係數，Trout 2013 年 wRC+ 176 無法驗算

## [2026-11-23] ingest | Park Factors、What is WAR?、WAR Misconceptions、WAR for Position Players、WAR for Pitchers
- 模式：discussed（使用者確認後寫入）
- 改名：五份 PDF 以規則命名存入 raw/articles/（`2010-02-27_fangraphs_park-factors.pdf`、`2010-02-15_fangraphs_what-is-war.pdf`、`2012-03-23_fangraphs_war-misconceptions.pdf`、`2012-04-02_fangraphs_war-position-players.pdf`、`2012-03-28_fangraphs_war-pitchers.pdf`）
- 新建：五篇來源頁、[[war]]、[[war-position-players]]、[[war-pitchers]]、[[batting-runs]]、[[bsr]]、[[replacement-level]]（needs-review）、[[runs-per-win]]、[[positional-adjustment]]、[[ex-war-mlb-2012-trout]]
- 更新：[[park-factor]]（stub → draft）、[[wrc-plus]]、[[wraa]]、[[ex-wrc-plus-mlb-2012-trout]]（PF 為減半顯示值）、[[index]]、[[overview]]
- 分歧：替補球隊 43 勝 vs .294 勝率，並列於 [[replacement-level]]
- 備註：Trout 2012 年 Batting、守位調整、WAR 驗算吻合；2013 年守位調整差 1.0（推測 DH 出賽）；runCS 公式在來源中缺少負號（推論）

## [2026-11-23] output | 教學投影片：從 wOBA 到 wRC+
- 檔案：`outputs/slides/woba-to-wrc-plus.html`（16 頁，獨立 HTML，數學式以 KaTeX 預先轉譯、字型內嵌，可離線開啟）
- 結構：指標意義 → 推導流程圖 → 第 0～4 步 → 旁支 Batting Runs → 結論 → 實際範例（Trout 2012 wRC+、Trout 2013 wOBA）→ 限制與來源
- 內容取自：[[woba]]、[[wraa]]、[[wrc]]、[[wrc-plus]]、[[batting-runs]]、[[run-expectancy-matrix]]、[[park-factor]]、[[ex-wrc-plus-mlb-2012-trout]]、[[ex-woba-mlb-2013-trout]]
- 備註：使用者指定 HTML 格式，未使用 Marp

## [2026-11-23] ingest | RE24、Park Factors – 5 Year Regressed
- 模式：batch（使用者指示整理後放入簡報）
- 改名：`RE24 _ Sabermetrics Library.pdf` → `2014-07-30_fangraphs_re24.pdf`；`Park Factors – 5 Year Regressed _ Sabermetrics Library.pdf` → `2016-05-16_fangraphs_park-factors-5-year-regressed.pdf`
- 新建：[[src-2014-weinberg-fangraphs-re24]]、[[src-2016-appelman-fangraphs-park-factors-5yr]]、[[re24]]
- 更新：[[run-expectancy-matrix]]（ΔRE 的直接得分項改為有來源；加入 2014 年中性矩陣；status → stable）、[[linear-weights]]、[[park-factor]]（計算方法）、[[ex-wrc-plus-mlb-2012-trout]]、[[index]]
- 修正：先前「顯示值 95 → 原始 90」的推論忽略了迴歸；改為假設 X = 0.9 時原始 ≈ 0.889

## [2026-11-23] output | 教學投影片 v2：從 wOBA 到 wRC+
- 檔案：`outputs/slides/woba-to-wrc-plus.html`（覆蓋 v1；20 頁）
- 修改：大綱與限制頁改為模組面板；流程圖改為三列並把步驟運算做成箭頭上的標籤；新增 RE 定義與 ΔRE 計算（[[src-2014-weinberg-fangraphs-re24]]）、線性權重的 n_x 定義、PF 計算頁（[[src-2016-appelman-fangraphs-park-factors-5yr]]）、Trout 原始數據表與資料位置代碼；補上 lgwOBA、lgR/PA、Batting Runs 定義；wRAA vs wRC 比較表；風格改為 80 年代復古像素 × Y2K
- 修正：顯示 PF 95 的原始值由「90」改為「約 0.889」（考慮迴歸）

## [2026-11-23] query | 球場係數的計算邏輯
- 依據：[[park-factor]]、[[src-2016-appelman-fangraphs-park-factors-5yr]]、[[src-2010-slowinski-fangraphs-park-factors]]
- 回答於對話中，未另建頁（內容已涵蓋於 [[park-factor]]）

## [2026-11-23] query | 球場係數計算的追問（客場基準、× T、減半、迴歸、X 的決定、新球場）
- 依據：[[park-factor]]、[[src-2016-appelman-fangraphs-park-factors-5yr]]
- 更新：[[park-factor]]（待確認現行 X 值）、[[src-2016-appelman-fangraphs-park-factors-5yr]]（標註疑似筆誤）

## [2026-11-23] output | 教學投影片 v3：擴充球場係數單元
- 檔案：`outputs/slides/woba-to-wrc-plus.html`（覆蓋 v2；23 頁）
- 修改：原本一頁的 PF 計算擴充為 4 頁：三步驟完整數值例（H = 11、R = 10、T = 15 → 104）、為什麼用客場與乘 T、為什麼減半與迴歸、新球場時間軸與限制；大綱頁碼同步更新
- 依據：本日對 [[park-factor]] 的連續查詢內容

## [2026-11-23] schema | 新增 SOP.md
- 新建專案根目錄 `SOP.md`：SOP-01 匯入文章、02 匯入數據、03 查詢問答、04 教學簡報、05 Lint、06 交付與版本控制，含報告模板、命名速查、常見狀況
- `AGENTS.md` 開頭加上 SOP 連結
- TODO：簡報建置與檢查腳本尚未存入 `scripts/slides/`

## [2026-11-23] schema | SOP-04 改為 graph，「整理重點與驗算」獨立為 loop
- `SOP.md` v1.1：SOP-04 改寫為「主題 → 教學簡報」graph（N1 範圍界定 → N2 內容 loop → N4–N6 產生與版面 loop → N7 交付 → N8 審閱 → R 規則回寫），附節點表、通過標準、指令
- 新增 `scripts/slides/`：`build.js`（建置）、`check.py`（版面關卡）、`spec_check.py`（內容關卡）、`template.html`、`package.json`
- 新增 `outputs/slides/woba-to-wrc-plus/`：spec.md、verify.py（29 項斷言通過）、src.html，作為第一個實際範例
- `AGENTS.md` 第 14 節：教學簡報預設 HTML，輸入「做簡報：<主題>」即啟動 SOP-04
- 測試：check.py 能抓到溢出、像素字體中文；build.js 能抓到公式錯誤；spec_check.py 能抓到驗算不符與必要缺失未解決

## [2026-11-23] output | 教學投影片：WAR 是怎麼算出來的（SOP-04 首次完整執行）
- 成品：`outputs/slides/war-explained.html`（16 頁）；工作檔與逐節點紀錄：`outputs/slides/war-explained/`（spec.md、verify.py、src.html、run-log.md、evidence/）
- 關卡：N2 三輪（18/19 → 19/19 → 由 N4 退回後 29/29）；N6 兩輪（目視抓到 \tfrac 字太小 → 修正後通過）
- 規則回寫：spec_check.py 失敗時列出 ✗ 項目；build.js 禁用 \tfrac；SOP-04 新增兩條版面規則
- 依據：[[war]]、[[war-position-players]]、[[war-pitchers]]、[[batting-runs]]、[[bsr]]、[[positional-adjustment]]、[[replacement-level]]、[[runs-per-win]]、[[ex-war-mlb-2012-trout]]

## [2026-11-23] output | war-explained：N8 審閱暫緩
- 使用者決定先交作業，審閱與修改留待日後；待辦見 `outputs/slides/war-explained/run-log.md` 第 6 節

## [2026-11-23] schema | SOP-04 改為「先交毛片、確認後才渲染」
- 新增 N3 毛片（`draft.md`，範本 `scripts/slides/draft_template.md`）：逐頁完整內容、缺失清單、需要補充的資料、確認欄
- 新增使用者審閱毛片的 🛑 檢查點；N1 不再中途停下，缺口一律帶進毛片
- `spec_check.py` 新增 `--draft`（毛片涵蓋每一頁）與 `--render`（已確認、缺失皆已解決或經使用者接受）
- `build.js`：工作資料夾的 spec.md 未設 `content_approved: true` 時拒絕建置
- 現有簡報：woba-to-wrc-plus 設為已確認（依 v1–v3 審閱）；war-explained 設為未確認（日後先補毛片）
- `AGENTS.md` 第 14 節同步更新
