"""Calcule le minutage des scènes (video/timeline.json) à partir du script.

Si la voix off d'une scène existe (audio/vo/<id>.mp3), sa durée réelle est utilisée ;
sinon la durée est estimée à 20 caractères par seconde (mesuré sur la voix « Perle »).
"""
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
CHARS_PER_SEC = 20.0
LEAD = 0.55   # silence avant la voix, le temps que la transition se pose
TAIL = 0.85   # respiration après la voix
MIN_DUR = {'intro': 6.8, 'sommaire': 6.6, 'p1': 3.2, 'p2': 3.2, 'p3': 3.4, 'gestion': 8.2, 'evaluation': 5.4, 'outro': 8.0}


def audio_duration(path):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(path)],
                         capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def main():
    script = json.loads((ROOT / 'script.json').read_text(encoding='utf-8'))
    t = 0.0
    scenes = []
    for s in script['scenes']:
        vo_file = ROOT / 'audio' / 'vo' / f"{s['id']}.mp3"
        real = vo_file.exists()
        vo_dur = audio_duration(vo_file) if real else len(s['vo']) / CHARS_PER_SEC
        dur = max(LEAD + vo_dur + TAIL, MIN_DUR.get(s['id'], 0))
        scenes.append({
            'id': s['id'], 'partie': s['partie'], 'vo': s['vo'],
            'start': round(t, 3), 'dur': round(dur, 3),
            'vo_start': round(t + LEAD, 3), 'vo_dur': round(vo_dur, 3), 'vo_reelle': real,
        })
        t += dur
    timeline = {'fps': 30, 'width': 1920, 'height': 1080, 'total': round(t, 3), 'scenes': scenes}
    (ROOT / 'timeline.json').write_text(json.dumps(timeline, ensure_ascii=False, indent=1), encoding='utf-8')
    (ROOT / 'timeline.js').write_text('window.TIMELINE = ' + json.dumps(timeline, ensure_ascii=False) + ';\n', encoding='utf-8')
    print(f"{len(scenes)} scènes, durée totale {t:.1f} s ({sum(s['vo_reelle'] for s in scenes)} voix réelles)")


if __name__ == '__main__':
    main()
