#!/usr/bin/env bash
# Loretta Ave v5 mux — Grok 2026-09-22 20:33 PDT
# Mix only when PictureLock is a real file AND duration maps to 205s.
set -euo pipefail

PIC="${1:-/home/workdir/artifacts/loretta_edit/Loretta_Ave_PictureLock_v4.mp4}"
BED="${2:-/home/workdir/artifacts/loretta_edit/Loretta_Ave_AudioBed_v5pre.m4a}"
OUT="${3:-/home/workdir/artifacts/loretta_edit/Loretta_Ave_PictureLock_v5.mp4}"
STARLIGHT="audio/starlight_trail.mp3"
PREMIX="audio/premix.m4a"
RADIO="audio/radio_broadcast.wav"

if [[ ! -f "$PIC" ]]; then
  echo "REFUSE: missing picture $PIC"
  exit 2
fi
# HTML stub guard
if file -b --mime-type "$PIC" | grep -qi 'text/html'; then
  echo "REFUSE: picture is HTML not video"
  exit 3
fi

DUR=$(ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 "$PIC" || echo 0)
# Need ~205s (3:25). MIX_SPEC 175.85s does not map to premix.
python3 - <<PY
dur=float("${DUR}" or 0)
if abs(dur-205.0)>1.0:
    raise SystemExit(f"REFUSE: picture duration {dur:.2f}s does not map to 205s premix/timeline")
print(f"OK duration {dur:.2f}s")
PY

echo "Would mux: picture + Starlight under full + premix Acts III-IV + keep Act I radio + closer MUTED"
echo "OUT $OUT"
echo "Do not unmute Hamza. Do not rip Moby. Do not generate AI Hamza."
# Actual ffmpeg left to the mix workspace when both files exist.
