// Moteur d'animation déterministe : renderFrame(t) place chaque élément pour l'instant t (en secondes).
// Aucune animation CSS n'est utilisée, pour que la capture image par image soit exacte.
(function () {
  const TL = window.TIMELINE;

  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const E = {
    lin: t => t,
    out3: t => 1 - Math.pow(1 - t, 3),
    in3: t => t * t * t,
    io3: t => (t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2),
    outExpo: t => (t >= 1 ? 1 : 1 - Math.pow(2, -10 * t)),
    ioExpo: t => (t <= 0 ? 0 : t >= 1 ? 1 : t < .5 ? Math.pow(2, 20 * t - 10) / 2 : (2 - Math.pow(2, -20 * t + 10)) / 2),
    outBack: t => { const c1 = 1.5, c3 = c1 + 1; return 1 + c3 * Math.pow(t - 1, 3) + c1 * Math.pow(t - 1, 2); },
  };
  const prog = (t, a, d) => clamp((t - a) / d);

  const ENTER_DUR = { fade: .8, 'wipe-left': 1.0, 'wipe-right': 1.0, 'wipe-up': 1.0, circle: 1.15, zoom: .9, none: 0 };

  const scenes = [];

  // Instant (secondes depuis le début de la scène) décrit par data-at :
  //   "1.2"            -> 1,2 s après le début de la scène
  //   "w:anagène@0.2"  -> au moment où la voix prononce « anagène » (+0,2 s) ; "w:cils#2" = 2e occurrence
  //   "vo", "voend@-1" -> début / fin de la voix ; "end@-1.5" -> 1,5 s avant la fin de la scène
  // Instant (depuis le début de la voix) où est prononcé le caractère idx du texte :
  // interpolé dans sa phrase quand les repères de phrase existent, sinon sur l'ensemble du texte.
  function voTime(d, idx) {
    const ph = d.phrases;
    if (ph && ph.length) {
      const p = ph.find(q => idx < q.i1) || ph[ph.length - 1];
      return p.t0 + clamp((idx - p.i0) / Math.max(1, p.i1 - p.i0)) * (p.t1 - p.t0);
    }
    return idx / d.vo.length * d.vo_dur;
  }

  // Délai entre le début de la scène et le début de sa voix (propre à chaque scène, voir timings.py).
  const lead = sc => sc.data.vo_start - sc.data.start;

  function parseAt(str, sc) {
    if (str == null || str === '') return null;
    const [base, offStr] = String(str).trim().split('@');
    const off = offStr ? parseFloat(offStr) : 0;
    if (base.startsWith('w:')) {
      let [word, nth] = base.slice(2).toLowerCase().split('#');
      nth = parseInt(nth || '1', 10);
      const vo = sc.data.vo.toLowerCase();
      let idx = -1;
      for (let k = 0; k < nth; k++) idx = vo.indexOf(word, idx + 1);
      if (idx < 0) console.warn('mot introuvable dans la voix :', word, sc.data.id);
      return lead(sc) + voTime(sc.data, Math.max(0, idx)) + off;
    }
    if (base === 'end') return sc.data.dur + off;
    if (base === 'vo') return lead(sc) + off;
    if (base === 'voend') return lead(sc) + sc.data.vo_dur + off;
    return parseFloat(base) + off;
  }

  function init() {
    TL.scenes.forEach((data, i) => {
      const el = document.getElementById('s-' + data.id);
      if (!el) throw new Error('scène absente : ' + data.id);
      el.style.zIndex = 10 + i;
      const sc = { data, el, enter: el.dataset.enter || 'fade', fx: [], kb: [], floats: [] };
      sc.enterDur = ENTER_DUR[sc.enter] ?? .8;
      // propagation des décalages (data-stagger)
      el.querySelectorAll('[data-stagger]').forEach(parent => {
        const base = parseAt(parent.dataset.at || '0.3', sc);
        const step = parseFloat(parent.dataset.stagger);
        let k = 0;
        parent.querySelectorAll(':scope > [data-fx]').forEach(ch => {
          if (!ch.dataset.at) ch.dataset.at = String((base + k * step).toFixed(3));
          k++;
        });
      });
      el.querySelectorAll('[data-fx]').forEach(node => {
        const f = {
          node, type: node.dataset.fx,
          at: parseAt(node.dataset.at || '0.3', sc),
          d: parseFloat(node.dataset.d || (node.dataset.fx === 'draw' ? 1.2 : .9)),
          dist: parseFloat(node.dataset.dist || 60),
          ease: E[node.dataset.ease || (node.dataset.fx === 'pop' ? 'outBack' : 'out3')],
          out: node.dataset.out != null ? parseAt(node.dataset.out, sc) : null,
        };
        if (f.type === 'draw') {
          let len = parseFloat(node.dataset.len || 0);
          if (!len && node.getTotalLength) len = node.getTotalLength();
          f.len = len || 1000;
          node.style.strokeDasharray = f.len + ' ' + f.len;
        }
        if (f.type === 'count') f.to = parseFloat(node.dataset.to);
        sc.fx.push(f);
      });
      el.querySelectorAll('[data-kb]').forEach(node => sc.kb.push({ node, mode: node.dataset.kb, amt: parseFloat(node.dataset.kbAmt || .12) }));
      el.querySelectorAll('[data-float]').forEach(node => sc.floats.push({ node, amp: parseFloat(node.dataset.float), ph: parseFloat(node.dataset.phase || 0) }));
      scenes.push(sc);
    });
  }

  function applyFx(f, lt) {
    let p = f.ease(prog(lt, f.at, f.d));
    let o = 1;
    if (f.out != null) o = 1 - E.io3(prog(lt, f.out, .6));
    const s = f.node.style;
    const D = f.dist;
    switch (f.type) {
      case 'up': s.opacity = p * o; s.transform = `translateY(${(1 - p) * D}px)`; break;
      case 'down': s.opacity = p * o; s.transform = `translateY(${-(1 - p) * D}px)`; break;
      case 'left': s.opacity = p * o; s.transform = `translateX(${(1 - p) * D}px)`; break;
      case 'right': s.opacity = p * o; s.transform = `translateX(${-(1 - p) * D}px)`; break;
      case 'fade': s.opacity = p * o; break;
      case 'blur': s.opacity = p * o; s.filter = `blur(${(1 - p) * 14}px)`; s.transform = `scale(${1.04 - .04 * p})`; break;
      case 'scale': s.opacity = p * o; s.transform = `scale(${.86 + .14 * p})`; break;
      case 'pop': s.opacity = clamp(p * 3) * o; s.transform = `scale(${.4 + .6 * p})`; break;
      case 'mask': // révélation masquée de bas en haut (texte qui monte dans sa ligne) ; marge haute finale pour les accents
        s.clipPath = `inset(${120 - 150 * p}% 0 -20% 0)`; s.transform = `translateY(${(1 - p) * D}px)`; s.opacity = o; break;
      case 'mask-x': s.clipPath = `inset(0 ${(1 - p) * 100}% 0 0)`; s.opacity = o; break;
      case 'width': s.transform = `scaleX(${p})`; s.opacity = o; break;
      case 'height': s.transform = `scaleY(${p})`; s.opacity = o; break;
      case 'draw': s.strokeDashoffset = f.len * (1 - p); s.opacity = (p > 0 ? 1 : 0) * o; break;
      case 'count': f.node.textContent = String(Math.round(p * f.to)); s.opacity = (lt >= f.at ? 1 : 0) * o; break;
      case 'track': s.opacity = p * o; s.letterSpacing = `${(f.dist / 100) * (1 - p) + parseFloat(f.node.dataset.ls || .2)}em`; s.filter = `blur(${(1 - p) * 8}px)`; break;
    }
  }

  function applyKb(k, lt, total) {
    const p = clamp(lt / total);
    const a = k.amt;
    let tr = '';
    switch (k.mode) {
      case 'in': tr = `scale(${1 + a - a * p})`; break;
      case 'out': tr = `scale(${1 + a * p})`; break;
      case 'left': tr = `scale(${1 + a}) translateX(${(.5 - p) * a * 50}%)`; break;
      case 'right': tr = `scale(${1 + a}) translateX(${(p - .5) * a * 50}%)`; break;
      case 'up': tr = `scale(${1 + a}) translateY(${(.5 - p) * a * 40}%)`; break;
      case 'scroll': tr = `translateY(${-E.io3(p) * a}px)`; break;
    }
    k.node.style.transform = tr;
  }

  function applyEnter(sc, lt) {
    const el = sc.el;
    const D = sc.enterDur;
    const p = sc === scenes[0] ? E.io3(prog(lt, 0, 1.4)) : D ? E.ioExpo(prog(lt, 0, D)) : 1;
    const inner = el.querySelector(':scope > .inner');
    el.style.clipPath = '';
    el.style.opacity = 1;
    el.style.transform = '';
    let bar = null;
    switch (sc.enter) {
      case 'fade': el.style.opacity = p; break;
      case 'zoom': el.style.opacity = p; el.style.transform = `scale(${1.06 - .06 * p})`; break;
      case 'wipe-left': el.style.clipPath = `inset(0 0 0 ${(1 - p) * 100}%)`; bar = { x: (1 - p) * 1920, v: true }; break;
      case 'wipe-right': el.style.clipPath = `inset(0 ${(1 - p) * 100}% 0 0)`; bar = { x: p * 1920, v: true }; break;
      case 'wipe-up': el.style.clipPath = `inset(${(1 - p) * 100}% 0 0 0)`; bar = { y: (1 - p) * 1080, v: false }; break;
      case 'circle': el.style.clipPath = `circle(${p * 125}% at 50% 52%)`; break;
    }
    if (inner) {
      const q = 1 - p;
      if (sc.enter === 'wipe-left') inner.style.transform = `translateX(${q * 160}px)`;
      else if (sc.enter === 'wipe-right') inner.style.transform = `translateX(${-q * 160}px)`;
      else if (sc.enter === 'wipe-up') inner.style.transform = `translateY(${q * 120}px)`;
      else if (sc.enter === 'circle') inner.style.transform = `scale(${1.08 - .08 * p})`;
      else inner.style.transform = '';
    }
    return (p > 0 && p < 1) ? bar : null;
  }

  const uiOn = sc => !!(sc && sc.data.partie && !/^p\d$/.test(sc.data.id));

  window.renderFrame = function (T) {
    const frame = Math.round(T * TL.fps);
    let wipeBar = null;
    let current = scenes[0];
    scenes.forEach((sc, i) => {
      const lt = T - sc.data.start;
      const next = scenes[i + 1];
      const visibleUntil = sc.data.dur + (next ? next.enterDur : 1);
      const visible = lt >= 0 && lt <= visibleUntil;
      sc.el.style.visibility = visible ? 'visible' : 'hidden';
      if (!visible) return;
      if (lt <= sc.data.dur) current = sc;
      const bar = applyEnter(sc, lt);
      if (bar) wipeBar = bar;
      sc.fx.forEach(f => applyFx(f, lt));
      sc.kb.forEach(k => applyKb(k, lt, visibleUntil));
      sc.floats.forEach(fl => { fl.node.style.translate = `0 ${Math.sin((T + fl.ph) * 1.1) * fl.amp}px`; });
    });

    // Interface commune : barre de transition, libellé de partie, progression, grain
    const wb = document.getElementById('wipebar');
    if (wipeBar) {
      wb.style.opacity = 1;
      if (wipeBar.v) { wb.style.width = '10px'; wb.style.height = '1080px'; wb.style.transform = `translate(${wipeBar.x - 5}px, 0)`; }
      else { wb.style.width = '1920px'; wb.style.height = '10px'; wb.style.transform = `translate(0, ${wipeBar.y - 5}px)`; }
    } else wb.style.opacity = 0;

    // Libellé de partie et logo : ils restent en place quand la partie ne change pas,
    // s'effacent au début d'une transition vers une ouverture, et réapparaissent une fois la transition posée.
    const ci = scenes.indexOf(current);
    const prev = scenes[ci - 1];
    const lt = T - current.data.start;
    const fadeOut = 1 - E.out3(prog(lt, 0, .35));
    const fadeIn = E.out3(prog(lt, current.enterDur * .85, .6));
    let uiOp = 0, partie = current.data.partie;
    if (!uiOn(current)) { if (uiOn(prev)) { uiOp = fadeOut; partie = prev.data.partie; } }
    else if (uiOn(prev) && prev.data.partie === current.data.partie) uiOp = 1;
    else if (uiOn(prev) && lt < .35) { uiOp = fadeOut; partie = prev.data.partie; }
    else uiOp = fadeIn;
    const endFade = 1 - prog(T, TL.total - .9, .7);
    document.getElementById('ui').style.opacity = uiOp * endFade;
    const label = document.getElementById('ui-part');
    if (label.textContent !== partie) label.textContent = partie;
    const pr = document.getElementById('progress');
    pr.style.transform = `scaleX(${T / TL.total})`;
    pr.style.opacity = endFade;
    const g = document.getElementById('grain');
    const gf = Math.floor(frame / 3);   // grain renouvelé toutes les 3 images : rendu pellicule, fichier plus léger
    g.style.backgroundPosition = `${(gf * 137) % 600}px ${(gf * 263) % 600}px`;
  };

  window.videoReady = (async () => {
    await document.fonts.ready;
    await Promise.all([...document.images].map(img => img.decode().catch(() => {})));
    init();
    window.renderFrame(0);
    return true;
  })();
})();
