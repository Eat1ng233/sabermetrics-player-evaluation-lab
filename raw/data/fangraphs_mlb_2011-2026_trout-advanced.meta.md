# fangraphs_mlb_2011-2026_trout-advanced.csv — Mike Trout Advanced（進階打擊數據）

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
| BB% / K% / BB/K | 保送率 / 三振率 / 保送三振比 |
| AVG / OBP / SLG / OPS / ISO | 打擊率 / 上壘率 / 長打率 / 整體攻擊指數 / 純長打率 |
| Spd / BABIP | 速度分數 / 場內球安打率 |
| wRC / wRAA / wOBA / wRC+ | 見 wiki 對應指標頁 |

## 清理與檢查
- **刻意省略**：原頁面的 UBR、wGDP、XBR、wSB 四個跑壘子欄位。PDF 版面中這四欄的對齊有歧義（部分年份缺值，數值位置與標題無法一一對應），為避免寫入錯誤數據而不收錄。跑壘總值請用 value 表的 `Base Running`。需要這四欄時，請從 FanGraphs 匯出 CSV 補上。
- 百分比欄位保留 `%` 符號，使用前需轉成數值。
