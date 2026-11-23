# fangraphs_mlb_2012_al-nonpitchers-value-totals.csv — 2012 美聯野手 Value 總和

## 來源
- **來源網址**：https://www.fangraphs.com/leaders/major-league?stats=bat&lg=al&qual=y&type=6&season=2012（Value 頁籤，Non-Pitchers，例行賽，不分隊）
- **擷取日期**：2026-11-23（頁面更新時間 2026-11-23 10:45 AM ET）
- **提供方式**：使用者列印成 PDF，原檔保留為 `raw/data/fangraphs_mlb_2026-11-23_leaderboard-2012-al-nonpitchers-value.pdf`
- **轉換方式**：表格只有一列，人工逐欄抄錄後再以程式檢查

## 欄位說明
欄位與 trout-value.csv 相同；為避免和 `League`（聯盟）混淆，聯盟調整欄改名為 `League Adj`。`Scope` 標示範圍為非投手。

## 清理與檢查
- RAR = Batting + Base Running + Fielding + Positional + League Adj + Replacement = 2551.9 ✓
- WAR = RAR ÷ RPW(2012 = 9.544) = 267.4 ✓
- **範圍疑點**：網址帶 `qual=y`，頁面也顯示 Qualified；但由 Replacement 反推的打席約 85,671，接近美聯總打席 85,797，表示總和應涵蓋全部野手，不只規定打席球員。
- **未解釋的差距**：League Adj 357.2 ≠ −(Batting + Base Running + Fielding + Positional) = 339.6，差 17.6。2024 WAR 更新只回溯到 2016 年，不能解釋 2012 年的差距。詳見 `outputs/slides/war-explained/verify.py`。
