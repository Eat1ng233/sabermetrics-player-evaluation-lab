#!/usr/bin/env python3
"""woba-to-wrc-plus 簡報的數字驗算（SOP-04 節點 N2b）

每一個出現在簡報上的數字，都在這裡用程式重算，並和資料來源比對。
任何一項不符就以 exit code 1 結束。
執行位置：本資料夾（spec_check.py 會自動切換）。
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

# 聯盟常數：wiki/metrics/woba.md「MLB 2010–2015 年常數」（GUTS）
GUTS = {2012: dict(lgwOBA=.315, scale=1.245, RPA=.114),
        2013: dict(lgwOBA=.314, scale=1.277, RPA=.110,
                   w=dict(BB=.690, HBP=.722, B1=.888, B2=1.271, B3=1.616, HR=2.101))}

results = []
def check(name, got, expect, tol, src):
    ok = abs(got - expect) <= tol
    results.append(ok)
    print(f"{'✓' if ok else '✗'} {name:<34} 算出 {got:>10.4f}  應為 {expect:<9} 容許 ±{tol}  [{src}]")

# ---- Trout 2013：從原始數據算 wOBA → wRAA → wRC（P.22）----
s = STD['2013']; n = lambda k: int(s[k])
ubb = n('BB') - n('IBB'); w = GUTS[2013]['w']
num = w['BB']*ubb + w['HBP']*n('HBP') + w['B1']*n('1B') + w['B2']*n('2B') + w['B3']*n('3B') + w['HR']*n('HR')
den = n('AB') + n('BB') - n('IBB') + n('SF') + n('HBP')
check('2013 uBB', ubb, 100, 0, 'STD·13·BB − IBB')
check('2013 分子', num, 298.458, 0.0005, '權重×次數')
check('2013 分母', den, 706, 0, 'STD·13')
woba13 = num / den
check('2013 wOBA', woba13, float(ADV['2013']['wOBA']), 0.0005, 'ADV·13·wOBA')
g = GUTS[2013]; pa13 = n('PA')
wraa13 = (0.423 - g['lgwOBA']) / g['scale'] * pa13
check('2013 wRAA', wraa13, float(ADV['2013']['wRAA']), 0.05, 'ADV·13·wRAA')
check('2013 wRC', wraa13 + g['RPA'] * pa13, float(ADV['2013']['wRC']), 0.5, 'ADV·13·wRC')

# ---- Trout 2012：wOBA → wRAA → wRC → wRC+（P.20–21）----
g = GUTS[2012]; pa12 = int(STD['2012']['PA']); woba12 = float(ADV['2012']['wOBA'])
wraa12 = (woba12 - g['lgwOBA']) / g['scale'] * pa12
check('2012 wRAA', wraa12, float(ADV['2012']['wRAA']), 0.05, 'ADV·12·wRAA')
check('2012 wRC', 48.2 + g['RPA'] * pa12, float(ADV['2012']['wRC']), 0.5, 'ADV·12·wRC')
PF, AL = 0.95, 10032 / 85797                                     # ART·wRC
wrcpa = 48.2 / pa12 + g['RPA']; park = g['RPA'] * (1 - PF)
check('2012 wRC+', (wrcpa + park) / AL * 100, float(ADV['2012']['wRC+']), 0.5, 'ADV·12·wRC+')
check('2012 wRC+（無球場調整）', wrcpa / AL * 100, 162.0, 0.05, '推論')
check('2012 Batting Runs', 48.2 + park*pa12 + (g['RPA'] - AL)*pa12, float(VAL['2012']['Batting']), 0.2, 'VAL·12·Batting')
check('Batting→wRC+ 換算', (1 + (float(VAL['2012']['Batting'])/pa12)/AL) * 100, 167.1, 0.05, '推論')

# ---- 球場係數範例（P.13–19，假設數字與文章例子）----
H, R, T = 11, 10, 15
raw = H*T / ((T-1)*R + H); ipf = (raw + 1) / 2; pf = 1 + (ipf - 1) * 0.9
check('PF 原始', raw, 1.093, 0.0005, '假設數字')
check('PF 減半', ipf, 1.046, 0.0005, '假設數字')
check('PF 迴歸', pf, 1.042, 0.0005, '假設數字')
check('漏掉 ×T', H / ((T-1)*R + H), 0.073, 0.0005, '假設數字')
for X, e in [(.6, 1.15), (.7, 1.175), (.8, 1.20), (.9, 1.225)]:
    check(f'iPF 1.25 迴歸 X={X}', 1 + .25 * X, e, 1e-9, 'ART·PF5yr')
check('減半例 105÷1.05', 105 / 1.05, 100, 1e-9, '假設數字')
check('不減半 105÷1.10', 105 / 1.10, 95.5, 0.05, '假設數字')
ipf95 = 1 - (1 - .95) / .9
check('顯示 95 → 原始（推論）', 2*ipf95 - 1, 0.889, 0.0005, '推論，X=0.9')

# ---- 得分期望值與線性權重（P.5–9）----
check('ΔRE 保送', .884 - .509, .375, 1e-9, 'RE 2010–15')
check('ΔRE 一壘安打', 1.784 - .859, .925, 1e-9, 'RE 2010–15')
check('ΔRE 安打得 1 分', 1.437 - 1.784 + 1, .653, 1e-9, 'RE 2010–15')
check('wOBA Scale 2015', .313 / .250, 1.252, 1e-9, 'ART·Deriving')
for k, rv, guts in [('BB', .55, .687), ('HR', 1.65, 2.065)]:
    check(f'權重 {k} = RV*×1.251', rv * 1.251, guts, 0.006, 'GUTS 2015')

print(f"\n通過 {sum(results)}／{len(results)}")
sys.exit(0 if all(results) else 1)
