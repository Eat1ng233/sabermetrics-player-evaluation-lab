# AGENTS.md — Sabermetrics Player Evaluation Lab

本文件是這個知識庫的 schema（規則文件）。任何 LLM agent（Claude Code、Codex 等）在這個資料夾工作前，必須先完整讀過本文件，並遵守其中的結構、格式與工作流程。本文件由使用者與 LLM 共同維護，規則有變動時直接修改本文件，並在 `wiki/log.md` 記錄。

---

## 1. 專案目的

以 Karpathy 的「LLM Wiki」模式，建立一個持續累積、互相連結的**賽伯計量學球員評估**知識庫。

- **用途**：自學、研究與寫作、教學與分享。頁面必須讓第三者也能讀懂。
- **讀者程度**：中階（熟悉 FanGraphs / Baseball Savant 的常見指標）。但**指標頁仍須完整解釋**，包含定義、推導過程與指標之間的連結，因為使用者會用這些頁面做推理（例如：wOBA 各事件權重如何從得分期望值推得，以及 wOBA 如何一路連到 wRC+）。
- **聯盟範圍**：MLB、NPB、KBO、CPBL，包含跨聯盟換算與聯盟環境調整。
- **優先領域**：
  1. 打擊與投球（wOBA、wRC+、xwOBA、FIP、xFIP、SIERA、Stuff+ 等）
  2. 守備與跑壘（OAA、DRS、UZR、FRV、BsR 等）
  3. Statcast 追蹤數據、新秀評等、合約價值（$/WAR）
- **次要領域**：WAR 各版本、預測系統（Steamer、ZiPS、PECOTA、Marcel）。不主動深挖，但需要時可建頁並連結。

人類的工作：挑選來源、決定分析方向、提出問題。
LLM 的工作：摘要、交叉連結、歸檔、維護一致性，以及其他所有整理工作。

---

## 2. 三層架構

| 層級 | 位置 | 規則 |
|---|---|---|
| 原始來源 | `raw/` | **唯讀**。LLM 只能讀取，絕不修改、改名或刪除。這是事實的最終依據。 |
| Wiki | `wiki/` | LLM 全權負責撰寫與維護。使用者閱讀，LLM 撰寫。 |
| Schema | `AGENTS.md` | 由使用者與 LLM 共同演進。 |

另有兩個輔助資料夾：
- `outputs/`：查詢產生的簡報（Marp）、圖表等成品。
- `scripts/`：預留給未來的 Python 程式（pandas、pybaseball）。目前不主動撰寫或執行程式，除非使用者要求。

---

## 3. 目錄結構

```
Sabermetrics Player Evaluation Lab/
├── AGENTS.md
├── raw/
│   ├── articles/      網路文章（Obsidian Web Clipper 剪下的 .md）
│   ├── papers/        論文、書籍（PDF）
│   ├── data/          數據檔（CSV、XLSX，例如 FanGraphs / Savant 匯出）
│   ├── transcripts/   Podcast、影片逐字稿
│   ├── notes/         使用者自己的筆記
│   └── assets/        圖片附件（Obsidian 附件資料夾）
├── wiki/
│   ├── index.md       全部頁面目錄（每次 ingest 都要更新）
│   ├── log.md         只追加的時間紀錄
│   ├── overview.md    整體綜述：知識庫目前涵蓋什麼、核心觀點
│   ├── dashboard.md   Dataview 動態查詢頁
│   ├── metrics/       指標頁
│   ├── concepts/      概念與方法頁
│   ├── sources/       來源摘要頁
│   ├── examples/      指標計算範例
│   ├── case-studies/  案例研究
│   └── comparisons/   比較與綜合頁
├── outputs/
│   ├── slides/        Marp 簡報
│   └── charts/        圖表
└── scripts/
```

---

## 4. 語言與命名

- **內文**：繁體中文（台灣用語）。指標名稱、專有名詞、公式符號保留英文，首次出現時附中文說明，例如「wOBA（weighted On-Base Average，加權上壘率）」。
- **檔名**：英文 kebab-case，全小寫，不含空格。
- **檔名前綴**（避免 wikilink 撞名）：

