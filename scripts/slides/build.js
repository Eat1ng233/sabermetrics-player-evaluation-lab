#!/usr/bin/env node
// SOP-04 節點 N5：建置
// 用法：node scripts/slides/build.js <src.html> <out.html>
// - 把 $$…$$（區塊）與 \(…\)（行內）用 KaTeX 預先轉譯成 HTML
// - 把 KaTeX 字型與像素字型以 base64 內嵌，產出可離線開啟的單一檔案
// - 有任何公式錯誤就以 exit code 1 結束（不輸出半成品）
const fs = require('fs');
const path = require('path');
const [, , src, out] = process.argv;
if (!src || !out) { console.error('用法：node build.js <src.html> <out.html>'); process.exit(2); }

const here = __dirname;
const nm = path.join(here, 'node_modules');
let katex;
try { katex = require(path.join(nm, 'katex')); }
catch (e) { console.error('找不到 katex。請先在 scripts/slides 執行：npm install'); process.exit(2); }

// 渲染關卡：工作資料夾裡有 spec.md 時，必須已經過使用者確認（SOP-04 N3 → N4）
const specPath = path.join(path.dirname(path.resolve(src)), 'spec.md');
if (fs.existsSync(specPath)) {
  const fm = (fs.readFileSync(specPath, 'utf8').match(/^---\n([\s\S]*?)\n---/) || [, ''])[1];
  if (!/^content_approved:\s*true\s*$/m.test(fm)) {
    console.error('內容尚未經使用者確認：請先交付毛片（draft.md），使用者確認後把 spec.md 的 content_approved 設為 true。');
    process.exit(1);
  }
}

let html = fs.readFileSync(src, 'utf8');

// 版面規則（由過去的目視檢查往前移到建置階段）：
// - 禁用 \tfrac：在投影片上字太小（woba-to-wrc-plus v1、war-explained v1 都發生過）
const lint = [];
html.split('\n').forEach((line, i) => { if (/\\tfrac/.test(line)) lint.push(`第 ${i + 1} 行使用 \\tfrac（請改用 \\dfrac）`); });
if (lint.length) { console.error(`版面規則錯誤 ${lint.length} 個：`); lint.forEach(e => console.error('  - ' + e)); process.exit(1); }
const dist = path.join(nm, 'katex', 'dist');
let css = fs.readFileSync(path.join(dist, 'katex.min.css'), 'utf8');
css = css.replace(/src:([^;}]*)/g, (m, srcs) => {
  const w = srcs.match(/url\((fonts\/[^)]+\.woff2)\)/);
  if (!w) return m;
  const b = fs.readFileSync(path.join(dist, w[1])).toString('base64');
  return `src:url(data:font/woff2;base64,${b}) format("woff2")`;
});
const ff = (name, rel) => {
  const p = path.join(nm, '@fontsource', rel);
  return `@font-face{font-family:"${name}";src:url(data:font/woff2;base64,${fs.readFileSync(p).toString('base64')}) format("woff2");font-display:swap}`;
};
html = html.replace('/*KATEX_CSS*/', css);
html = html.replace('/*PIXEL_FONTS*/',
  ff('Press Start 2P', 'press-start-2p/files/press-start-2p-latin-400-normal.woff2') +
  ff('VT323', 'vt323/files/vt323-latin-400-normal.woff2'));

const errors = [];
let n = 0;
const render = (tex, display) => {
  n++;
  try { return katex.renderToString(tex.trim(), { displayMode: display, throwOnError: true, strict: false, output: 'html' }); }
  catch (e) { errors.push(`${display ? '$$' : '\\('} ${tex.trim().slice(0, 60)} … → ${e.message}`); return `<span class="katex-error">${tex}</span>`; }
};
html = html.replace(/\$\$([\s\S]+?)\$\$/g, (m, t) => render(t, true));
html = html.replace(/\\\(([\s\S]+?)\\\)/g, (m, t) => render(t, false));

if (errors.length) {
  console.error(`公式錯誤 ${errors.length} 個：`); errors.forEach(e => console.error('  - ' + e));
  process.exit(1);
}
fs.writeFileSync(out, html);
console.log(JSON.stringify({ ok: true, formulas: n, sizeKB: Math.round(html.length / 1024), out }));
