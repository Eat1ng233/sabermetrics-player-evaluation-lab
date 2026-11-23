# fangraphs_mlb_2013_trout-game-log.csv — Mike Trout 2013 逐場紀錄

## 來源
- **來源網址**：https://www.fangraphs.com/players/mike-trout/10155/game-log?position=NP&season=2013&type=0
- **擷取日期**：2026-11-23
- **提供方式**：使用者從瀏覽器列印成 PDF，原檔保留為 `raw/data/fangraphs_mlb_2026-11-23_trout-2013-game-log.pdf`
- **轉換方式**：`pdftotext -layout` 抽出文字，再以 Python 解析每一列「Team Opp BO Pos PA H 2B 3B HR R RBI SB CS」
- **範圍**：2013 例行賽 157 場；不含 Total 列
- **用途**：驗證 war-explained P.15 的 Positional −1.2（Trout 2013 擔任 DH 的場數）

## 欄位說明
| 欄位 | 說明 |
|---|---|
| Row | PDF 列印順序（大致由新到舊），不是日期 |
| Team / Opp | 所屬球隊 / 對手（`@` 表示客場） |
| BO | 打序 |
| Pos | 當場守備位置；`CF-LF` 表示比賽中換位置 |
| PA … CS | 打席、安打、二壘安打、三壘安打、全壘打、得分、打點、盜壘、盜壘失敗 |

## 清理與檢查
- **刻意省略日期欄**：PDF 分頁時有重複列印的日期，而且日期欄與資料列錯位（例如 4 月 1 日被對到 OAK，實際該場是 @CIN），無法可靠地把日期對回每一場，所以不收錄。
- **刻意省略比率欄**（BB%、K%、ISO、BABIP、AVG、OBP、SLG、wOBA、wRC+ 等）：可由計數欄重算，或改用季資料。
- 157 列的加總與頁面 Total 列完全相同：PA 716、H 190、2B 39、3B 9、HR 27、R 109、RBI 97、SB 33、CS 7。
- 位置統計：CF 101、LF 37、DH 9、CF-LF 6、LF-CF 4。
