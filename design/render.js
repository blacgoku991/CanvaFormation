// Rend un fichier HTML en PDF (A4 paysage) et signale les débordements de mise en page.
// Usage : node design/render.js <entrée.html> <sortie.pdf>
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [input, output] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(input), { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);

  const problems = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll('section.page').forEach((sec, i) => {
      const id = sec.dataset.id || `#${i + 1}`;
      const box = sec.getBoundingClientRect();
      // Zones qui débordent de leur propre cadre
      sec.querySelectorAll('.content, [data-fit]').forEach(el => {
        if (el.scrollHeight > el.clientHeight + 2 || el.scrollWidth > el.clientWidth + 2) {
          out.push(`page ${i + 1} (${id}) : ${el.className || el.tagName} déborde de ${el.scrollHeight - el.clientHeight}px en hauteur / ${el.scrollWidth - el.clientWidth}px en largeur`);
        }
      });
      // Texte qui sort de la page
      sec.querySelectorAll('p, li, td, th, h1, h2, h3, h4, .h-sub, .h-title, .alert, .card').forEach(el => {
        const r = el.getBoundingClientRect();
        if (r.width === 0 || r.height === 0) return;
        if (r.bottom > box.bottom + 1 || r.right > box.right + 1 || r.left < box.left - 1 || r.top < box.top - 1) {
          out.push(`page ${i + 1} (${id}) : « ${el.textContent.trim().slice(0, 50)} » sort de la page`);
        }
      });
    });
    return out;
  });
  problems.forEach(p => console.log('DÉBORDEMENT', p));

  await page.pdf({ path: output, preferCSSPageSize: true, printBackground: true });
  await browser.close();
})();
