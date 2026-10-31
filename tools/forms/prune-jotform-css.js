// Builds the self-hosted Fog waiver stylesheet from what Jotform is currently serving.
//
// What it does:
//   1. Loads the live form and pulls out the custom CSS rules (everything from the
//      `--fog-blue` variables onward in Jotform's combined <style>).
//   2. Re-scopes every selector so it is safe as an external @import:
//        html body ...  ->  html.supernova body ...   (live form only; the builder's <html> has no class)
//        anything else  ->  .supernova ...            (live form AND the builder canvas)
//   3. Loads four copies of the form (original/candidate x desktop/phone) and checks the
//      candidate renders identically on every element, page and width.
//   4. Greedily removes rules that change nothing, keeping state-dependent rules
//      (hover, focus, errors, review screen, disabled Next) and the builder-only block.
//   5. Writes the result to docs/assets/forms/fog-waiver.css.
//
// Usage:  node tools/forms/prune-jotform-css.js [--no-prune]
// Needs:  playwright (Chromium). Nothing is ever submitted: the script only reads styles.

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const FORM = 'https://form.jotform.com/263017776830057';
const OUT = path.join(__dirname, '..', '..', 'docs', 'assets', 'forms', 'fog-waiver.css');
const EXTRA = path.join(__dirname, 'extra-rules.css');   // fixes: must keep the render identical (checked)
const FEATURES = path.join(__dirname, 'features.css');    // new behaviour: added after the check
const PRUNE = !process.argv.includes('--no-prune');

const KEEP = /hover|focus|active|checked|error|previewContainer|previewButtons|checkSubmission|backToForm|printForm|form-field-hidden|js-non-displayed|placeholder|disabled|invalid|required|prefers-reduced|#cid_171 \.form-header|#id_200 p|\.form-all li \.form-label|\.form-all #id_59, |\.form-all \.form-textbox|#cid_171 \.form-subHeader/;

// Rules on the page root itself look redundant in a top-level tab but matter when the form is embedded in an iframe.
const ROOT = /(^|,\s*)(html\.supernova|html\.supernova body|html\.supernova body::(before|after))\s*(,|$)/;

const PROPS = ['display','position','top','left','width','height','margin-top','margin-right','margin-bottom','margin-left','padding-top','padding-right','padding-bottom','padding-left','border-top-width','border-left-width','border-top-color','border-left-color','background-color','background-image','color','font-size','font-weight','font-family','letter-spacing','text-transform','line-height','grid-template-columns','flex-direction','flex-wrap','gap','transform','opacity','overflow-y','z-index','box-shadow','max-width','pointer-events','text-align','border-radius','content'];

async function frame(browser, width) {
  const page = await browser.newPage({ viewport: { width, height: 840 } });
  await page.goto(FORM, { waitUntil: 'load' });
  await page.waitForTimeout(3000);
  return page;
}

// Runs inside the page: helpers shared by every frame.
const HELPERS = () => {
  window.__split = (sel) => { const out = []; let d = 0, cur = ''; for (const ch of sel) { if (ch === '(' || ch === '[') d++; if (ch === ')' || ch === ']') d--; if (ch === ',' && d === 0) { out.push(cur.trim()); cur = ''; } else cur += ch; } if (cur.trim()) out.push(cur.trim()); return out; };
  window.__pref = (s) => { if (/^:root\b/.test(s)) return s; if (/^html\s+body\b/.test(s)) return s.replace(/^html\s+body/, 'html.supernova body'); if (/^html\b/.test(s)) return s.replace(/^html/, 'html.supernova'); if (/^body\b/.test(s)) return 'html.supernova ' + s; return '.supernova ' + s; };
  window.__ourStyle = () => [...document.querySelectorAll('style')].find(x => x.textContent.includes('--sb-gray-50'));
  window.__show = (k) => { const secs = [...document.querySelectorAll('ul.form-section')]; secs.forEach((s, i) => s.style.display = i === k ? '' : 'none'); if (k > 0) secs[0].classList.add('js-non-displayed-page'); else secs[0].classList.remove('js-non-displayed-page'); };
  window.__snap = (props, pseudos) => { const els = [document.documentElement, ...document.body.querySelectorAll('*')]; const out = []; for (const e of els) { if (e.tagName === 'STYLE' || e.tagName === 'SCRIPT' || (e !== document.documentElement && e !== document.body && e.closest('[style*="display: none"], .form-field-hidden') && !e.getClientRects().length && e.tagName === 'IFRAME')) { for (const ps of pseudos) out.push(''); continue; } for (const ps of pseudos) { const c = getComputedStyle(e, ps); out.push(props.map(p => c.getPropertyValue(p)).join('|')); } } return out; };
};

