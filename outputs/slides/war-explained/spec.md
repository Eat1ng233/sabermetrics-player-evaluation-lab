---
title: 簡報規格：WAR 是怎麼算出來的
type: slide-spec
slug: war-explained
version: v4
status: draft-delivered
content_approved: false
approval_note: 等待使用者審閱毛片 draft.md（d3）
updated: 2026-11-24
---

# 簡報規格：WAR 是怎麼算出來的

> SOP-04 v1.2（先交毛片、確認後才渲染）的狀態檔。舊版（v1.1 流程直接渲染）已由使用者要求刪除，本版從 N1 重新執行。

## 主題與讀者
- **主題**：野手 WAR 的六個組成如何加總成 RAR，再換算成勝場；投手 WAR 概覽
- **讀者**：不熟悉賽伯計量學的初學者
- **主線**：打擊、跑壘、守備、守位、聯盟、替補 → RAR → ÷ RPW → WAR

## 使用的 wiki 頁面
`metrics/war`、`metrics/war-position-players`、`metrics/war-pitchers`、`metrics/batting-runs`、`metrics/bsr`、`metrics/uzr`、`metrics/drs`、`metrics/fip`、`concepts/positional-adjustment`、`concepts/replacement-level`、`concepts/runs-per-win`、`concepts/park-factor`、`examples/ex-war-mlb-2012-trout`

## 頁面規劃
| 頁 | 模組 | 內容 |
|---|---|---|
| 1 | 封面 | 主線 |
| 2 | 路線圖 | 模組面板 |
| 3 | WAR 在回答什麼 | 定義、單位、解讀尺度 |
| 4 | 流程圖 | 六個組成 → RAR → ÷ RPW → WAR；投手分支 |
| 5 | 替補水準 | 為什麼不用平均、1,000 WAR、.294、2013 年統一 |
| 6 | 打擊 | Batting Runs |
| 7 | 跑壘 | BsR = UBR + wSB + wGDP；2016 起 XBR |
| 8 | 守備 | UZR 四個組成、接球計算例、2016 起 Statcast |
| 9 | 捕手與 DRS | rSB + RPP、framing、DRS 組成、DRS vs UZR |
| 10 | 守位調整 | 守位表、Def = Fielding + Positional |
| 11 | 聯盟與替補得分 | 兩個公式；全大聯盟總和驗算 |
| 12 | RPW | 得分換勝場 |
| 13 | FIP | DIPS、公式、常數、評級 |
| 14 | 投手 WAR | 九步流程概覽；framing 調整 |
| 15 | 結論 | 每個組成回答什麼 |
| 16 | 原始數據 | Trout Value 表、守備局數、逐場紀錄、聯盟總和 |
| 17 | 範例 1 | Trout 2012 逐項拆解；League、Replacement 驗算；17.6 差距 |
| 18 | 範例 2 | Trout 2013：DH 9 場補上守位調整 |
| 19 | 限制與誤解 | 面板；方法更新時間線 |

## 符號表
| 符號 | 定義 | 出處 |
|---|---|---|
| WAR | 比替補球員多贏的勝場 | war |
| RAR | 比替補球員多創造的得分 = 六個組成加總 | war-position-players |
| RPW | 每多贏一場需要的得分 | runs-per-win |
| R/9 | 聯盟每九局得分（得分環境） | runs-per-win |
| Batting | 經球場與聯盟調整的 wRAA | batting-runs |
| wRAA | 比聯盟平均打者多創造的得分 | wraa |
| PF | 球場係數（網站顯示值 ÷ 100） | park-factor |
| BsR | 跑壘得分 = UBR + wSB + wGDP | bsr |
| runSB、runCS | 盜壘成功、失敗的得分價值 | bsr |
| lgwSB | 聯盟平均每次上一壘的盜壘得分 | bsr |
| Fielding | 相對同守位平均的守備得分（UZR；捕手 rSB + RPP；2016 起 Statcast） | war-position-players |
| UZR | ARM + DPR + RngR + ErrR，相對同守位平均的守備得分 | uzr |
| v、p | 一類擊球沒被接到的平均得分、平均守備員的接殺機率 | uzr |
| Def | Fielding + Positional | uzr |
| XBR | Statcast 跑壘指標（2016 起取代 UBR、wGDP） | bsr |
| FIP | 只用 HR、BB、HBP、K 估計的 ERA | fip |
| Framing | 捕手偷好球換成的得分（相對平均），2019 起計入 WAR | war-position-players |
| DRS | rSB + rBU + rGDP + rARM + rHR + rPM，Fielding Bible 的守備救分 | drs |
| RPP | 捕手防止暴投、捕逸的得分 | war-position-players |
| C | FIP 常數：讓聯盟平均 FIP ＝ 聯盟平均 ERA | fip |
| Positional | 守位調整 = 守備局數 ÷ 9 ÷ 162 × 守位得分值 | positional-adjustment |
| Inn | 守備局數 | positional-adjustment |
| League | 讓各聯盟高於平均得分總和為 0 的調整 | war-position-players |
| Replacement | 替補水準得分 = 570 × 場次比例 × RPW ÷ lgPA × PA | replacement-level |
| lgPA | 該季 MLB 總打席 | replacement-level |
| ifFIP | 把內野高飛球算成三振的 FIP | war-pitchers |
| dRPW | 投手專屬的動態每勝得分 | war-pitchers |
| gmLI | 後援投手登板時的平均槓桿 | war-pitchers |

