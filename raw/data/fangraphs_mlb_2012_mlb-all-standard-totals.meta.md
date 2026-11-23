# fangraphs_mlb_2012_mlb-all-standard-totals.csv — 2012 全大聯盟打擊總和（Standard／Dashboard）

## 來源
- **來源網址**：https://www.fangraphs.com/leaders/major-league?pos=all&stats=bat&type=8&season=2012（All Leagues、All Positions、例行賽、Min PA 0）
- **擷取日期**：2026-11-24（頁面更新時間 2026-11-23 10:45 AM ET）
- **提供方式**：使用者列印成 PDF，原檔保留為 `raw/data/fangraphs_mlb_2026-11-24_leaderboard-2012-mlb-all-standard.pdf`
- **轉換方式**：表格只有一列，人工逐欄抄錄後以程式檢查；xwOBA 欄空白（2012 年沒有 Statcast），不收錄

## 欄位說明
| 欄位 | 說明 |
|---|---|
| TG | 球隊出賽總數（每場比賽算兩次）；TG ÷ 2 ＝ MLB 場次 |
| G / PA | 球員出賽數總和 / 總打席 |
| 其餘 | 同 Trout 的 standard、advanced、value 表 |

## 清理與檢查
- TG 4860 ÷ 2 ＝ 2430 場 ✓（完整球季）
- R ÷ PA ＝ 21017 ÷ 184179 ＝ .1141 ≈ GUTS 2012 lgR/PA .114 ✓
- BsR、Off、Def、WAR 與 `fangraphs_mlb_2012_mlb-all-value-totals.csv` 一致 ✓
- 用途：2012 MLB 總打席 lgPA ＝ 184,179（之前由替補得分反推約 183,900，誤差 0.15%）