(async () => {
  const browser = await chromium.launch();
  const oD = await frame(browser, 1272), oM = await frame(browser, 390);
  const cD = await frame(browser, 1272), cM = await frame(browser, 390);
  for (const p of [oD, oM, cD, cM]) await p.evaluate(HELPERS);

  // 1-2. extract + rescope (in the desktop original)
  const extra = fs.existsSync(EXTRA) ? fs.readFileSync(EXTRA, 'utf8') : '';
  const cand = await oD.evaluate(() => {
    const sh = window.__ourStyle().sheet; const top = [...sh.cssRules];
    const first = top.findIndex(r => r.cssText.includes('--fog-blue'));
    const tmp = new CSSStyleSheet(); tmp.replaceSync(top.slice(first).map(r => r.cssText).join('\n'));
    const xf = (rules) => { for (const r of rules) { if (r.selectorText) r.selectorText = window.__split(r.selectorText).map(window.__pref).join(', '); else if (r.cssRules) xf(r.cssRules); } };
    xf(tmp.cssRules);
    return [...tmp.cssRules].map(r => r.cssText);
  });

  // install the candidate in place of the inline rules (as an @import would sit: before Jotform's theme rules)
  const install = (rules) => {
    const st = window.__ourStyle(); const sh = st.sheet;
    const first = [...sh.cssRules].findIndex(r => r.cssText.includes('--fog-blue'));
    for (let i = sh.cssRules.length - 1; i >= first; i--) sh.deleteRule(i);
    const c = document.createElement('style'); c.id = 'cand'; st.parentNode.insertBefore(c, st); c.textContent = rules.join('\n');
  };
  await cD.evaluate(install, cand); await cM.evaluate(install, cand);

  const pairs = [[oD, cD], [oM, cM]];
  async function same(props, pseudos, report) {
    for (const [o, c] of pairs) for (const k of [0, 1, 2]) {
      await o.evaluate(k => window.__show(k), k); await c.evaluate(k => window.__show(k), k);
      const a = await o.evaluate(([p, s]) => window.__snap(p, s), [props, pseudos]);
      const b = await c.evaluate(([p, s]) => window.__snap(p, s), [props, pseudos]);
      if (a.length !== b.length) return false;
      for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) {
        if (report) { const lab = await c.evaluate(([i, n]) => { const els = [document.documentElement, ...document.body.querySelectorAll('*')]; const e = els[Math.floor(i / n)]; if (!e) return '?'; const li = e.closest && e.closest('li'); return e.tagName + '#' + e.id + '.' + String(e.className).slice(0, 40) + ' in li#' + (li ? li.id : '-') + ' pseudo#' + (i % n); }, [i, pseudos.length]); console.error('  element:', lab); const pa = a[i].split('|'), pb = b[i].split('|'); const d = props.map((pr, j) => pa[j] !== pb[j] ? pr + ': ' + pa[j] + ' -> ' + pb[j] : null).filter(Boolean); console.error('diff page', k, (o === oD ? 'desktop' : 'phone'), 'slot', i, d.slice(0, 4).join('; ')); }
        return false; }
    }
    return true;
  }

  const ALLP = [null, '::before', '::after'];
  if (!(await same(PROPS, ALLP))) { console.error('Rescoped candidate differs from live before pruning. Stopping.'); process.exit(1); }
  console.log('Rescoped candidate matches live:', cand.length, 'rules');

  // 4. greedy prune, last rule first
  if (PRUNE) {
    const work = await cD.evaluate(() => { const s = document.getElementById('cand').sheet; const w = []; [...s.cssRules].forEach((r, i) => { if (r.cssRules && !r.selectorText) [...r.cssRules].forEach((_, j) => w.push([i, j])); else if (r.selectorText) w.push([i]); }); return w.reverse(); });
    let removed = 0;
    for (const p of work) {
      const info = await cD.evaluate(p => { const s = document.getElementById('cand').sheet; const r = p.length === 1 ? s.cssRules[p[0]] : s.cssRules[p[0]].cssRules[p[1]]; return { sel: r.selectorText, props: [...r.style], text: r.cssText }; }, p);
      if (!info.sel || KEEP.test(info.sel) || ROOT.test(info.sel) || info.props.some(x => x.startsWith('--'))) continue;
      const props = info.props.filter(x => !x.startsWith('--')); if (!props.length) continue;
      const pseudos = /::?(before|after)/.test(info.sel) ? ALLP : [null];
      const del = p => { const s = document.getElementById('cand').sheet; if (p.length === 1) s.deleteRule(p[0]); else s.cssRules[p[0]].deleteRule(p[1]); };
      const ins = ([p, t]) => { const s = document.getElementById('cand').sheet; if (p.length === 1) s.insertRule(t, p[0]); else s.cssRules[p[0]].insertRule(t, p[1]); };
      await cD.evaluate(del, p); await cM.evaluate(del, p);
      if (await same(props, pseudos)) removed++;
      else { await cD.evaluate(ins, [p, info.text]); await cM.evaluate(ins, [p, info.text]); }
    }
    console.log('Removed', removed, 'rules that changed nothing');
  }
  // Add extra-rules.css, then re-check everything (rules can prop each other up).
  if (extra) {
    const addExtra = (css) => { const t = new CSSStyleSheet(); t.replaceSync(css); const s = document.getElementById('cand').sheet; for (const r of t.cssRules) s.insertRule(r.cssText, s.cssRules.length); };
    await cD.evaluate(addExtra, extra); await cM.evaluate(addExtra, extra);
  }
  if (!(await same(PROPS, ALLP, true))) { console.error('Final candidate differs from live. Not writing the file.'); process.exit(1); }
  console.log('Final candidate matches live on every element, page and width');

  if (fs.existsSync(FEATURES)) {
    const feat = fs.readFileSync(FEATURES, 'utf8');
    const addF = (css) => { const t = new CSSStyleSheet(); t.replaceSync(css); const s = document.getElementById('cand').sheet; for (const r of t.cssRules) s.insertRule(r.cssText, s.cssRules.length); };
    await cD.evaluate(addF, feat);
  }
  let rules = await cD.evaluate(() => [...document.getElementById('cand').sheet.cssRules].filter(r => !(r.cssRules && !r.selectorText && r.cssRules.length === 0)).map(r => r.cssText));
  const header = `/* Fog Rugby liability waiver (Jotform 263017776830057), self-hosted styles.
   Built by tools/forms/prune-jotform-css.js from the live form, then pruned and verified.
   Scoping: "html.supernova body ..." rules apply to the live form only;
            ".supernova ..." rules apply to the live form and the Jotform builder canvas.
   Jotform's Inject Custom CSS box holds only the @import for this file. */
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600;700;800&display=swap');
`;
  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  fs.writeFileSync(OUT, header + rules.join('\n') + '\n');
  console.log('Wrote', OUT, fs.statSync(OUT).size, 'bytes');
  await browser.close();
})();
