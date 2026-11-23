---
title: Dashboard
type: overview
aliases: [儀表板]
domain: [method]
leagues: [general]
tags: [dashboard]
sources: []
source_count: 0
status: stable
created: 2026-11-23
updated: 2026-11-23
---

# Dashboard

> 需要安裝 Obsidian 的 Dataview 外掛才會顯示查詢結果。

## 指標一覽
```dataview
TABLE full_name AS "全名", domain AS "領域", leagues AS "聯盟", source_count AS "來源數", status AS "狀態"
FROM "wiki/metrics"
SORT domain ASC, file.name ASC
```

## 待審閱或有爭議的頁面
```dataview
TABLE type AS "類型", status AS "狀態", updated AS "更新日期"
FROM "wiki"
WHERE status = "needs-review" OR contains(tags, "contested")
SORT updated DESC
```

## 來源不足的頁面（少於 2 個來源）
```dataview
TABLE type AS "類型", source_count AS "來源數"
FROM "wiki/metrics" OR "wiki/concepts"
WHERE source_count < 2
SORT source_count ASC
```

## 最近更新
```dataview
TABLE type AS "類型", updated AS "更新日期"
FROM "wiki"
WHERE updated
SORT updated DESC
LIMIT 15
```

## 來源清單
```dataview
TABLE source_type AS "類型", author AS "作者", published AS "發表", ingest_mode AS "匯入模式"
FROM "wiki/sources"
SORT published DESC
```

## 計算範例（依聯盟與球季）
```dataview
TABLE metric AS "指標", league AS "聯盟", season AS "球季", subject AS "對象"
FROM "wiki/examples"
SORT league ASC, season DESC
```
