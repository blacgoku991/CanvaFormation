# Guide de design — Manuel Dolce Lash & Brow

Le style à suivre : **un magazine beauté de luxe**, en reprenant l'exemple Ls.signaturedesign que la cliente aime.
- Grands titres Didone, avec beaucoup d'air autour.
- Photos de peau douces et claires.
- Palette ivoire, nude et chocolat, avec une touche de **bordeaux** (le ruban du sac de la marque « Beauté du regard »).
- Format **A4 paysage, 297 × 210 mm**.

Pages modèles à regarder AVANT de commencer (elles fixent le niveau attendu) :
- `design/pages/010-couverture.html`
- `design/pages/030-partie1-ouverture.html`
- `design/pages/050-chute.html` : page de contenu, colonne de titre à gauche et cartes.
- `design/pages/210-cils-rehaussement.html` : protocole, tableau d'étapes et encadré « Important ».

Leurs aperçus se trouvent dans `design/preview/manuel/page-*.png`.

## Fichiers et rendu

- Une page (ou plusieurs) par fichier : `design/pages/NNN-nom.html`. Chaque page est un
  `<section class="page" data-id="identifiant">…</section>`.
- **Ne modifie jamais `design/styles.css`**, ni les fichiers des autres. Les styles propres à une page vont dans
  un `<style>` en tête du fichier. Chaque sélecteur y est préfixé par `[data-id="identifiant"]`.
  Pour plusieurs pages d'un même fichier, utilise une classe propre au fichier.
- Pour un renvoi de page (sommaire, ouvertures), écris `{{p:identifiant}}`. Le numéro est calculé au build.
- Rendu partiel, pour voir TES pages :
  `python3 design/build.py manuel --only=070,080 --tag=<ton-lot>`
  Les PNG sont écrits dans `design/_work/<ton-lot>/png/page-*.png`. Ouvre-les avec Read et regarde vraiment chaque page.
  Le build affiche `DÉBORDEMENT …` quand un élément sort de son cadre : il ne doit en rester **aucun**.
- N'utilise pas le build complet (sans `--tag`) : il est réservé à l'assemblage final.

## Squelette d'une page de contenu

```html
<section class="page" data-id="mon-id">
  <div class="runhead"><span class="brand">Dolce Lash &amp; Brow · Support pédagogique</span><span>Partie I — Sourcils</span></div>
  <div class="content"> … </div>   <!-- zone utile : 18 mm de marges latérales, de 27 mm du haut à 19 mm du bas -->
  <div class="folio"><span>Dolce Lash &amp; Brow • Manuel de formation</span><span class="num"></span></div>
</section>
```

Texte de l'en-tête de droite, selon la partie :
- `Partie I — Sourcils`
- `Partie II — Les cils`
- `Partie III — Pratique professionnelle`
- `Partie IV — Évaluation`

## Classes disponibles (styles.css)

**Titres et textes**
- `.kicker` : petit sur-titre bordeaux, en capitales espacées, précédé d'un filet (`.kicker.plain` pour l'avoir sans filet).
- `.h-display` : très grand titre Didone. `.h-title` : titre de page en Didone capitales, avec `<span class="no">4.</span>` pour le numéro de section en italique bordeaux.
- `.h-sub` : intertitre Didone, avec `<span class="no">`. `.h-label` : intertitre en petites capitales sans empattement.
- `.lead` : phrase d'accroche en Cormorant italique. `.note` : citation encadrée de deux filets. `.small`, `.muted`.

**Listes**
- `ul.dots` : puces rondes rose poudré.
- `ol.steps` : étapes numérotées 01, 02… en grands chiffres italiques bordeaux.

**Blocs**
- `.card` (+ `.soft`, `.blush`, `.cream`) : cartes.
- `.alert` avec `<div class="alert-title">Important</div>` : encadré de sécurité bordeaux. **Toute consigne de sécurité ou mise en garde importante doit être dans un `.alert`**, ou rester au moins très visible.
- `.pending` avec `.pending-title` : emplacement d'un contenu que la cliente doit encore fournir.
- `.photo-slot` avec `.slot-title` : cadre pointillé pour une photo à fournir.

**Données**
- `.chip` (+ `.fill`, `.soft`) : pastille, pour les temps de pose, ratios ou pourcentages.
- `table.data` : tableaux élégants. `td.key` met la 1re colonne en Didone, avec `<em>` pour une partie en bordeaux.

**Mise en page**
- `.grid-2`, `.grid-3`, `.grid-12-8`, `.grid-8-12` : grilles.
- `.stack`, `.stack-s`, `.stack-l` : espacement vertical.
- `.rule`, `.rule.short` : filets.

**Grands éléments**
- `.big-num` (`.dark`, `.ghost`) : très grand chiffre façon magazine.
- (supprimé) `.blend` : Canva n'importe pas les modes de fusion ; poser les photos sur fond blanc dans une carte blanche.

**Couleurs** (variables CSS)
- Fonds : `--ivory` (fond des pages), `--paper`, `--cream`, `--sand`, `--blush`.
- Rose et tons moyens : `--rose`, `--taupe`, `--mocha`.
- Textes et titres : `--espresso`, `--ink`.
- Accent : `--bordeaux`, `--bordeaux-soft`.

