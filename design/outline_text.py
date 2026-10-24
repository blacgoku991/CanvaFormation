"""Chiffres « en contour » convertis en tracés SVG (au lieu de -webkit-text-stroke).

Canva ne sait pas importer un texte en contour : il le remplit. Un tracé vectoriel, lui, arrive intact.
Usage : python3 design/outline_text.py   -> design/assets/numerals/<texte>-<couleur>.svg
"""
import pathlib
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

ROOT = pathlib.Path(__file__).resolve().parent
FONT = ROOT / 'fonts' / 'canva' / 'PlayfairDisplay-400.woff'
COLORS = {'bordeaux': '#7A2430', 'rose': '#D8B7AF', 'blanc': '#FFFFFF', 'taupe': '#A48A7B'}
TEXTS = ['01', '02', '03', '04', '1.5', '15']
STROKE = 7          # en unités de police (1000 par cadratin)
STROKE_PETIT = 20   # variante « -petit » pour les chiffres de 10 à 15 mm de haut (trait lisible à l'écran)
TRACKING = -20      # approche entre les chiffres


def outline(text, color, stroke=STROKE):
    font = TTFont(FONT)
    gs, cmap = font.getGlyphSet(), font.getBestCmap()
    x, paths, bounds = 0, [], None
    for ch in text:
        g = cmap[ord(ch)]
        g = g + '.lf' if g + '.lf' in gs else g        # chiffres alignés (les chiffres par défaut sont elzéviriens)
        pen = SVGPathPen(gs)
        gs[g].draw(pen)
        bp = BoundsPen(gs); gs[g].draw(bp)
        if bp.bounds:
            b = (bp.bounds[0] + x, bp.bounds[1], bp.bounds[2] + x, bp.bounds[3])
            bounds = b if bounds is None else (min(bounds[0], b[0]), min(bounds[1], b[1]), max(bounds[2], b[2]), max(bounds[3], b[3]))
        paths.append(f'<path transform="translate({x} 0)" d="{pen.getCommands()}"/>')
        x += gs[g].width + TRACKING
    m = stroke
    x0, y0, x1, y1 = bounds[0] - m, bounds[1] - m, bounds[2] + m, bounds[3] + m
    w, h = x1 - x0, y1 - y0
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}">'
            f'<g transform="translate({-x0:.0f} {y1:.0f}) scale(1 -1)" fill="none" stroke="{COLORS[color]}" stroke-width="{stroke}" stroke-linejoin="round">'
            + ''.join(paths) + '</g></svg>\n')


def main():
    out = ROOT / 'assets' / 'numerals'
    out.mkdir(parents=True, exist_ok=True)
    for t in TEXTS:
        for c in COLORS:
            (out / f"{t.replace('.', '-')}-{c}.svg").write_text(outline(t, c), encoding='utf-8')
            (out / f"{t.replace('.', '-')}-{c}-petit.svg").write_text(outline(t, c, STROKE_PETIT), encoding='utf-8')
    print(f'{2 * len(TEXTS) * len(COLORS)} fichiers -> {out}')


if __name__ == '__main__':
    main()
