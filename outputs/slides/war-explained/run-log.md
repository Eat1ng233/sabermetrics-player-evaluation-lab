---
title: 執行紀錄：做簡報「WAR 是怎麼算出來的」（SOP-04 v1.2）
type: run-log
slug: war-explained
date: 2026-11-23
graph: SOP.md › SOP-04 v1.2（先交毛片、確認後才渲染）
result: 已交付毛片，停在「🛑 使用者審閱毛片」；尚未渲染
---

# 執行紀錄：做簡報「WAR 是怎麼算出來的」

> 依 `SOP.md` 的 SOP-04 v1.2 執行。舊版（v1.1 流程，直接渲染）已依使用者要求刪除，本次從 N1 重新開始。原始輸出存在 `evidence/`。

## 1. 執行資訊

| 項目 | 內容 |
|---|---|
| 輸入 | 「做簡報：WAR 是怎麼算出來的」 |
| 流程版本 | SOP-04 v1.2 |
| 使用的 wiki 頁面 | war、war-position-players、war-pitchers、batting-runs、bsr、positional-adjustment、replacement-level、runs-per-win、park-factor、ex-war-mlb-2012-trout |
| 使用的數據 | `raw/data/fangraphs_mlb_2011-2026_trout-{standard,advanced,value}.csv`、球員頁 PDF 的 Fielding 表 |
| 目前產出 | `spec.md`（19 符號、18 筆數字）、`verify.py`（29 項斷言）、`draft.md`（16 頁毛片） |
| 目前狀態 | ⏸ 等待使用者審閱毛片；`content_approved: false` |

## 2. 實際走過的路徑

```
N1 範圍界定（不停下，缺口帶入缺失清單）
 → N2 第 1 輪 ✓ 29/29
 → N3 毛片 → 毛片關卡 ✓
 → 🛑 使用者審閱毛片  ← 目前位置
    （渲染關卡、build.js 已確認會擋下未確認的內容）
```

## 3. 逐節點紀錄

