# Analyse design de l'exemple Ls.signaturedesign

Source : `sources/456f8945-image.jpg`. C'est une photo d'écran de MacBook prise au téléphone (718 × 1560 px). Elle est en biais d'environ 36°, avec une forte perspective : le côté droit de l'écran est plus loin. L'écran affiche une double page du manuel « Présentation du Browlift ».

## Méthode et limites

- Image redressée : rotation de 36°, puis correction de perspective (homographie calée sur les 4 coins de la page de droite). J'ai ensuite extrapolé la page de gauche. Fichiers de travail, dans `/tmp/claude-0/-home-user/1210b0de-a323-5e4c-ab8b-e83b4ca9ec20/scratchpad/wf/` :
  - double page à plat : `spread_flat.jpg` et `spread_flat_small.jpg` ;
  - pages seules : `right_page.jpg` et `left_page.jpg` ;
  - zooms : `z_title_left.jpg`, `z_title_right.jpg`, `z_profile.jpg`, `z_hand.jpg` et `m_p1..4.jpg`.
- **Dans la maquette, rien n'est penché.** L'inclinaison vient de la prise de vue. Une fois l'image remise à plat, tous les textes sont horizontaux.
- **Les couleurs sont faussées par la prise de vue** : écran photographié sous une lampe chaude, avec une dominante rosée et orangée. Les codes hex mesurés sont donc corrigés plus bas en valeurs « recommandées ».
- **La définition est très faible** : le corps de texte fait environ 5 px de haut dans l'original. Les titres et les intertitres sont sûrs. Le corps de texte est une reconstruction probable.
- Ne font **pas** partie de la maquette :
  - le texte blanc « Ls.signaturedesign », qui est l'identifiant de la story Instagram ;
  - l'heure, le réseau et la batterie du téléphone.

---

## 1. Mise en page

### Format
- **Double page composée en deux moitiés exactement égales.** Je l'ai vérifié : la moitié gauche, extrapolée par l'homographie, tombe pile sur le bord de la photo.
- Une fois redressée, les proportions restent naturelles avec un **ratio d'environ 1,41:1**. Cela correspond à **un A4 paysage (297 × 210 mm) traité comme deux pages de 148,5 × 210 mm**, ou à deux A4 portrait côte à côte. C'est la même structure que le choix de la cliente (`DECISIONS.md` : A4 paysage).
- Il n'y a ni ombre de pliure ni filet de séparation. La page blanche de droite coupe la photo par une **arête verticale nette**.

### Schéma (double page à plat)
```
┌──────────────────────────────┬──────────────────────────────┐
│▓▓▓ PHOTO PLEINE PAGE ▓▓▓▓▓▓▓▓│   TOUT SAVOIR SUR        ░░░░│
│▓ fond nuit ▓ visage serré ▓▓▓│      LE BROWLIFT       ░░░░░░│
│▓▓▓ sourcils au 1/3 haut ▓▓▓▓▓│ texte ………………………      ░ profil ░│
│▓▓▓▓▓▓    (0)1   ▓▓▓▓▓▓▓▓▓▓▓▓│ • puce                ░ fondu ░│
│▓▓▓▓  PRÉSENTATION  ▓▓▓▓▓▓▓▓▓▓│ • puce               ░ dans le░│
│▓▓ DU BROWLIFT ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│ **phrase clé**       ░ blanc ░░│
│▓▓▓▓▓ bouche / main ▓▓▓▓▓▓▓▓▓▓│ À QUI S'ADRESSE … ?   ░░░░░░░░│
│▓▓▓▓ pull maille blanc ▓▓▓▓▓▓▓│ • … • …                ░░░░░░░│
│▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│ **conclusion en gras**  ░░░░░░│
└──────────────────────────────┴──────────────────────────────┘
   page « ouverture » (sombre)      page « contenu » (claire)
```

