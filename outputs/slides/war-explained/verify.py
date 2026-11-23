#!/usr/bin/env python3
"""war-explained 簡報的數字驗算（SOP-04 節點 N2b）

每一個出現在簡報上的數字，都在這裡用程式重算，並和資料來源比對。
任何一項不符就以 exit code 1 結束。
"""
import csv, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
DATA = ROOT / 'raw' / 'data'
def load(name):
    with open(DATA / name, encoding='utf-8') as f:
        return {r['Season']: r for r in csv.DictReader(f)}
STD = load('fangraphs_mlb_2011-2026_trout-standard.csv')
ADV = load('fangraphs_mlb_2011-2026_trout-advanced.csv')
VAL = load('fangraphs_mlb_2011-2026_trout-value.csv')
v = lambda y, k: float(VAL[y][k])

RPW = {2012: 9.544, 2013: 9.264}                 # GUTS（wiki/concepts/runs-per-win）
RPA = {2012: .114}                               # GUTS
PF12, AL12 = 0.95, 10032 / 85797                 # ART·wRC
POS = dict(C=12.5, SS=7.5, B2=2.5, B3=2.5, CF=2.5, LF=-7.5, RF=-7.5, B1=-12.5, DH=-17.5)   # ART·WARpp
INN = {2012: dict(LF=328.0, CF=885 + 2/3, RF=12.0),   # PDF·FLD·12（球員頁 Fielding 表；.2 = 2/3 局）
       2013: dict(LF=356.0, CF=952 + 2/3)}            # PDF·FLD·13

results = []
def check(name, got, expect, tol, src):
    ok = abs(got - expect) <= tol
    results.append(ok)
    print(f"{'✓' if ok else '✗'} {name:<30} 算出 {got:>10.4f}  應為 {expect:<9} 容許 ±{tol}  [{src}]")

# ---- 替補水準（P.5）----
check('替補球隊總勝場', 2430 - 1000, 1430, 0, 'ART·WAR')
check('替補球隊每隊勝場', (2430 - 1000) / 30, 47.7, 0.05, '推論')
check('替補勝率', (2430 - 1000) / 30 / 162, .294, 0.0005, 'ART·WAR')
check('野手 WAR 份額', 1000 * .57, 570, 0, 'ART·WARpp')

# ---- RPW（P.10）----
check('2012 R/9（由 RPW 反推）', (RPW[2012] - 3) / 1.5, 4.363, 0.0005, '推論')
check('2013 R/9（由 RPW 反推）', (RPW[2013] - 3) / 1.5, 4.176, 0.0005, '推論')

# ---- RPW 表（P.10）：GUTS 數值與推論的 R/9 ----
for yr, rpw, r9 in [(2010, 9.643, 4.43), (2011, 9.454, 4.30), (2012, 9.544, 4.36), (2013, 9.264, 4.18), (2014, 9.117, 4.08), (2015, 9.421, 4.28)]:
    check(f'{yr} R/9 = (RPW−3)/1.5', (rpw - 3) / 1.5, r9, 0.005, 'GUTS → 推論')
check('2013 runCS ≈ −(2×R/27+0.075)', -(2 * ((RPW[2013] - 3) / 1.5) / 27 + 0.075), -0.384, 0.001, 'GUTS 2013 → 推論')

# ---- Trout 2012 拆解（P.14）----
y = '2012'; pa = int(STD[y]['PA']); wraa = float(ADV[y]['wRAA'])
park = RPA[2012] * (1 - PF12) * pa
league_bat = (RPA[2012] - AL12) * pa
check('2012 球場調整', park, 3.64, 0.005, 'ART·wRC')
check('2012 聯盟調整（打擊）', league_bat, -1.87, 0.005, 'ART·wRC')
check('2012 Batting', wraa + park + league_bat, v(y, 'Batting'), 0.2, 'VAL·12·Batting')
pos12 = sum(INN[2012][p] / 9 / 162 * POS[p] for p in INN[2012])
for p, e in [('LF', -1.69), ('CF', 1.52), ('RF', -0.06)]:
    check(f'2012 Positional {p}', INN[2012][p] / 9 / 162 * POS[p], e, 0.005, 'PDF·FLD·12')
check('2012 Positional', pos12, v(y, 'Positional'), 0.05, 'VAL·12·Positional')
check('2012 Off = Bat + BsR', v(y, 'Batting') + v(y, 'Base Running'), v(y, 'Offense'), 0.11, 'VAL·12·Offense')
check('2012 Def = Fld + Pos', v(y, 'Fielding') + v(y, 'Positional'), v(y, 'Defense'), 0.11, 'VAL·12·Defense')
rar = sum(v(y, k) for k in ['Batting', 'Base Running', 'Fielding', 'Positional', 'League', 'Replacement'])
check('2012 RAR 加總', rar, v(y, 'RAR'), 0.15, 'VAL·12·RAR')
check('2012 WAR = RAR ÷ RPW', v(y, 'RAR') / RPW[2012], v(y, 'WAR'), 0.05, 'VAL·12·WAR')
check('2012 lgPA（由替補得分反推）', 570 * RPW[2012] * pa / v(y, 'Replacement'), 183900, 100, '推論')

# ---- Trout 2013（P.15）----
y = '2013'
rar13 = sum(v(y, k) for k in ['Batting', 'Base Running', 'Fielding', 'Positional', 'League', 'Replacement'])
check('2013 RAR 加總', rar13, v(y, 'RAR'), 0.15, 'VAL·13·RAR')
check('2013 WAR = RAR ÷ RPW', v(y, 'RAR') / RPW[2013], v(y, 'WAR'), 0.06, 'VAL·13·WAR')
pos13 = sum(INN[2013][p] / 9 / 162 * POS[p] for p in INN[2013])
check('2013 Positional（只算 LF+CF）', pos13, -0.20, 0.005, 'PDF·FLD·13')
check('2013 DH 局數（推論補足差距）', (v(y, 'Positional') - pos13) / POS['DH'] * 162 * 9, 83.5, 0.05, '推論')

print(f"\n通過 {sum(results)}／{len(results)}")
sys.exit(0 if all(results) else 1)