| 類型 | 資料夾 | 檔名格式 | 範例 |
|---|---|---|---|
| 指標 | `metrics/` | `<指標名>.md` | `woba.md`、`wrc-plus.md`、`fip.md` |
| 概念 | `concepts/` | `<概念名>.md` | `run-expectancy-matrix.md`、`park-factor.md` |
| 來源 | `sources/` | `src-<年>-<作者>-<短標題>.md` | `src-2007-tango-the-book.md` |
| 計算範例 | `examples/` | `ex-<指標>-<聯盟>-<年>-<主題>.md` | `ex-woba-mlb-2024-weights.md` |
| 案例研究 | `case-studies/` | `cs-<主題>.md` | `cs-era-fip-gap-2023.md` |
| 比較 | `comparisons/` | `cmp-<a>-vs-<b>.md` | `cmp-drs-vs-oaa.md` |

- 符號轉換：`+` 寫成 `-plus`，`-` 寫成 `-minus`，`%` 寫成 `-pct`，例如 `era-minus.md`、`k-pct.md`。

---

## 5. 連結規則（Obsidian）

- 一律使用 `[[wikilink]]`，不使用 markdown 相對路徑連結。
- 顯示文字不同時用別名：`[[wrc-plus|wRC+]]`。
- 每個頁面至少要有 **1 個連入連結**與 **2 個連出連結**（剛建立的來源頁除外）。
- 指標第一次出現在某頁時要加連結，同一頁後續出現不必重複連結。
- 提到尚未建立的重要概念時，仍然加上 wikilink（留下紅連結），並在 Lint 時列為待建頁面。
- 圖片引用 `raw/assets/` 中的檔案：`![[檔名.png]]`。

---

## 6. 數學公式（LaTeX）

所有數學公式一律使用 LaTeX，語法須相容於 Obsidian 內建的 MathJax。

- 行內公式：`$...$`，例如 `$\text{wOBA}$`。
- 獨立公式：`$$...$$`，前後各空一行。
- 多步推導用 `aligned` 環境：

```latex
$$
\begin{aligned}
\text{wRAA} &= \frac{\text{wOBA} - \text{lgwOBA}}{\text{wOBA Scale}} \times \text{PA} \\
\text{wRC}  &= \text{wRAA} + \frac{\text{lgR}}{\text{PA}_{\text{lg}}} \times \text{PA}
\end{aligned}
$$
```

規則：
1. 多字母的指標名稱與變數用 `\text{}` 包起來，例如 `\text{BB}`、`\text{HR}`、`\text{lgwOBA}`，避免被當成相乘的單一字母。
2. 每個獨立公式下方必須附**變數說明**清單，逐一說明每個符號代表什麼、資料從哪裡來。
3. 有常數的公式（例如 wOBA 權重、FIP 常數、wOBA Scale）必須註明該常數**隨聯盟與球季而變**，並附上特定聯盟、特定年份的數值與出處。
4. 公式之後盡量附一個**代入數字的例子**，或連結到 `examples/` 的計算範例頁。
5. 不要在 frontmatter、檔名或標題中使用 LaTeX。
6. 不要用程式碼區塊或純文字表示公式（例如 `wOBA = (0.69*BB + ...)`）。

---

## 7. Frontmatter（Dataview）

每個 wiki 頁面（`index.md`、`log.md` 除外）開頭都必須有 YAML frontmatter。欄位名稱固定為英文，值盡量使用下列受控詞彙，Dataview 查詢才能一致。

### 7.1 共用欄位

```yaml
---
title: wOBA（加權上壘率）
type: metric            # metric | concept | source | example | case-study | comparison | overview
aliases: [wOBA, weighted On-Base Average, 加權上壘率]
domain: [batting]       # batting | pitching | fielding | baserunning | value | statcast | prospect | contract | method
leagues: [MLB]          # MLB | NPB | KBO | CPBL | MiLB | general
tags: [rate-stat, linear-weights]
sources: ["[[src-2007-tango-the-book]]"]
source_count: 1
status: draft           # stub | draft | stable | needs-review
created: 2026-11-23
updated: 2026-11-23
---
```

