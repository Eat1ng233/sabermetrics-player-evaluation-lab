---
title: 簡報規格：從 wOBA 到 wRC+
type: slide-spec
slug: woba-to-wrc-plus
version: v3
status: passed
updated: 2026-11-23
---

# 簡報規格：從 wOBA 到 wRC+

> 這是 SOP-04「整理重點與驗算」loop 的狀態檔。每一輪 loop 都更新這份檔案，再用 `spec_check.py` 判斷能否進入產生簡報的階段。

## 主題與讀者
- **主題**：wOBA 一路推導到 wRC+，含旁支 Batting Runs 與球場係數
- **讀者**：不熟悉賽伯計量學的初學者
- **主線**：得分期望值 → 線性權重 → wOBA → wRAA → wRC → wRC+（旁支：Batting Runs）

## 使用的 wiki 頁面
`metrics/woba`、`metrics/wraa`、`metrics/wrc`、`metrics/wrc-plus`、`metrics/batting-runs`、`metrics/re24`、`concepts/run-expectancy-matrix`、`concepts/linear-weights`、`concepts/park-factor`、`examples/ex-woba-mlb-2015-derivation`、`examples/ex-woba-mlb-2013-trout`、`examples/ex-wrc-plus-mlb-2012-trout`

## 頁面規劃
| 頁 | 模組 | 內容 |
|---|---|---|
| 1 | 封面 | 主線 |
| 2 | 路線圖 | 8 個模組 |
| 3 | 指標意義 | 5 個指標的問題、單位、平均、調整 |
| 4 | 流程圖 | 三列＋箭頭標籤 |
| 5–7 | 得分價值 | RE 定義、ΔRE、線性權重 |
| 8–12 | 逐步推導 | 出局 = 0、Scale、wRAA、wRC、wRC+ |
| 13–16 | 球場係數 | 三步驟、原始係數、減半與迴歸、新球場與限制 |
| 17 | 旁支 | Batting Runs |
| 18 | 結論 | 每一步加入一件事 |
| 19 | 原始數據 | Trout 2012、2013 |
| 20–22 | 範例 | 2012 wRC+、球場效果、2013 wOBA |
| 23 | 限制與延伸 | 6 個面板 |

## 符號表
| 符號 | 定義 | 出處 |
|---|---|---|
| RE(s) | 狀態 s 下到該局結束的平均得分 | run-expectancy-matrix |
| ΔRE | 結束狀態 RE − 開始狀態 RE + 該打席得分 | src-2014-weinberg-fangraphs-re24 |
| n_s | 狀態 s 出現的次數 | run-expectancy-matrix |
| x | 事件類型（uBB、1B、HR、出局…） | linear-weights |
| n_x | 該季事件 x 發生的總次數 | linear-weights |
| RV_x | 事件 x 的平均得分價值（線性權重） | linear-weights |
| RV*_x | 相對出局的得分價值 = RV_x − RV_out | woba |
| wOBA Scale | 聯盟 OBP（扣除 IBB）÷ 聯盟原始 wOBA | woba |
| w_x | wOBA 權重 = RV*_x × Scale | woba |
| lgwOBA | 同季 MLB 全體打者的 wOBA | woba |
| PA | 打席數 | woba |
| lgR/PA | MLB 總得分 ÷ 總打席 | wrc |
| PF | 球場係數（網站顯示值 ÷ 100，已減半與迴歸） | park-factor |
| H、R、T | 主場每場得分、客場每場得分、聯盟球隊數 | park-factor |
| iPF | 減半後的球場係數 | park-factor |
| X | 迴歸係數，依資料年數查表 | park-factor |
| wRC_lg / PA_lg | 所屬聯盟不含投手的野手 wRC／PA | wrc-plus |

## 數字表
| 數字 | 值 | 出處代碼 | 驗算 |
|---|---|---|---|
| Trout 2013 uBB | 100 | STD·13·BB − STD·13·IBB | ✓ verify.py |
| Trout 2013 分子 | 298.458 | GUTS 2013 × STD·13 | ✓ verify.py |
| Trout 2013 分母 | 706 | STD·13 | ✓ verify.py |
| Trout 2013 wOBA | .423 | ADV·13·wOBA | ✓ verify.py |
| Trout 2013 wRAA | 61.1 | ADV·13·wRAA | ✓ verify.py |
| Trout 2013 wRC | 140 | ADV·13·wRC | ✓ verify.py |
| Trout 2013 wRC+ | 176 | ADV·13·wRC+ | 無法驗算（缺 2013 年球場係數，FanGraphs 只提供 2016 年後） |
| Trout 2012 wRAA | 48.2 | ADV·12·wRAA | ✓ verify.py |
| Trout 2012 wRC | 121 | ADV·12·wRC | ✓ verify.py |
| Trout 2012 wRC+ | 167 | ADV·12·wRC+ | ✓ verify.py |
| 2012 無球場調整 wRC+ | 162 | 推論 | ✓ verify.py |
| 2012 Batting Runs | 49.97 | VAL·12·Batting | ✓ verify.py |
| 球場係數三步驟 | 1.093／1.046／1.042 | 假設數字 | ✓ verify.py |
| 迴歸表 | 1.15／1.175／1.20／1.225 | ART·PF5yr | ✓ verify.py |
| 顯示 95 的原始值 | 0.889 | 推論 | ✓ verify.py |
| ΔRE 三例 | .375／.925／.653 | RE 2010–15 | ✓ verify.py |
| wOBA Scale 2015 | 1.251 | ART·Deriving | ✓ verify.py |
| 2015 RV 表 | +0.29 … −0.26 | ART·Deriving | 無法驗算（需要 2015 年逐打席資料） |
| RE 矩陣 | 24 格 | ART·Deriving | 無法驗算（來源直接提供，非計算結果） |

## 推論清單
- 球隊實力在主場／客場相除時抵銷（P.14）
- 出局平移在兩個 wOBA 相減時抵銷（P.10）
- 顯示值 95 換回原始值 ≈ 0.889，假設 X = 0.9（P.21）
- Batting Runs 與 wRC+ 的換算式（P.17）

## 缺失清單
| 類別 | 項目 | 重要性 | 狀態 |
|---|---|---|---|
| 無法驗證的數字 | Trout 2013 wRC+ 176 缺球場係數 | 選擇性 | 接受（已在簡報註明） |
| 待確認的問題 | FanGraphs 現行是否仍用同一組 X | 選擇性 | 接受（已在簡報註明） |
| 無法驗證的數字 | 2015 聯盟原始 wOBA .250 | 選擇性 | 接受 |

## Loop 紀錄
| 輪 | 結果 | 處理 |
|---|---|---|
| v1 | 使用者回饋 13 點，多為定義不足 | 補符號表全部定義、RE 與 PF 計算頁 |
| v2 | 發現 PF 推論忽略迴歸 | 修正為 0.889，加入推論清單 |
| v3 | 球場係數討論 6 題回流 | 新增 P.13–16 |
| v3-check | spec_check 與 check.py 全部通過 | — |