### Page gauche : ouverture de chapitre
- **Photo à fond perdu sur toute la page.** Le portrait est très serré, du front au menton, et le visage occupe environ 90 % de la largeur. Les cheveux sont tirés, sur un fond nuit noir bleuté.
- Les yeux et les sourcils sont au **tiers supérieur** (environ 25 à 35 % de la hauteur). Les sourcils sont le sujet du chapitre, ils sont donc mis en avant.
- La pliure coupe le visage juste après le 2e œil. On a l'impression que la page de contenu glisse sur la photo.
- En bas, une main posée sur la joue : ongles amande nude laiteux, bague et créole dorées, manche en maille côtelée blanche. Ces éléments apportent de la texture et un côté « lifestyle ».
- **Le bloc-titre est centré horizontalement**, sur un axe à environ 48–51 % de la largeur. Il est empilé en 3 niveaux imbriqués :
  1. **« 01 »** fantôme, de 24 à 41 % de la hauteur. **Le « 0 » encercle l'œil gauche du modèle.** C'est un cadrage voulu et la signature de la mise en page.
  2. **« PRÉSENTATION »**, à environ 40–43 % de la hauteur. Il **chevauche le pied du « 01 »**.
  3. **« DU BROWLIFT »**, à environ 43–50 % de la hauteur, sur **73 % de la largeur** (de 11 à 84 %). Il passe sur l'arête du nez et les pommettes.
- L'interligne est très serré : les trois niveaux se touchent presque et se lisent comme un seul « logo-titre ».
- Le blanc reste lisible sur la peau grâce à sa grande taille et au mi-ton bronzé de la peau. Il ne passe ni sur les yeux ni sur la bouche, sauf le « 0 », qui est volontairement transparent.

### Page droite : contenu
- Fond blanc rosé uni. Il n'y a ni cadre, ni filet, ni en-tête visible. Une minuscule marque en bas à droite pourrait être un folio, mais elle est illisible.
- **Grille en 2 zones :**
  - **Colonne de texte à gauche**, d'environ 5 % à 58 % de la largeur (≈ 53 %). Les lignes font environ 65 à 75 caractères.
  - **Zone image à droite**, sur environ 42 %. C'est un **profil féminin fondu dans le blanc** : yeux fermés, menton relevé, épaule nue. Il est à fond perdu en haut et à droite, et se dissout vers le bas et vers la gauche.
- **Le profil regarde vers le texte.** Le nez et les lèvres pointent vers la colonne et guident la lecture. Aucune ligne de texte ne passe sur le visage.
- **Titre** de 9,5 à 16 % de la hauteur, de 14 à 58 % de la largeur. Il tient sur 2 lignes **décalées** : la 2e est plus grande et décalée vers la droite.
- **Corps** de 21 à 92 % de la hauteur. La page est dense mais aérée.
- **Marges** : environ 10 % en haut, environ 8 % en bas, et seulement 4 à 5 % à gauche. Cette marge gauche est étroite, c'est un point à améliorer.
- Tout est **aligné à gauche, en drapeau à droite** (pas de justification).
- **Rythme** des blocs :
  1. paragraphe ;
  2. liste à puces ;
  3. paragraphe qui se termine par une phrase en **gras** ;
  4. intertitre en capitales ;
  5. liste ;
  6. paragraphe avec phrase en **gras** ;
  7. intertitre ;
  8. liste ;
  9. **conclusion en gras**.

  Il y a une ligne vide entre les blocs et un espace un peu plus grand avant chaque intertitre.

---

## 2. Typographie

### Ce qu'on observe
| Niveau | Où | Style observé | Taille relative (hauteur de capitale / hauteur de page) |
|---|---|---|---|
| Numéro géant « 01 » | page gauche | Didone (même famille que le titre), chiffres alignés. Le 0 est ovale, épais sur les flancs et filiforme en haut et en bas. Le 1 a un empattement. **Blanc à environ 45–55 % d'opacité**, en « fantôme » sur la peau. | ≈ 15–16 % (≈ 2,5 × la capitale de « DU BROWLIFT ») |
| Sur-titre « PRÉSENTATION » | page gauche | Didone en capitales, blanc. **Approche serrée, voire négative** : « NT » et « TA » se touchent. | ≈ 2,3 % |
| Titre « DU BROWLIFT » | page gauche | **Didone de mode** à fort contraste plein/délié et axe vertical. Empattements filiformes plats et non raccordés. **Capitales seules**, graisse regular à medium, pas d'italique. Chasse normale, pas condensée. Le W est fait de deux V entrecroisés, typique des Didone « fashion ». Interlettrage nul. Peut-être une ombre très légère (incertain). | ≈ 5,4 % |
| Titre de page « TOUT SAVOIR SUR / LE BROWLIFT » | page droite | Didone noire, d'aspect plus fin et plus étroit. **Les déliés sont presque invisibles** et les lettres semblent « cassées » à cette résolution, signe d'un contraste extrême (coupe display ou hairline). Ligne 1 plus petite, ligne 2 environ 1,5 fois plus grande. **Interligne négatif** : les lignes se frôlent. 2e ligne décalée à droite. | L1 ≈ 2,8 % · L2 ≈ 4,2 % |
| Intertitres « À QUI S'ADRESSE LE BROWLIFT ? » | page droite | **Sans-serif gras en capitales**, même corps que le texte, sans interlettrage, noir. Un peu « bruts ». | = corps |
| Corps de texte | page droite | Sans-serif neutre, humaniste ou géométrique (rendu proche de Canva Sans, Open Sans ou Montserrat). Regular gris très foncé, avec **phrases clés en gras** de même couleur. Interligne ≈ 1,45–1,5. | pas de ligne ≈ 1,9 % de la hauteur |
| Puces | page droite | **Petits disques pleins noirs**, retrait d'environ 3–4 mm, texte aligné après la puce. Listes de 3 à 4 items courts. | — |