### 7.2 各類型的額外欄位

| 類型 | 額外欄位 |
|---|---|
| metric | `full_name`、`scale`（例如 `OBP-scale`、`100=avg`、`runs`、`wins`）、`upstream`（推導所依賴的指標或概念）、`downstream`（依賴此指標的指標）、`stabilization`（穩定所需樣本，可留空） |
| source | `source_type`（`article` / `paper` / `book` / `data` / `transcript` / `note`）、`author`、`publisher`、`published`、`url`、`raw_path`、`ingest_mode`（`discussed` / `batch`） |
| example | `metric`、`league`、`season`、`subject`（範例中使用的球員或情境） |
| case-study | `question`（要回答的問題）、`metrics_used`、`league`、`season` |
| comparison | `compared`（被比較的項目清單） |

### 7.3 規則

- `updated` 在每次修改頁面時更新。
- `source_count` 必須與 `sources` 清單長度一致。
- `upstream`、`downstream`、`sources` 的值使用帶引號的 wikilink，例如 `"[[woba]]"`，這樣 Obsidian 圖譜與 Dataview 都能辨識。

---

## 8. 頁面模板

### 8.1 指標頁（`metrics/`）

指標頁是本知識庫的核心，**必須寫到可以拿來推理的深度**。

```markdown
# wOBA（加權上壘率）

> 一句話定義：……

## 它在回答什麼問題
為什麼需要這個指標、它修正了舊指標的什麼缺點。

## 定義與公式
（LaTeX 獨立公式 + 變數說明）

## 推導過程
從第一原理一步步說明數字從哪裡來。
例如 wOBA：得分期望值矩陣（RE24）→ 各事件平均得分價值 → 減去出局價值 →
縮放到上壘率尺度（wOBA Scale）→ 最終權重。
每一步都要說明「為什麼這樣做」，不只是「做了什麼」。

## 推導鏈：上游與下游
- 上游：[[run-expectancy-matrix]]、[[linear-weights]]
- 下游：[[wraa]] → [[wrc]] → [[wrc-plus]]
用公式寫出從本指標轉換到下游指標的關鍵步驟。

## 聯盟與年份差異
各聯盟（MLB / NPB / KBO / CPBL）常數的差異、資料可取得性、計算來源。

## 如何解讀
尺度、聯盟平均值、好壞門檻（標註出處與年份）。

## 限制與常見誤用

## 不同觀點
（見第 10 節，來源有分歧時才寫）

## 範例
- [[ex-woba-mlb-2024-weights]]

## 相關頁面

## 來源
- [[src-...]]：引用的具體內容或頁碼
```

### 8.2 概念頁（`concepts/`）
結構：一句話定義 → 詳細說明（有公式就用 LaTeX）→ 在球員評估中的用途 → 相關指標 → 限制 → 不同觀點 → 來源。
例如：得分期望值矩陣、Linear Weights、Park Factor、聯盟環境調整、樣本穩定性（stabilization）、迴歸平均、MLE（Major League Equivalency）、替補水準（replacement level）。

### 8.3 來源摘要頁（`sources/`）
```markdown
# 〈來源標題〉

## 基本資訊
作者、出處、日期、原始檔位置：`raw/...`

## 核心論點
3～7 點，用自己的話改寫，不大段抄錄原文。

## 關鍵數據與公式
（LaTeX）

## 對 Wiki 的影響
- 新建頁面：[[...]]
- 更新頁面：[[...]]：更新了什麼
- 與既有內容的矛盾：[[...]]（見該頁「不同觀點」段落）

## 待追問的問題
```

### 8.4 計算範例頁（`examples/`）
1. **目標**：要算什麼。
2. **輸入資料**：表格列出原始數據，每個數字註明出處與擷取日期（例如「FanGraphs，2026-11-20 擷取」或 `raw/data/xxx.csv`）。
3. **使用的常數**：聯盟、年份、出處。
4. **逐步計算**：每一步都寫 LaTeX 公式並代入數字，展示中間結果。
5. **結果與驗證**：與 FanGraphs、Savant 等公開數值比對，有落差時說明原因（四捨五入、常數版本、資料修正等）。
6. **解讀**。
7. 連回對應的指標頁。

