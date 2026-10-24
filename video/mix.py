"""Mixage final : musique + effets + voix off (si disponible), avec atténuation de la musique sous la voix.

Sorties : audio/mix.wav et out/sous-titres.srt
"""
import json
import pathlib
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
        a = a_up if target < v else a_dn
        v = target + (v - target) * a ** step
        out[i:i + step] = v
    return out


def srt_time(s):
    h, r = divmod(s, 3600); m, r = divmod(r, 60)
    return f'{int(h):02d}:{int(m):02d}:{int(r):02d},{int(round((r % 1) * 1000)):03d}'


def chunks(text, maxlen=72):
    """Découpe aux fins de phrase, puis aux virgules, pour des sous-titres lisibles."""
    import re
    out = []
    for phrase in re.split(r'(?<=[.!?])\s+', text.strip()):
        while len(phrase) > maxlen:
            cuts = [m.end() for m in re.finditer(r'[,:;]\s', phrase) if 12 < m.end() < len(phrase) - 8]
            if not cuts:
                cuts = [m.start() for m in re.finditer(r'\s', phrase)]
            cut = min(cuts, key=lambda c: abs(c - len(phrase) / 2))
            out.append(phrase[:cut].strip()); phrase = phrase[cut:].strip()
        out.append(phrase)
    return [c for c in out if c]


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
    for s in tl['scenes']:
        f = ROOT / 'audio' / 'vo' / f"{s['id']}.mp3"
        if not f.exists():
            continue
        v = decode(f)
        s0 = int(s['vo_start'] * SR)
        n = min(len(v), N - s0)
        voice[s0:s0 + n] += v[:n]
        has_voice = True

    if has_voice:
        # voix à environ -16 dB RMS sur les passages parlés
        speech = np.abs(voice) > .01
        rms = np.sqrt(np.mean(voice[speech] ** 2)) if speech.any() else 1
        voice *= 10 ** (-16 / 20) / max(rms, 1e-6)
        presence = smooth((np.abs(voice) > .004).astype(float), attack=.08, release=.7)
        presence = np.convolve(presence, np.ones(4410) / 4410, mode='same')
        music_gain = .62 - .44 * np.clip(presence, 0, 1)      # musique nettement plus basse sous la voix
    else:
        music_gain = np.full(N, .62)

    mix = music * music_gain + sfx * .55 + voice[None, :]
    peak = np.max(np.abs(mix))
    if peak > .97:
        mix *= .97 / peak
    pcm = (np.clip(mix, -1, 1) * 32767).astype('<i2')
    with wave.open(str(ROOT / 'audio' / 'mix.wav'), 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(pcm.T.copy().tobytes())

    # Sous-titres (répartition proportionnelle au nombre de caractères)
    cues, k = [], 1
    for s in tl['scenes']:
        parts = chunks(s['vo'])
        total_chars = sum(len(p) for p in parts)
        t = s['vo_start']
        for p in parts:
            d = s['vo_dur'] * len(p) / total_chars
            cues.append(f'{k}\n{srt_time(t)} --> {srt_time(t + d - .05)}\n{p}\n')
            t += d; k += 1
    (ROOT / 'out').mkdir(exist_ok=True)
    (ROOT / 'out' / 'sous-titres.srt').write_text('\n'.join(cues), encoding='utf-8')
    print(f"mix {'avec' if has_voice else 'sans'} voix -> audio/mix.wav ; {k - 1} sous-titres")


if __name__ == '__main__':
    main()
