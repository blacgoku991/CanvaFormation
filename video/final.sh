#!/bin/sh
# Assemble l'image (out/video-muette.mp4) et le son (audio/mix.wav) en un MP4 léger, prêt à partager.
set -e
cd "$(dirname "$0")"
ffmpeg -y -v error -i out/video-muette.mp4 -i audio/mix.wav -map 0:v -map 1:a \
  -c:v libx264 -preset slow -crf 21 -maxrate 9M -bufsize 18M -pix_fmt yuv420p \
  -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:a aac -b:a 192k -ar 48000 \
  -movflags +faststart -shortest "${1:-out/Video-Dolce-Lash-Brow.mp4}"
ls -la "${1:-out/Video-Dolce-Lash-Brow.mp4}"
