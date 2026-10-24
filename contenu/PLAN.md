# Plan du manuel — A4 paysage

Chaque ligne correspond à un fichier `design/pages/NNN-nom.html` (une ou plusieurs `section.page`) avec son ou ses `data-id`.
Les sources sont dans `contenu/transcription/`.

| Fichier | data-id | Contenu | Source | Lot |
|---|---|---|---|---|
| 010-couverture | couverture | Couverture | — | FAIT |
| 020-sommaire | sommaire | Sommaire (numéros automatiques) | sommaire.md | FAIT |
| 030-partie1-ouverture | partie-1 | Ouverture Partie I — Sourcils | — | FAIT |
| 040-cycle | cycle | Le cycle de vie du sourcil (schéma `assets/schema-cycle.svg.html` + texte) | cycle-de-vie-sourcil.md | 1 |
| 050-chute | chute | Pourquoi les sourcils tombent-ils ? | pourquoi-sourcils-tombent.md | FAIT (texte à vérifier) |
| 060-diagnostic | diagnostic | §1, page A : titre « 1. Restructuration des sourcils & mapping ». La synthèse « Diagnostic et restructuration » de brow-lift-thuya-teinture.md sert d'ouverture, puis Objectif, Matériel nécessaire, Étape 1 — Diagnostic et préparation | restructuration-mapping.md + brow-lift-thuya-teinture.md (§1) | 1 |
| 070-mapping | mapping | §1, page B : Étape 2 — Mapping (tableau A/B/C + schéma `assets/schema-mapping.svg.html`), Étapes 3, 4, 5 | restructuration-mapping.md | 1 |
| 080-browlift | browlift | §2 Brow Lift — Thuya : protocole, tableau des temps de pose (pastilles), Étape finale, Précaution (dans un `.alert`) | brow-lift-thuya-teinture.md | 2 |
| 090-teinture | teinture | §3 Teinture des sourcils — Brow Daddy, avec en rappel la vigilance « Teinture hybride » du tableau des points de vigilance. Il peut partager la page du §4 si le résultat reste aéré ; sinon il a sa propre page | brow-lift-thuya-teinture.md + fiche-technique-brow-lift-hygiene.md | 2 |
| 100-decoloration | decoloration | §4 Décoloration des sourcils — ZOLA (photos produits) | decoloration-sourcils.md | 2 |
| 110-atelier | atelier | Atelier visuel — Brow Lift (3 photos `atelier-brow-1..3.jpg` + « Crédit photo : @refreshednrefined ») | atelier-visuel-brow-lift.md | 3 |
| 120-hygiene | hygiene | Hygiène, sécurité et qualité : checklist du poste de travail et points de vigilance par technique | fiche-technique-brow-lift-hygiene.md | 3 |
| 200-partie2-ouverture | partie-2 | Ouverture Partie II — Les cils | — | FAIT |
| 210-cils-rehaussement | rehaussement | §5 Diagnostic avant rehaussement et §6 Rehaussement Noemi Innovate | partie-2-cils-contenu.md | FAIT (texte à vérifier) |
| 220-teinture-cils | teinture-cils | §7 Teinture des cils — Noemi, §8 Lash Botox — Noemi Intense, Step 1.5, Conseils après prestation | partie-2-cils-contenu.md | 4 |
| 300-partie3-ouverture | partie-3 | Ouverture Partie III — Pratique professionnelle | — | FAIT |
| 310-fiche-technique | fiche-technique | Fiche technique — Brow Lift : avant, pendant, après la séance | fiche-technique-brow-lift-hygiene.md | 3 |
| 320-photographier | photographier | Photographier son travail | photographier-reseaux-sociaux.md | 5 |
| 330-reseaux | reseaux | Développer son activité sur les réseaux sociaux : 1. identité, 2. Instagram, 3. les cinq piliers | photographier-reseaux-sociaux.md | 5 |
| 340-reseaux-2 | reseaux-2 | Suite des réseaux sociaux : 4. Réaliser un Reel efficace, 5. Exemple de calendrier hebdomadaire, 6. Attirer une clientèle locale | gestion-activite-fidelisation.md | 5 |
| 350-gestion | gestion | Gestion d’activité et fidélisation : Accueil, prix et organisation, Expérience cliente, Mesurer ses résultats | gestion-activite-fidelisation.md | 4 |
| 400-partie4-ouverture | partie-4 | Ouverture Partie IV — Évaluation | — | FAIT |
| 410-qcm | qcm, qcm-2 | Évaluation QCM, 2 pages : questions 1 à 8, puis 9 à 15 + score et observations. **Aucune réponse indiquée** | qcm-page-1.md, qcm-page-2.md | 6 |
| 430-sources | sources | Sources et vérification des protocoles + fournisseur Only Lash Paris (liens cliquables) | sources-verification.md | 4 |
| 990-dos | dos | 4e de couverture | — | FAIT |
| corrige/010-corrige | corrige | **Document séparé** : corrigé du QCM réservé à la formatrice | qcm-page-*.md + AUDIT.md | 6 |