### 8.5 案例研究頁（`case-studies/`）
結構：問題 → 背景數據 → 用哪些指標分析、為什麼 → 分析過程 → 結論（可信度與限制）→ 不同觀點 → 來源。

### 8.6 比較頁（`comparisons/`）
以比較表為核心（方法、資料來源、尺度、優缺點、穩定性、取得難度），後面接說明段落。來源有分歧時依第 10 節並列呈現。

---

## 9. 多聯盟規則

- 任何數值、常數、門檻都必須標註**聯盟與球季**，例如「MLB 2024 年 wOBA Scale = 1.24（FanGraphs Guts!）」。
- 不同聯盟的數值不可直接比較，除非經過換算或標準化（例如 wRC+ 這類以聯盟平均為 100 的指標），並說明換算方法。
- 指標頁的「聯盟與年份差異」段落要說明：
  - 該聯盟是否有官方或公開來源提供此指標（例如 NPB 的 DELTA、KBO 的 Statiz、CPBL 的公開資料）。
  - 沒有現成數值時，自行計算需要哪些原始數據。
  - 追蹤數據（Statcast 類）在各聯盟的可取得程度。
- 跨聯盟換算（MLE、NPB 與 KBO 轉 MLB 等）建立專門的概念頁，並注意年代與樣本差異。

---

## 10. 矛盾與分歧處理

原則：**並列呈現、標註出處、不下結論**。

- 當不同來源對同一件事有不同說法（例如 DRS 和 OAA 對同一位球員的評價、不同 WAR 版本的 FIP 與 RA9 取捨、Stuff+ 的預測力），在相關頁面的 `## 不同觀點` 段落並列呈現：

```markdown
## 不同觀點

> [!note] 觀點 A：〈簡述〉
> 依據：……
> 來源：[[src-...]]

> [!note] 觀點 B：〈簡述〉
> 依據：……
> 來源：[[src-...]]

**分歧所在**：說明兩方是因為方法、資料、樣本還是定義不同而產生差異（只描述，不評判誰對）。
```

- 新來源推翻或修正舊說法時，**不刪除舊說法**，改為並列並註明時間先後。
- 在 frontmatter 加上 `needs-review` 狀態或 `contested` 標籤，方便 Lint 與 Dataview 追蹤。
- LLM 自己的推論必須和來源的說法明確區分，以 `> [!info] 推論` callout 標示。

---

## 11. 工作流程

### 11.1 Ingest（匯入來源）

匯入方式依來源類型而定：

| 來源類型 | 模式 | 做法 |
|---|---|---|
| 重要文章、論文、書籍章節、逐字稿 | **討論模式** | 先讀完來源，向使用者報告 3～7 個重點與預計更動的頁面，等使用者回覆後才寫入 |
| 數據檔、簡短文章、補充性資料 | **批次模式** | 直接處理並寫入，完成後列出變更清單供使用者檢查 |

不確定時，預設使用討論模式。使用者也可以直接指定模式。

步驟：
1. 讀取 `raw/` 中的來源（PDF 太長時分段讀取；有圖片時先讀文字，再查看重要圖片）。
2. （討論模式）報告重點並等待使用者回覆。
3. 在 `wiki/sources/` 建立來源摘要頁。
4. 更新或建立相關的指標、概念、比較頁（一個來源通常會影響 5～15 頁）。
5. 有矛盾時，依第 10 節處理。
6. 更新每個被修改頁面的 frontmatter（`sources`、`source_count`、`updated`）。
7. 更新 `wiki/index.md`。
8. 需要時更新 `wiki/overview.md`。
9. 在 `wiki/log.md` 追加紀錄。
10. git commit（見第 13 節）。

### 11.2 Query（查詢）

