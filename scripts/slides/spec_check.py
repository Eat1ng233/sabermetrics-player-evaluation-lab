#!/usr/bin/env python3
"""SOP-04 內容關卡（三種模式）

用法：
  python3 scripts/slides/spec_check.py outputs/slides/<slug>/            # N2d 內容關卡
  python3 scripts/slides/spec_check.py outputs/slides/<slug>/ --draft    # N3 毛片關卡
  python3 scripts/slides/spec_check.py outputs/slides/<slug>/ --render   # N4 渲染關卡

N2d（預設）：
  1. 符號表：每個符號都有定義與出處
  2. 數字表：每個數字都有出處代碼，驗算欄是 ✓ 或「無法驗算（原因）」，不可為 ✗
  3. verify.py：exit 0
  4. 缺失清單：允許有未解決項目（會帶進毛片），但每列都要有類別、重要性、狀態
--draft（N3，另外檢查）：
  5. draft.md 存在，且「頁面規劃」的每一頁都有對應的「### P.n」段落
  6. draft.md 有「缺失清單」與「需要補充的資料」兩節
--render（N4，另外檢查 5–6，以及）：
  7. spec.md 的 frontmatter 為 content_approved: true（只有使用者確認後才能改）
  8. 缺失清單每一列的狀態都是「已解決」或「接受（使用者確認）」
全部通過才以 exit code 0 結束。
"""
import re, subprocess, sys, pathlib, json

def section(md, heading):
    m = re.search(r'^##\s*(?:\d+\.\s*)?' + re.escape(heading) + r'\s*$(.*?)(?=^##\s|\Z)', md, re.M | re.S)
    return m.group(1) if m else None

def table(md, heading):
    body = section(md, heading)
    if body is None: return None
    rows = [l.strip() for l in body.splitlines() if l.strip().startswith('|')]
    if len(rows) < 2: return []
    head = [c.strip() for c in rows[0].strip('|').split('|')]
    return [dict(zip(head, [c.strip() for c in r.strip('|').split('|')])) for r in rows[2:]]

def frontmatter(md):
    m = re.match(r'^---\n(.*?)\n---', md, re.S)
    return dict(re.findall(r'^(\w+):\s*(.*)$', m.group(1), re.M)) if m else {}

def main(d, mode):
    d = pathlib.Path(d).resolve(); md = (d / 'spec.md').read_text(encoding='utf-8')
    errs, todo = [], []
    # ---- N2d ----
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
            if not (r.get('類別') and r.get('重要性') and r.get('狀態')):
                errs.append(f"缺失清單：{r.get('項目')} 缺類別、重要性或狀態")
            elif '未解決' in r['狀態']:
                todo.append(f"{r['重要性']}｜{r.get('項目')}")
    vp = d / 'verify.py'
    if not vp.exists(): errs.append('缺少 verify.py')
    else:
        r = subprocess.run([sys.executable, '-I', str(vp)], capture_output=True, text=True, cwd=str(d))
        print(r.stdout.strip())
        if r.returncode != 0:
            failed = [l.strip() for l in r.stdout.splitlines() if l.strip().startswith('✗')]
            errs += ['verify.py 未通過：' + l for l in failed] or ['verify.py 未通過：' + ((r.stderr.strip().splitlines() or ['(無訊息)'])[-1])]
    # ---- N3 毛片 ----
    if mode in ('draft', 'render'):
        dp = d / 'draft.md'
        if not dp.exists(): errs.append('缺少 draft.md（毛片）')
        else:
            dm = dp.read_text(encoding='utf-8')
            plan = table(md, '頁面規劃') or []
            pages = set()
            for r in plan:
                for a, b in re.findall(r'(\d+)(?:\s*[–-]\s*(\d+))?', r.get('頁', '')):
                    pages.update(range(int(a), int(b or a) + 1))
            have = {int(x) for x in re.findall(r'^###\s*P\.(\d+)', dm, re.M)}
            miss = sorted(pages - have)
            if miss: errs.append('毛片缺少頁面：' + '、'.join(f'P.{p}' for p in miss))
            for h in ('缺失清單', '需要補充的資料'):
                if section(dm, h) is None: errs.append(f'毛片缺少「## {h}」一節')
    # ---- N4 渲染 ----
    if mode == 'render':
        fm = frontmatter(md)
        if fm.get('content_approved', '').lower() != 'true':
            errs.append('內容尚未經使用者確認（spec.md 的 content_approved 不是 true）')
        for r in gap or []:
            s = r.get('狀態', '')
            if not ('已解決' in s or '接受（使用者確認）' in s):
                errs.append(f"缺失清單：「{r.get('項目')}」狀態為「{s}」，需為「已解決」或「接受（使用者確認）」")
    print(json.dumps({'spec': str(d / 'spec.md'), 'mode': mode, 'symbols': len(sym or []), 'numbers': len(num or []),
                      'open_items': todo, 'ok': not errs, 'errors': errs}, ensure_ascii=False, indent=1))
    return 0 if not errs else 1

if __name__ == '__main__':
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    mode = 'render' if '--render' in sys.argv else 'draft' if '--draft' in sys.argv else 'content'
    sys.exit(main(sys.argv[1], mode))
