"""Voix off féminine générée en local (Kokoro, voix française « ff_siwis »), en attendant la voix ElevenLabs.

Usage : python3 voix_locale.py <dossier contenant kokoro-v1.0.onnx et voices-v1.0.bin>
Modèle : https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0
Sortie : audio/vo/<id>.mp3, une piste par scène (lue ensuite par timings.py et mix.py),
         et audio/vo/<id>.json, l'instant de début et de fin de chaque phrase.
"""
import json
import pathlib
import re
import subprocess
import sys

import numpy as np
from kokoro_onnx import Kokoro

ROOT = pathlib.Path(__file__).resolve().parent
SPEED = 1.08
PAUSE = 0.34    # silence entre deux phrases (s)

# Prononciation imposée (en phonèmes) pour les noms de marque et les mots qu'espeak lit à l'anglaise.
# Seule l'entrée de la synthèse change : le texte affiché et les sous-titres gardent l'orthographe d'origine.
PRONONCIATION = {
    'Dolce Lash and Brow': 'dɔltʃˈe lˈaʃ ɛnd bʁˈaw',
    'Brow': 'bʁaw',
    'Thuya': 'tyjˈa',
    'Daddy': 'dˈadi',
    'Lash': 'lˈaʃ',
    'Noemi': 'nɔemˈi',
    'Reels': 'ʁˈilz',
    'mapping': 'mapˈiŋ',
    'rehaussement': 'ʁəˌosəmˈɑ̃',
    'rythme': 'ʁˈitm',
}
TERMES = re.compile('|'.join(re.escape(t) for t in sorted(PRONONCIATION, key=len, reverse=True)))


def phonemes(k, text):
    out, pos = [], 0
    for m in TERMES.finditer(text):
        if text[pos:m.start()].strip():
            out.append(k.tokenizer.phonemize(text[pos:m.start()], 'fr-fr'))
        out.append(PRONONCIATION[m.group()])
        pos = m.end()
    if text[pos:].strip():
        out.append(k.tokenizer.phonemize(text[pos:], 'fr-fr'))
    ph = re.sub(r'\([a-z-]+\)', '', ' '.join(out))       # retire les bascules de langue d'espeak, ex. « (en) »
    ph = re.sub(r'\blˈə\b', 'lə', ph)                    # article isolé en fin de segment : pas d'accent
    return re.sub(r'\s+([.,:;!?])', r'\1', ph)


def trim(x, sr, thr=.008):
    idx = np.where(np.abs(x) > thr)[0]
    if not len(idx):
        return x
    a = max(0, idx[0] - int(.03 * sr))
    b = min(len(x), idx[-1] + int(.12 * sr))
    return x[a:b]


def main():
    model_dir = pathlib.Path(sys.argv[1])
    k = Kokoro(str(model_dir / 'kokoro-v1.0.onnx'), str(model_dir / 'voices-v1.0.bin'))
    script = json.loads((ROOT / 'script.json').read_text(encoding='utf-8'))
    out = ROOT / 'audio' / 'vo'
    out.mkdir(parents=True, exist_ok=True)
    for s in script['scenes']:
        # Synthèse phrase par phrase : on connaît ainsi l'instant exact où commence chaque phrase,
        # ce qui permet de caler les animations sur la voix (repères écrits dans audio/vo/<id>.json).
        parts, anchors, t = [], [], 0.0
        for m in re.finditer(r'[^.!?]+[.!?]*', s['vo']):
            if not m.group().strip():
                continue
            i0 = m.start() + len(m.group()) - len(m.group().lstrip())
            audio, sr = k.create(phonemes(k, m.group().strip()), voice='ff_siwis', speed=SPEED, is_phonemes=True)
            audio = trim(np.asarray(audio, dtype=np.float32), sr)
            if parts:
                parts.append(np.zeros(int(PAUSE * sr), dtype=np.float32)); t += PAUSE
            anchors.append({'i0': i0, 'i1': m.end(), 't0': round(t, 3), 't1': round(t + len(audio) / sr, 3)})
            parts.append(audio); t += len(audio) / sr
        audio = np.concatenate(parts)
        speech = audio[np.abs(audio) > .02]
        audio = audio * (10 ** (-20 / 20) / (np.sqrt(np.mean(speech ** 2)) + 1e-9))   # même niveau parlé (-20 dBFS RMS) pour toutes les scènes
        audio = audio * min(1.0, .95 / (np.max(np.abs(audio)) + 1e-9))
        pcm = (np.clip(audio, -1, 1) * 32767).astype('<i2')
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 's16le', '-ar', str(sr), '-ac', '1', '-i', '-',
                        '-c:a', 'libmp3lame', '-q:a', '2', str(out / f"{s['id']}.mp3")], input=pcm.tobytes(), check=True)
        (out / f"{s['id']}.json").write_text(json.dumps({'phrases': anchors}, ensure_ascii=False), encoding='utf-8')
        print(f"{s['id']:<13} {len(audio) / sr:5.2f} s  {len(anchors)} phrase(s)")

if __name__ == '__main__':
    main()
