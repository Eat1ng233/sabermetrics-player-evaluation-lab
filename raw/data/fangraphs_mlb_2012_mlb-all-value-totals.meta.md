# fangraphs_mlb_2012_mlb-all-value-totals.csv — 2012 全大聯盟 Value 總和（含投手打擊）

## 來源
- **來源網址**：https://www.fangraphs.com/leaders/major-league?pos=all&stats=bat&type=6&season=2012（Value 頁籤，All Leagues，All Positions，例行賽，Min PA = 0）
- **擷取日期**：2026-11-24
- **提供方式**：使用者列印成 PDF，原檔保留為 `raw/data/fangraphs_mlb_2026-11-24_leaderboard-2012-mlb-all-value.pdf`
- **轉換方式**：表格只有一列，人工逐欄抄錄後以程式檢查

## 欄位說明
同 `fangraphs_mlb_2012_al-nonpitchers-value-totals.csv`；`Scope = All Positions` 表示包含投手的打擊。

## 清理與檢查
- Batting + Base Running + Fielding + Positional + League Adj = 0.0 ✓（聯盟調整讓全大聯盟高於平均的得分剛好抵銷）
- Replacement 5440.2 = 570 × RPW(9.544) = 5440.1 ✓（全聯盟替補得分 = 570 WAR 換成得分）
- RAR = Replacement；WAR = 570.0 ✓
- **沒有 PA 欄位**：這是 Value 頁籤。原本要的「2012 MLB 總打席」需要 Standard 頁籤（`type=8`）的同樣篩選。