1. 先讀 `wiki/index.md` 找出相關頁面，再深入閱讀。
2. 回答時引用 wiki 頁面（`[[...]]`）。必要時回到 `raw/` 原文確認。
3. Wiki 中沒有足夠資訊時明確說明，並建議可補充的來源，不要用記憶填補而不標註。
4. 答案有長期價值時（比較、推導、案例分析），**詢問使用者是否存回 wiki**，同意後依對應類型建頁。
5. 輸出形式可以是 markdown 頁面、比較表、Marp 簡報（存 `outputs/slides/`）或圖表（存 `outputs/charts/`）。
6. 在 `log.md` 追加紀錄。

### 11.3 Lint（健康檢查）

使用者要求時執行，檢查以下項目並產出報告：

- 頁面之間互相矛盾，但尚未寫入「不同觀點」段落。
- 已被新來源取代的過時說法。
- 孤立頁面（沒有連入連結）。
- 紅連結（被提到但尚未建頁的概念）。
- frontmatter 缺欄位、`source_count` 不一致、`updated` 過舊。
- 公式沒有用 LaTeX，或缺少變數說明。
- 數值沒有標註聯盟與年份。
- 指標頁缺少「推導過程」或「推導鏈」段落。
- 建議接下來可以研究的問題與可補充的來源。

報告先給使用者看，經同意後才批次修正。

---

## 12. index.md 與 log.md

### index.md
- 依類型分區：指標（再依 domain 細分）、概念、比較、案例研究、計算範例、來源。
- 每一行格式：`- [[檔名|顯示名稱]] — 一句話摘要（來源數：N）`
- 每次 ingest 或新增頁面時都要更新。

### log.md
- **只追加，不修改舊紀錄。**
- 每筆紀錄格式固定，方便用 `grep "^## \[" wiki/log.md | tail -5` 解析：

```markdown
## [2026-11-23] ingest | The Book 第 1 章
- 模式：discussed
- 新建：[[src-2007-tango-the-book]]、[[run-expectancy-matrix]]
- 更新：[[woba]]（加入推導過程）
- 備註：……
```

- 類型限定為：`setup` | `ingest` | `query` | `lint` | `schema`（修改本文件）| `output`。

---

## 13. 版本控制（git）

- 整個資料夾是一個 git repo。
- 每完成一次 ingest、存回 wiki 的 query、lint 修正或 schema 修改，就做一次 commit。
- commit 訊息格式與 log 類型一致：`ingest: The Book ch.1`、`lint: fix orphan pages`、`schema: add LaTeX rules`。
- `raw/` 中的大型檔案（超過 50MB 的 PDF 或數據檔）先詢問使用者是否要納入版本控制。

---

## 14. 輸出（Marp 簡報與圖表）

- Marp 簡報存放在 `outputs/slides/<主題>.md`，frontmatter 加上 `marp: true`。內容取自 wiki，並在最後一頁列出引用的 wiki 頁面。
- 圖表存放在 `outputs/charts/`。產生圖表的程式放在 `scripts/`，以便重現。
- 輸出內容只是 wiki 的衍生品；有新的發現時，要回寫到 wiki 對應頁面。

---

## 15. 數據與正確性

- 所有數字都要能追溯到 `raw/` 中的檔案，或註明出處與擷取日期。
- 計算結果必須自行驗算。有程式可用時用程式計算，不要心算後直接寫入。
- 不憑記憶寫入具體數值（例如某年的 wOBA 權重）。沒有來源時，在頁面標記 `> [!warning] 待查證`，並把 `status` 設為 `needs-review`。
- 引用原文時以改寫為主，直接引用要簡短並標註出處。

---

## 16. 禁止事項

- 修改、移動或刪除 `raw/` 中的任何檔案。
- 刪除 wiki 頁面或 log 紀錄（需要合併或廢棄頁面時，先詢問使用者）。
- 把 LLM 的推論寫得像是來源的說法。
- 在沒有標註聯盟、年份與出處的情況下寫入數值或常數。
- 用非 LaTeX 的方式寫數學公式。
- 討論模式下，未經使用者回覆就寫入。
