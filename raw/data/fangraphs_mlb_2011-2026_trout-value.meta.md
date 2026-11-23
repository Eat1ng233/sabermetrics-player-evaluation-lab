# fangraphs_mlb_2011-2026_trout-value.csv — Mike Trout Value（WAR 組成）

## 來源
- **來源網址**：https://www.fangraphs.com/players/mike-trout/10155/stats/batting
- **擷取日期**：2026-11-23（頁面標示更新時間：2026-11-23 12:01 AM ET）
- **提供方式**：使用者從瀏覽器列印成 PDF，原檔保留為 `raw/data/fangraphs_mlb_2026-11-23_trout-player-page.pdf`
- **轉換方式**：用 `pdftotext -layout` 抽出文字，再以 Python 依欄位解析
- **範圍**：只保留 MLB 例行賽各球季（2011–2026），排除 2027 年預測（FGDC、Steamer）與生涯 Total 列
- **編碼**：UTF-8，逗號分隔；欄位名稱沿用 FanGraphs 原始名稱

## 欄位說明
| 欄位 | 說明 |
|---|---|
| Batting | 打擊得分（經球場與聯盟調整，相對平均） |
| Base Running | 跑壘得分（BsR） |
| Fielding | 守備得分 |
| Positional | 守位調整 |
| Offense / Defense | 進攻 / 防守合計 |
| League | 聯盟調整 |
| Replacement | 替補水準調整 |
| RAR / WAR | 高於替補水準的得分 / 勝場 |
| Dollars ($M) | FanGraphs 估算的市場價值，單位百萬美元（原欄位為 `Dollars`，已去掉 `$` 符號） |

## 清理與檢查
- 原頁面的 `Salary` 欄在 PDF 中為空白，未收錄。
- 已檢查：每一季 $\text{Batting}+\text{Base Running}\approx\text{Offense}$（誤差 ≤ 0.1，屬四捨五入）。
