"""Prépare le kit Canva livré avec le manuel : photos HD utilisées, polices, palette, pages en image, guide.

Usage : python3 design/kit_canva.py   (après python3 design/build.py manuel)
Sortie : livrables/Kit-Canva-Dolce-Lash-Brow/ et livrables/Kit-Canva-Dolce-Lash-Brow.zip
"""
import pathlib
import re
import shutil
import subprocess

from fontTools.ttLib import TTFont

ROOT = pathlib.Path(__file__).resolve().parent
PROJECT = ROOT.parent
KIT = PROJECT / 'livrables' / 'Kit-Canva-Dolce-Lash-Brow'

PALETTE = [
    ('Ivoire (fond des pages)', '#F7F2EC'), ('Papier (cartes)', '#FCFAF7'), ('Crème', '#F0E7DD'), ('Sable', '#E4D5C6'),
    ('Rose poudré', '#F0E0DC'), ('Rose', '#D8B7AF'), ('Taupe', '#A48A7B'), ('Moka', '#6E5047'),
    ('Espresso (titres)', '#3B2823'), ('Encre (texte)', '#2F2320'), ('Bordeaux (accent)', '#7A2430'), ('Bordeaux clair (encadrés)', '#F3E3E2'),
]

GUIDE = """# Kit Canva — Dolce Lash & Brow

Ce dossier accompagne le manuel (Manuel-Dolce-Lash-Brow.pdf) pour le modifier dans Canva.

## Importer le manuel dans Canva
1. Dans Canva : « Créer un design » → « Importer un fichier » → choisir **Manuel-Dolce-Lash-Brow.pdf**.
2. Canva ouvre chaque page avec ses textes modifiables, ses photos et ses formes.
3. Après l'import, feuilletez les pages : Canva peut décaler légèrement certains textes ; il suffit alors d'ajuster la zone de texte.

## Polices utilisées
Le manuel n'utilise que trois polices, choisies parce qu'elles sont proposées dans Canva :
- **Playfair Display** — titres et numéros (Regular, Italic, Medium, Medium Italic, SemiBold)
- **Cormorant Garamond** — phrases d'introduction en italique (Light Italic, Italic, Medium Italic)
- **Montserrat** — texte courant et petites capitales espacées (Light, Light Italic, Regular, Italic, Medium, SemiBold)

Si l'une d'elles est remplacée à l'import, sélectionnez le texte et choisissez-la dans la liste des polices de Canva. Les fichiers sont aussi dans le dossier « polices » (Canva Pro permet de les ajouter à votre kit de marque).

Bon à savoir :
- Dans Canva, Playfair Display affiche ses chiffres « à l'ancienne » (le 3, le 5 et le 9 descendent sous la ligne) : c'est normal, la police est la même.
- Les grands chiffres en contour (01, 02, 03, 04, 1.5) sont des dessins vectoriels : on peut les déplacer, les agrandir ou changer leur couleur, mais pas les retaper au clavier.
- Après l'import, vérifiez une page avec de petites capitales espacées (par exemple « AU PROGRAMME DE CETTE PARTIE ») : si Canva a séparé les lettres, retapez le texte puis réglez l'espacement des lettres dans Canva.
- Page 29 (quatrième de couverture) : la photo de soie est le fond de la page. Clic droit sur la photo → « Définir comme arrière-plan » pour qu'elle ne se sélectionne plus par erreur.

## Couleurs
{palette}

## Photos
Le dossier « photos » contient toutes les photos du manuel en haute définition, nommées par numéro de page (p05-… = page 5). Pour remplacer une photo dans Canva : glissez la nouvelle image sur l'ancienne.

## Pages en image
Le dossier « pages-en-image » contient chaque page en JPG haute définition, utile pour un aperçu, une story ou un post.
"""


def main():
    html = (ROOT / 'manuel.html').read_text(encoding='utf-8')
    if KIT.exists():
        shutil.rmtree(KIT)
    (KIT / 'photos').mkdir(parents=True)
    (KIT / 'polices').mkdir()
    (KIT / 'pages-en-image').mkdir()

    # Photos : chaque image bitmap utilisée, nommée d'après la première page où elle apparaît
    pages = re.split(r'(?=<section[^>]*class="[^"]*\bpage\b)', html)[1:]
    seen = {}
    for num, page in enumerate(pages, start=1):
        for src in re.findall(r'src="(assets/[^"]+\.(?:jpe?g|png))"', page):
            if src in seen or 'numerals' in src or src.endswith('grain.png'):
                continue
            seen[src] = num
            path = ROOT / src
            shutil.copy(path, KIT / 'photos' / f'p{num:02d}-{path.name}')
    # Polices au format TTF (accepté partout, y compris par Canva Pro)
    for f in sorted((ROOT / 'fonts' / 'canva').glob('*.woff')):
        font = TTFont(f)
        font.flavor = None
        font.save(KIT / 'polices' / (font['name'].getDebugName(6) + '.ttf'))
    # Pages en image (200 dpi)
    pdf = PROJECT / 'livrables' / 'Manuel-Dolce-Lash-Brow.pdf'
    subprocess.run(['pdftoppm', '-r', '200', '-jpeg', '-jpegopt', 'quality=90', str(pdf), str(KIT / 'pages-en-image' / 'page')], check=True)
    palette = '\n'.join(f'- {name} : **{hexa}**' for name, hexa in PALETTE)
    (KIT / 'LISEZ-MOI.md').write_text(GUIDE.format(palette=palette), encoding='utf-8')
    zip_path = shutil.make_archive(str(KIT), 'zip', KIT.parent, KIT.name)
    print(f'{len(seen)} photos, kit -> {zip_path}')


if __name__ == '__main__':
    main()
