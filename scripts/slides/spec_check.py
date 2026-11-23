#!/usr/bin/env python3
"""SOP-04 節點 N2d：內容關卡（「整理重點與驗算」loop 的通過標準）

用法：python3 scripts/slides/spec_check.py outputs/slides/<slug>/

檢查 <slug>/spec.md 與 <slug>/verify.py，全部通過才以 exit code 0 結束：
  1. 符號表：每個符號都有定義與出處
  2. 數字表：每個數字都有出處代碼，且驗算欄不是 ✗（「無法驗算」必須寫原因）
  3. 缺失清單：沒有「必要」且「未解決」的項目
  4. verify.py：以 exit code 0 結束（程式化驗算全部通過）
"""
import re, subprocess, sys, pathlib, json

def table(md, heading):
    m = re.search(r'^##\s*' + re.escape(heading) + r'\s*$(.*?)(?=^##\s|\Z)', md, re.M | re.S)
    if not m: return None
    rows = [l.strip() for l in m.group(1).splitlines() if l.strip().startswith('|')]
    if len(rows) < 2: return []
    head = [c.strip() for c in rows[0].strip('|').split('|')]
    out = []
    for r in rows[2:]:
        cells = [c.strip() for c in r.strip('|').split('|')]
        out.append(dict(zip(head, cells)))
    return out

def main(d):
    d = pathlib.Path(d).resolve(); md = (d / 'spec.md').read_text(encoding='utf-8')
    errs = []
    sym = table(md, '符號表')
    if sym is None: errs.append('缺少「## 符號表」')
    else:
        for r in sym:
            if not r.get('定義') or not r.get('出處'): errs.append(f"符號表：{r.get('符號')} 缺定義或出處")
    num = table(md, '數字表')
    if num is None: errs.append('缺少「## 數字表」')
    else:
        for r in num:
            v = r.get('驗算', '')
            if not r.get('出處代碼'): errs.append(f"數字表：{r.get('數字')} 缺出處代碼")
            if '✗' in v: errs.append(f"數字表：{r.get('數字')} 驗算不符")
            elif '✓' not in v and not re.search(r'無法驗算（.+）', v):
                errs.append(f"數字表：{r.get('數字')} 驗算欄需為 ✓、✗ 或「無法驗算（原因）」")
    gap = table(md, '缺失清單')
    if gap is None: errs.append('缺少「## 缺失清單」')
    else:
        for r in gap:
            if '必要' in r.get('重要性', '') and '未解決' in r.get('狀態', ''):
                errs.append(f"缺失清單：必要項目未解決 → {r.get('項目')}")
    vp = d / 'verify.py'
    if not vp.exists(): errs.append('缺少 verify.py')
    else:
        r = subprocess.run([sys.executable, '-I', str(vp)], capture_output=True, text=True, cwd=str(d))
        print(r.stdout.strip())
        if r.returncode != 0: errs.append('verify.py 未通過：' + (r.stderr.strip().splitlines() or ['(無訊息)'])[-1])
    print(json.dumps({'spec': str(d / 'spec.md'), 'symbols': len(sym or []), 'numbers': len(num or []),
                      'ok': not errs, 'errors': errs}, ensure_ascii=False, indent=1))
    return 0 if not errs else 1

if __name__ == '__main__':
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1]))
