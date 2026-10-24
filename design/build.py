"""Assemble les pages HTML du manuel puis produit le PDF et les aperçus PNG.

Usage :
  python3 design/build.py [manuel|corrige]            # document complet -> livrables/
  python3 design/build.py manuel --only=070,080 --tag=lot3
      # aperçu partiel (pages dont le nom commence par 070 ou 080)
      # -> design/_work/lot3/ (PDF + PNG), sans toucher aux livrables
Options : --no-png
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
PROJECT = ROOT.parent
DOCS = {
    'manuel': (ROOT / 'pages', 'Manuel-Dolce-Lash-Brow.pdf', 'Dolce Lash & Brow — Manuel de formation'),
    'corrige': (ROOT / 'corrige', 'Corrige-QCM-Formatrice.pdf', 'Dolce Lash & Brow — Corrigé du QCM'),
}

HEAD = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{title}</title>
<link rel="stylesheet" href="fonts/fonts.css">
<link rel="stylesheet" href="styles.css">
</head>
<body>
{body}
</body>
</html>
"""


def option(name):
    for a in sys.argv[1:]:
        if a.startswith(f'--{name}='):
            return a.split('=', 1)[1]
    return None


def build(doc, png=True, only=None, tag=None):
    pages_dir, pdf_name, title = DOCS[doc]
    fragments = sorted(pages_dir.glob('*.html'))
    if only:
        prefixes = tuple(only.split(','))
        fragments = [f for f in fragments if f.name.startswith(prefixes)]
    body = '\n'.join(f.read_text(encoding='utf-8') for f in fragments)

    # Numéros de page : {{p:identifiant}} -> numéro de la section data-id="identifiant"
    tags = re.findall(r'<section[^>]*class="[^"]*\bpage\b[^"]*"[^>]*>', body)
    numbers = {}
    for i, t in enumerate(tags, start=1):
        m = re.search(r'data-id="([^"]+)"', t)
        if m:
            numbers[m.group(1)] = i
    missing = set()

    def repl(m):
        key = m.group(1)
        if key not in numbers:
            missing.add(key)
            return '??'
        return f'{numbers[key]:02d}'

    body = re.sub(r'\{\{p:([\w-]+)\}\}', repl, body)
    if missing and not only:
        print('ATTENTION renvois de page introuvables :', ', '.join(sorted(missing)))

    if tag:
        out_dir = ROOT / '_work' / tag
        html_path = ROOT / f'_work-{tag}.html'
    else:
        out_dir = PROJECT / 'livrables'
        html_path = ROOT / f'{doc}.html'
    out_dir.mkdir(parents=True, exist_ok=True)
    html_path.write_text(HEAD.format(title=title, body=body), encoding='utf-8')

    pdf_path = out_dir / pdf_name
    subprocess.run(['node', str(ROOT / 'render.js'), str(html_path), str(pdf_path)], check=True)
    print(f'{len(tags)} pages -> {pdf_path}')

    if png:
        prev = (out_dir / 'png') if tag else (ROOT / 'preview' / doc)
        prev.mkdir(parents=True, exist_ok=True)
        for old in prev.glob('*.png'):
            old.unlink()
        subprocess.run(['pdftoppm', '-r', '110', '-png', str(pdf_path), str(prev / 'page')], check=True)
        print(f'aperçus -> {prev}')


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    build(args[0] if args else 'manuel', png='--no-png' not in sys.argv,
          only=option('only'), tag=option('tag'))
