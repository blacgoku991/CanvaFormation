# Vidéo motion design — Dolce Lash & Brow

Vidéo de présentation de la formation : 1920×1080, 30 i/s, environ 2 min 30.

## Chaîne de fabrication

1. `script.json` : le texte de la voix off, scène par scène.
2. `voix_locale.py <dossier modèle Kokoro>` : génère la voix dans `audio/vo/<id>.mp3`.
   - Ces fichiers peuvent être remplacés par la voix ElevenLabs « Perle » (voir `script.json`) : il suffit de garder les mêmes noms.
3. `timings.py` : calcule le minutage des scènes (`timeline.json`, `timeline.js`) d'après la durée réelle de chaque voix.
4. `music.py` : produit la musique d'ambiance et les effets de transition (`audio/musique.wav`, `audio/sfx.wav`). Tout est synthétisé en local.
5. `node render.js video out/video-muette.mp4` : rendu image par image de `index.html` (animations pilotées par `engine.js`).
   - Pour contrôler quelques instants précis : `node render.js stills 12 40.5`.
6. `mix.py` : assemble voix, musique (baissée sous la voix) et effets dans `audio/mix.wav`. Il écrit aussi les sous-titres, `out/sous-titres.srt`.
7. Assemblage final avec ffmpeg (voir `final.sh`).

Après chaque changement de voix, relancer les étapes 3 à 7.
