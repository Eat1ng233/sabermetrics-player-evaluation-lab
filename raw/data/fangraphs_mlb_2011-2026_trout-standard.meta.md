# fangraphs_mlb_2011-2026_trout-standard.csv — Mike Trout Standard（傳統打擊數據）

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
| G / AB / PA | 出賽數 / 打數 / 打席 |
| H / 1B / 2B / 3B / HR | 安打 / 一壘、二壘、三壘安打 / 全壘打 |
| R / RBI | 得分 / 打點 |
| BB / IBB | 四壞（含故意）/ 故意四壞 |
| SO / HBP | 三振 / 觸身球 |
| SF / SH | 高飛犧牲打 / 犧牲觸擊 |
| GDP / SB / CS / AVG | 雙殺打 / 盜壘 / 盜壘失敗 / 打擊率 |

## 清理與檢查
- 每一季都已檢查：$\text{1B}+\text{2B}+\text{3B}+\text{HR}=\text{H}$、$\text{H}/\text{AB}$ 與 AVG 一致、由 H、BB、HBP、AB、SF 算出的 OBP 與 advanced 表一致。
