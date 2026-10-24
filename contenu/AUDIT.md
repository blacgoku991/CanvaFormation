# Audit éditorial — Manuel de formation Dolce Lash & Brow

Date : 24 octobre 2026. Audit réalisé avant la refonte graphique (A4 paysage).

**Périmètre.** J'ai relu les 17 transcriptions de `contenu/transcription/` en entier. Elles comprennent `brow-lift-thuya-teinture.md` (source `3d19aee4`), arrivée pendant l'audit et intégrée ici. J'ai aussi revérifié dans `sources/` les points sensibles :
- page décoloration (`882f6e3e`) ;
- page mapping (`7092270e`) ;
- page cycle de vie (`d5c88c8b`) ;
- page sources (`d5e9ba52`) ;
- page Partie II (`402cd44e`) ;
- page gestion (`33b4d2f9`) ;
- page Brow Lift Thuya (`3d19aee4`) ;
- planche HD de l'atelier (`5e1872c7`) ;
- exemple de design (`456f8945`).

J'ai lu `DECISIONS.md` et `PLAN.md`. Leurs arbitrages sont repris ici et signalés comme tels.

**Statuts utilisés dans ce document**
- **[CORRIGER]** : correction autorisée, à appliquer directement dans le nouveau design.
- **[ARBITRÉ]** : déjà tranché dans `PLAN.md` ou `DECISIONS.md`. Le numéro de l'arbitrage est indiqué.
- **[À VALIDER]** : à faire confirmer par la formatrice. Ne pas l'appliquer sans son accord.
- **[NE PAS TOUCHER]** : forme d'origine à conserver telle quelle.

Rappel : cet audit ne réécrit aucun contenu. Toute correction absente des listes B1 et B2 est interdite.

---

## 0. Synthèse — les 12 points qui comptent

1. **Contenu encore manquant**, même après réception de la page « Brow Lift — Thuya » :
   - le protocole et le temps de pose de la **teinture Brow Daddy** (le §3 dit lui-même « restent à confirmer ») ;
   - la rubrique **« Diagnostic et application en cabine »**, qui n'a pas de page dédiée ;
   - la partie **« Anatomie »** de « Anatomie et cycle de vie du poil » ;
   - l'ancien **point « 4. »** de la page Gestion (la numérotation saute de 3 à 5).
