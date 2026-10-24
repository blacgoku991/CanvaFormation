// Préparation « import Canva », exécutée dans la page juste avant l'impression PDF (voir render.js).
// Canva gère mal les masques de découpe d'un PDF. On les supprime donc sans changer l'aspect :
//  1. Photos : toute photo dont une partie seulement est visible (object-fit, débord masqué, coins ou arche
//     arrondis) est remplacée par une image déjà recadrée à la zone visible, arrondis et fond compris
//     (au plus 300 dpi, jamais agrandie au-delà du fichier d'origine).
//  2. Arches en filet (bordure arrondie ouverte en bas) : remplacées par un tracé SVG unique.
window.canvaProof = async function canvaProof(DPI = 300) {
  const CSS_PX_PER_IN = 96;
  const px = v => parseFloat(v) || 0;
  const transparent = c => !c || c === 'transparent' || /rgba\(.*,\s*0\)$/.test(c);
  const bgBehind = el => {
    for (let e = el.parentElement; e; e = e.parentElement) {
      const c = getComputedStyle(e).backgroundColor;
      if (!transparent(c)) return c;
    }
    return '#F7F2EC';
  };
  const radii = s => [px(s.borderTopLeftRadius), px(s.borderTopRightRadius), px(s.borderBottomRightRadius), px(s.borderBottomLeftRadius)];
  const rounded = s => radii(s).some(v => v > .5);
  const paddingBox = (e, s) => {
    const b = e.getBoundingClientRect();
    return [b.left + px(s.borderLeftWidth), b.top + px(s.borderTopWidth), b.right - px(s.borderRightWidth), b.bottom - px(s.borderBottomWidth)];
  };
  const report = { photos: 0, arches: 0 };

  // ---- 1. Photos recadrées
  const imgs = [...document.querySelectorAll('section.page img')].filter(i => i.naturalWidth && !/\.svg(\?|#|$)/i.test(i.src));
  for (const img of imgs) {
    const page = img.closest('section.page');
    const cs = getComputedStyle(img);
    if (cs.visibility === 'hidden' || cs.display === 'none') continue;
    let transformed = false;
    for (let e = img; e && e !== page; e = e.parentElement) if (getComputedStyle(e).transform !== 'none') { transformed = true; break; }
    if (transformed) continue;

    const r = img.getBoundingClientRect();
    const cl = r.left + px(cs.borderLeftWidth) + px(cs.paddingLeft);
    const ct = r.top + px(cs.borderTopWidth) + px(cs.paddingTop);
    const cw = r.width - px(cs.borderLeftWidth) - px(cs.borderRightWidth) - px(cs.paddingLeft) - px(cs.paddingRight);
    const ch = r.height - px(cs.borderTopWidth) - px(cs.borderBottomWidth) - px(cs.paddingTop) - px(cs.paddingBottom);
    if (cw < 1 || ch < 1) continue;
    const nw = img.naturalWidth, nh = img.naturalHeight;
    let dw = cw, dh = ch;
    if (cs.objectFit === 'cover' || cs.objectFit === 'contain' || cs.objectFit === 'scale-down') {
      let s = (cs.objectFit === 'cover' ? Math.max : Math.min)(cw / nw, ch / nh);
      if (cs.objectFit === 'scale-down') s = Math.min(1, s);
      dw = nw * s; dh = nh * s;
    } else if (cs.objectFit === 'none') { dw = nw; dh = nh; }
    const [opx, opy = '50%'] = cs.objectPosition.split(' ');
    const off = (v, free) => (v.endsWith('%') ? free * parseFloat(v) / 100 : px(v));
    const dx = cl + off(opx, cw - dw), dy = ct + off(opy, ch - dh);

    // Zone visible : boîte de contenu (object-fit y découpe) ∩ ancêtres qui masquent leur débord ∩ page
    let v = [Math.max(dx, cl), Math.max(dy, ct), Math.min(dx + dw, cl + cw), Math.min(dy + dh, ct + ch)];
    let shape = rounded(cs) ? img : null;
    for (let e = img.parentElement; e; e = e.parentElement) {
      const s = getComputedStyle(e);
      if (s.overflow !== 'visible' || e === page) {
        const b = paddingBox(e, s);
        v = [Math.max(v[0], b[0]), Math.max(v[1], b[1]), Math.min(v[2], b[2]), Math.min(v[3], b[3])];
        if (!shape && e !== page && rounded(s)) shape = e;
      }
      if (e === page) break;
    }
    // Forme arrondie avec un fond propre (ex. arche blanche autour d'un produit) : on recouvre toute la forme
    if (shape && shape !== img) {
      const s = getComputedStyle(shape);
      if (!transparent(s.backgroundColor)) {
        const b = shape.getBoundingClientRect(), pr = page.getBoundingClientRect();
        v = [Math.max(b.left, pr.left), Math.max(b.top, pr.top), Math.min(b.right, pr.right), Math.min(b.bottom, pr.bottom)];
      }
    }
    if (v[2] - v[0] < 2 || v[3] - v[1] < 2) continue;
    const whole = Math.abs(v[0] - dx) < .5 && Math.abs(v[1] - dy) < .5 && Math.abs(v[2] - dx - dw) < .5 && Math.abs(v[3] - dy - dh) < .5;
    if (whole && !shape) continue;                       // rien n'est masqué : on laisse la photo telle quelle

    // Taille de sortie : 300 dpi au plus, sans dépasser la définition du fichier d'origine
    const vw = v[2] - v[0], vh = v[3] - v[1];
    const nativePerCss = nw / dw;                        // pixels source par pixel CSS
    const k = Math.min(nativePerCss, DPI / CSS_PX_PER_IN);
    const ow = Math.max(1, Math.round(vw * k)), oh = Math.max(1, Math.round(vh * k));
    const cv = document.createElement('canvas');
    cv.width = ow; cv.height = oh;
    const ctx = cv.getContext('2d');
    ctx.imageSmoothingQuality = 'high';
    const png = /\.png(\?|#|$)/i.test(img.src);
    if (shape) {
      const s = getComputedStyle(shape);
      if (!png) { ctx.fillStyle = bgBehind(shape); ctx.fillRect(0, 0, ow, oh); }
      const b = shape === img ? r : shape.getBoundingClientRect();
      ctx.save();
      ctx.beginPath();
      ctx.roundRect((b.left - v[0]) * k, (b.top - v[1]) * k, b.width * k, b.height * k, radii(s).map(x => x * k));
      ctx.clip();
      if (shape !== img && !transparent(s.backgroundColor)) { ctx.fillStyle = s.backgroundColor; ctx.fillRect(0, 0, ow, oh); }
    }
    ctx.drawImage(img, 0, 0, nw, nh, (dx - v[0]) * k, (dy - v[1]) * k, dw * k, dh * k);
    if (shape) ctx.restore();

    // Nouvelle image à la même place (même parent, positionnée), l'ancienne est masquée sans bouger la mise en page
    const out = document.createElement('img');
    out.src = cv.toDataURL(png ? 'image/png' : 'image/jpeg', .92);
    out.alt = img.alt;
    let cb = img.parentElement;
    while (cb && cb !== page && getComputedStyle(cb).position === 'static') cb = cb.parentElement;
    if (getComputedStyle(cb).position === 'static') cb.style.position = 'relative';
    const cbr = cb.getBoundingClientRect(), cbs = getComputedStyle(cb);
    Object.assign(out.style, {
      position: 'absolute', margin: '0', padding: '0', border: '0', maxWidth: 'none', maxHeight: 'none', objectFit: 'fill',
      left: (v[0] - cbr.left - px(cbs.borderLeftWidth)) + 'px', top: (v[1] - cbr.top - px(cbs.borderTopWidth)) + 'px',
      width: vw + 'px', height: vh + 'px',
    });
    if (cs.zIndex !== 'auto') out.style.zIndex = cs.zIndex;
    img.after(out);
    img.style.visibility = 'hidden';
    if (shape && shape !== img) { shape.style.borderRadius = '0'; shape.style.backgroundColor = 'transparent'; }
    report.photos++;
  }
  await Promise.all([...document.images].map(i => (i.decode ? i.decode().catch(() => {}) : null)));

  // ---- 2. Arches en filet
  const NS = 'http://www.w3.org/2000/svg';
  for (const el of document.querySelectorAll('section.page *')) {
    if (el instanceof SVGElement) continue;
    const s = getComputedStyle(el);
    const bt = px(s.borderTopWidth), bb = s.borderBottomStyle === 'none' ? 0 : px(s.borderBottomWidth);
    const rl = px(s.borderTopLeftRadius), rr = px(s.borderTopRightRadius);
    if (!(bt > 0 && s.borderTopStyle !== 'none' && bb === 0 && (rl > .5 || rr > .5))) continue;
    const w = el.offsetWidth, h = el.offsetHeight;
    const bl = s.borderLeftStyle === 'none' ? 0 : px(s.borderLeftWidth), br = s.borderRightStyle === 'none' ? 0 : px(s.borderRightWidth);
    const b = bt;
    const r1 = Math.min(rl, w / 2, h), r2 = Math.min(rr, w / 2, h);
    const a1 = Math.max(.1, r1 - b / 2), a2 = Math.max(.1, r2 - b / 2);
    let d = bl ? `M ${b / 2} ${h} V ${r1}` : `M ${b / 2} ${r1}`;
    d += ` A ${a1} ${a1} 0 0 1 ${r1} ${b / 2} H ${w - r2} A ${a2} ${a2} 0 0 1 ${w - b / 2} ${r2}`;
    if (br) d += ` V ${h}`;
    const svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('width', w); svg.setAttribute('height', h); svg.setAttribute('viewBox', `0 0 ${w} ${h}`);
    Object.assign(svg.style, { position: 'absolute', left: (-bl) + 'px', top: (-bt) + 'px', overflow: 'visible', pointerEvents: 'none' });
    const path = document.createElementNS(NS, 'path');
    path.setAttribute('d', d); path.setAttribute('fill', 'none');
    path.setAttribute('stroke', s.borderTopColor); path.setAttribute('stroke-width', b);
    svg.appendChild(path);
    // La bordure disparaît, remplacée par un rembourrage équivalent : la mise en page ne bouge pas
    el.style.paddingTop = (px(s.paddingTop) + bt) + 'px';
    el.style.paddingLeft = (px(s.paddingLeft) + bl) + 'px';
    el.style.paddingRight = (px(s.paddingRight) + br) + 'px';
    el.style.border = '0';
    el.style.borderRadius = '0';
    if (s.position === 'static') el.style.position = 'relative';
    el.prepend(svg);
    report.arches++;
  }
  return report;
};
