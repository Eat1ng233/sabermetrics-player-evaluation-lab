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