**Polices** (toutes disponibles dans Canva, fichiers statiques dans `fonts/canva/`, déclarées dans `fonts/fonts-canva.css`) : `--display` (Playfair Display), `--serif` (Cormorant Garamond), `--sans` (Montserrat 300 pour le texte).

**Compatibilité import Canva** : pas de -webkit-text-stroke (chiffres en contour = `assets/numerals/*.svg`), pas de mode de fusion, de filtre ni d'ombre portée, pas de texte justifié ni de césure, pas de calque posé sur toute la page ; une étiquette et son texte dans le même élément.

## Règles de design

1. **Air et hiérarchie** : un seul grand titre par page, une colonne de titre ou un en-tête clair, puis un contenu
   rythmé par des cartes, des tableaux ou des étapes. Pas de pavés de texte de plus de 110 mm de large. Utilise
   2 ou 3 colonnes plutôt qu'une seule colonne large.
2. **Remplir la page harmonieusement** : pas de grand vide d'un côté et de texte serré de l'autre. Si une page est
   légère, agrandis les éléments, ajoute un visuel (assets ci-dessous), un grand chiffre fantôme ou une citation
   `.lead` reprise du texte. Si elle est trop chargée, signale-le plutôt que de passer sous 8,4 pt.
3. Corps de texte à 9,6 pt (minimum 8,4 pt pour du texte secondaire). Titres de page entre 20 et 26 pt.
4. Le bordeaux reste un accent : numéros, filets, pastilles, encadrés Important. Jamais de grands aplats, sauf la
   bande de couverture.
5. Pas d'emojis. Pas d'icônes d'une autre bibliothèque. Les petits schémas sont dessinés en SVG inline, avec des
   traits fins `--espresso` / `--rose` et un style épuré.
6. Cohérence : mêmes en-têtes, pieds de page, marges et composants que les pages modèles.

## Règles de texte (non négociables)

- Le texte vient des transcriptions vérifiées `contenu/transcription/*.md`. Reprends-le **mot pour mot**. Seules les
  corrections listées dans `contenu/AUDIT.md` sont autorisées : coquilles, accents, typographie, noms de produits
  harmonisés. Ne résume pas, ne reformule pas, ne supprime aucune phrase.
- N'invente **aucun** contenu technique : temps, ratios, produits, étapes, contre-indications. Tu peux ajouter des
  libellés de structure (sur-titres de type « Partie I — Sourcils », « Étape 1 », « Au programme ») et appliquer la
  renumérotation prévue au plan.
- Les avertissements (vérifier la notice, ne pas appliquer sans validation, avis médical…) restent intégralement et
  bien visibles.
- Typographie française :
  - apostrophe ’ ;
  - guillemets « … » avec espaces insécables (`«&nbsp;…&nbsp;»`) ;
  - espace insécable avant : ; ? ! (`&nbsp;`) ;
  - tiret cadratin — dans les titres de produits.
- Filigranes : seul le filigrane @refreshednrefined (atelier visuel) existe ; il reste visible, jamais masqué ni effacé, avec la mention « Crédit photo : @refreshednrefined » (décision de la cliente). Aucun autre visuel tiers (mockup, infographie d'origine) n'est réutilisé.

## Visuels disponibles (`design/assets/`)

| Fichier | Contenu | Remarques |
|---|---|---|
| `logo-dolce.png` | Logo « dolce lash & brow », noir sur fond transparent, 720 × 103 px | pour la couverture et la 4e de couverture |
| `portrait-couverture.jpg` | Portrait 3/4 de la mannequin, yeux fermés, fond blanc, 1129 × 1210 px | déjà sur la couverture ; possible en gros plan recadré (yeux, lèvres) |
| `portrait-regard-haut.jpg` | Gros plan front, sourcils et yeux fermés, fond blanc, 1129 × 668 px | ouverture de la Partie I et page « chute » ; à recadrer autrement si tu le réutilises |
| `portrait-regard-haut-chaud.jpg` | Même image, version plus chaude | |
| `portrait-cou-bas.jpg` | Bas du visage, lèvres, cou, épaule, fond blanc, 1129 × 838 px | |
| `sac-jambes.jpg` | Bord du sac rose « Beauté du regard » avec ruban bordeaux, jambes en escarpins noirs, fond gris clair, 457 × 1070 px (vertical) | |
| `zola-bb-blond-powder.jpg` | Pot ZOLA BB Blond powder, fond blanc, 200 × 208 px | afficher à 45 mm maximum |
| `atelier-brow-1.jpg`, `-2.jpg`, `-3.jpg` | Les 3 présentations de sourcils de l'atelier visuel, dans l'ordre de la planche d'origine (ne pas leur attribuer de légende « naturel / discipliné / structuré » : non validé par la cliente ; numéroter 1, 2, 3), bandes 1200 × ~385 px (HD) | **la 3e porte le filigrane @refreshednrefined : ne jamais le masquer, le recadrer ni l'effacer** ; ajouter sous les photos « Crédit photo : @refreshednrefined » |
| `zola-oxydant-3.jpg` | Flacon oxydant ZOLA 3 %, fond blanc, 110 × 215 px | afficher à 45 mm maximum |

Les images sont de résolution moyenne : n'agrandis pas une photo au-delà d'environ 1,4× sa taille naturelle à 96 dpi.
