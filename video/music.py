"""Musique d'ambiance et effets de transition, synthétisés en local (aucun échantillon externe).

Sorties : audio/musique.wav (nappe, piano feutré, basse, rythmique légère)
          audio/sfx.wav     (souffles de transition, impacts doux aux ouvertures de partie)
Le minutage suit video/timeline.json.
"""
import json
import pathlib
import wave

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parent
SR = 44100
rng = np.random.default_rng(11)


def midi(n):
    return 440.0 * 2 ** ((n - 69) / 12)


def write_wav(path, stereo):
    data = np.clip(stereo, -1, 1)
    pcm = (data * 32767).astype('<i2')
    with wave.open(str(path), 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(pcm.T.copy().tobytes())


def lowpass(x, cutoff):
    """Filtre passe-bas du 1er ordre appliqué deux fois (pente douce)."""
    a = np.exp(-2 * np.pi * cutoff / SR)
    for _ in range(2):
        y = np.empty_like(x)
        acc = 0.0
        b = 1 - a
        # boucle vectorisée par blocs via lfilter maison
        y = _iir(x, a, b)
        x = y
    return x


def _iir(x, a, b):
    # y[n] = b*x[n] + a*y[n-1] — implémentation par somme cumulée pondérée (stable pour a<1)
    n = len(x)
    out = np.empty(n)
    block = 4096
    prev = 0.0
    powers = a ** np.arange(1, block + 1)
    for s in range(0, n, block):
        seg = x[s:s + block] * b
        m = len(seg)
        p = powers[:m]
        # convolution avec noyau exponentiel tronqué au bloc + report de l'état précédent
        k = a ** np.arange(m)
        conv = np.convolve(seg, k)[:m]
        out[s:s + m] = conv + prev * p
        prev = out[s + m - 1]
    return out


def highpass(x, cutoff):
    return x - lowpass(x, cutoff)


def reverb(stereo, seconds=2.4, decay=.75, wet=.32):
    n = int(seconds * SR)
    t = np.arange(n) / SR
    out = []
    for ch in range(2):
        ir = rng.standard_normal(n) * np.exp(-t / decay * 3)
        ir = lowpass(ir, 5200)
        ir[:int(.012 * SR)] *= np.linspace(0, 1, int(.012 * SR))
        ir /= np.sqrt(np.sum(ir ** 2))
        L = len(stereo[ch]) + n
        nfft = 1 << (L - 1).bit_length()
        y = np.fft.irfft(np.fft.rfft(stereo[ch], nfft) * np.fft.rfft(ir, nfft), nfft)[:len(stereo[ch])]
        out.append(stereo[ch] * (1 - wet) + y * wet * 1.6)
    return np.array(out)


def env_adsr(n, a, r, sustain_len):
    e = np.ones(n)
    na, nr = min(n, int(a * SR)), int(r * SR)
    e[:na] = np.linspace(0, 1, na) ** 1.6
    end = min(n, int(sustain_len * SR))
    if end + nr <= n:
        e[end:end + nr] = np.linspace(1, 0, nr) ** 1.4
        e[end + nr:] = 0
    return e


def main():
    tl = json.loads((ROOT / 'timeline.json').read_text(encoding='utf-8'))
    total = tl['total'] + 2.5
    N = int(total * SR)
    t = np.arange(N) / SR
    mus = np.zeros((2, N))

    bpm = 76
    beat = 60 / bpm
    bar = 4 * beat
    chords = [
        [50, 57, 61, 64, 66],   # Ré maj9
        [47, 54, 57, 61, 62],   # Si m9
        [43, 50, 54, 57, 59],   # Sol maj9
        [45, 52, 59, 61, 66],   # La 6/9 sus
    ]
    nbars = int(np.ceil(total / bar))
    groove_start = tl['scenes'][1]['start'] - .1          # la rythmique entre avec le sommaire
    outro = [s for s in tl['scenes'] if s['id'] == 'outro'][0]['start']

    # Nappe
    for b in range(nbars):
        ch = chords[b % 4]
        t0 = b * bar
        n = int((bar + 2.2) * SR)
        s0 = int(t0 * SR)
        if s0 >= N: break
        n = min(n, N - s0)
        tt = np.arange(n) / SR
        e = env_adsr(n, 1.3, 1.9, bar)
        for k, note in enumerate(ch):
            f = midi(note + 12)
            for side, det in ((0, -.0035), (1, .0035)):
                w = np.zeros(n)
                for h in range(1, 7):
                    w += np.sin(2 * np.pi * f * (1 + det) * h * tt + h * .7 + k) / h ** 1.7
                mus[side, s0:s0 + n] += w * e * .02
    mus[0] = lowpass(mus[0], 1800); mus[1] = lowpass(mus[1], 1800)

    # Piano feutré (arpèges)
    pattern = [(0, 0, .9), (1.5, 2, .55), (2, 3, .7), (3, 4, .5), (3.5, 2, .45)]
    piano = np.zeros((2, N))
    for b in range(nbars):
        ch = chords[b % 4]
        tones = [n + 24 for n in ch[1:]] + [ch[0] + 36]
        for pos, idx, vel in pattern:
            st = max(0.0, b * bar + pos * beat + rng.uniform(-.008, .008))
            if st >= total - 1.5: continue
            f = midi(tones[idx % len(tones)])
            n = int(2.6 * SR)
            s0 = int(st * SR)
            n = min(n, N - s0)
            if n <= 0: continue
            tt = np.arange(n) / SR
            env = np.exp(-tt / .62) * np.minimum(1, tt / .006)
            w = (np.sin(2 * np.pi * f * tt) + .32 * np.sin(2 * np.pi * 2 * f * tt) * np.exp(-tt / .25)
                 + .12 * np.sin(2 * np.pi * 3 * f * tt) * np.exp(-tt / .12))
            pan = .5 + .28 * np.sin(idx * 1.7 + b)
            v = vel * .06 * (1 + .1 * rng.standard_normal())
            piano[0, s0:s0 + n] += w * env * v * (1 - pan) * 2
            piano[1, s0:s0 + n] += w * env * v * pan * 2
    piano[0] = lowpass(piano[0], 5200); piano[1] = lowpass(piano[1], 5200)
    mus += piano

    # Basse
    bass = np.zeros(N)
    for b in range(nbars):
        st = b * bar
        if st < groove_start - .2 or st >= outro: continue
        f = midi(chords[b % 4][0] - 12)
        for pos, dur in ((0, 2.6 * beat), (2.5 * beat, 1.3 * beat)):
            s0 = int((st + pos) * SR)
            n = min(int(dur * SR), N - s0)
            tt = np.arange(n) / SR
            env = np.minimum(1, tt / .03) * np.exp(-tt / (dur * .8))
            bass[s0:s0 + n] += (np.sin(2 * np.pi * f * tt) + .25 * np.sin(4 * np.pi * f * tt)) * env * .085
    bass = lowpass(bass, 420)
    mus += bass

    # Rythmique légère (grosse caisse douce, charleston, shaker)
    perc = np.zeros((2, N))
    nbeats = int(total / beat)
    for i in range(nbeats):
        st = i * beat
        if st < groove_start or st >= outro - .2: continue
        s0 = int(st * SR)
        if i % 4 in (0, 2):
            n = int(.32 * SR); tt = np.arange(n) / SR
            f = 46 + 70 * np.exp(-tt / .03)
            k = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt / .10) * .10
            perc[:, s0:s0 + n] += k[:N - s0]
        for off, vol in ((.5, .06), (.25, .024), (.75, .024)):
            h0 = int((st + off * beat) * SR)
            n = int(.05 * SR)
            if h0 + n >= N: continue
            noise = highpass(rng.standard_normal(n), 7000) * np.exp(-np.arange(n) / SR / .012)
            perc[0, h0:h0 + n] += noise * vol * (1.2 if off == .25 else .8)
            perc[1, h0:h0 + n] += noise * vol * (.8 if off == .25 else 1.2)
    mus += perc

    # Mise en forme générale : fondu d'entrée, sortie, réverbe
    fade_in = np.minimum(1, t / 2.5)
    fade_out = np.clip((total - t) / 4.0, 0, 1)
    mus *= fade_in * fade_out
    mus = reverb(mus)
    mus /= np.max(np.abs(mus)) + 1e-9
    mus *= .80
    write_wav(ROOT / 'audio' / 'musique.wav', mus)

    # Effets : souffle à chaque transition, impact doux aux ouvertures de partie
    sfx = np.zeros((2, N))
    for s in tl['scenes'][1:]:
        st = s['start']
        opener = s['id'] in ('p1', 'p2', 'p3', 'evaluation')
        dur = 1.1 if opener else .75
        s0 = int((st - dur * .55) * SR)
        n = int(dur * SR)
        if s0 < 0 or s0 + n >= N: continue
        tt = np.arange(n) / SR
        noise = rng.standard_normal(n)
        sweep = np.zeros(n)
        # bruit filtré dont la brillance monte puis redescend (effet « whoosh »)
        for cut in (900, 2200, 4800):
            band = lowpass(noise, cut) - lowpass(noise, cut * .45)
            w = np.exp(-((tt / dur - .55) ** 2) / (2 * (.16 if cut > 2000 else .22) ** 2))
            sweep += band * w
        env = np.sin(np.pi * tt / dur) ** 1.5
        sweep *= env * (.9 if opener else .55)
        pan = np.linspace(.25, .75, n) if s['id'] in ('cycle', 'couleur', 'rehaussement', 'fiche') else np.linspace(.75, .25, n)
        sfx[0, s0:s0 + n] += sweep * (1 - pan) * 2
        sfx[1, s0:s0 + n] += sweep * pan * 2
        if opener:
            b0 = int(st * SR); n2 = int(1.8 * SR); tt2 = np.arange(n2) / SR
            boom = np.sin(2 * np.pi * np.cumsum(38 + 60 * np.exp(-tt2 / .05)) / SR) * np.exp(-tt2 / .45)
            shimmer = sum(np.sin(2 * np.pi * midi(n_) * tt2) for n_ in (74, 81, 86)) * np.exp(-tt2 / .7) * .18
            sfx[:, b0:b0 + n2] += (boom * .9 + shimmer)[:N - b0]
    sfx = reverb(sfx, seconds=1.6, decay=.5, wet=.25)
    sfx /= np.max(np.abs(sfx)) + 1e-9
    sfx *= .55
    write_wav(ROOT / 'audio' / 'sfx.wav', sfx)
    print(f'musique et effets : {total:.1f} s')


if __name__ == '__main__':
    main()