Pour 320, 330 et 340, le lot 5 peut répartir les rubriques autrement (2 ou 3 pages) pour équilibrer les pages, à condition de garder les data-id `photographier`, `reseaux` et `reseaux-2` (ce dernier peut être supprimé s'il n'y a que 2 pages).

## Arbitrages éditoriaux (appliqués partout, en plus des corrections de AUDIT.md)

1. **Produit ZOLA** : écrire « ZOLA BB Blond Powder » partout, comme sur l'emballage. Remplacer « Baby Blonde Powder ».
2. **Accents de la page décoloration** : « OXYDANT UTILISÉ : ZOLA 3 % », « associé à », « concentré », « mélange ».
3. **Cycle de vie** : la page s'intitule « Le cycle de vie du sourcil ». Le schéma vectoriel remplace l'image titrée « cycle de vie des cils ». Libellés des 4 phases repris du visuel d'origine : Anagène — Phase de croissance ; Catagène — Phase de transition ; Télogène — Phase de repos ; Anagène — Le cycle recommence, nouvelle pousse de poils.
4. **Numérotation des rubriques business** :
   - Réseaux sociaux de 1 à 6 : 1. Construire une identité professionnelle ; 2. Optimiser son profil Instagram ; 3. Les cinq piliers de contenu ; 4. Réaliser un Reel efficace ; 5. Exemple de calendrier hebdomadaire ; 6. Attirer une clientèle locale.
   - « Mesurer ses résultats » passe dans Gestion d’activité, sans numéro (l'ancien « 5. »).
5. **Précaution Brow Lift** : « ceux demandés pour ton support de formation » devient « ceux demandés pour ce support de formation » (le texte s'adresse aux apprenantes).
6. **Fiche technique** :
   - « Pour la gamme Thuya citée dans le manuel initial » devient « Pour la gamme Thuya présentée au §2 (Brow Lift — Thuya) ».
   - « Les temps présentés dans la version initiale » devient « Les temps présentés au §2 ».
7. **Sommaire** : « Gestion d·activité » devient « Gestion d’activité ».
8. **Séparateurs** : « Partie I — Sourcils » (tiret cadratin). Nom de marque : « Dolce Lash & Brow ».
9. **Section 1** : le titre « 1. Diagnostic et restructuration » de la page Brow Lift et le titre « 1. RESTRUCTURATION DES SOURCILS & MAPPING » forment un seul §1. Titre retenu : « 1. Restructuration des sourcils & mapping ». La synthèse « Diagnostic et restructuration » est reprise mot pour mot en tête de section, sous ce même intitulé.
10. **Filigrane** @refreshednrefined : il reste visible. Ajouter « Crédit photo : @refreshednrefined ». Ne pas légender les 3 photos naturel / discipliné / structuré : les numéroter 1, 2, 3.
