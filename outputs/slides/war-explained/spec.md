---
title: 簡報規格：WAR 是怎麼算出來的
type: slide-spec
slug: war-explained
version: v1
status: passed
content_approved: false
approval_note: 舊流程直接渲染，使用者尚未審閱內容；日後回來時先補毛片 draft.md
updated: 2026-11-23
---

# 簡報規格：WAR 是怎麼算出來的

## 主題與讀者
- **主題**：野手 WAR 的六個組成如何加總成 RAR，再換算成勝場；投手 WAR 概覽
- **讀者**：不熟悉賽伯計量學的初學者（看過或沒看過 wOBA → wRC+ 簡報皆可）
- **主線**：打擊、跑壘、守備、守位、聯盟、替補 → RAR → ÷ RPW → WAR

## 使用的 wiki 頁面
`metrics/war`、`metrics/war-position-players`、`metrics/war-pitchers`、`metrics/batting-runs`、`metrics/bsr`、`concepts/positional-adjustment`、`concepts/replacement-level`、`concepts/runs-per-win`、`concepts/park-factor`、`examples/ex-war-mlb-2012-trout`

## 頁面規劃
| 頁 | 模組 | 內容 |
|---|---|---|
| 1 | 封面 | 主線 |
| 2 | 路線圖 | 模組面板 |
| 3 | WAR 在回答什麼 | 定義、單位、解讀尺度 |
| 4 | 流程圖 | 六個組成 → RAR → ÷ RPW → WAR；投手分支 |
| 5 | 替補水準 | 為什麼不用平均、1,000 WAR、.294、分歧 |
| 6 | 打擊 | Batting Runs |
| 7 | 跑壘 | BsR = UBR + wSB + wGDP |
| 8 | 守備與守位 | UZR、捕手、守位調整表 |
| 9 | 聯盟與替補得分 | 兩個公式 |
| 10 | RPW | 得分換勝場 |
| 11 | 投手 WAR | 九步流程概覽 |
| 12 | 結論 | 每個組成回答什麼 |
| 13 | 原始數據 | Trout 2012、2013 Value 表與守備局數 |
| 14 | 範例 1 | Trout 2012 逐項拆解 |
| 15 | 範例 2 | Trout 2013：守位調整對不上 |
| 16 | 限制與誤解 | 面板 |

## 符號表
| 符號 | 定義 | 出處 |
|---|---|---|
| WAR | 比替補球員多贏的勝場 | war |
| RAR | 比替補球員多創造的得分 = 六個組成加總 | war-position-players |
| RPW | 每多贏一場需要的得分 | runs-per-win |
| Batting | 經球場與聯盟調整的 wRAA | batting-runs |
| wRAA | 比聯盟平均打者多創造的得分 | wraa |
| PF | 球場係數（網站顯示值 ÷ 100） | park-factor |
| BsR | 跑壘得分 = UBR + wSB + wGDP | bsr |
| Fielding | 相對同守位平均的守備得分（UZR；捕手 rSB + RPP） | war-position-players |
| Positional | 守位調整 = 守備局數 ÷ 9 ÷ 162 × 守位得分值 | positional-adjustment |
| League | 讓各聯盟高於平均得分總和為 0 的調整 | war-position-players |
| Replacement | 替補水準得分 = 570 × 場次比例 × RPW ÷ lgPA × PA | replacement-level |
| lgPA | 該季 MLB 總打席 | replacement-level |
| Inn | 守備局數 | positional-adjustment |
| ifFIP | 把內野高飛球算成三振的 FIP | war-pitchers |
| dRPW | 投手專屬的動態每勝得分 | war-pitchers |
| gmLI | 後援投手登板時的平均槓桿 | war-pitchers |

## 數字表
| 數字 | 值 | 出處代碼 | 驗算 |
|---|---|---|---|
| 替補球隊勝場 | 1430 → 每隊 47.7 | ART·WAR | ✓ verify.py |
| 替補勝率 | .294 | ART·WAR | ✓ verify.py |
| 野手份額 | 570 WAR | ART·WARpp | ✓ verify.py |
| 2012、2013 R/9 | 4.363、4.176 | 推論 | ✓ verify.py |
| RPW 表 2010–2015 與 R/9 | 9.643 … 9.421；4.43 … 4.28 | GUTS → 推論 | ✓ verify.py |
| 2013 runCS | −0.384 | GUTS 2013 → 推論 | ✓ verify.py |
| 2012 Positional 分項 | −1.69、+1.52、−0.06 | PDF·FLD·12 | ✓ verify.py |
| 2012 球場調整、聯盟調整 | +3.64、−1.87 | ART·wRC | ✓ verify.py |
| 2012 Batting | 49.97（FG 50.1） | VAL·12·Batting | ✓ verify.py |
| 2012 Positional | −0.23（FG −0.2） | PDF·FLD·12 | ✓ verify.py |
| 2012 Off、Def | 64.4、10.2 | VAL·12 | ✓ verify.py |
| 2012 RAR、WAR | 96.1、10.1 | VAL·12 | ✓ verify.py |
| 2012 lgPA | ≈ 183,900 | 推論 | ✓ verify.py |
| 2013 RAR、WAR | 94.0、10.1 | VAL·13 | ✓ verify.py |
| 2013 Positional | 只算 LF + CF = −0.20（FG −1.2） | PDF·FLD·13 | ✓ verify.py |
| 2013 推論 DH 局數 | ≈ 83.5 局（約 9.3 場） | 推論 | ✓ verify.py |
| 守位調整表 | C +12.5 … DH −17.5 | ART·WARpp | 無法驗算（來源直接提供的常數） |
| 投手替補水準 | 先發 0.12、後援 0.03 | ART·WARp | 無法驗算（來源直接提供的常數） |
| 2012 Fielding、BsR、League | 10.4、14.3、2.7 | VAL·12 | 無法驗算（需 BIS 資料或聯盟總和） |

## 推論清單
- 替補球隊每隊約 47.7 勝（由 1,000 WAR 換算）
- 由 RPW 反推 R/9
- 由替補得分反推 2012 MLB 總打席
- 2013 守位調整差距來自指定打擊出賽

## 缺失清單
| 類別 | 項目 | 重要性 | 狀態 |
|---|---|---|---|
| 缺少的解釋 | FIP 沒有 wiki 頁面，投手 WAR 只能做概覽 | 選擇性 | 接受（P.11 標示待補） |
| 缺少的解釋 | UZR、DRS 沒有 wiki 頁面 | 選擇性 | 接受 |
| 缺少的數據 | Trout 2013 指定打擊出賽局數 | 選擇性 | 未解決 |
| 待確認的問題 | 替補球隊 43 勝 vs .294 | 選擇性 | 接受（P.5 並列） |
| 待確認的問題 | FanGraphs 現行守備是否改用 OAA／FRV、捕手是否含 framing | 選擇性 | 接受（P.16 標示） |

## Loop 紀錄
| 輪 | 結果 | 處理 |
|---|---|---|
| 1 | 18/19，「2013 DH 局數」規格寫 75.4，實算 83.5 | 改用實算值；spec_check 改為列出失敗項目 |
| 2 | 19/19 通過 | 進入 N4 |
| 3（由 N4 退回） | 撰寫時新增 RPW 表、R/9、runCS、守位分項，共 11 個數字不在規格中 | 補進數字表與 verify.py，29/29 通過 |
| N6-1 | 自動檢查通過；目視發現 \tfrac 字太小 | 改 \dfrac；build.js 新增禁用 \tfrac |
| N6-2 | 自動與目視皆通過 | 交付 v1 |
