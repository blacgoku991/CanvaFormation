"""Mixage final : musique + effets + voix off (si disponible), avec atténuation de la musique sous la voix.

Sorties : audio/mix.wav et out/sous-titres.srt
"""
import json
import pathlib
import re
import subprocess
import wave

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parent
SR = 44100


def read_wav(path):
    with wave.open(str(path)) as w:
        x = np.frombuffer(w.readframes(w.getnframes()), dtype='<i2').reshape(-1, w.getnchannels()).astype(float) / 32768
    return x.T


def decode(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(path), '-ar', str(SR), '-ac', '1', '-f', 's16le', '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype='<i2').astype(float) / 32768


def smooth(env, attack=.12, release=.55):
    out = np.empty_like(env)
    a_up, a_dn = np.exp(-1 / (attack * SR)), np.exp(-1 / (release * SR))
    # lissage asymétrique, calculé par blocs pour rester rapide
    step = 64
    v = env[0]
    for i in range(0, len(env), step):
        target = env[i:i + step].max()
        a = a_dn if target < v else a_up      # montée rapide (attaque), redescente lente (relâchement)
        v = target + (v - target) * a ** step
        out[i:i + step] = v
    return out


def srt_time(s):
    ms = int(round(s * 1000))
    return f'{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}'


# Virgules d'énumération retirées dans les sous-titres (« A, B, et C » -> « A, B et C ») ; la voix, elle, garde sa pause.
ENUM_ET = re.compile(r'(professionnelle|désinfecté|efficaces|soignée), et ')
MOTS_OUTILS = {'le', 'la', 'les', 'un', 'une', 'des', 'du', 'de', 'd’', 'se', 'à', 'au', 'aux', 'et', 'ou', 'en',
               'pour', 'sur', 'sous', 'dans', 'avec', 'sans', 'par', 'que', 'son', 'sa', 'ses', 'votre', 'vos', 'deux', 'trois'}


def typo(text):
    """Typographie des sous-titres : nom de marque, apostrophes courbes, espace insécable avant : ; ? !"""
    text = text.replace('Lash and Brow', 'Lash & Brow').replace("'", '’')
    return re.sub(r' ([:;?!])', '\u00a0\\1', text)


def coupable(p, i):
    """Peut-on couper (ou passer à la ligne) à l'espace p[i] ? Jamais après un mot outil ni avant : ; ? !"""
    return p[:i].rsplit(' ', 1)[-1].lower() not in MOTS_OUTILS and not re.match(r' ?[:;?!]', p[i + 1:i + 3])


def split(p, maxlen=64):
    """Découpe récursive d'une phrase : d'abord aux signes de ponctuation, sinon à un espace bien placé."""
    p = p.strip()
    if len(p) <= maxlen:
        return [p]
    cuts = [m.end() for m in re.finditer(r'[,:;]\s', p) if 14 <= m.end() <= len(p) - 14]
    if not cuts:
        cuts = [m.start() for m in re.finditer(' ', p) if 14 <= m.start() <= len(p) - 14 and coupable(p, m.start())]
    if not cuts:
        return [p]
    cut = min(cuts, key=lambda c: abs(c - len(p) / 2))
    return split(p[:cut], maxlen) + split(p[cut:], maxlen)


def two_lines(c, width=42):
    """Au-delà de 42 caractères, passe à la ligne à l'espace le plus central possible."""
    if len(c) <= width:
        return c
    spaces = [m.start() for m in re.finditer(' ', c) if coupable(c, m.start())]
    if not spaces:
        return c
    i = min(spaces, key=lambda i: max(i, len(c) - i - 1))
    return c[:i] + '\n' + c[i + 1:]


def silences(v, hop=441):
    """Centres (en s) des pauses de la voix d'une scène, pour caler les coupures de sous-titres."""
    n = len(v) // hop
    if n < 3:
        return []
    db = 20 * np.log10(np.sqrt(np.mean(v[:n * hop].reshape(n, hop) ** 2, axis=1)) + 1e-9)
    quiet = db < np.median(db[db > db.max() - 40]) - 25
    out, i = [], 0
    while i < n:
        if quiet[i]:
            j = i
            while j < n and quiet[j]:
                j += 1
            if j - i >= 6:
                out.append((i + j) / 2 * hop / SR)
            i = j
        else:
            i += 1
    return out


def main():
    tl = json.loads((ROOT / 'timeline.json').read_text(encoding='utf-8'))
    music = read_wav(ROOT / 'audio' / 'musique.wav')
    sfx = read_wav(ROOT / 'audio' / 'sfx.wav')
    N = int((tl['total'] + .1) * SR)
    music, sfx = music[:, :N], sfx[:, :N]
    if music.shape[1] < N:
        music = np.pad(music, ((0, 0), (0, N - music.shape[1])))
        sfx = np.pad(sfx, ((0, 0), (0, N - sfx.shape[1])))

    voice = np.zeros(N)
    has_voice = False
    pauses = {}
    for s in tl['scenes']:
        f = ROOT / 'audio' / 'vo' / f"{s['id']}.mp3"
        if not f.exists():
            continue
        v = decode(f)
        s0 = int(s['vo_start'] * SR)
        n = min(len(v), N - s0)
        voice[s0:s0 + n] += v[:n]
        pauses[s['id']] = [s['vo_start'] + c for c in silences(v)]
        has_voice = True

    if has_voice:
        # voix à environ -16 dB RMS sur les passages parlés
        speech = np.abs(voice) > .01
        rms = np.sqrt(np.mean(voice[speech] ** 2)) if speech.any() else 1
        voice *= 10 ** (-16 / 20) / max(rms, 1e-6)
        speaking = (np.abs(voice) > .004).astype(float)
        hold = int(.6 * SR)                                      # la musique reste basse pendant les courtes pauses entre phrases
        c = np.concatenate([[0], np.cumsum(speaking)])
        i = np.arange(len(speaking))
        speaking = ((c[i + 1] - c[np.maximum(i + 1 - hold, 0)]) > 0).astype(float)
        ahead = int(.15 * SR)                                    # la musique commence à baisser juste avant la voix
        speaking = np.concatenate([speaking[ahead:], np.zeros(ahead)])
        presence = smooth(speaking, attack=.08, release=.7)
        presence = np.convolve(presence, np.ones(2205) / 2205, mode='same')
        music_gain = .60 - .47 * np.clip(presence, 0, 1)      # musique nettement plus basse sous la voix
    else:
        music_gain = np.full(N, .62)

    mix = music * music_gain + sfx * .5 + voice[None, :]
    tail = int(1.0 * SR)
    mix[:, -tail:] *= np.linspace(1, 0, tail) ** 2          # tout s'éteint avec le fondu au noir final
    peak = np.max(np.abs(mix))
    if peak > .97:
        mix *= .97 / peak
    pcm = (np.clip(mix, -1, 1) * 32767).astype('<i2')
    with wave.open(str(ROOT / 'audio' / 'mix.wav'), 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(pcm.T.copy().tobytes())

    # Sous-titres : chaque phrase est placée sur ses repères réels (audio/vo/<id>.json), découpée au besoin,
    # et chaque coupure interne est recalée sur la pause de voix la plus proche.
    cues = []
    for s in tl['scenes']:
        phrases = s.get('phrases') or [{'i0': 0, 'i1': len(s['vo']), 't0': 0, 't1': s['vo_dur']}]
        for ph in phrases:
            text = ENUM_ET.sub(r'\1 et ', s['vo'][ph['i0']:ph['i1']].strip())
            parts = split(text)
            t0, t1 = s['vo_start'] + ph['t0'], s['vo_start'] + ph['t1']
            total_chars = sum(len(c) for c in parts)
            bounds, acc = [t0], t0
            for c in parts[:-1]:
                acc += (t1 - t0) * len(c) / total_chars
                near = [x for x in pauses.get(s['id'], []) if abs(x - acc) <= .45 and bounds[-1] + .6 < x < t1 - .6]
                bounds.append(min(near, key=lambda x: abs(x - acc)) if near else acc)
            bounds.append(t1)
            for c, a_, b_ in zip(parts, bounds, bounds[1:]):
                cues.append((a_, b_ - .04, two_lines(typo(c))))
    cues = [f'{k}\n{srt_time(a_)} --> {srt_time(b_)}\n{c}\n' for k, (a_, b_, c) in enumerate(cues, 1)]
    k = len(cues) + 1
    (ROOT / 'out').mkdir(exist_ok=True)
    (ROOT / 'out' / 'sous-titres.srt').write_text('\n'.join(cues), encoding='utf-8')
    print(f"mix {'avec' if has_voice else 'sans'} voix -> audio/mix.wav ; {k - 1} sous-titres")


if __name__ == '__main__':
    main()
