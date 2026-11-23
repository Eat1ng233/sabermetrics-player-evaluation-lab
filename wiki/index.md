# Index

本知識庫所有頁面的目錄。每次 ingest 或新增頁面時，由 LLM 更新。
格式：`- [[檔名|顯示名稱]] — 一句話摘要（來源數：N）`

綜述：[[overview]]｜動態查詢：[[dashboard]]｜紀錄：[[log]]

---

## 指標（metrics）

### 打擊（batting）
- [[woba|wOBA]] — 依事件得分價值加權、縮放到 OBP 尺度的綜合打擊指標；含完整推導（來源數：3）
- [[wraa|wRAA]] — 把 wOBA 與聯盟平均的差距換算成累計得分（來源數：2）
- [[wrc|wRC]] — wRAA 加回聯盟平均得分，打者創造的總得分（來源數：1）
- [[wrc-plus|wRC+]] — 經球場與聯盟調整、以 100 為平均的打擊指數（來源數：1）

### 投球（pitching）
_（尚無頁面）_

### 守備（fielding）
_（尚無頁面）_

### 跑壘（baserunning）
_（尚無頁面）_

### Statcast／追蹤數據（statcast）
_（尚無頁面）_

### 綜合價值、新秀與合約（value / prospect / contract）
_（尚無頁面）_

## 概念與方法（concepts）
- [[run-expectancy-matrix|得分期望值矩陣]] — 24 種壘包出局狀態到局末的平均得分；含 2010–2015 年矩陣（來源數：1）
- [[linear-weights|Linear Weights]] — 每種事件的平均得分價值，wOBA 權重的來源（來源數：2）
- [[park-factor|Park Factor]] — 球場係數與 wRC+ 的加法調整（來源數：1，stub）

## 比較（comparisons）
_（尚無頁面）_

## 案例研究（case-studies）
_（尚無頁面）_

## 計算範例（examples）
- [[ex-woba-mlb-2015-derivation|wOBA 權重推導（MLB 2015）]] — 從得分期望值到最終權重的五個步驟（來源數：1）
- [[ex-woba-mlb-2013-trout|Trout 2013 wOBA、wRAA、wRC]] — 逐步計算並與 FanGraphs 數據核對（來源數：2）
- [[ex-wrc-plus-mlb-2012-trout|Trout 2012 wRC+]] — wRC+ 五步驟計算，含球場調整（來源數：1）

## 來源（sources）
- [[src-2016-weinberg-fangraphs-deriving-woba|The Beginner's Guide To Deriving wOBA]] — wOBA 權重的完整推導、2010–2015 年常數（2016，Weinberg）
- [[src-2010-slowinski-fangraphs-wrc|FanGraphs Library — wRC and wRC+]] — wRC、wRC+ 的公式與解讀（2010，Slowinski）
- [[src-2010-slowinski-fangraphs-woba|FanGraphs Library — wOBA]] — wOBA 的定義、2013 年公式、Scale、門檻與限制（2010，Slowinski）
