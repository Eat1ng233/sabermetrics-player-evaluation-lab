# Log

只追加的時間紀錄。查詢最近 5 筆：`grep "^## \[" wiki/log.md | tail -5`

---

## [2026-11-23] setup | 建立知識庫架構
- 建立 `AGENTS.md`（schema）與資料夾結構：`raw/`、`wiki/`、`outputs/`、`scripts/`
- 建立 `wiki/index.md`、`wiki/log.md`、`wiki/overview.md`、`wiki/dashboard.md`
- 主要規則：繁體中文內文、英文 kebab-case 檔名、Obsidian wikilink、Dataview frontmatter、公式一律用 LaTeX、多聯盟（MLB/NPB/KBO/CPBL）、矛盾並列呈現、依來源類型選擇 ingest 模式
