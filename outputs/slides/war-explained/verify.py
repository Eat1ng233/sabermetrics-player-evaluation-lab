#!/usr/bin/env python3
"""war-explained 簡報的數字驗算（SOP-04 節點 N2b）

每一個會出現在簡報上的數字，都在這裡用程式重算，並和資料來源比對。
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

RPW = {2010: 9.643, 2011: 9.454, 2012: 9.544, 2013: 9.264, 2014: 9.117, 2015: 9.421}   # GUTS（wiki/concepts/runs-per-win）
RPA12 = .114                                                                        # GUTS 2012
PF12, AL12 = 0.95, 10032 / 85797                                                    # ART·wRC
POS = dict(C=12.5, SS=7.5, B2=2.5, B3=2.5, CF=2.5, LF=-7.5, RF=-7.5, B1=-12.5, DH=-17.5)   # ART·WARpp
INN = {2012: dict(LF=328.0, CF=885 + 2/3, RF=12.0),   # PDF·FLD·12（.2 = 2/3 局）
       2013: dict(LF=356.0, CF=952 + 2/3)}            # PDF·FLD·13

results = []
def check(name, got, expect, tol, src):
    ok = abs(got - expect) <= tol
    results.append(ok)
    print(f"{'✓' if ok else '✗'} {name:<30} 算出 {got:>10.4f}  應為 {expect:<9} 容許 ±{tol}  [{src}]")

# ---- P.5 替補水準 ----
check('替補球隊總勝場', 2430 - 1000, 1430, 0, 'ART·WAR')
check('替補球隊每隊勝場', (2430 - 1000) / 30, 47.7, 0.05, '推論')
check('替補勝率', (2430 - 1000) / 30 / 162, .294, 0.0005, 'ART·WAR')
check('野手 WAR 份額', 1000 * .57, 570, 0, 'ART·WARpp')
check('43 勝換算勝率', 43 / 162, .265, 0.0005, 'ART·Misc → 推論')

# ---- P.7 跑壘：runCS ----
check('2013 runCS ≈ −(2×R/27+0.075)', -(2 * ((RPW[2013] - 3) / 1.5) / 27 + 0.075), -0.384, 0.001, 'GUTS 2013 → 推論')

# ---- P.10 RPW 表與 R/9 ----
for yr, r9 in [(2010, 4.43), (2011, 4.30), (2012, 4.36), (2013, 4.18), (2014, 4.08), (2015, 4.28)]:
    check(f'{yr} R/9 = (RPW−3)/1.5', (RPW[yr] - 3) / 1.5, r9, 0.005, 'GUTS → 推論')

# ---- P.14 Trout 2012 拆解 ----
y = '2012'; pa = int(STD[y]['PA']); wraa = float(ADV[y]['wRAA'])
park = RPA12 * (1 - PF12) * pa; league_bat = (RPA12 - AL12) * pa
check('2012 球場調整', park, 3.64, 0.005, 'ART·wRC')
check('2012 聯盟調整（打擊）', league_bat, -1.87, 0.005, 'ART·wRC')
check('2012 Batting', wraa + park + league_bat, v(y, 'Batting'), 0.2, 'VAL·12·Batting')
for p, e in [('LF', -1.69), ('CF', 1.52), ('RF', -0.06)]:
    check(f'2012 Positional {p}', INN[2012][p] / 9 / 162 * POS[p], e, 0.005, 'PDF·FLD·12')
check('2012 Positional', sum(INN[2012][p] / 9 / 162 * POS[p] for p in INN[2012]), v(y, 'Positional'), 0.05, 'VAL·12·Positional')
check('2012 Off = Bat + BsR', v(y, 'Batting') + v(y, 'Base Running'), v(y, 'Offense'), 0.11, 'VAL·12·Offense')
check('2012 Def = Fld + Pos', v(y, 'Fielding') + v(y, 'Positional'), v(y, 'Defense'), 0.11, 'VAL·12·Defense')
rar = sum(v(y, k) for k in ['Batting', 'Base Running', 'Fielding', 'Positional', 'League', 'Replacement'])
check('2012 RAR 加總', rar, v(y, 'RAR'), 0.15, 'VAL·12·RAR')
check('2012 WAR = RAR ÷ RPW', v(y, 'RAR') / RPW[2012], v(y, 'WAR'), 0.05, 'VAL·12·WAR')
check('2012 lgPA（由替補得分反推）', 570 * RPW[2012] * pa / v(y, 'Replacement'), 183900, 100, '推論')

# ---- P.15 Trout 2013 ----
y = '2013'
rar13 = sum(v(y, k) for k in ['Batting', 'Base Running', 'Fielding', 'Positional', 'League', 'Replacement'])
check('2013 RAR 加總', rar13, v(y, 'RAR'), 0.15, 'VAL·13·RAR')
check('2013 WAR = RAR ÷ RPW', v(y, 'RAR') / RPW[2013], v(y, 'WAR'), 0.06, 'VAL·13·WAR')
pos13 = sum(INN[2013][p] / 9 / 162 * POS[p] for p in INN[2013])
check('2013 Positional（只算 LF+CF）', pos13, -0.20, 0.005, 'PDF·FLD·13')
check('2013 DH 局數（推論補足差距）', (v(y, 'Positional') - pos13) / POS['DH'] * 162 * 9, 83.5, 0.05, '推論')
check('2013 DH 場數（推論）', (v(y, 'Positional') - pos13) / POS['DH'] * 162, 9.3, 0.05, '推論')


# ---- d2 新增：使用者補上的資料（2026-11-24）----
GL = list(csv.DictReader(open(DATA / 'fangraphs_mlb_2013_trout-game-log.csv', encoding='utf-8')))
check('2013 逐場 PA 加總 = 球季 PA', sum(int(r['PA']) for r in GL), float(STD['2013']['PA']), 0, 'LOG·13')
check('2013 逐場出賽數', len(GL), float(STD['2013']['G']), 0, 'LOG·13')
dh_g = sum(r['Pos'] == 'DH' for r in GL)
check('2013 DH 先發場數', dh_g, 9, 0, 'LOG·13')
pos13_dh = pos13 + dh_g * 9 / 9 / 162 * POS['DH']
check('2013 Positional（LF+CF+DH 9 場×9 局）', pos13_dh, v('2013', 'Positional'), 0.05, 'LOG·13 + PDF·FLD·13 → VAL·13')

AL = next(csv.DictReader(open(DATA / 'fangraphs_mlb_2012_al-nonpitchers-value-totals.csv', encoding='utf-8')))
a = lambda k: float(AL[k])
check('AL12 RAR 加總', sum(a(k) for k in ['Batting', 'Base Running', 'Fielding', 'Positional', 'League Adj', 'Replacement']), a('RAR'), 0.15, 'LDR·AL12')
check('AL12 WAR = RAR ÷ RPW', a('RAR') / RPW[2012], a('WAR'), 0.05, 'LDR·AL12')
check('AL12 由 Replacement 反推 PA（≈ 美聯總打席 85797）', a('Replacement') / (570 * RPW[2012] / 183900), 85671, 1, 'LDR·AL12 → 推論')
four = a('Batting') + a('Base Running') + a('Fielding') + a('Positional')
pa12 = float(STD['2012']['PA'])
check('Trout 2012 League（文章公式，用美聯四項總和）', -four / 85797 * pa12, 2.53, 0.005, 'ART·WARpp + LDR·AL12 → 推論')
check('Trout 2012 League（美聯 League 總額按 PA 分攤）', a('League Adj') / 85797 * pa12, v('2012', 'League'), 0.05, 'LDR·AL12 → VAL·12·League')
check('美聯 League 總額 − 四項總和的相反數（未解釋的差距）', a('League Adj') + four, 17.6, 0.05, 'LDR·AL12 → 推論')


# ---- d2 新增：全大聯盟總和（2026-11-24）與新來源的數字 ----
MLB = next(csv.DictReader(open(DATA / 'fangraphs_mlb_2012_mlb-all-value-totals.csv', encoding='utf-8')))
m = lambda k: float(MLB[k])
check('MLB12 四項＋League ＝ 0（含投手打擊）', m('Batting') + m('Base Running') + m('Fielding') + m('Positional') + m('League Adj'), 0, 0.05, 'LDR·MLB12')
check('MLB12 Replacement ＝ 570 × RPW', 570 * RPW[2012], m('Replacement'), 0.15, 'LDR·MLB12 + GUTS')
check('MLB12 WAR ＝ Replacement ÷ RPW ＝ 570', m('Replacement') / RPW[2012], 570.0, 0.05, 'LDR·MLB12')
check('Trout 2012 替補得分佔全聯盟比例 ＝ PA ÷ lgPA', v('2012', 'Replacement') / m('Replacement') * 183900, pa12, 4, 'VAL·12 + LDR·MLB12 → 推論')
check('UZR 例：接到 ＝ 0.8 × (1 − 0.4)', 0.8 * (1 - 0.4), 0.48, 1e-9, 'ART·UZR')
check('UZR 例：沒接到 ＝ −0.8 × 0.4（推論）', -0.8 * 0.4, -0.32, 1e-9, '推論')
check('UZR 例：平均守備員期望值 ＝ 0（推論）', 0.4 * 0.48 + 0.6 * (-0.32), 0, 1e-9, '推論')


# ---- d3 新增：2012 全大聯盟總打席（2026-11-24）----
STDM = next(csv.DictReader(open(DATA / 'fangraphs_mlb_2012_mlb-all-standard-totals.csv', encoding='utf-8')))
lgPA12 = float(STDM['PA'])
check('MLB12 場次 ＝ TG ÷ 2', float(STDM['TG']) / 2, 2430, 0, 'LDR·MLB12S')
check('MLB12 lgR/PA ＝ R ÷ PA', float(STDM['R']) / lgPA12, RPA12, 0.0005, 'LDR·MLB12S → GUTS')
check('Trout 2012 Replacement ＝ 570 × RPW ÷ lgPA × PA', 570 * 2430 / 2430 * RPW[2012] / lgPA12 * pa12, v('2012', 'Replacement'), 0.05, 'LDR·MLB12S + GUTS → VAL·12')
check('反推 lgPA 的誤差（推論 183,900 vs 實際）', (lgPA12 - 183900) / lgPA12, 0.0015, 0.0001, '推論 vs LDR·MLB12S')
check('BsR、Off、Def、WAR 兩張表一致', float(STDM['Off']) + float(STDM['Def']) + float(STDM['WAR']), m('Offense') + m('Defense') + m('WAR'), 0.05, 'LDR·MLB12S vs LDR·MLB12')


# ---- d3 新增：替補水準統一、framing（2026-11-24）----
check('.265 ≈ 43 勝（統一前 FanGraphs）', .265 * 162, 43, 0.1, 'ART·RL13 → 推論')
check('.320 換算勝場（統一前 B-R）', .320 * 162, 51.8, 0.05, 'ART·RL13 → 推論')
check('Greinke 2011：FIP ＋ framing/9', 3.00 + 0.31, 3.31, 1e-9, 'ART·FRM19')

print(f"\n通過 {sum(results)}／{len(results)}")
sys.exit(0 if all(results) else 1)