## 數字表
| 數字 | 值 | 出處代碼 | 驗算 |
|---|---|---|---|
| 替補球隊勝場 | 1430 → 每隊 47.7 | ART·WAR | ✓ verify.py |
| 替補勝率 | .294 | ART·WAR | ✓ verify.py |
| 43 勝的勝率 | .265 | ART·Misc | ✓ verify.py |
| 野手份額 | 570 WAR | ART·WARpp | ✓ verify.py |
| 2013 runCS | −0.384 | GUTS 2013 → 推論 | ✓ verify.py |
| RPW 表 2010–2015 與 R/9 | 9.643 … 9.421；4.43 … 4.28 | GUTS → 推論 | ✓ verify.py |
| 2012 球場調整、聯盟調整 | +3.64、−1.87 | ART·wRC | ✓ verify.py |
| 2012 Batting | 49.97（FG 50.1） | VAL·12·Batting | ✓ verify.py |
| 2012 Positional 分項與合計 | −1.69、+1.52、−0.06；−0.23（FG −0.2） | PDF·FLD·12 | ✓ verify.py |
| 2012 Off、Def | 64.4、10.2 | VAL·12 | ✓ verify.py |
| 2012 RAR、WAR | 96.1、10.1 | VAL·12 | ✓ verify.py |
| 2012 lgPA | ≈ 183,900（推論）；實際 184,179 | 推論 → LDR·MLB12S | ✓ verify.py |
| 2012 Replacement | 570 × 9.544 ÷ 184179 × 639 ＝ 18.87 | LDR·MLB12S | ✓ verify.py |
| 2012 MLB 場次、R | 2430（TG 4860 ÷ 2）、21,017 | LDR·MLB12S | ✓ verify.py |
| 替補水準歷史 | .265 ≈ 43 勝、.320 ≈ 52 勝、.294 ＝ 47.7 勝；628 位中 1 人低於 0 | ART·RL13 → 推論 | ✓ verify.py（628 位為來源數字，無法驗算） |
| Greinke framing 例 | 3.00 ＋ 0.31 ＝ 3.31 | ART·FRM19 | ✓ verify.py |
| framing 影響 | McCann ＋18.8、Doumit −16.1 | ART·FRM19 | 無法驗算（來源直接提供的數字） |
| DRS 組成與 rHR 1.6 分 | — | ART·DRS | 無法驗算（來源直接提供的數字） |
| 2013 RAR、WAR | 94.0、10.1 | VAL·13 | ✓ verify.py |
| 2013 Positional | 只算 LF + CF = −0.20（FG −1.2） | PDF·FLD·13 | ✓ verify.py |
| 2013 推論 DH | ≈ 83.5 局（約 9.3 場） | 推論 | ✓ verify.py |
| 2013 逐場紀錄 | 157 場、PA 716；DH 9 場 | LOG·13 | ✓ verify.py |
| 2013 Positional（含 DH） | −0.20 − 0.97 = −1.17 | LOG·13 + PDF·FLD·13 | ✓ verify.py |
| 2012 League（分攤） | 357.2 ÷ 85797 × 639 = 2.66 | LDR·AL12 | ✓ verify.py |
| 2012 League（文章公式）與差距 | 339.6 → 2.53；差 17.6 | LDR·AL12 → 推論 | ✓ verify.py |
| 2012 全大聯盟總和 | −815.9、+1.0、+16.6、+353.8、444.5 → 0；5440.2 ＝ 570 × 9.544；WAR 570 | LDR·MLB12 | ✓ verify.py |
| UZR 計算例 | 0.48；−0.32；期望值 0 | ART·UZR → 推論 | ✓ verify.py |
| UZR 評級 | +15 … −15 | ART·UZR | 無法驗算（來源直接提供的常數） |
| FIP 係數、常數、評級 | 13、3、2；≈ 3.10；3.20 … 5.00 | ART·FIP | 無法驗算（來源直接提供的常數） |
| 守位調整表 | C +12.5 … DH −17.5 | ART·WARpp | 無法驗算（來源直接提供的常數） |
| 投手替補水準 | 先發 0.12、後援 0.03 | ART·WARp | 無法驗算（來源直接提供的常數） |
| 2012 BsR、Fielding | 14.3、10.4 | VAL·12 | 無法驗算（需 BIS 資料） |