**Tailles reconstituées.** Si la double page fait un A4 paysage (297 × 210 mm) :
- « DU BROWLIFT » ≈ 46–48 pt ;
- « PRÉSENTATION » ≈ 20 pt ;
- « 01 » ≈ 130–140 pt ;
- titre de page : environ 24 pt pour la 1re ligne et 37 pt pour la 2e ;
- corps ≈ 8 pt sur un interligne de 11,5 pt. **C'est trop petit à l'impression : prévoir 9–10 pt.**

Si chaque page fait un A4 portrait, il faut multiplier ces tailles par 1,41.

**Hiérarchie.** Numéro fantôme, puis titre display, puis sur-titre, puis titre de page en 2 tailles, puis intertitre en sans-serif gras capitales, puis corps et phrase clé en gras, puis puces. Il n'y a que **2 familles**, une Didone et un sans-serif, et **aucune couleur d'accent**. Le contraste vient de la taille et de la graisse.

### Polices Google Fonts les plus proches
| Rôle | Recommandation | Pourquoi | Alternatives / à éviter |
|---|---|---|---|
| Titres display, « 01 », titres de page | **Bodoni Moda** (400–500, axe `opsz` à 72–96) | C'est la vraie Didone de Google Fonts. À grand `opsz`, ses déliés deviennent filiformes **comme dans l'exemple**. Capitales larges et élégantes, chiffres à fort contraste pour le « 01 », graisses variables, accents français en latin-ext. Déjà installée dans `design/fonts/`. | **Playfair Display** : la plus connue, mais aux déliés plus épais et à l'esprit plus « blog », un peu moins couture. **Gloock** : Didone display très contrastée, bonne en très grand, plus lourde. **Prata** : Didone d'une seule graisse au charme un peu vintage, utile pour les sur-titres. **Gilda Display** : contraste moyen, trop douce par rapport à l'exemple. |
| Sur-titres fins (option) | **Bodoni Moda 400** en capitales serrées, comme l'exemple | Garder la même famille que le titre donne l'effet « bloc imbriqué » de l'exemple. | **Italiana** : très fine et peu contrastée. Élégante en sur-titre espacé, mais ce n'est **pas** le style des titres de l'exemple. **Marcellus** : capitales évasées type Trajan, plus « spa ». Ne correspond pas, à éviter pour coller à l'exemple. |
| Accroches et citations (ajout de raffinement) | **Cormorant Garamond Italic** (300–500) | Ce n'est pas dans l'exemple. Mais une italique garalde très contrastée se marie très bien avec la Didone, pour une accroche ou une citation. À doser : 1 par page au maximum. | — |
| Corps, listes, intertitres | **Jost** (300–400 pour le corps, 500–600 pour le gras et les intertitres) | Géométrique façon Futura, fine et lumineuse. Elle donne un rendu plus « luxe » que le sans-serif de l'exemple tout en gardant sa neutralité. Très lisible en 9–10 pt. | **Montserrat** : la plus proche du rendu Canva, mais plus large et plus lourde. **Open Sans** et **Lato** : proches de l'original, mais plus neutres et moins chics. |

Amélioration conseillée pour les intertitres : Jost 600 en capitales, **interlettrage de 0,12 à 0,16 em**, corps à 85–90 % de celui du texte, et éventuellement une couleur de marque. Les intertitres deviennent plus raffinés que le gras serré de l'exemple. Les grands titres Didone, eux, restent **sans interlettrage**.

---

## 3. Palette et traitement photo