2. **Deux sections portent le numéro « 1. »** : « 1. Diagnostic et restructuration » (page Brow Lift) et « 1. RESTRUCTURATION DES SOURCILS & MAPPING ». Elles sont fusionnées par l'arbitrage PLAN #9.
3. **Deux séries « 1, 2, 3… » se chevauchent** en Partie III : réseaux sociaux 1–3, puis gestion 1, 2, 3, 5. La renumérotation 1–6 est prévue par PLAN #4, mais elle **masque le point 4 manquant** : à confirmer avec la cliente.
4. **Bloc oxydant de la page décoloration saisi sans accents** (5 mots), et **nom de produit divergent** : « BB Blond Powder » contre « Baby Blonde Powder ». Arbitré.
5. **Page « cycle de vie du sourcil » illustrée par un schéma « cycle de vie des cils »**. De plus, le texte cite 4 phases (dont l'exogène) alors que le schéma n'en montre que 3, plus un retour à l'anagène.
6. **Tension de sécurité majeure en Partie II.** Le tableau « Ordre des étapes enseigné » place le Lash Botox (Step 1.5) **entre** Step 1 et Step 2. Or l'encadré « Important » de la même page dit : « certains systèmes imposent de neutraliser avant tout soin. Ne pas appliquer cette séquence sans validation. » L'encadré doit rester collé au tableau.
7. **Tous les temps de pose chiffrés** (Thuya 8 / 10 / 11–12 min, Noemi 10 min, décoloration 3–20 min) sont présentés comme **non validés par les fabricants**. Ils ne doivent jamais apparaître sans leur avertissement.
8. **Photos de l'atelier visuel** : filigrane d'un compte tiers, **@refreshednrefined** (lecture confirmée sur la version HD). Le crédit ne remplace pas une autorisation. Le manuel dit lui-même « ne jamais présenter comme sien le travail d'une autre professionnelle ».
9. **Autres visuels d'origine inconnue** :
   - mockup du site **Only Lash Paris** (page sources) ;
   - photos produits ZOLA ;
   - schéma et photo du mapping ;
   - infographie du cycle ;
   - portrait de couverture et photo du sac et des jambes.

   Les droits sont à confirmer.
10. **QCM** : le corrigé est proposé en D. Trois questions ne sont pas, ou pas entièrement, couvertes par le manuel :
    - Q4 (sensation de brûlure) ;
    - Q5 (« lamination », « étape de réduction », rôle du neutralisant) ;
    - Q10 (pourquoi choisir le support en silicone).

    Les bonnes réponses sont très déséquilibrées : A = 8, B = 6, C = 1.
11. **Page Sources incomplète.** Aucune référence pour Thuya, ZOLA, Noemi Intense ni StainMe. Une source, Noemi Freelift, ne sert à rien dans le manuel, et son URL est tronquée.
12. **Contradiction interne au guide de design.** `GUIDE-DESIGN.md` dit « Les filigranes et crédits d'autrui ne doivent jamais apparaître », alors que `DECISIONS.md` et PLAN #10 imposent de **garder** le filigrane et d'ajouter le crédit. La décision de la cliente prime : la règle du guide est à corriger.

---

## A. Contenu manquant

### A1. Sommaire ↔ pages fournies

| Rubrique du sommaire (`sommaire.md`) | Page(s) correspondante(s) | Statut |
|---|---|---|
| PARTIE I · SOURCILS (ouverture) | `partie-1-ouverture.md` | Couvert |
| · Anatomie et cycle de vie du poil | `cycle-de-vie-sourcil.md` (titre « LE CYCLE DE VIE DU SOURCIL ») | **Partiel.** Le cycle est traité, mais **aucun contenu d'anatomie** (follicule, bulbe, structure du poil). Le titre de page diffère du sommaire. |
| · Pourquoi les sourcils tombent-ils ? | `pourquoi-sourcils-tombent.md` | Couvert |
| · Diagnostic et application en cabine | Pas de page dédiée. Approchants : « 1. Diagnostic et restructuration » (`brow-lift-thuya-teinture.md`), « Étape 1 — Diagnostic et préparation » (`restructuration-mapping.md`), encadré « En pratique, avant une prestation : » (`pourquoi-sourcils-tombent.md`), « Avant la séance » (fiche technique) | **Manquant ou partiel.** Le diagnostic est couvert par fragments ; **« application en cabine » ne l'est pas du tout**. PLAN fait pointer cette entrée vers la page §1-A (`060-diagnostic`) : solution acceptable à faire valider. Sinon, demander la page à la cliente. |
| · Restructuration et mapping | `restructuration-mapping.md` (§1) + synthèse §1 de `brow-lift-thuya-teinture.md` | Couvert. Le §1 existe deux fois : voir A3. |
| · Brow Lift : technique et temps de pose | `brow-lift-thuya-teinture.md` (§2 « Brow Lift — Thuya ») + `fiche-technique-brow-lift-hygiene.md` | Couvert **depuis la réception de `3d19aee4`**. Les temps restent « non validés par Thuya » : voir G. |
| · Teinture hybride et décoloration | §3 « Teinture des sourcils — Brow Daddy » (`brow-lift-thuya-teinture.md`) + §4 (`decoloration-sourcils.md`) | **§3 incomplet**, de l'aveu du texte : « Le protocole de teinture et son temps de pose restent à confirmer ». Pas de ratio, alors que la page Sources cite « Brow Daddy Hybrid Tint — ratio distributeur ». Pas d'étapes, pas de temps. Le §4 est complet. |
| · Atelier visuel Brow Lift et sécurité | `atelier-visuel-brow-lift.md` + « HYGIÈNE, SÉCURITÉ ET QUALITÉ » (2ᵉ moitié de `fiche-technique-brow-lift-hygiene.md`) | Couvert, à condition de placer « Hygiène, sécurité et qualité » ici : voir F. |
| PARTIE II · CILS (ouverture) | `partie-2-ouverture.md` | Couvert |
| · Diagnostic, rehaussement de cils, teinture et Lash Botox | `partie-2-cils-contenu.md` (§5 à §8 + « Conseils après prestation ») | Couvert. La rubrique unique du sommaire regroupe 5 sous-parties. |
| PARTIE III · PRATIQUE PROFESSIONNELLE | Pas d'intercalaire d'origine | Ouverture créée par le design (`300`), sans texte nouveau |
| · Fiches pratiques et suivi des clientes | « FICHE TECHNIQUE — BROW LIFT » (1ʳᵉ moitié de `fiche-technique-brow-lift-hygiene.md`) | **Partiel.** Le sommaire annonce **des fiches**, mais il n'en existe **qu'une** (Brow Lift). Aucune fiche pour la décoloration, la teinture, le rehaussement ou le Lash Botox, et **aucune « fiche de diagnostic »**, pourtant citée dans le « Matériel nécessaire » du §1. Le « suivi des clientes » se réduit à deux phrases (fiche technique, gestion). |
| · Réseaux sociaux et communication | `photographier-reseaux-sociaux.md` + sections numérotées 1, 2, 3 de `gestion-activite-fidelisation.md` | Couvert, mais **mal rangé** : voir F. Le point « 4. » est absent. |
| · Gestion d·activité et fidélisation | `gestion-activite-fidelisation.md` (« Accueil, prix et organisation », « Expérience cliente », « 5. Mesurer ses résultats ») | Couvert |
| PARTIE IV · ÉVALUATION | Pas d'intercalaire d'origine | Ouverture créée par le design (`400`) |
| · Questionnaire de connaissances et références | `qcm-page-1.md`, `qcm-page-2.md`, `sources-verification.md` | Couvert. Le corrigé n'est pas fourni : voir D. Il ira dans un PDF séparé (DECISIONS). |
| (4ᵉ de couverture) | Aucune page d'origine | Créée par le design (`990`). N'y mettre **aucun texte inventé** : logo et nom de marque seulement. |

### A2. Renvois vers du contenu absent ou introuvable

| Fichier | Passage | Problème | Statut |
|---|---|---|---|
| `fiche-technique-brow-lift-hygiene.md` l.17 | « Pour la gamme Thuya citée dans le manuel initial » | Renvoi vers un « manuel initial ». Ce contenu est maintenant fourni (§2 de `brow-lift-thuya-teinture.md`). | [ARBITRÉ PLAN #6] → « présentée au §2 (Brow Lift — Thuya) » |
| `fiche-technique-brow-lift-hygiene.md` l.17 | « Les temps présentés dans la version initiale » | Même renvoi | [ARBITRÉ PLAN #6] → « Les temps présentés au §2 » |
| `sources-verification.md` l.11 | « Noemi USA — support, Hybrid Dye et Innovate » | **« Hybrid Dye »** n'est nommé nulle part dans le manuel. Le §7 parle seulement de « la teinture Noemi autorisée pour les cils ». S'agit-il du même produit ? | [À VALIDER] |
| `sources-verification.md` l.19–23 | « Brow Daddy Hybrid Tint — gamme officielle » / « — ratio distributeur » | Le §3 ne donne **aucun ratio**, ni temps, ni protocole | [À VALIDER] La cliente fournit le ratio, ou la mention « ratio distributeur » reste une simple source |
| `sources-verification.md` l.27–29 | « Noemi Freelift — guide technique » + URL tronquée « …rehaussement-cils-sa[?] » | **Freelift n'est utilisé nulle part** : le rehaussement du manuel se fait avec Noemi **Innovate**. Source orpheline, et URL incomplète (cachée par le mockup). | [À VALIDER] Supprimer la source ou ajouter le contenu ; obtenir l'URL complète, **ne pas la compléter de mémoire** |
| `sources-verification.md` l.37 | « Les produits Thuya, Brow Daddy, Noemi et ZOLA utilisés… » | Aucune **référence technique** pour Thuya, ZOLA (BB Blond Powder, oxydant 3 %), Noemi Intense (Lash Botox) ni Brow Daddy StainMe | [À VALIDER] Compléter la liste des sources si la cliente les a |
| `decoloration-sourcils.md` l.28 | « Les revendeurs indiquent 3 à 20 minutes selon le résultat visé ; » | « Les revendeurs » : aucun n'est cité dans les sources. La phrase **se termine par un point-virgule**, sans suite : texte peut-être tronqué. | [À VALIDER] |
| `brow-lift-thuya-teinture.md` l.28 | « (Hybrid Tint ou StainMe) » | **StainMe** n'apparaît ni dans les sources, ni dans le tableau de vigilance (qui parle de « Teinture hybride ») | [À VALIDER] |
| `restructuration-mapping.md` l.13 | « …miroir et fiche de diagnostic. » | Aucun modèle de fiche de diagnostic n'est fourni (voir A1, « Fiches pratiques ») | [À VALIDER] La cliente fournit sa fiche, ou rien |
| `restructuration-mapping.md` l.39 | « respecter les consignes spécifiques si une teinture ou un Brow Lift est associé » | Renvoi vers les §2 et §3, désormais présents ; mais les consignes de **teinture** restent « à confirmer » | Information |
| `photographier-reseaux-sociaux.md` l.34 | « Teinture hybride : entretien et précautions » | Idée de publication. Le manuel ne contient **aucune consigne d'entretien** pour la teinture hybride. | Information |
| `qcm-page-1.md` l.37 | « rôle du neutralisant dans une lamination », « après l'étape de réduction » | Termes absents du manuel : voir D (Q5) | [À VALIDER] |
| `cycle-de-vie-sourcil.md` / sommaire | « Anatomie… » | Aucune page d'anatomie | [À VALIDER] |

### A3. Numérotations qui sautent ou se répètent

| Zone | Numérotation constatée | Problème | Traitement proposé |
|---|---|---|---|
| Partie I | **1** (« 1. Diagnostic et restructuration », `brow-lift-thuya-teinture.md`), **1** (« 1. RESTRUCTURATION DES SOURCILS & MAPPING »), 2, 3, 4 | « 1. » en double. La suite 1 → 4 est désormais complète (2 et 3 reçus). | [ARBITRÉ PLAN #9] Un seul §1, intitulé « 1. Restructuration des sourcils & mapping ». La synthèse « Diagnostic et restructuration » est placée en tête, sans numéro. |
| Partie II | 5, 6, 7, 8, puis « Conseils après prestation » **non numéroté** | Suite logique de la Partie I (1–4 → 5–8). La dernière rubrique n'a pas de numéro. | [À VALIDER] « 9. Conseils après prestation », ou garder sans numéro (forme d'origine) |
| Partie III, réseaux sociaux | 1, 2, 3 (`photographier-reseaux-sociaux.md`) | Repart à 1 | Voir ligne suivante |
| Partie III, page gestion | **1, 2, 3, 5** (`gestion-activite-fidelisation.md` l.20, 24, 35, 43) | **Le 4 manque.** Ces 4 sections relèvent des réseaux sociaux et doublonnent la série 1–3 précédente. | [ARBITRÉ PLAN #4] Réseaux 1 → 6 (ex-gestion 1, 2, 3 → 4, 5, 6) ; « Mesurer ses résultats » passe en Gestion, sans numéro. **Réserve** : `DECISIONS.md` attend encore le « point 4 de Gestion d'activité ». La renumérotation ne doit pas faire oublier qu'**un contenu manque peut-être**. À confirmer avec la cliente avant l'assemblage final ; si le point 4 arrive, l'insérer après « 6. Attirer une clientèle locale ». |
| QCM | 1 → 15, continu | RAS | — |
| Restructuration | Étape 1 → Étape 5, continu | RAS. Ne pas confondre avec « Étape 1 : permanente / Étape 2 : neutralisant » du Brow Lift ni avec « Step 1 / 1.5 / 2 » de Noemi (voir C2). | Traitement visuel distinct |

### A4. Mise à jour de la liste « En attente » de `DECISIONS.md`
- §2 Brow Lift (Thuya, temps de pose) : **reçu** (`3d19aee4`).
- §3 Teinture : **reçu mais incomplet** (protocole, ratio et temps de pose « à confirmer »).
- « Diagnostic et application en cabine » : **toujours sans page dédiée**.
- Point 4 de la page Gestion : **toujours absent**.
- À ajouter : contenu « Anatomie », fiche(s) pratique(s) et fiche de diagnostic, URL Freelift, sources Thuya / ZOLA / Intense / StainMe, et l'**autorisation écrite de @refreshednrefined**.

---

## B. Coquilles, fautes et typographie

### B1. Corrections ponctuelles autorisées

| # | Fichier (ligne) | Texte original | Correction | Statut |
|---|---|---|---|---|
| 1 | `sommaire.md` (33) | Gestion d·activité et fidélisation | Gestion d’activité et fidélisation | [ARBITRÉ PLAN #7] |
| 2 | `sommaire.md` (17–37) | « · » en tête de chaque entrée | Supprimer (la puce vient du design) | [CORRIGER] |
| 3 | `sommaire.md` (9) ; `couverture.md` (15) et en-têtes et pieds de page de toutes les pages | DOLCE LASH & BROW  ·  SUPPORT PÉDAGOGIQUE / DOLCE LASH & BROW  •  Support de formation (doubles espaces, deux séparateurs « · » et « • ») | Dolce Lash & Brow · Support pédagogique (une espace insécable de chaque côté du séparateur, un seul séparateur) | [ARBITRÉ PLAN #8] pour la marque ; [CORRIGER] pour les espaces |
| 4 | `sommaire.md` (15) ; `partie-1-ouverture.md` (7) ; `brow-lift-thuya-teinture.md` (4) | PARTIE I · SOURCILS / PARTIE I — SOURCILS / PARTIE I — LES SOURCILS | Partie I — Sourcils (voir la réserve de symétrie en C3) | [ARBITRÉ PLAN #8] |
| 5 | `sommaire.md` (25) ; `partie-2-ouverture.md` (7) ; `partie-2-cils-contenu.md` (7) | PARTIE II · CILS / PARTIE II — LES CILS | Partie II — Les cils (en-têtes du guide) | [ARBITRÉ GUIDE-DESIGN] |
| 6 | `restructuration-mapping.md` (13) | petits ciseaux si nécessaires | petits ciseaux si nécessaire | [CORRIGER] |
| 7 | `restructuration-mapping.md` (7) | 1. RESTRUCTURATION DES SOURCILS & MAPPING | 1. Restructuration des sourcils & mapping (capitales éventuelles par CSS) | [ARBITRÉ PLAN #9] |
| 8 | `brow-lift-thuya-teinture.md` (6) | ## 1. Diagnostic et restructuration | Diagnostic et restructuration (sans « 1. », en tête du §1) | [ARBITRÉ PLAN #9] |
| 9 | `decoloration-sourcils.md` (34) | OXYDANT UTILISE : ZOLA 3 % | OXYDANT UTILISÉ : ZOLA 3 % | [ARBITRÉ PLAN #2] |
| 10 | `decoloration-sourcils.md` (36) | Oxydant teinture sourcils ZOLA a 3 % | Oxydant teinture sourcils ZOLA à 3 % | [CORRIGER] (accent oublié par PLAN #2, même bloc) |
| 11 | `decoloration-sourcils.md` (36) | associe a la poudre | associé à la poudre | [ARBITRÉ PLAN #2] |
| 12 | `decoloration-sourcils.md` (37) | ZOLA Baby Blonde Powder | ZOLA BB Blond Powder | [ARBITRÉ PLAN #1] |
| 13 | `decoloration-sourcils.md` (38) | Ne pas remplacer par un oxydant plus concentre. | Ne pas remplacer par un oxydant plus concentré. | [ARBITRÉ PLAN #2] |
| 14 | `decoloration-sourcils.md` (40) | Respecter le ratio de melange | Respecter le ratio de mélange | [ARBITRÉ PLAN #2] |
| 15 | `decoloration-sourcils.md` (36–38) | Retours à la ligne forcés au milieu de la phrase (« …associe a la poudre / ZOLA Baby Blonde Powder… ») | Paragraphe continu | [CORRIGER] (mise en forme seulement) |
| 16 | `decoloration-sourcils.md` (28) | …3 à 20 minutes selon le résultat visé ; | …3 à 20 minutes selon le résultat visé. | [À VALIDER] La phrase est peut-être tronquée : demander s'il manque une suite. Par défaut, mettre un point final. |
| 17 | `fiche-technique-brow-lift-hygiene.md` (13) | les notices des   références exactes | les notices des références exactes | [CORRIGER] |
| 18 | `fiche-technique-brow-lift-hygiene.md` (17) | Pour la gamme Thuya citée dans le manuel initial | Pour la gamme Thuya présentée au §2 (Brow Lift — Thuya) | [ARBITRÉ PLAN #6] |
| 19 | `fiche-technique-brow-lift-hygiene.md` (17) | Les temps présentés dans la version initiale | Les temps présentés au §2 | [ARBITRÉ PLAN #6] |
| 20 | `partie-2-cils-contenu.md` (25) | **Important :**   ces temps | Important : ces temps (une espace insécable avant « : », une seule espace après). Si « Important » devient le titre de l'encadré : « Ces temps… » | [CORRIGER] |
| 21 | `partie-2-cils-contenu.md` (33) | il est nommé  **Noemi Intense — Step 1.5 — Lash Botox** . Le temps | il est nommé **Noemi Intense — Step 1.5 — Lash Botox**. Le temps | [CORRIGER] |
| 22 | `brow-lift-thuya-teinture.md` (12) | **terminer par la crème de soin Thuya** , à la fin de la prestation. | **terminer par la crème de soin Thuya**, à la fin de la prestation. | [CORRIGER] |
| 23 | `brow-lift-thuya-teinture.md` (24) | ces temps sont ceux demandés pour ton support de formation | ces temps sont ceux demandés pour ce support de formation | [ARBITRÉ PLAN #5] |
| 24 | `brow-lift-thuya-teinture.md` (22, 24 — image d'origine) | « Étape finale :    appliquer… », « Précaution :    ces temps… » (grands blancs) | Une seule espace après « : » | [CORRIGER] |
| 25 | `brow-lift-thuya-teinture.md` (4) ; `partie-2-cils-contenu.md` (7) | Titre « PARTIE I — LES SOURCILS » / « PARTIE II — LES CILS » répété sur une page de contenu | Supprimer ces titres (ils restent sur l'intercalaire et dans l'en-tête courant) | [CORRIGER] (structure) |
| 26 | `gestion-activite-fidelisation.md` (22) | (« / Réservation via le lien en bio ») : guillemet ouvrant isolé en fin de ligne | («&nbsp;Réservation via le lien en bio&nbsp;») | [CORRIGER] |
| 27 | `gestion-activite-fidelisation.md` (20, 24, 35, 43) | 1. Réaliser un Reel efficace / 2. Exemple de calendrier… / 3. Attirer une clientèle locale / 5. Mesurer ses résultats | 4. / 5. / 6. dans le chapitre Réseaux sociaux ; « Mesurer ses résultats » sans numéro, en Gestion | [ARBITRÉ PLAN #4] (réserve en A3) |
| 28 | `qcm-page-1.md`, `qcm-page-2.md` (toutes les réponses) | petit signe « ı » devant chaque réponse (case à cocher mal exportée) | ☐ | [CORRIGER] |
| 29 | `cycle-de-vie-sourcil.md` (11, schéma) | LE CYCLE DE VIE DES CILS | Supprimer (le titre de la page suffit) ; schéma redessiné | [ARBITRÉ PLAN #3] |
| 30 | `cycle-de-vie-sourcil.md` (11, schéma) | LE CYCLE RECOMMENCE NOUVELLE POUSSE DE POILS (ponctuation manquante) | Le cycle recommence, nouvelle pousse de poils | [ARBITRÉ PLAN #3] |
| 31 | Pieds de page de toutes les pages | « Manuel de formation » / « Support pédagogique » / « Support de formation » (3 libellés) | Un seul jeu de libellés, celui du gabarit : en-tête « Support pédagogique », pied de page « Manuel de formation » | [CORRIGER] (gabarit) |
| 32 | `sources-verification.md` (29) | https://browlashworld.com/fr/blog-cils/noemi-freelift-mode-emploi-rehaussement-cils-sa[?] | URL complète fournie par la cliente ; sinon, retirer le lien | [À VALIDER] |

### B2. Règles typographiques systématiques (à appliquer partout)
- **Espaces insécables** avant « : », « ; », « ? », « ! », à l'intérieur des guillemets « … », et entre un nombre et « % ». J'en ai compté **86** dans le texte courant :
  - 13 dans `gestion-activite-fidelisation.md` ;
  - 11 dans `qcm-page-2.md` ;
  - 10 dans `qcm-page-1.md` ;
  - 10 dans `photographier-reseaux-sociaux.md` ;
  - 8 dans `fiche-technique-brow-lift-hygiene.md` ;
  - 7 dans `decoloration-sourcils.md` ;
  - 6 dans `restructuration-mapping.md` ;
  - 5 dans `brow-lift-thuya-teinture.md` ;
  - 5 dans `cycle-de-vie-sourcil.md` ;
  - 4 dans `pourquoi-sourcils-tombent.md` ;
  - 3 dans `partie-2-cils-contenu.md` ;
  - 3 dans `sommaire.md` ;
  - 1 dans `atelier-visuel-brow-lift.md`.

  Les espaces existent déjà dans le texte : il suffit de les rendre insécables (`&nbsp;`).
- **Espace insécable entre un nombre et son unité**, pour éviter les coupures en fin de ligne : « 8 minutes », « 10 minutes », « 11 à 12 minutes maximum », « 3 à 20 minutes », « 3 % », « 1 dose », « 2 doses ».
- **Apostrophes** : elles sont déjà typographiques (’) partout dans le texte courant, sans aucune apostrophe droite. Les garder ainsi dans le HTML.
- **Guillemets** : toujours « … » avec espaces insécables (`gestion-activite-fidelisation.md` ×2, `qcm-page-2.md` ×1).
- **Tirets cadratins** « — » dans les titres de produits et d'étapes (A — Début, Étape 1 — …, Noemi Innovate — Step 1) : les conserver.
- **Casse des titres** : l'original mélange capitales (« 1. RESTRUCTURATION… », « OXYDANT UTILISE ») et casse normale (« 4. Décoloration des sourcils », « Sources et vérification des protocoles »). Écrire tous les titres **en casse normale accentuée** dans le HTML et passer en capitales par CSS si besoin. Cela évite les capitales sans accent comme « UTILISE ».
- **Puces** : les « • » tapés à la main deviennent de vraies listes (`ul.dots`).
- **Doubles espaces** : supprimer partout (voir B1 #3, 17, 20, 21, 24).

### B3. Tournures à proposer à la formatrice (NE PAS appliquer sans son accord)

| Fichier (ligne) | Original | Proposition | Motif |
|---|---|---|---|
| `gestion-activite-fidelisation.md` (13) | Confirmer les rendez-vous, expliquer les retards et les conditions d’annulation. | …expliquer les conditions en cas de retard et d’annulation. | « Expliquer les retards » n'a pas de sens clair (vérifié sur l'original `33b4d2f9`) |
| `brow-lift-thuya-teinture.md` (12) | puis **terminer par la crème de soin Thuya**, à la fin de la prestation. | (laisser, ou supprimer « à la fin de la prestation ») | Pléonasme, et redite avec « Étape finale : » |
| `qcm-page-2.md` (11) | En reprenant le temps de la teinture sourcils | …de la teinture des sourcils | Tournure elliptique |
| `qcm-page-2.md` (39) | aux recommandations fabricant | aux recommandations du fabricant | Tournure elliptique |
| `decoloration-sourcils.md` (36) | Oxydant teinture sourcils ZOLA à 3 % | Oxydant pour teinture des sourcils ZOLA à 3 % | Tournure elliptique (style catalogue) |
| `sources-verification.md` (37) | auprès de Only Lash Paris | auprès d’Only Lash Paris | Les deux formes sont admises |
| `pourquoi-sourcils-tombent.md` (31) | En pratique, avant une prestation : | En pratique, avant une prestation | Un titre d'encadré ne se termine pas par « : » |
| `restructuration-mapping.md` (7) | …DES SOURCILS & MAPPING | …des sourcils et mapping | Le sommaire écrit « et » |
| `qcm-page-1.md` (37) | dans une lamination | dans un Brow Lift | Terminologie : « lamination » n'apparaît nulle part ailleurs (voir C2 et D) |
| `qcm-page-2.md` (13) | le support en silicone | le pad en silicone | Le manuel dit « pad » (voir C2) |

### B4. Faux positifs : formes à conserver [NE PAS TOUCHER]
- « Noemi » sans tréma (nom de marque).
- « Step 1.5 » avec un point décimal (nomenclature du produit, identique dans le QCM).
- « OXIDANT » sur l'étiquette contre « Oxydant » dans le texte.
- « ZOLA », « Hybrid Tint », « StainMe », « Innovate », « Intense » : orthographe des marques.
- « agressive », « surépiler » (jargon métier).
- « l’exogène » (nom de phase).
- « Faire valider le dessin à la cliente » (tournure admise).
- Les majuscules de « Stories à la une : Tarifs, Résultats, Avis, FAQ, Accès, Disponibilités » (noms de rubriques Instagram).
- « Cochez » (vouvoiement de la consigne du QCM).
- « me contacter » dans la colonne « Question à se poser » (voix de la praticienne).
- « Reel », « Story » : anglicismes du réseau, cohérents entre eux.

---

## C. Incohérences

### C1. Noms de produits et de marques

| Élément | Graphies relevées | Recommandation |
|---|---|---|
| Poudre décolorante ZOLA | « ZOLA BB Blond Powder » (intertitre), « ZOLA Baby Blonde Powder » (bloc oxydant), « BB BLOND powder » (boîte photographiée) | « ZOLA BB Blond Powder » partout [ARBITRÉ PLAN #1] |
| Lash Botox Noemi | « Noemi Intense — Lash Botox (soin cils et sourcils) » (tableau §6) ; « 8. Lash Botox — Noemi Intense, Step 1.5 » (titre §8) ; « Noemi Intense — Step 1.5 — Lash Botox » (texte §8, « Dans ce manuel, il est nommé… ») ; « Lash Botox dit « Step 1.5 » » (QCM 12) ; « soin Intense » (§6 Important) | Le texte §8 fixe le nom officiel. Garder les autres formes, qui restent compréhensibles. Option [À VALIDER] : aligner le titre §8 sur « Lash Botox — Noemi Intense — Step 1.5 ». |
| Teinture des sourcils | « Teinture hybride » (sommaire, tableau de vigilance, réseaux sociaux) ; « 3. Teinture des sourcils — Brow Daddy » ; « Hybrid Tint ou StainMe » ; « Brow Daddy Hybrid Tint » et « Noemi … Hybrid Dye » (sources) | Le titre du §3 ne dit pas « hybride » ; StainMe n'est cité nulle part ailleurs. [À VALIDER] Préciser si StainMe entre dans la « teinture hybride » ; sinon la ligne de vigilance et le sommaire ne la couvrent pas. |
| Teinture des cils | « la teinture Noemi autorisée pour les cils avec son révélateur compatible » (§7) — aucune référence précise | [À VALIDER] Est-ce le « Hybrid Dye » cité dans les sources ? |
| Rehaussement | « Noemi Innovate » (§6, sources) ; « Noemi Freelift » (sources seulement) | Freelift est une source orpheline (voir A2) |
| Brow Lift | Thuya (§2, fiche technique). La source « Noemi Innovate » a une URL « lash-lift-brow-lift-innovate-noemi » (Innovate sert aussi au Brow Lift). | Pas de contradiction, mais le manuel n'enseigne le Brow Lift qu'avec Thuya, et aucune source technique Thuya n'est listée |
| Fournisseur | « Only Lash Paris (Brow & Lash) » (×2, texte) ; logo du site sur le mockup : « only lash paris — BROWS & LASHES » | [À VALIDER] Vérifier la dénomination exacte (« Brow & Lash » ou « Brows & Lashes ») |
| Marque de la formatrice | « dolce lash & brow » (logo), « DOLCE LASH & BROW » (en-têtes et pieds de page), « dolcelash&brow » (sac photographié) | « Dolce Lash & Brow » dans le texte ; logo inchangé [ARBITRÉ PLAN #8] |

### C2. Termes techniques
- **Brow Lift / browlift / lamination.** Le texte du manuel écrit **« Brow Lift »** de façon homogène, sur 10 occurrences. « browlift » et « Browlift » n'apparaissent que sur le **mockup du site fournisseur** ; « BROWLIFT » que dans l'**exemple de design** Ls.signaturedesign (rien de cela n'est du texte du manuel). Seule exception : **QCM 5 « lamination »**, l'unique occurrence. → Garder « Brow Lift » ; pour Q5, voir B3 et D.
- **Rehaussement / lash lift.** Le manuel dit « rehaussement (de cils) » de façon homogène (7 occurrences hors URL). « lash lift » n'apparaît que dans une URL. « Lash Botox » reste en anglais (nom du soin). → RAS.
- **Étapes du Brow Lift.**
  - 1ʳᵉ étape : « lotion permanente » (§2, fiche), « permanente » (en-tête de tableau), « Étape 1 ».
  - 2ᵉ étape : « neutralisant » (§2, fiche, QCM 5), « deuxième étape » (§2), « Étape 2 », « deuxième lotion » (Précaution §2).
  - QCM 5 parle d'« étape de réduction », un terme **absent** du manuel.

  → Ces termes désignent les mêmes choses ; le design peut les rapprocher visuellement (par exemple « Étape 1 : permanente »), sans réécrire.
- **Trois systèmes d'étapes** dans la même partie du manuel :
  - « Étape 1 → 5 » du mapping (déroulé de la prestation) ;
  - « Étape 1 / 2 » de Thuya (lotions) ;
  - « Step 1 / 1.5 / 2 » de Noemi (produits).

  → Prévoir un traitement visuel distinct (par exemple pastilles produit pour les Steps, numéros d'étapes pour le déroulé) pour éviter la confusion.
- **Pad / support en silicone.** « pads adaptés » (§5) et « pad en silicone » (§6), mais « support en silicone » dans le QCM 10. → B3.
- **Test de sensibilité / test préalable.** « test de sensibilité » (§4, QCM 2) contre « test préalable » (vigilance, teinture hybride). Synonymes acceptables. Remarque : **ni le §2 Brow Lift ni le §6 rehaussement ne mentionnent de test**, alors que le QCM 2 (réponse C) suppose qu'il en existe un pour le Brow Lift. [À VALIDER]
- **Oxydant / révélateur.** « oxydant » (ZOLA, §4) et « révélateur » (Noemi, §7) : vocabulaire propre à chaque marque. → RAS.
- **Registre.** Infinitifs partout ; « Cochez » au vouvoiement dans le QCM ; un seul tutoiement (« ton support », corrigé par PLAN #5).
- **Lieux.** « cabine » (sommaire), « salon » (gestion), « poste de travail » (hygiène). → RAS.

### C3. Titres, séparateurs, en-têtes et pieds de page
- **Titres de parties.**
  - Partie I : « PARTIE I · SOURCILS » (sommaire), « PARTIE I — SOURCILS » (ouverture), « PARTIE I — LES SOURCILS » (page Brow Lift).
  - Partie II : « PARTIE II · CILS » (sommaire), « PARTIE II — LES CILS » (ouverture et page de contenu).
  - Le plan retient « Partie I — Sourcils » et « Partie II — Les cils ». **L'article n'est présent que pour la Partie II : asymétrie.** [À VALIDER] Choisir une paire symétrique : « Les sourcils / Les cils » (formes présentes dans les originaux) ou « Sourcils / Cils » (forme du sommaire).
- **Séparateurs** : « · » (sommaire, en-tête du cycle), « • » (pieds de page, en-tête de « Pourquoi… »), « — » (ouvertures). → Un seul séparateur par usage, fixé par le gabarit.
- **Pieds de page** : « Manuel de formation » (cycle, pourquoi, mapping), « Support pédagogique » (atelier, fiche, photographier, gestion), « Support de formation » (couverture, décoloration, sources, Brow Lift Thuya). Certaines pages n'ont **aucun** pied de page : ouvertures, Partie II contenu, QCM. → Gabarit unique.
- **En-têtes** : en gras sur une page, en graisse normale sur une autre, absents ailleurs. → Gabarit unique.
- **Intitulés du sommaire ≠ titres de page.**
  - « Anatomie et cycle de vie du poil » ≠ « Le cycle de vie du sourcil ».
  - « Brow Lift : technique et temps de pose » ≠ « 2. Brow Lift — Thuya ».
  - « Teinture hybride et décoloration » ≠ « 3. Teinture des sourcils — Brow Daddy » + « 4. Décoloration des sourcils ».
  - « Atelier visuel Brow Lift et sécurité » ≠ « Atelier visuel — Brow Lift » + « Hygiène, sécurité et qualité ».
  - « Fiches pratiques… » (pluriel) ≠ une seule fiche.
  - « Questionnaire de connaissances et références » ≠ « Évaluation QCM » + « Sources et vérification des protocoles ».

  → Garder les intitulés d'origine du sommaire (ils renvoient sans ambiguïté aux bonnes pages) et les titres d'origine des pages. Ne rien renommer sans accord.
- **Deux titres de niveau 1 sur une même page** : « Fiche technique — Brow Lift » + « Hygiène, sécurité et qualité » ; « Photographier son travail » + « Développer son activité sur les réseaux sociaux ». → À séparer (voir F).

### C4. Titre de page ≠ visuel
- **Cycle de vie.**
  - La page dit « du sourcil », le schéma « DES CILS », le sommaire « du poil ».
  - Le texte décrit **4 phases** (anagène, catagène, télogène, **exogène**) ; le schéma montre anagène, catagène, télogène, puis à nouveau anagène, **sans l'exogène**.
  - PLAN #3 reprend les 4 libellés du schéma d'origine. Le SVG redessiné (`schema-cycle.svg.html`) dessine la libération de l'ancien poil dans la 4ᵉ colonne, mais aucun des libellés retenus ne nomme l'exogène : le décalage entre texte et schéma demeure.
  - [À VALIDER] Accepter ce décalage, ou ajouter dans le schéma le mot « exogène », repris mot pour mot du texte (« phase de libération du poil »), ce qui n'invente rien.
- **Mapping.** Le texte place le repère B « souvent vers le bord externe de l’iris, regard droit », alors que le schéma d'origine fait passer la ligne B **par la pupille** (point rouge). Le schéma vectoriel `schema-mapping.svg.html` suit **le texte** (bord externe de l'iris) : c'est correct, à conserver.
- **Atelier visuel.**
  - Le texte dit « **la photographie ci-dessous** montre trois présentations ». Le design découpe la planche en 3 images : elles doivent rester **sous** le texte d'introduction, sinon « ci-dessous » devient faux. Option [À VALIDER] : adapter le mot.
  - Les 3 vues ne sont pas légendées alors que les puces demandent de travailler « sur chacune des trois images ». → Numéroter 1, 2, 3 [ARBITRÉ PLAN #10].
- **Ouverture Partie II « Les cils »** : même photo (sourcils brossés) que la Partie I, aucun visuel de cils. → Recommandé : un visuel ou un accent propre à chaque partie.
- **Couverture et ouvertures** : la même photo est utilisée trois fois.

### C5. Contradictions entre protocole, fiche technique, points de vigilance et QCM
1. **Lash Botox entre Step 1 et Step 2.**
   - Le §6 l'enseigne (« Ordre des étapes enseigné »).
   - L'encadré Important du §6 dit : « Vérifier expressément auprès du fabricant… certains systèmes imposent de neutraliser avant tout soin. Ne pas appliquer cette séquence sans validation. »
   - Le §8 dit : « sa place exacte dans la procédure restent à valider ».
   - Le tableau de vigilance dit : « emplacement dans la séquence à vérifier auprès du fabricant ».
   - Le QCM 12 retient la réponse B (« À l’étape prescrite par la notice »).

   → Ce n'est pas une contradiction au sens strict, puisque la séquence est conditionnelle. C'est en revanche **le point le plus sensible du manuel** : le tableau ne doit jamais apparaître sans l'encadré, et le temps « 10 minutes » ne doit pas être mis en avant sans sa réserve. Recommandé : que la formatrice obtienne de Noemi une confirmation écrite.
2. **Temps de pose chiffrés et prudence.**
   - Chiffres : Thuya 8 / 10 / 11–12 min (§2), Noemi 10 min (§6), décoloration 3–20 min (« les revendeurs »).
   - Réserves : la fiche technique dit « ne doivent pas être appliqués automatiquement » ; la Précaution du §2 dit « pas présentés comme des durées officiellement validées par Thuya », « Ne jamais dépasser les limites du fabricant » ; le QCM 3 attend « La notice… et le diagnostic ».

   → Cohérent **si** chaque tableau garde sa réserve. Si la limite d'une notice est inférieure à « 11 à 12 minutes maximum », c'est la notice qui s'applique (« qui prime sur ce manuel »).
3. **Séquence du Brow Lift.** La fiche technique (« préparation, lotion permanente, retrait complet, neutralisant, retrait et soin final ») correspond au §2 (nettoyer → lotion permanente → retirer complètement → neutralisant → retirer → crème de soin). → Cohérent.
4. **Peau irritée : niveau d'interdiction variable.**
   - §1 synthèse : « sans intervenir sur une peau irritée ou lésée ».
   - Étape 4 : « **Éviter** l’épilation sur peau lésée, irritée ou fragilisée ».
   - « Pourquoi… » : « **Reporter** tout traitement chimique sur une zone irritée ».
   - Checklist : « **Aucune** prestation sur une zone présentant une infection, une lésion ou une irritation active ».
   - QCM 1 : « reporter le soin ».

   → Pas de contradiction de fond, mais une intensité variable. Ne pas réécrire ; donner le même poids visuel d'alerte à chacune de ces phrases.
5. **Associer Brow Lift et teinture.** Le §3 (« Après un Brow Lift, vérifier la compatibilité et les durées spécifiques avant d’associer les deux prestations »), l'Étape 5 du mapping et le QCM 6 sont cohérents. Mais le manuel ne donne **aucune donnée de teinture** : l'apprenante ne peut pas appliquer ce qu'on lui demande de vérifier.
6. **Test de sensibilité.** Il est exigé en décoloration (§4, étape 1) et en teinture hybride (vigilance). Il n'est pas mentionné pour le Brow Lift ni pour le rehaussement, alors que le QCM 2 le suppose. Voir C2.
7. **QCM hors manuel** : Q4, Q5 et Q10 (voir D).
8. **Droits sur les photos et discours du manuel.** « ne jamais présenter comme sien le travail d’une autre professionnelle » (`photographier-reseaux-sociaux.md`) alors que l'atelier visuel utilise des photos portant le filigrane @refreshednrefined. Voir E1.
9. **Règle du guide contre décision de la cliente.** `design/GUIDE-DESIGN.md` (« Règles de texte ») dit « Les filigranes et crédits d'autrui ne doivent jamais apparaître ». `DECISIONS.md`, PLAN #10 et le tableau des visuels du même guide disent de garder le filigrane et d'ajouter « Crédit photo : @refreshednrefined ». → **La décision de la cliente prime** ; corriger la phrase du guide pour éviter qu'un designer masque le crédit.
10. **Notes de transcription périmées.** `atelier-visuel-brow-lift.md` (ligne VISUEL et notes) et `photographier-reseaux-sociaux.md` (note l.48) donnent encore « @refreshedinrefined [?] ». `DECISIONS.md` mentionne aussi une ancienne lecture erronée, « @refreshedandsheek ». La planche HD `5e1872c7` montre lisiblement **« @refreshednrefined »** (vérifié). → Mettre à jour ces notes.
11. **Tableau de vigilance en Partie I.** Il traite aussi du rehaussement de cils et du Lash Botox, enseignés en Partie II. Voir F pour le choix de placement.

---

## D. QCM — corrigé proposé (pour le PDF « formatrice » séparé, jamais dans le manuel élève)

Ce corrigé n'existe pas dans l'original. Il est **déduit du contenu du manuel** et **doit être validé par la formatrice** avant diffusion.

| Q | Réponse | Justification par le manuel | Couverture |
|---|---|---|---|
| 1 | **B** — Irritation ou lésion sur la zone à traiter | Checklist hygiène : « Aucune prestation sur une zone présentant une infection, une lésion ou une irritation active. » ; « Pourquoi… » : « Reporter tout traitement chimique sur une zone irritée… » ; §1 : « sans intervenir sur une peau irritée ou lésée ». | Couvert |
| 2 | **B** — Pour évaluer le poil, la peau et les contre-indications | Fiche technique, « Avant la séance » : antécédents de réaction, irritations ou lésions, « porosité, l’épaisseur, la densité et la direction des poils » ; tableau du §2 selon la « Nature du poil » ; §4 : « Effectuer le diagnostic, vérifier les contre-indications et le test de sensibilité » (réfute C). | Couvert (le test n'est pas mentionné pour le Brow Lift : voir C2) |
| 3 | **A** — La notice de la référence exacte et le diagnostic | Précaution du §2 : « Vérifier la notice des références exactes » ; tableau selon la nature du poil ; fiche : temps « à confirmer sur les notices… ne doivent pas être appliqués automatiquement » ; Sources : « la notice… prime sur ce manuel » ; §4 : « Adapter au poil et à l’objectif, pas uniquement à la couleur de peau » (réfute C). | Couvert |
| 4 | **C** — Arrêter, retirer le produit et évaluer la situation | **Aucune consigne explicite sur la brûlure.** Passages les plus proches : §4 « Surveiller visuellement et retirer… », « surveiller toute irritation », « contrôler… la tolérance cutanée » ; fiche « Vérifier… la tolérance cutanée et le confort » ; checklist « En cas de projection oculaire : rinçage immédiat abondant et avis médical urgent ». C est la seule réponse sûre. | **Non couvert explicitement.** [À VALIDER] La formatrice peut fournir une consigne « en cas de brûlure » (ne pas l'inventer). |
| 5 | **A** — Fixer la nouvelle forme du poil après l’étape de réduction | Le §2 et la fiche placent le **neutralisant** en 2ᵉ étape, après la lotion permanente. Mais le manuel **n'explique pas le rôle** du neutralisant (« fixer ») et n'emploie **ni « lamination » ni « étape de réduction »**. B et C sont absurdes ; A se trouve par élimination. | **Partiel.** [À VALIDER] Harmoniser « lamination » → « Brow Lift » (B3), ou faire ajouter par la formatrice une phrase sur le rôle du neutralisant. |
| 6 | **A** — Pour éviter une réaction indésirable ou un surtraitement | §3 : « Après un Brow Lift (Thuya), vérifier la compatibilité et les durées spécifiques avant d’associer les deux prestations » (Brow Daddy, autre marque) ; vigilance : « Éviter le surtraitement, utiliser uniquement l’oxydant compatible… », « Sensibilisation possible » ; Sources : notices de référence pour « les compatibilités ». | Couvert |
| 7 | **B** — Respecter la morphologie, l’implantation et les souhaits réalistes | §1 Objectif : « ligne harmonieuse adaptée au visage, tout en respectant la pousse naturelle, la densité et les souhaits de la cliente » ; Étape 2 : « Adapter à l’implantation naturelle », « selon la morphologie ». | Couvert |
| 8 | **B** — Irritation cutanée et fragilisation des poils | « Pourquoi… » : « les traitements chimiques mal adaptés… peuvent casser les poils ou fragiliser la zone » ; §4 : « surveiller toute irritation », « tolérance cutanée » ; vigilance : « Éviter le surtraitement ». | Couvert |
| 9 | **A** — En suivant la notice de la gamme et le diagnostic | §7 : « Préparer, appliquer et retirer selon la notice exacte… éventuels ajustements de temps après rehaussement » ; §5 (diagnostic) ; aucun temps fixe dans le manuel (réfute B et C). | Couvert |
| 10 | **A** — Pour adapter la courbure à la longueur et à la direction des cils | §5 : « choisir les pads adaptés » ; §6 : « positionner le pad en silicone et aligner soigneusement les cils » ; vigilance : « contrôler le placement des cils ». La **raison** (courbure, longueur, direction) n'est pas écrite, et le terme diffère (« support » au lieu de « pad »). | **Partiel** |
| 11 | **A** — Éviter le contact des produits avec l’œil et respecter les consignes de sécurité | §4 : « sans contact avec les yeux » ; §7 : « Respecter les précautions oculaires » ; vigilance : « Protéger l’œil » ; checklist : projection oculaire. | Couvert |
| 12 | **B** — À l’étape prescrite par la notice du système utilisé | §8 : « sa place exacte dans la procédure restent à valider avec la notice du fabricant » ; Important du §6 : « Ne pas appliquer cette séquence sans validation » ; vigilance Lash Botox. | Couvert, mais **piège pédagogique** : le tableau du §6 « enseigne » justement la place entre les deux étapes. A est fausse à cause de « Systématiquement… sans vérification ». Bien expliquer ce point en correction. |
| 13 | **A** — Pour la traçabilité et le suivi en cas de réaction | Fiche : « noter les produits, lots, temps effectivement appliqués et réactions » ; gestion : « Conserver un suivi des prestations et des éventuelles réactions ». | Couvert (le mot « traçabilité » n'est pas employé) |
| 14 | **A** — Des conseils adaptés à la technique et aux recommandations fabricant | Fiche : « Remettre les recommandations du fabricant » ; Partie II, « Conseils après prestation » ; Étape 5 du mapping ; §4 : « Après prestation : éviter les frottements… ». | Couvert |
| 15 | **B** — Évaluer leur état et différer la prestation si nécessaire | §5 : « Observer les cils, leur état et les éventuelles contre-indications » ; « Pourquoi… » : « Reporter tout traitement chimique… lorsque l’état des poils paraît préoccupant » (sourcils, appliqué ici par analogie). | Couvert (par analogie pour les cils) |

**Remarques pour la formatrice (aucune modification sans son accord)**
- **Répartition des bonnes réponses** : A = 8 (Q3, 5, 6, 9, 10, 11, 13, 14), B = 6 (Q1, 2, 7, 8, 12, 15), C = 1 (Q4). La réponse A est juste cinq fois sur six de Q9 à Q14. Une apprenante peut deviner ; mélanger l'ordre des réponses est recommandé.
- Plusieurs distracteurs sont évidents (« Nettoyer les pinceaux », « Décolorer la peau », « Ce n’est jamais nécessaire ») : le QCM est facile.
- **Zones non évaluées** : cycle du poil, repères du mapping, ratio de décoloration, et toute la Partie III (photos, réseaux, gestion). À la discrétion de la formatrice.
- La consigne « Cochez une seule réponse par question. 15 questions — 1 point par bonne réponse » et « Score : … / 15 » sont cohérentes.
- La page 2 du QCM n'a pas de titre de rappel. Le design peut ajouter un libellé de structure (« Évaluation QCM — suite »).

---

## E. Droits et images tierces

| # | Visuel (page d'origine) | Constat | Risque | Recommandation |
|---|---|---|---|---|
| E1 | Planche de 3 sourcils — « Atelier visuel — Brow Lift » (`5c5b0b5d` ; HD `5e1872c7` ; `design/assets/atelier-brow-1..3.jpg`) | Filigrane blanc **« @refreshednrefined »** sur la vue 3, lisible sur la version HD. Les 3 vues montrent le même sourcil, avec le même cadrage, dans un montage typique d'un compte Instagram : **les 3 photos sont très probablement de cette professionnelle**, pas seulement la 3ᵉ. | **Élevé.** Travail d'une tierce personne dans un support commercial de formation, en contradiction avec la règle du manuel lui-même. | [ARBITRÉ DECISIONS] Filigrane conservé (jamais effacé, recadré ni masqué) + « Crédit photo : @refreshednrefined ». **En plus** : obtenir de ce compte une **autorisation écrite** de reproduction. À défaut, remplacer par des photos avant / après de la formatrice. Le crédit seul ne vaut pas autorisation. |
| E2 | Mockup de smartphone — page « Sources » (`d5e9ba52`) | Capture du site **Only Lash Paris** (logo, textes marketing, catégorie « Browlift », photos produits **Thuya**) dans un gabarit d'iPhone. Il cache une partie du texte et l'URL Freelift. | Moyen : marque et contenus d'un tiers, gabarit de mockup d'origine inconnue | **Ne pas reprendre** le mockup. Garder la mention texte du fournisseur et des liens cliquables. Pour montrer le logo Only Lash Paris, demander son accord. |
| E3 | Photos produits ZOLA — page décoloration (`882f6e3e` ; `design/assets/zola-*.jpg`) | Packshots détourés (pot « BB BLOND powder », flacon « OXIDANT 3 % »), sans doute pris sur le site de la marque ou d'un revendeur. La boîte porte « ZOLA × @… » (compte partenaire illisible). | Faible à moyen (photos d'identification de produit) | Confirmer l'origine. Idéalement, photographier les produits de la formatrice ou utiliser les visuels presse ZOLA avec accord. Le « @… » est illisible à 45 mm : ne pas l'agrandir. |
| E4 | Schéma du visage (crayon, lignes rouges et bleues, lettres C B A A B C) + photo de mapping au fil (femme brune, mains gantées de noir) — page mapping (`7092270e`) | Aucun filigrane, mais **origine inconnue** : très probablement trouvés sur internet (Pinterest, Instagram, banque d'images). | Moyen | Schéma : remplacé par le SVG maison `schema-mapping.svg.html` (recommandé). Photo : la remplacer par une photo de la formatrice ou une photo sous licence, ou la retirer. |
| E5 | Infographie « LE CYCLE DE VIE DES CILS » sur fond texturé crème — page cycle (`d5c88c8b`) | Origine inconnue (modèle de type Canva ou visuel d'un tiers) ; de plus, mauvais titre | Moyen | Remplacée par le SVG maison `schema-cycle.svg.html` [ARBITRÉ PLAN #3]. Ne pas réutiliser l'image d'origine. |
| E6 | Portrait de couverture (profil, yeux fermés) — couverture et ouvertures I et II (`20508de6`, `da60b703`, `2ca20cc7` ; `portrait-*.jpg`) | Aucun filigrane. Banque d'images, IA ou séance photo : inconnu. Personne identifiable. | Moyen (droit d'auteur et droit à l'image) | [À VALIDER] La formatrice confirme qu'elle a la licence ou l'autorisation du modèle |
| E7 | Sac rose « Beauté du regard » / « dolcelash&brow » avec jambes en escarpins — fond de 7 pages (`aa1568b2`, `d5c88c8b`, `a71c0fb7`, `7092270e`, `882f6e3e`, `5c5b0b5d`, `3d19aee4` ; `sac-jambes.jpg`) | Le sac porte la marque de la formatrice : probable visuel de marque (séance photo, mockup ou IA). Aucun crédit. | Faible si c'est un visuel commandé par la formatrice | [À VALIDER] Confirmer l'origine et les droits (modèle, photographe ou générateur) |
| E8 | Exemple de design « Ls.signaturedesign » (`456f8945`) | Photo d'écran du travail d'une autre graphiste (« PRÉSENTATION DU BROWLIFT »), avec le crédit « Ls.signaturedesign » et la photo d'un modèle tiers | Élevé si on copie | **Inspiration de style seulement.** Ne reprendre ni ses photos, ni ses textes, ni une mise en page identique. |
| E9 | Marques citées : Noemi, Brow Daddy, Thuya, ZOLA, Only Lash Paris, Instagram ; mot « Botox » | Usage pour désigner les produits : normal. « Botox » est une **marque déposée** (toxine botulique) ; « Lash Botox » est l'appellation du marché. | Faible | Garder la phrase du manuel « Le Lash Botox est un soin cosmétique et non une injection. », bien visible, car elle lève l'ambiguïté. |

---

## F. Structure finale proposée

Ce plan est aligné sur `contenu/PLAN.md` (fichiers et `data-id` entre crochets). **Chaque fichier transcrit y est rattaché.** Les écarts par rapport au sommaire d'origine sont justifiés après le plan.

**Couverture** [`010-couverture` / `couverture`] ← `couverture.md`

**Sommaire** [`020-sommaire` / `sommaire`] ← `sommaire.md`. Intitulés d'origine conservés, avec les corrections B1 #1 et #2 et les numéros de page automatiques.

**PARTIE I — SOURCILS** (voir la réserve de symétrie en C3)
1. Ouverture Partie I [`030` / `partie-1`] ← `partie-1-ouverture.md`
2. *Anatomie et cycle de vie du poil* → « Le cycle de vie du sourcil » [`040` / `cycle`] ← `cycle-de-vie-sourcil.md` + schéma SVG. **Anatomie manquante** : emplacement `.pending` seulement si la formatrice annonce un contenu.
3. *Pourquoi les sourcils tombent-ils ?* [`050` / `chute`] ← `pourquoi-sourcils-tombent.md`
4. *Diagnostic et application en cabine* → **pas de page dédiée.** L'entrée du sommaire pointe vers le §1-A [`060` / `diagnostic`], comme dans PLAN. [À VALIDER] Si la formatrice fournit une page « application en cabine », l'insérer ici, avant le §1.
5. *Restructuration et mapping* → §1, deux pages :
   - §1-A [`060` / `diagnostic`] ← synthèse « Diagnostic et restructuration » (`brow-lift-thuya-teinture.md` l.6–8, sans numéro) + Objectif, Matériel nécessaire, Étape 1 (`restructuration-mapping.md`) ;
   - §1-B [`070` / `mapping`] ← Étapes 2 à 5 + tableau A / B / C + schéma SVG (`restructuration-mapping.md`).
6. *Brow Lift : technique et temps de pose* → §2 Brow Lift — Thuya [`080` / `browlift`] ← `brow-lift-thuya-teinture.md` l.10–24. Tableau des temps et **Précaution dans un `.alert` collé au tableau**.
7. *Teinture hybride et décoloration* →
   - §3 Teinture des sourcils — Brow Daddy [`090` / `teinture`] ← `brow-lift-thuya-teinture.md` l.26–30, avec un rappel de la ligne de vigilance « Teinture hybride ». **Contenu incomplet** : la phrase « restent à confirmer » doit rester visible ;
   - §4 Décoloration [`100` / `decoloration`] ← `decoloration-sourcils.md`.
8. *Atelier visuel Brow Lift et sécurité* →
   - Atelier visuel — Brow Lift [`110` / `atelier`] ← `atelier-visuel-brow-lift.md` (photos 1, 2, 3 **sous** le texte, filigrane et crédit) ;
   - Hygiène, sécurité et qualité [`120` / `hygiene`] ← `fiche-technique-brow-lift-hygiene.md`, 2ᵉ moitié (checklist + points de vigilance).

**PARTIE II — LES CILS**

9. Ouverture Partie II [`200` / `partie-2`] ← `partie-2-ouverture.md`
10. *Diagnostic, rehaussement de cils, teinture et Lash Botox* → deux pages :
    - §5 + §6 [`210` / `rehaussement`] ← `partie-2-cils-contenu.md` l.9–25 (titre « PARTIE II — LES CILS » retiré de la page de contenu) ;
    - §7 + §8 + Conseils après prestation [`220` / `teinture-cils`] ← `partie-2-cils-contenu.md` l.27–37.

**PARTIE III — PRATIQUE PROFESSIONNELLE**

11. Ouverture Partie III [`300` / `partie-3`]. Pas de source ; seul le titre du sommaire.
12. *Fiches pratiques et suivi des clientes* → Fiche technique — Brow Lift [`310` / `fiche-technique`] ← `fiche-technique-brow-lift-hygiene.md`, 1ʳᵉ moitié (avant, pendant, après la séance ; renvois B1 #18 et #19).
13. *Réseaux sociaux et communication* →
    - Photographier son travail [`320` / `photographier`] ← `photographier-reseaux-sociaux.md` l.7–14 ;
    - Développer son activité sur les réseaux sociaux, 1 à 3 [`330` / `reseaux`] ← `photographier-reseaux-sociaux.md` l.16–37 ;
    - suite 4 à 6 [`340` / `reseaux-2`] ← `gestion-activite-fidelisation.md` l.20–41 (ex-1, 2, 3 → 4, 5, 6). **Emplacement de l'ex-point « 4. » à réserver** tant que la formatrice n'a pas confirmé qu'il n'existe pas.
14. *Gestion d’activité et fidélisation* [`350` / `gestion`] ← `gestion-activite-fidelisation.md` l.7–18 (Accueil, prix et organisation ; Expérience cliente) + l.43–50 (« Mesurer ses résultats », sans numéro).

**PARTIE IV — ÉVALUATION**

15. Ouverture Partie IV [`400` / `partie-4`]. Pas de source.
16. *Questionnaire de connaissances…* → Évaluation QCM, 2 pages [`410` / `qcm`, `qcm-2`] ← `qcm-page-1.md`, `qcm-page-2.md`. **Aucune réponse indiquée.**
17. *…et références* → Sources et vérification des protocoles [`430` / `sources`] ← `sources-verification.md` (sans le mockup ; liens cliquables ; URL Freelift à compléter ou à retirer).

**4ᵉ de couverture** [`990` / `dos`]. Pas de source : logo et nom de marque, sans texte inventé.

**Document séparé** : Corrigé du QCM, réservé à la formatrice [`corrige/010-corrige`] ← section D de cet audit, après sa validation.

### Écarts par rapport au sommaire d'origine, et leur justification
1. **Ouvertures des Parties III et IV et 4ᵉ de couverture ajoutées.** Le sommaire annonce 4 parties, mais seules I et II ont un intercalaire d'origine. Ajout purement structurel, pour un rythme homogène. Aucun texte nouveau, en dehors des intitulés du sommaire.
2. **Page « Fiche technique + Hygiène » coupée en deux.** La fiche Brow Lift va en Partie III ; « Hygiène, sécurité et qualité » va en Partie I.
   - *Raisons* : le sommaire place « …et sécurité » en Partie I, juste après l'atelier visuel ; il annonce des « Fiches pratiques et suivi des clientes » en Partie III. La fiche (avant, pendant, après ; noter lots et réactions ; programmer un suivi) est une fiche pratique de suivi. Les deux contenus avaient chacun leur titre de niveau 1 : deux sections distinctes avaient simplement été collées sur une même page.
   - *Inconvénient* : le tableau de vigilance cite le rehaussement de cils et le Lash Botox avant la Partie II. C'est acceptable, car le tableau est transversal et, en le lisant tôt, l'apprenante connaît les règles de sécurité avant toute technique chimique.
   - *Option* [À VALIDER] : ajouter en Partie II un renvoi de structure « Voir aussi : Hygiène, sécurité et qualité, p. {{p:hygiene}} ».
3. **Sections 1, 2, 3 de la page Gestion (Reel, calendrier, clientèle locale) déplacées vers « Réseaux sociaux et communication » et renumérotées 4 à 6** [ARBITRÉ PLAN #4]. Leur contenu est entièrement consacré aux réseaux sociaux. Leur numérotation reprenait à 1 alors que la série 1–3 des réseaux venait de se terminer. Le sommaire sépare bien « Réseaux sociaux et communication » de « Gestion d’activité ».
4. **« Mesurer ses résultats » reste en Gestion d’activité, sans numéro** [ARBITRÉ PLAN #4]. Ses indicateurs « Réservations » et « Clientes fidèles » relèvent de la gestion et de la fidélisation. *Alternative* : ses indicateurs « Visites du profil » et « Messages reçus » le rattacheraient aussi aux réseaux. Les deux placements se défendent ; l'arbitrage est conservé.
5. **« Photographier son travail » ouvre le chapitre Réseaux sociaux**, comme sur la page d'origine, dont c'était le premier titre. Il sert de transition (photos avant / après, autorisation de publication).
6. **Fusion des deux « 1. »** [ARBITRÉ PLAN #9]. La synthèse du §1 de la page Brow Lift (ancienne version du manuel) introduit le §1 détaillé, sans perte de texte.
7. **Titres « PARTIE I — LES SOURCILS » et « PARTIE II — LES CILS » retirés des pages de contenu.** Ce sont des doublons des intercalaires ; ils restent dans l'en-tête courant.
8. **« Diagnostic et application en cabine » renvoie vers le §1-A.** C'est l'approximation la plus fidèle (le diagnostic y est traité), mais elle reste **à valider** : « application en cabine » n'a pas de contenu.

---

## G. Points de sécurité : à reproduire mot pour mot et bien visibles

Règle générale : chaque phrase ci-dessous est reprise **intégralement**, avec seulement les corrections de B1 et B2. Les phrases marquées ⚠ vont dans un encadré `.alert`. Les autres restent au moins en évidence : gras, pastille ou carte. Un **temps de pose chiffré ne doit jamais être affiché sans la réserve qui l'accompagne, sur la même page et à côté.**

### G1. Primauté des notices (page Sources, à rappeler en tête de protocole si possible)
- ⚠ « Vérifier la notice livrée avec chaque produit, qui prime sur ce manuel. »
- ⚠ « Les notices des fabricants restent les références pour les temps de pose, les compatibilités et les précautions de chaque produit. »

### G2. Limites du rôle et avis médical (« Pourquoi les sourcils tombent-ils ? »)
- ⚠ « Une perte en plaques, rapide, persistante ou associée à rougeur, démangeaisons, squames ou douleur mérite un avis médical. »
- ⚠ « Une technicienne esthétique ne pose pas de diagnostic médical. »
- ⚠ « Reporter tout traitement chimique sur une zone irritée ou lorsque l’état des poils paraît préoccupant. »
- « Observer la densité, les zones clairsemées, l’état de la peau et la résistance apparente du poil. Questionner sans juger sur les épilations et soins récents. »
- (Cycle) « Les durées varient selon les personnes et les follicules ; les schémas ne sont pas un chronomètre individuel. »

### G3. §1 Diagnostic, restructuration et mapping
- « Épiler uniquement les poils hors du tracé, sans intervenir sur une peau irritée ou lésée. » (synthèse §1)
- « Faire valider le dessin à la cliente avant l’épilation. »
- ⚠ « Éviter l’épilation sur peau lésée, irritée ou fragilisée ; pour la cire, respecter les contre-indications propres à la méthode. »
- « Ne couper que les pointes qui dépassent réellement, avec parcimonie. »
- « Conseiller d’éviter les frottements et produits irritants immédiatement après la prestation ; respecter les consignes spécifiques si une teinture ou un Brow Lift est associé. »
- Matériel d'hygiène à garder visible : « goupillons jetables, pince désinfectée ».

### G4. §2 Brow Lift — Thuya (Précaution collée au tableau des temps)
- Titre du tableau, à conserver tel quel : « Temps de pose — protocole demandé pour la formation ».
- Tableau des temps : 8 / 8 minutes ; 10 / 10 minutes ; « 11 à 12 minutes maximum » / « 11 à 12 minutes maximum ».
- ⚠ « Précaution : ces temps sont ceux demandés pour ce support de formation ; ils ne sont pas présentés comme des durées officiellement validées par Thuya. Vérifier la notice des références exactes, notamment pour la deuxième lotion, avant toute application sur une cliente. Ne jamais dépasser les limites du fabricant. »
- « Étape finale : appliquer la crème de soin Thuya après le retrait du neutralisant, en respectant le mode d’emploi de cette crème. »
- Fiche technique, ⚠ « Les temps présentés au §2 sont des valeurs pédagogiques à confirmer sur les notices de chaque référence : ils ne doivent pas être appliqués automatiquement. »

### G5. §3 Teinture des sourcils — Brow Daddy
- ⚠ « Après un Brow Lift, vérifier la compatibilité et les durées spécifiques avant d’associer les deux prestations. »
- ⚠ « Le protocole de teinture et son temps de pose restent à confirmer à partir de la référence exacte du produit. » (À ne pas réduire en note de bas de page : c'est la seule « consigne » de temps de cette section.)
- « Protéger la peau et contrôler la coloration. »
- Vigilance : « Sensibilisation possible : respecter le test préalable et la notice exacte. »

### G6. §4 Décoloration — ZOLA
- « Effectuer le diagnostic, vérifier les contre-indications et le test de sensibilité. »
- « Protéger la peau autour des sourcils et porter des gants. »
- « Mélanger dans un récipient non métallique : 1 dose de poudre pour 2 doses d’oxydant ZOLA compatible, conformément à la notice du produit. » (ratio en pastille, sans jamais le séparer de « conformément à la notice du produit »)
- ⚠ « Appliquer uniquement sur les poils des sourcils, sans contact avec les yeux. »
- « Surveiller visuellement et retirer dès que le résultat souhaité est atteint. »
- « Les revendeurs indiquent 3 à 20 minutes selon le résultat visé » : garder « Les revendeurs indiquent ». Ne pas afficher « 3–20 min » seul, comme si c'était un temps validé.
- « Adapter au poil et à l’objectif, pas uniquement à la couleur de peau. » + « Sur peau foncée comme sur peau claire, contrôler régulièrement l’éclaircissement, la tolérance cutanée et le contraste recherché. »
- ⚠ « Ne pas remplacer par un oxydant plus concentré. »
- ⚠ « Respecter le ratio de mélange et les limites de pose de la notice. »
- « Après prestation : éviter les frottements et surveiller toute irritation. »
- Vigilance : « Éviter le surtraitement, utiliser uniquement l’oxydant compatible indiqué par le fabricant. »

### G7. Atelier visuel
- ⚠ « Les images ne constituent pas un protocole de pose. »
- « Faire valider la forme et le résultat attendu avant la prestation. »

### G8. Hygiène, sécurité et qualité (checklist complète, sans en retirer une ligne)
- « Plan de travail propre ; mains lavées ; instruments nettoyés puis désinfectés selon leur usage. »
- « Produits identifiés, non périmés, fermés et conservés conformément aux notices. »
- « Consommables à usage unique disponibles ; déchets éliminés dans les filières adaptées. »
- ⚠ « Aucune prestation sur une zone présentant une infection, une lésion ou une irritation active. »
- ⚠ « En cas de projection oculaire : rinçage immédiat abondant et avis médical urgent. »
- Tableau « Points de vigilance par technique » complet (4 lignes : teinture hybride, décoloration, rehaussement de cils, Lash Botox).

### G9. Fiche technique Brow Lift
- « Accueillir la cliente, vérifier les antécédents de réaction et les éventuelles irritations ou lésions. »
- « …photographier avec consentement. »
- « Préparer le matériel désinfecté, un minuteur, les consommables à usage unique et les notices des références exactes. »
- « Vérifier la forme, la tolérance cutanée et le confort de la cliente. »
- « Remettre les recommandations du fabricant et noter les produits, lots, temps effectivement appliqués et réactions. »
- « Programmer un suivi adapté sans promettre une durée identique pour toutes les clientes. »

### G10. Partie II — Cils (le point le plus sensible du manuel)
- §5 : « Vérifier l’absence d’irritation ou d’infection oculaire, effectuer les contrôles prévus par les notices et choisir les pads adaptés. »
- §6 : « …protéger les cils inférieurs… »
- Tableau « Ordre des étapes enseigné » : Step 1 = 10 minutes ; Step 1.5 = « Selon notice du soin » ; Step 2 = 10 minutes.
- ⚠ **Collé au tableau, en taille de texte au moins égale à celle du tableau** (dans l'original, ce texte était gris et plus petit : défaut à corriger) : « Important : ces temps de 10 minutes correspondent au protocole demandé pour la formation et doivent être confirmés sur les notices Noemi Innovate du lot utilisé. Vérifier expressément auprès du fabricant que le soin Intense peut être appliqué entre Step 1 et Step 2 : certains systèmes imposent de neutraliser avant tout soin. Ne pas appliquer cette séquence sans validation. »
- §7 : « Préparer, appliquer et retirer selon la notice exacte. Respecter les précautions oculaires et les éventuels ajustements de temps après rehaussement. »
- ⚠ §8 : « Le Lash Botox est un soin cosmétique et non une injection. » + « Le temps de pose et sa place exacte dans la procédure restent à valider avec la notice du fabricant. »
- Vigilance : « Protéger l’œil, contrôler le placement des cils et respecter les temps du système. » ; « Soin cosmétique : emplacement dans la séquence à vérifier auprès du fabricant. »

### G11. Éthique, consentement et données (Partie III)
- « …demander une autorisation explicite avant toute publication. »
- « Conserver les originaux et ne jamais présenter comme sien le travail d’une autre professionnelle. »
- « …éviter les filtres qui changent la couleur de la peau ou du poil. »
- « …montrer le détail de la prestation sans masquer les précautions… » (Reel)
- « Avis authentiques publiés avec accord » ; « Collaborer avec des professionnels complémentaires, sans échanges d’avis trompeurs. »
- « Conserver un suivi des prestations et des éventuelles réactions, avec des données limitées au nécessaire. »

---

## H. Questions à poser à la formatrice (récapitulatif)
1. Existe-t-il une page « Diagnostic et application en cabine » ? Sinon, accepte-t-elle que l'entrée du sommaire renvoie au §1 ?
2. Un contenu « Anatomie » est-il prévu ?
3. Teinture Brow Daddy : protocole, ratio (la source « ratio distributeur » est citée) et temps de pose ? StainMe fait-il partie de la « teinture hybride » ?
4. Quel était le point « 4. » de la page Gestion ? Existe-t-il ?
5. Décoloration : la phrase « Les revendeurs indiquent 3 à 20 minutes selon le résultat visé ; » est-elle complète ?
6. Teinture des cils Noemi : quelle référence (Hybrid Dye ?)
7. Source Noemi Freelift : à garder (URL complète ?) ou à retirer ?
8. Sources Thuya, ZOLA, Noemi Intense et StainMe à ajouter ?
9. Nom exact du fournisseur : « Only Lash Paris (Brow & Lash) » ou « Brows & Lashes » ?
10. Autorisation écrite de @refreshednrefined pour les 3 photos de l'atelier ; sinon, photos de remplacement ?
11. Origine et droits de la photo du portrait, de la photo du sac et des jambes, des photos produits ZOLA et de la photo de mapping.
12. Validation du corrigé du QCM (section D) et décision sur Q4, Q5 et Q10 ; mélanger l'ordre des réponses ?
13. Symétrie des titres de parties : « Les sourcils / Les cils » ou « Sourcils / Cils » ?
14. Numéroter « 9. Conseils après prestation » ?
15. « Confirmer les rendez-vous, expliquer les retards… » : quelle formulation souhaitée ?
