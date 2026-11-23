# Index

本知識庫所有頁面的目錄。每次 ingest 或新增頁面時，由 LLM 更新。
格式：`- [[檔名|顯示名稱]] — 一句話摘要（來源數：N）`

綜述：[[overview]]｜動態查詢：[[dashboard]]｜紀錄：[[log]]

---

## 指標（metrics）

### 打擊（batting）
- [[woba|wOBA]] — 依事件得分價值加權、縮放到 OBP 尺度的綜合打擊指標；含完整推導（來源數：3）
- [[wraa|wRAA]] — 把 wOBA 與聯盟平均的差距換算成累計得分（來源數：3）
- [[wrc|wRC]] — wRAA 加回聯盟平均得分，打者創造的總得分（來源數：1）
- [[wrc-plus|wRC+]] — 經球場與聯盟調整、以 100 為平均的打擊指數（來源數：3）
- [[batting-runs|Batting Runs]] — 經球場與聯盟調整的 wRAA，WAR 打擊組成（來源數：3）

### 投球（pitching）
_（尚無頁面）_

### 守備（fielding）
_（尚無頁面）_

### 跑壘（baserunning）
- [[bsr|BsR]] — 跑壘得分 = UBR + wSB + wGDP；含 wSB 推導（來源數：1）

### Statcast／追蹤數據（statcast）
_（尚無頁面）_

### 綜合價值、新秀與合約（value / prospect / contract）
- [[war|WAR]] — 高於替補水準的勝場；總覽、解讀、誤用、各版本（來源數：4）
- [[war-position-players|野手 WAR 計算]] — 六個組成與 RPW 換算（來源數：1）
- [[war-pitchers|投手 WAR 計算]] — ifFIP → FIPR9 → 動態 RPW → 替補水準 → 槓桿（來源數：1）

## 概念與方法（concepts）
- [[run-expectancy-matrix|得分期望值矩陣]] — 24 種壘包出局狀態到局末的平均得分；含 2010–2015 年矩陣（來源數：1）
- [[linear-weights|Linear Weights]] — 每種事件的平均得分價值，wOBA 權重的來源（來源數：2）
- [[park-factor|Park Factor]] — 球場係數的成因、減半顯示、加法與乘法調整、限制（來源數：4）
- [[replacement-level|替補水準]] — 1,000 WAR、.294；含來源分歧（來源數：4，needs-review）
- [[runs-per-win|RPW]] — 每勝得分與各年數值（來源數：3）
- [[positional-adjustment|守位調整]] — 各守位每 162 場的調整值（來源數：1）

## 比較（comparisons）
_（尚無頁面）_

## 案例研究（case-studies）
_（尚無頁面）_

## 計算範例（examples）
- [[ex-woba-mlb-2015-derivation|wOBA 權重推導（MLB 2015）]] — 從得分期望值到最終權重的五個步驟（來源數：1）
- [[ex-woba-mlb-2013-trout|Trout 2013 wOBA、wRAA、wRC]] — 逐步計算並與 FanGraphs 數據核對（來源數：2）
- [[ex-wrc-plus-mlb-2012-trout|Trout 2012 wRC+]] — wRC+ 五步驟計算，含球場調整（來源數：2）
- [[ex-war-mlb-2012-trout|Trout 2012 WAR]] — 野手 WAR 逐項拆解並對照 FanGraphs（來源數：3）

## 來源（sources）
- [[src-2012-slowinski-fangraphs-war-position-players|FanGraphs Library — WAR for Position Players]] — 野手 WAR 完整計算（2012，Slowinski）
- [[src-2012-slowinski-fangraphs-war-pitchers|FanGraphs Library — WAR for Pitchers]] — 投手 WAR 完整計算（2012，Slowinski／Weinberg 更新）
- [[src-2012-slowinski-fangraphs-war-misconceptions|FanGraphs Library — WAR Misconceptions]] — WAR 的五個常見誤解（2012，Slowinski）
- [[src-2010-slowinski-fangraphs-park-factors|FanGraphs Library — Park Factors]] — 球場係數的成因與限制（2010，Slowinski）
- [[src-2010-slowinski-fangraphs-what-is-war|FanGraphs Library — What is WAR?]] — WAR 定義、版本、解讀（2010，Slowinski）
- [[src-2016-weinberg-fangraphs-deriving-woba|The Beginner's Guide To Deriving wOBA]] — wOBA 權重的完整推導、2010–2015 年常數（2016，Weinberg）
- [[src-2010-slowinski-fangraphs-wrc|FanGraphs Library — wRC and wRC+]] — wRC、wRC+ 的公式與解讀（2010，Slowinski）
- [[src-2010-slowinski-fangraphs-woba|FanGraphs Library — wOBA]] — wOBA 的定義、2013 年公式、Scale、門檻與限制（2010，Slowinski）
