#!/usr/bin/env python3
"""SOP-04 節點 N6：版面檢查

用法：python3 scripts/slides/check.py <deck.html> [--shots <資料夾>]

逐頁開啟簡報並檢查，全部通過才以 exit code 0 結束：
  1. overflow   ：內容超出投影片範圍（檢查時會關閉 flex 壓縮，避免溢出被「壓扁重疊」掩蓋）
  2. katex      ：殘留的 .katex-error
  3. pixel_cjk  ：像素字體（Press Start 2P / VT323）裡直接出現中文字（應包 .zh）
  4. empty      ：沒有標題（h1/h2）的頁面
  5. fo_clip    ：SVG foreignObject（流程圖箭頭標籤）裡的內容超出框高被裁掉
                 （war-explained 第一次渲染時 P.4「第 2 步」被裁掉，前四項都沒抓到）
結果以 JSON 輸出；--shots 會存每頁截圖，供目視檢查（節點 N6 的人工部分）。

需要：pip install playwright && python3 -m playwright install chromium
（或以環境變數 CHROME_PATH 指定已安裝的 Chrome）
"""
import asyncio, json, os, sys, pathlib

JS = r"""
() => {
  const s = document.querySelector('.slide.active');
  const body = s.querySelector('.body') || s;
  // 以整張投影片為邊界：內容溢出時 .body 會被撐大，不能拿它當基準
  const sr = s.getBoundingClientRect();
  const pad = parseFloat(getComputedStyle(body).paddingBottom) * (sr.width / s.offsetWidth) * 0.5;
  const r = {bottom: sr.bottom - pad, right: sr.right - 4};
  const out = {overflow: [], katex: 0, pixel_cjk: [], empty: false, fo_clip: []};
  body.querySelectorAll('*').forEach(e => {
    if (e.closest('svg') && !e.closest('foreignObject')) return;
    const q = e.getBoundingClientRect();
    if (q.width && (q.bottom > r.bottom + 1 || q.right > r.right + 1))
      out.overflow.push((e.className && e.className.baseVal === undefined ? e.tagName + '.' + e.className : e.tagName) + ` (+${Math.round(Math.max(q.bottom - r.bottom, q.right - r.right))}px)`);
  });
  out.katex = s.querySelectorAll('.katex-error').length;
  const cjk = /[㐀-鿿＀-￯　-〿]/;
  s.querySelectorAll('*').forEach(e => {
    const f = getComputedStyle(e).fontFamily;
    if (!/Press Start 2P|VT323/.test(f)) return;
    for (const n of e.childNodes) if (n.nodeType === 3 && cjk.test(n.textContent))
      out.pixel_cjk.push(e.tagName + ': ' + n.textContent.trim().slice(0, 20));
  });
  out.empty = !s.querySelector('h1, h2');
  s.querySelectorAll('foreignObject').forEach(fo => {
    const fr = fo.getBoundingClientRect();
    fo.querySelectorAll('*').forEach(e => {
      const q = e.getBoundingClientRect();
      if (q.height && (q.bottom > fr.bottom + 1 || q.right > fr.right + 1))
        out.fo_clip.push((e.className || e.tagName) + ': ' + (e.textContent || '').trim().slice(0, 16) + ` (+${Math.round(Math.max(q.bottom - fr.bottom, q.right - fr.right))}px)`);
    });
  });
  out.fo_clip = out.fo_clip.slice(0, 5);
  out.overflow = out.overflow.slice(0, 5);
  return out;
}
"""

async def main(deck, shots):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        kw = {'args': ['--no-sandbox']}
        if os.environ.get('CHROME_PATH'): kw['executable_path'] = os.environ['CHROME_PATH']
        b = await p.chromium.launch(**kw)
        pg = await b.new_page(viewport={'width': 1300, 'height': 800})
        await pg.goto(pathlib.Path(deck).resolve().as_uri() + '#1')
        await pg.wait_for_timeout(600)
        # 關閉 flex 壓縮：否則內容過多時子元素會被壓扁、互相重疊，而不會表現為溢出
        await pg.add_style_tag(content='.body > *, .body .grid2 > *, .body .grid3 > * {flex-shrink:0 !important}')
        n = await pg.evaluate("document.querySelectorAll('.slide').length")
        report, fails = [], 0
        for k in range(n):
            await pg.evaluate(f"window.__show && window.__show({k})")
            await pg.wait_for_timeout(120)
            o = await pg.evaluate(JS)
            bad = bool(o['overflow'] or o['katex'] or o['pixel_cjk'] or o['empty'] or o['fo_clip'])
            fails += bad
            report.append({'page': k + 1, 'ok': not bad, **{kk: v for kk, v in o.items() if v}})
            if shots:
                os.makedirs(shots, exist_ok=True)
                await pg.screenshot(path=os.path.join(shots, f'p{k+1:02d}.png'))
        await b.close()
    print(json.dumps({'deck': deck, 'pages': n, 'failed_pages': fails,
                      'problems': [r for r in report if not r['ok']]}, ensure_ascii=False, indent=1))
    return 0 if fails == 0 else 1

if __name__ == '__main__':
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    shots = sys.argv[sys.argv.index('--shots') + 1] if '--shots' in sys.argv else None
    sys.exit(asyncio.run(main(sys.argv[1], shots)))
