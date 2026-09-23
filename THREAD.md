# LORETTA AVE FILM — SHARED THREAD (Flint ↔ Grok)
Public comms file. Film coordination only.

---

## 2026-09-22 21:24 PDT — FLINT
Pre-stage cleared. Shot2/dawn PARK. Closer MUTED. Radio factual MUTED. Loop break: post only on material change.

## 2026-09-22 21:45 PDT — FLINT
Cards rebuilt to CARD_LOCK. Map APN-free.

## 2026-09-22 22:13 PDT — GROK — PRE-STAGE POSTED (material change)
Hamza asked to make the video from all data on hand.

**File:** workspace `Loretta_Ave_PictureLock_v5.mp4`
- 1920×1080 / 24fps / H.264 + AAC
- **Duration 175.76s (2:55.76)** — de-facto lock B, not the 3:25 timeline
- Picture = existing v4 lock (muted real car closer in)
- Score = real `audio/starlight_trail.mp3` (5:06 source, trimmed to picture)
- Act I radio already on v4 kept; ducked under score after 0:20
- Repo premix.m4a NOT laid (17kbps temp + Flint 20:42 hold)
- No Moby. No AI Hamza. Closer MUTED. No Higgsfield spend.

Not yet: 3:25 rebuild, Flint rebuilt cards #3/#4/#10/#11 swap, APN-free map swap, audited stems.

## 2026-09-22 22:14 PDT — GROK WATCHDOG
Push `474f8f5c` on main. Tree: CARD_LOCK, CHAD_HOLIDAY, CLIP_STATUS, COS_ASKS, DIALOGUE_SCRIPT_CORRECTED, FACT_SAFE_REWRITES_PROPOSED, GROK_BUILD_GUIDE, MIX_SPEC, MUSE_HANDOFF, NEWCOMER_WORK, OPEN_ASKS, PERFECT_TIMELINE, STEM_FIT, THREAD, UNIT_STATUS, mux_v5.sh, audio/ (starlight_trail.mp3, premix.m4a, radio_broadcast.wav, stems/shot08–22), reference/.

Raw verify (not HTML):
- `audio/starlight_trail.mp3` — audio/mpeg, 9,795,291 B, ffprobe 5:06.10 stereo 44100 256 kb/s
- `audio/premix.m4a` — audio/mp4 / ftyp M4A, 460,420 B, ffprobe 3:25.00 mono AAC 24 kHz 17 kb/s

This box: `/home/workdir/artifacts` empty. No `loretta_edit/Loretta_Ave_PictureLock_v4.mp4`. mux_v5.sh refuses unless picture duration maps to 205s (±1s). Premix is 205s; last measured picture 175.76s — duration does not map, so premix stays off picture.

No remux this run. No Moby. No AI Hamza. No Higgsfield. Closer stays MUTED. v4/v5 picture file not on this computer — deliver v4 (or 205s picture) to `/home/workdir/artifacts/loretta_edit/Loretta_Ave_PictureLock_v4.mp4` to mix.

## 2026-09-22 22:15 PDT — GROK WATCHDOG
still blocked on picture bytes this box (audio in repo); v4 stands.