| # | 節點 | 做了什麼 | 結果 | 證據 |
|---|---|---|---|---|
| 1 | **N1 範圍界定** | 讀 `index.md` 與 `raw/`。野手 WAR 主線頁面齊全；缺口：FIP、UZR 無頁面，替補水準有來源分歧，`raw/` 沒有 2012 MLB 總打席、2012 美聯野手總和、Trout 2013 DH 出賽 | 依 v1.2 規則**不停下**，7 個缺口帶入缺失清單 | — |
| 2 | **N2 第 1 輪** | 寫 `spec.md` 與 `verify.py` | ✅ **29/29**；7 筆選擇性缺失列為「未解決」帶入毛片 | `evidence/n2-round1_spec_check.txt` |
| 3 | **N3 毛片** | 依 `draft_template.md` 撰寫 16 頁完整內容；缺失清單標出影響頁數與目前處理方式；需要補充的資料寫明取得路徑、格式、存放位置 | — | `draft.md` |
| 4 | **N3 毛片關卡** | `spec_check.py --draft` | ✅ 16 頁都有內容；「缺失清單」、「需要補充的資料」兩節都在 | `evidence/n3_draft_check.txt` |
| 5 | **確認關卡驗證** | 在使用者確認前，試跑渲染關卡與建置 | ✅ 如預期被擋下：`--render` 列出 8 項原因（未確認＋7 筆未解決）；`build.js` 拒絕建置 | `evidence/n4_render_gate_blocked.txt`、`evidence/n5_build_blocked.txt` |
| 6 | **🛑 使用者審閱毛片** | 使用者回覆：上傳毛片第 2 節要求的 6 份檔案 | ▶ 回到 SOP-01／02 匯入 | — |
| 7 | **SOP-02 匯入資料** | 逐場紀錄轉 CSV（157 場，PA 716、H 190 等 9 項與 Total 列完全相符）；美聯 Value 總和轉 CSV；季後賽 PA 表只保留原檔並標註不可用 | 2 份可用、1 份需重新匯出 | `raw/data/*.meta.md` |
| 8 | **N2 第 2 輪** | `verify.py` 新增 10 項；缺失清單更新（2 筆已解決、1 筆新增） | ✅ **39/39**；spec_check 通過 | `evidence/n2-round2_spec_check.txt` |
| 9 | **SOP-01 文章（討論模式）** | 2024 WAR 更新、UZR、FIP 三篇存入 `raw/articles/`，重點回報使用者 | 使用者同意寫入 FIP、UZR | — |
| 10 | **SOP-01 寫入 wiki** | 新增 `fip.md`、`uzr.md`、3 個來源頁；更新野手 WAR、BsR、投手 WAR、index（含「不同觀點」：UZR vs Statcast） | — | `wiki/log.md` |
| 11 | **SOP-02 匯入資料** | 使用者重新匯出的檔案是 Value 頁籤（全大聯盟、例行賽），沒有 PA 欄；轉成 CSV＋meta | 五項加總 0.0 ✓、替補 ＝ 570 × RPW ✓；總打席仍缺 | `raw/data/fangraphs_mlb_2012_mlb-all-value-totals.meta.md` |
| 12 | **N2 第 3 輪** | `verify.py` 新增 7 項；spec 頁面 16 → 18、符號 +7、數字 +9 | ✅ **46/46**；spec_check 通過 | `evidence/n2-round3_spec_check.txt` |
| 13 | **N3 毛片 d2** | 新增 P.8 UZR、P.12 FIP；P.16 League 已驗算＋17.6 差距；P.17 DH 9 場 | ✅ `--draft` 通過；`--render` 如預期擋下（未確認＋5 筆未解決） | `evidence/n3-d2_draft_check.txt`、`evidence/n4-d2_render_gate_blocked.txt` |
| 14 | **🛑 使用者審閱毛片 d2** | 使用者回覆：上傳 2012 總打席與 3 篇文章（替補水準統一、DRS、捕手 framing） | ▶ 回到 SOP-01／02 | — |
| 15 | **SOP-02 匯入資料** | Standard 頁籤總和轉 CSV＋meta：lgPA 184,179 | ✅ Trout Replacement 18.87 ≈ 18.9 | `raw/data/fangraphs_mlb_2012_mlb-all-standard-totals.meta.md` |
| 16 | **N2 第 4 輪** | `verify.py` 新增 5 項；缺失「2012 MLB 總打席」改為已解決 | ✅ **51/51**；spec_check 通過 | `evidence/n2-round4_spec_check.txt` |
| 17 | **SOP-01 文章（討論模式）** | 3 篇存入 `raw/articles/`，重點回報使用者 | 使用者同意寫入 | — |
| 18 | **SOP-01 寫入 wiki** | 新增 `drs.md` 與 3 個來源頁；更新替補水準（分歧改為時間先後，移除 needs-review）、野手 WAR、投手 WAR、UZR、WAR、index | — | `wiki/log.md` |
| 19 | **N2 第 5 輪** | `verify.py` 新增 3 項；spec 頁面 18 → 19；缺失 9 筆中 8 筆已解決 | ✅ **54/54**；spec_check 通過 | `evidence/n2-round5_spec_check.txt` |
| 20 | **N3 毛片 d3** | 新增 P.9 捕手與 DRS；P.5 替補水準歷史；P.14 framing；P.17 Replacement 已驗算＋17.6 兩個假說；P.19 方法更新時間線 | ✅ `--draft` 通過；`--render` 擋下（未確認＋1 筆未解決） | `evidence/n3-d3_draft_check.txt`、`evidence/n4-d3_render_gate_blocked.txt` |
| 21 | **🛑 使用者審閱毛片 d3** | 使用者接受缺失 #4（17.6 差距標示推論）；確認欄第 2、3 項勾選；內容確認（第 1 項）使用者表示還要再看 | ⏸ 等待內容確認 | — |
| 22 | **確認** | 使用者回覆「確認，開始渲染」→ `content_approved: true` | ✅ `--render` 通過（0 筆未處理） | `evidence/n4-d3_render_gate_passed.txt` |
| 23 | **N4 撰寫 src.html** | 依 d3 逐頁撰寫 19 頁，套用 template.html | — | `src.html` |
| 24 | **N5／N6 第 1 輪** | build 通過；check.py 19/19 通過；目視發現 P.4「第 2 步」標籤被裁掉、P.17 公式偏小 | ❌ 目視未通過 | `evidence/n6-round1_check.json` |
| 25 | **R 規則回寫** | `check.py` 新增 `fo_clip`（foreignObject 內容被裁掉）；用第 1 輪成品測試 → 擋下 P.4；SOP 版面規則新增一條 | ✅ 規則生效 | `evidence/r-check-fo-clip-test.json` |
| 26 | **N5／N6 第 2 輪** | 放寬標籤框、放大公式 | ✅ build、check.py 19/19、目視通過 | `evidence/n5-round2_build.txt`、`evidence/n6-round2_check.json` |
| 27 | **N7 交付** | `outputs/slides/war-explained.html`（19 頁，511 KB，可離線） | ✅ | — |
| 28 | **🛑 N8 使用者審閱成品** | 等待回饋 | ⏸ | — |

## 4. 和 v1.1 執行的差別

| | v1.1（已刪除） | v1.2（本次） |
|---|---|---|
| 使用者第一次看到的東西 | 渲染好的 16 頁簡報 | 毛片：逐頁內容＋缺失清單＋需要補充的資料 |
| 缺失怎麼告知 | 散在簡報各頁的「待補」與交付訊息中 | 集中在毛片第 1、2 節，標出影響哪幾頁與取得方式 |
| 內容有問題時 | 要重新渲染 | 只改毛片，不必渲染 |
| 「確認後才渲染」 | 靠 agent 自律 | 由 `spec_check.py --render` 與 `build.js` 強制 |

本次 N2 第 1 輪即通過，原因是沿用了 v1.1 執行中被關卡擋下兩次（推論數字寫成估計值、撰寫時新增未驗證數字）後修正的計算邏輯。

## 5. 下一步（已完成至 N7）

1. 使用者審閱 `draft.md`：回覆內容修改、提供第 2 節的資料，或接受目前的處理方式。
2. 有資料 → SOP-02 匯入 → 回 N2；有內容修改 → 規則回寫 → 回 N2。
3. 確認後：`content_approved: true`、缺失狀態更新 → `spec_check.py --render` → N4–N6 渲染 loop → N7 交付 → N8。
