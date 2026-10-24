// Rendu image par image de la vidéo (Chromium + ffmpeg).
// Usage :
//   node video/render.js stills 3.5 12 40       -> PNG aux instants donnés (video/_stills/)
//   node video/render.js video sortie.mp4 [début] [fin]   -> MP4 muet 1920×1080 à 30 i/s
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

const ROOT = __dirname;

async function open() {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  page.on('console', m => { if (m.type() === 'warning' || m.type() === 'error') console.log('[page]', m.text()); });
  page.on('pageerror', e => console.log('[page error]', e.message));
  await page.goto('file://' + path.join(ROOT, 'index.html'), { waitUntil: 'load' });
  await page.evaluate(() => window.videoReady);
  return { browser, page };
}

async function stills(times) {
  const { browser, page } = await open();
  const out = path.join(ROOT, '_stills');
  fs.mkdirSync(out, { recursive: true });
  for (const t of times) {
    await page.evaluate(t => window.renderFrame(t), t);
    const file = path.join(out, `t${String(t).padStart(6, '0')}.png`);
    await page.screenshot({ path: file, clip: { x: 0, y: 0, width: 1920, height: 1080 } });
    console.log(file);
  }
  await browser.close();
}

async function video(outFile, from, to) {
  const { browser, page } = await open();
  const tl = await page.evaluate(() => window.TIMELINE);
  const fps = tl.fps;
  const start = from ?? 0;
  const end = to ?? tl.total;
  const n = Math.round((end - start) * fps);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', outFile], { stdio: ['pipe', 'inherit', 'inherit'] });
  const t0 = Date.now();
  for (let i = 0; i < n; i++) {
    const t = start + i / fps;
    await page.evaluate(t => window.renderFrame(t), t);
    const buf = await page.screenshot({ type: 'jpeg', quality: 95, clip: { x: 0, y: 0, width: 1920, height: 1080 } });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 150 === 0) console.log(`image ${i}/${n} (${((Date.now() - t0) / 1000).toFixed(0)} s)`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await browser.close();
  console.log(`${n} images -> ${outFile} en ${((Date.now() - t0) / 1000).toFixed(0)} s`);
}

(async () => {
  const [mode, ...args] = process.argv.slice(2);
  if (mode === 'stills') await stills(args.map(Number));
  else if (mode === 'video') await video(args[0], args[1] != null ? Number(args[1]) : null, args[2] != null ? Number(args[2]) : null);
  else console.log('mode inconnu');
})();