## 推論清單
- 替補球隊每隊約 47.7 勝（由 1,000 WAR 換算）；43 勝約為 .265
- 由 RPW 反推 R/9；runCS 的負號
- 由替補得分反推 2012 MLB 總打席
- 2013 守位調整差距來自指定打擊出賽（已由 LOG·13 證實）
- UZR 沒接到的扣分與期望值 0
- FIP 係數約為「事件相對場內球的失分 × 9」
- 美聯 League 差 17.6 的兩個假說：投手打擊、捕手 framing
- .320 換算約 52 勝
- DRS 寫成加總公式；捕手 WAR 公式中的「⋯」

## 缺失清單
| 類別 | 項目 | 重要性 | 狀態 |
|---|---|---|---|
| 缺少的數據 | Trout 2013 指定打擊出賽（P.18） | 選擇性 | 已解決：DH 9 場，Positional −1.17 ≈ −1.2（LOG·13） |
| 缺少的數據 | 2012 MLB 總打席（驗證 P.17 的 Replacement 18.9） | 選擇性 | 已解決：lgPA ＝ 184,179，Trout Replacement 算出 18.87 ≈ 18.9（LDR·MLB12S） |
| 缺少的數據 | 2012 美聯野手 Value 總和（P.17 League） | 選擇性 | 已解決：分攤得 2.66 ≈ 2.7（LDR·AL12） |
| 待確認的問題 | 美聯 League 357.2 比文章公式 339.6 多 17.6（P.17） | 選擇性 | 接受（使用者確認）：兩個假說標示「推論」並列 |
| 缺少的解釋 | FIP 沒有 wiki 頁面（P.13、P.14） | 選擇性 | 已解決：新增 fip.md、P.13 |
| 缺少的解釋 | UZR 沒有 wiki 頁面（P.8） | 選擇性 | 已解決：新增 uzr.md、P.8 |
| 待確認的問題 | 替補球隊 43 勝 vs .294（P.5） | 選擇性 | 已解決：2013 年統一替補水準，43 勝是統一前的 .265（ART·RL13） |
| 待確認的問題 | 捕手 framing 是否計入（P.9、P.14、P.19） | 選擇性 | 已解決：2019 年起計入（ART·FRM19） |
| 缺少的解釋 | DRS 沒有 wiki 頁面（P.9） | 選擇性 | 已解決：新增 drs.md、P.9 |

## Loop 紀錄
| 輪 | 結果 | 處理 |
|---|---|---|
| N2-1 | 29/29 通過；7 筆選擇性缺失帶入毛片 | 進入 N3 |
| N3 | --draft 通過（16 頁、兩個必要段落都在） | 交付毛片，等待使用者審閱 |
| N2-2 | 使用者補上 6 份檔案；新增 10 項驗算，39/39 通過；2 筆已解決、新增 1 筆待確認 | 回報使用者；文章待同意後匯入，再出毛片 d2 |
| N2-3 | 使用者同意匯入 FIP、UZR；補上全大聯盟 Value 總和；新增 7 項驗算，46/46 通過；頁面 16 → 18 | 進入 N3 |
| N3 d2 | --draft 通過（18 頁） | 交付毛片 d2，等待使用者審閱 |
| N2-4 | 使用者補上 2012 總打席與 3 篇文章；新增 5 項驗算，51/51 通過；總打席已解決 | 文章待同意後匯入，再出毛片 d3 |
| N2-5 | 使用者同意匯入 3 篇文章；新增 3 項驗算，54/54 通過；頁面 18 → 19；缺失只剩 1 筆 | 進入 N3 |
| N3 d3 | --draft 通過（19 頁） | 交付毛片 d3，等待使用者審閱 |