Les couleurs sont mesurées (médiane d'une zone) sur l'image redressée. Les valeurs recommandées corrigent la dominante chaude et rosée de la prise de vue.

| Rôle | Mesuré | Recommandé | Commentaire |
|---|---|---|---|
| Fond de la page de contenu | `#F2EAE7` (de `#EFE5E5` à `#F3EBF1`) | `#FBF7F5` (porcelaine) ou ivoire `#F8F3EF` | Blanc chaud, probablement presque blanc dans le fichier d'origine |
| Texte | gris-noir (flou) | `#1E1A1A` (noir doux) | Jamais de noir pur bleuté |
| Fond nuit derrière le portrait | `#0D0B1C` | `#15121A` | Noir légèrement violacé ou bleuté qui fait ressortir la peau dorée |
| Peau, zones éclairées (front, pommettes) | `#E7A687` / `#EBA485` | `#E8B193` | Pêche dorée lumineuse |
| Peau, mi-ton bronzé | `#D47953` | `#C98463` | Terracotta ou caramel, chaleur « glow » |
| Peau, ombre | `#C98864` | `#A8705A` | — |
| Lèvres gloss nude | `#D3745E` (lumière) / `#AC555D` (ombre) | `#C98A80` | Nude rosé brillant |
| Profil fondu : joue | `#D7A79A` | `#E3C2B8` | Rose poudré pastel |
| Profil fondu : cou et épaule | `#D6C9C4` | `#E9DFDB` | Se dissout dans le blanc |
| Lèvres du profil | `#C58A8B` | `#C48C8E` | Vieux rose |
| Titres blancs | `#FCFBFC` | `#FFFFFF` | — |
| « 01 » fantôme | rendu ≈ `#EBCFC3` sur la peau | `#FFFFFF` à 45–55 % d'opacité | Il doit laisser voir l'œil à travers |
| Bijoux (bague, créole) | estimation visuelle | `#C9A46A` | Or doux, présent **uniquement dans la photo**, jamais en couleur de texte |

**Traitement photo.**
- **Portrait de gauche** : rendu chaud et doré, peau bronzée lumineuse avec des reflets « glow » sur le front, le nez et les pommettes. Lèvres glossy, sourcils très nets et brossés (effet browlift). Le fond sombre isole le visage. Les contrastes sont forts.
- **Profil de droite** : désaturé, pastel, high-key. Il est posé à environ 40–55 % d'opacité, ou bien fondu par un dégradé vers le blanc, à gauche et en bas. Il sert d'**ambiance**, pas d'illustration.

**Contrastes.**
- Page gauche très contrastée (nuit, peau dorée, blanc) et page droite douce (noir doux sur blanc rosé). **L'alternance sombre/clair entre les deux pages crée le rythme** du manuel.
- L'exemple n'a **aucune couleur d'accent graphique**, à part le noir, le blanc et les couleurs des photos. La touche bordeaux et rose poudré prévue dans `design/GUIDE-DESIGN.md` est un ajout de marque pour Dolce Lash & Brow. Il faut la garder **rare** (sur-titres, numéros, filets fins) pour ne pas perdre le côté épuré.

---

## 4. Texte lisible à l'écran

### Page gauche (certain)
- `01`
- `PRÉSENTATION`
- `DU BROWLIFT`

### Page droite
**Titre (certain)** : `TOUT SAVOIR SUR` / `LE BROWLIFT`

**Intertitres (quasi certains)** : `À QUI S'ADRESSE LE BROWLIFT ?` et `À QUI NE S'ADRESSE PAS LE BROWLIFT ?`

**Corps (reconstruction probable ; `[?]` = mot douteux ; **gras** = ce qui apparaît en gras à l'écran)** :

> Le browlift est un traitement restructurant réalisé en plusieurs étapes, comparable au principe d'une permanente de lissage, spécifiquement adapté aux sourcils.
>
> Il permet de :
> • Discipliner les poils
> • Modifier leur direction
> • Apporter une impression de densité immédiate
> • Structurer la ligne du regard
>
> La solution appliquée assouplit temporairement la fibre du poil, la rendant plus malléable et facile à repositionner.
> **Selon la technique de coiffage choisie, il est possible d'obtenir différents rendus : naturel, duveteux, lifté ou plus structuré et défini.**
>
> **À QUI S'ADRESSE LE BROWLIFT ?**
>
> Le browlift convient aux personnes :
> • Ayant des sourcils naturellement fournis à très fournis
> • Présentant des poils indisciplinés ou poussant vers le bas
> • Souhaitant un effet plus dense [?] et mieux structuré
>
> Plus la densité de poils est importante, plus le résultat sera visible et harmonieux.
> **La technique peut être réalisée sur la majorité des clientes, à condition qu'il y ait suffisamment de matière pour travailler la mise en forme.**
>
> **À QUI NE S'ADRESSE PAS LE BROWLIFT ?**
>
> Le browlift n'est pas adapté :
> • Aux personnes ayant très peu ou pas de poils
> • En cas d'alopécie sourcilière importante
> • En présence de lésions, irritations ou infections cutanées
> • Par mesure de précaution, chez les femmes enceintes ou allaitantes
>
> **Sans poils suffisants, la technique ne peut produire de résultat visible, puisqu'il s'agit d'un travail sur la fibre existante.**

Ce texte et ces photos appartiennent à l'exemple d'un autre compte. On reprend la **structure** et le **style**, pas le contenu : le texte du manuel Dolce Lash & Brow vient des photos de la cliente (`contenu/transcription/`).

---

## 5. Les codes du style

### À reproduire
1. **Univers « magazine beauté de luxe »** (Vogue Beauty, Harper's Bazaar), dans un esprit *quiet luxury* et *clean girl* : peu d'éléments, très bien placés.
2. **Alternance de 2 types de pages :**
   - une **ouverture** avec photo à fond perdu sombre et chaude, et un titre blanc ;
   - un **contenu** sur fond blanc chaud, avec texte et photo fantôme.
3. **Numéro de chapitre géant en fantôme** (Didone, blanc translucide), **imbriqué** dans le titre et **en dialogue avec la photo** : le 0 qui encadre l'œil. Pour chaque ouverture, placer le chiffre en fonction d'un détail de l'image.
4. **Titres Didone en capitales sur 2 niveaux** : sur-titre petit, puis titre grand. Interlignage serré, voire négatif, lignes parfois décalées, aucun interlettrage.
5. **Contraste typographique net** entre une Didone display très contrastée et un sans-serif simple et fin pour le corps. Pas de 3e famille, ou alors une italique pour les accroches.
6. **Photo fantôme dans la marge** de la page de contenu : profil pastel fondu dans le blanc, **orienté vers le texte**, sans jamais passer sous les lignes.
7. **Lecture facile** : listes de 3–4 puces courtes, intertitres-questions (« À qui s'adresse… ? »), et **une phrase clé en gras par bloc** qui sert de « ce qu'il faut retenir ».
8. **Photographie** : gros plans éditoriaux, peau lumineuse et dorée, sourcils et cils très nets (le sujet de la formation), bijoux or discrets, textures douces (maille, peau, gloss).
9. **Pas de « décor »** : ni cadres, ni boîtes lourdes, ni icônes, ni motifs. Le luxe vient de la typographie, de la photo et de l'espace.

### À améliorer par rapport à l'exemple (pour un manuel imprimé)
- **Marge gauche** trop étroite (environ 5 %) : passer à 15–18 mm (`design/styles.css` prévoit 18 mm).
- **Corps** trop petit (environ 8 pt sur un A4 paysage) : prévoir 9–10 pt en Jost, avec un interligne de 1,45–1,5.
- **Intertitres** en gras serré un peu bruts : utiliser des capitales espacées en Jost 500–600, éventuellement en couleur de marque.
- **Repères absents** (en-tête, folio, n° de partie) : un manuel de formation en a besoin pour se repérer. Ils doivent rester discrets et fins.
- **« 01 » peu lisible** sur la peau claire : doser l'opacité (45–60 %) et vérifier le contraste à chaque ouverture.
- **Consignes de sécurité** (contre-indications, femmes enceintes, etc.) : dans l'exemple, elles sont noyées dans une liste. Dans le manuel, elles doivent être **bien visibles** (encadré `.alert` du guide).

### À éviter
- Polices manuscrites ou script en grande quantité, polices fantaisie, et la police par défaut de Canva partout.
- Trop de couleurs, dégradés vifs, aplats saturés, rose bonbon, **texte doré métallisé**, effets « néon ».
- Encadrés épais, ombres portées marquées, contours de texte, cliparts, icônes cartoon, emojis.
- Corps de texte posé sur une photo, et titre posé sur les zones clés du visage (yeux, bouche), sauf élément volontairement transparent comme le « 0 ».
- Texte justifié avec rivières, lignes de plus de 75 caractères, paragraphes longs sans respiration.
- Interlettrage large sur les grands titres Didone : il casse l'élégance. Le garder pour les petits sur-titres en sans-serif.
- Polices étirées ou en faux gras, photos déformées, pixellisées ou recadrées n'importe comment.
- Recopier les photos ou le texte de l'exemple, ou effacer le filigrane d'un créateur : on cite le crédit photo quand on utilise une image tierce (voir `DECISIONS.md`).
