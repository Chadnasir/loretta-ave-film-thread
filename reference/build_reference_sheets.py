#!/usr/bin/env python3
"""Build production reference sheets (labeled contact-sheet PNGs) for the
Loretta Ave film elements. Local-only: no credits, no network, no uploads.

Outputs (under REFERENCE_DIR):
  cards_reference.png    - 12 cards in CARD_LOCK timeline order, QC-labeled
  segments_reference.png - all top-level segment mp4s + knoll reveal, labeled

Re-run after card rebuilds land: update QC dicts below (CARD_QC / SEGMENT_NOTES)
and run:  python3 build_reference_sheets.py
"""

import os
import subprocess
import textwrap
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont, ImageOps

# ---------------------------------------------------------------- config ---

SEGMENTS_DIR = os.path.expanduser("~/workspace/higgsfield-video/segments")
CARDS_DIR = os.path.join(SEGMENTS_DIR, "cards")
KNOLL_MP4 = os.path.expanduser(
    "~/workspace/higgsfield-video/renders/new/loretta_shot01_knoll_reveal_ai_h264.mp4")
REFERENCE_DIR = os.path.expanduser("~/workspace/higgsfield-video/reference")
FRAMES_CACHE = "/tmp/ref_frames"

# Card QC status (ground truth from frame-by-frame inspection vs CARD_LOCK.md).
# status word -> display color. Update these after rebuilds and re-run.
STATUS_COLORS = {
    "PASS": (46, 204, 113),                # green
    "REBUILD IN PROGRESS": (231, 76, 60),  # red
    "SPARE - NOT IN LOCK": (149, 165, 166),# grey
    "BANNED - DO NOT USE": (231, 76, 60),  # red
}

# Cards in CARD_LOCK timeline order. `slot` is the lock's timeline window.
# `status` must be a key of STATUS_COLORS.
CARDS = [
    {"file": "not_land.mp4",      "label": "CARD #1",       "slot": "0:22-0:30",
     "status": "PASS"},
    {"file": "data_saw.mp4",      "label": "CARD #2",       "slot": "0:31-0:38",
     "status": "PASS"},
    {"file": "homes_1000.mp4",    "label": "CARD #3",       "slot": "0:51-0:58",
     "status": "PASS"},
    {"file": "acres.mp4",         "label": "CARD #4",       "slot": "0:59-1:05",
     "status": "PASS"},
    {"file": "lots_232.mp4",      "label": "CARD #5",       "slot": "0:59-1:05",
     "status": "PASS"},
    {"file": "package_landed.mp4","label": "CARD #6",       "slot": "1:24-1:32",
     "status": "PASS"},
    {"file": "builders_saw.mp4",  "label": "CARD #7",       "slot": "2:03-2:08",
     "status": "PASS"},
    {"file": "vision_came.mp4",   "label": "CARD #8",       "slot": "2:36-2:39",
     "status": "PASS"},
    {"file": "before_exists.mp4", "label": "CARD #9",       "slot": "2:53-2:59",
     "status": "PASS"},
    {"file": "builds_before_exists.mp4", "label": "CARD #10", "slot": "3:20.5-3:23",
     "status": "PASS"},
    {"file": "available_loopnet.mp4", "label": "CARD #11", "slot": "3:23-3:25",
     "status": "PASS"},
    {"file": "location.mp4",      "label": "SPARE",         "slot": "not in CARD_LOCK",
     "status": "SPARE - NOT IN LOCK"},
    {"file": "del_webb.mp4",      "label": "BANNED",        "slot": "never on screen per CARD_LOCK",
     "status": "BANNED - DO NOT USE"},
]

# Per-segment note overrides. Default note for everything else: "QC PENDING".
SEGMENT_NOTES = {
    "kenburns_map.mp4": "PASS - APNs removed, outlines only",
    "closer_hamza_real_8s.mp4": "MUTED - approved closer",
}
DEFAULT_SEGMENT_NOTE = "QC PENDING"
KNOLL_NOTE = "QC PENDING"

# ---------------------------------------------------------------- style ----

BG = (12, 12, 12)
PANEL = (22, 22, 22)
TEXT = (235, 235, 235)
DIM = (165, 165, 165)
ACCENT = (212, 175, 105)   # gold accent for headers
THUMB_W, THUMB_H = 520, 292
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


# --------------------------------------------------------------- helpers ---

def probe(path):
    """Return (duration_seconds, width, height) or (None, None, None)."""
    try:
        d = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries",
             "format=duration:stream=width,height", "-of",
             "default=noprint_wrappers=1", path],
            capture_output=True, text=True, timeout=30)
        dur = w = h = None
        for line in d.stdout.splitlines():
            k, _, v = line.partition("=")
            if k == "duration":
                dur = float(v)
            elif k == "width":
                w = int(v)
            elif k == "height":
                h = int(v)
        return dur, w, h
    except Exception:
        return None, None, None


def extract_frame(path, out_png):
    """Middle frame of `path` -> `out_png`. Returns True on success."""
    dur, _, _ = probe(path)
    if dur is None or dur <= 0:
        return False
    try:
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", "-ss", str(dur / 2),
             "-i", path, "-frames:v", "1", out_png],
            check=True, timeout=60)
        return os.path.exists(out_png)
    except Exception:
        return False


def thumb(path, cache_name):
    """Letterboxed thumbnail image (THUMB_W x THUMB_H), or None."""
    os.makedirs(FRAMES_CACHE, exist_ok=True)
    frame_png = os.path.join(FRAMES_CACHE, cache_name + ".png")
    if not os.path.exists(frame_png):
        if not extract_frame(path, frame_png):
            return None
    try:
        im = Image.open(frame_png).convert("RGB")
    except Exception:
        return None
    box = Image.new("RGB", (THUMB_W, THUMB_H), BG)
    im.thumbnail((THUMB_W, THUMB_H), Image.LANCZOS)
    box.paste(im, ((THUMB_W - im.width) // 2, (THUMB_H - im.height) // 2))
    return box


def wrap(draw, text, fnt, max_w):
    """Wrap text to fit max_w pixels; returns list of lines.
    Overlong single words (e.g. long filenames) are hard-broken."""
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        if draw.textlength(w_, font=fnt) > max_w:
            if cur:
                lines.append(cur)
                cur = ""
            chunk = ""
            for ch in w_:
                if draw.textlength(chunk + ch, font=fnt) <= max_w - 20:
                    chunk += ch
                else:
                    lines.append(chunk)
                    chunk = ch
            cur = chunk
            continue
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines or [""]


def draw_cell(draw, x, y, cell_w, lines, label_h):
    """Draw the label block under a thumbnail. lines = [(text, font, color)]."""
    draw.rectangle([x, y, x + cell_w, y + label_h], fill=PANEL)
    cy = y + 14
    for text, fnt, color in lines:
        for ln in wrap(draw, text, fnt, cell_w - 28):
            draw.text((x + 14, cy), ln, font=fnt, fill=color)
            cy += fnt.size + 8
    return cy


def header(draw, sheet_w, title, subtitle):
    draw.text((48, 36), title, font=font(44, bold=True), fill=ACCENT)
    draw.text((48, 96), subtitle, font=font(28), fill=DIM)
    return 170  # y where the grid starts

# ------------------------------------------------------------ cards sheet ---

def build_cards_sheet():
    cols = 3
    cell_w = THUMB_W + 40
    label_h = 210
    gutter = 24
    margin = 48
    sheet_w = margin * 2 + cols * cell_w + (cols - 1) * gutter
    rows = (len(CARDS) + cols - 1) // cols
    cell_h = THUMB_H + 16 + label_h
    sheet_h = 170 + rows * cell_h + (rows - 1) * gutter + margin

    sheet = Image.new("RGB", (sheet_w, sheet_h), BG)
    draw = ImageDraw.Draw(sheet)
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M %Z")
    header(draw, sheet_w, "LORETTA AVE - TITLE CARDS REFERENCE",
           f"{len(CARDS)} cards vs CARD_LOCK.md - generated {stamp} - "
           "green=PASS  red=REBUILD/BANNED  grey=SPARE")

    missing = []
    for i, card in enumerate(CARDS):
        r, c = divmod(i, cols)
        x = margin + c * (cell_w + gutter)
        y = 170 + r * (cell_h + gutter)
        path = os.path.join(CARDS_DIR, card["file"])
        t = thumb(path, "card_" + card["file"].replace(".mp4", ""))
        if t is None:
            t = Image.new("RGB", (THUMB_W, THUMB_H), (40, 20, 20))
            d2 = ImageDraw.Draw(t)
            d2.text((THUMB_W // 2 - 90, THUMB_H // 2 - 20), "MISSING",
                    font=font(36, bold=True), fill=(231, 76, 60))
            missing.append(card["file"])
        sheet.paste(t, (x + 20, y))
        color = STATUS_COLORS[card["status"]]
        draw_cell(draw, x + 20, y + THUMB_H + 16, THUMB_W, [
            (f'{card["label"]}  |  {card["slot"]}', font(30, bold=True), TEXT),
            (card["file"], font(28), DIM),
            (card["status"], font(30, bold=True), color),
        ], label_h)

    out = os.path.join(REFERENCE_DIR, "cards_reference.png")
    sheet.save(out)
    return out, missing


# --------------------------------------------------------- segments sheet ---

def build_segments_sheet():
    seg_files = sorted(f for f in os.listdir(SEGMENTS_DIR)
                       if f.endswith(".mp4") and os.path.isfile(os.path.join(SEGMENTS_DIR, f)))
    items = [("segments", f) for f in seg_files]
    if os.path.exists(KNOLL_MP4):
        items.append(("knoll", os.path.basename(KNOLL_MP4)))
    else:
        print("WARNING: knoll reveal not found:", KNOLL_MP4)

    cols = 4
    cell_w = THUMB_W + 40
    label_h = 225
    gutter = 24
    margin = 48
    sheet_w = margin * 2 + cols * cell_w + (cols - 1) * gutter
    rows = (len(items) + cols - 1) // cols
    cell_h = THUMB_H + 16 + label_h
    sheet_h = 170 + rows * cell_h + (rows - 1) * gutter + margin

    sheet = Image.new("RGB", (sheet_w, sheet_h), BG)
    draw = ImageDraw.Draw(sheet)
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M %Z")
    header(draw, sheet_w, "LORETTA AVE - SEGMENTS REFERENCE",
           f"{len(items)} elements ({len(seg_files)} segments + knoll) - generated {stamp}")

    missing = []
    for i, (kind, fname) in enumerate(items):
        r, c = divmod(i, cols)
        x = margin + c * (cell_w + gutter)
        y = 170 + r * (cell_h + gutter)
        path = KNOLL_MP4 if kind == "knoll" else os.path.join(SEGMENTS_DIR, fname)
        t = thumb(path, ("knoll_" if kind == "knoll" else "seg_") + fname.replace(".mp4", ""))
        if t is None:
            t = Image.new("RGB", (THUMB_W, THUMB_H), (40, 20, 20))
            d2 = ImageDraw.Draw(t)
            d2.text((THUMB_W // 2 - 90, THUMB_H // 2 - 20), "MISSING",
                    font=font(36, bold=True), fill=(231, 76, 60))
            missing.append(fname)
        sheet.paste(t, (x + 20, y))

        dur, w, h = probe(path)
        if dur is None:
            spec = "duration unknown"
        else:
            spec = f"{dur:.2f}s"
            if w and h:
                spec += f"  {w}x{h}"
        note = KNOLL_NOTE if kind == "knoll" else SEGMENT_NOTES.get(fname, DEFAULT_SEGMENT_NOTE)
        note_color = ACCENT if note != DEFAULT_SEGMENT_NOTE else DIM
        tag = "KNOLL REVEAL" if kind == "knoll" else "SEGMENT"
        draw_cell(draw, x + 20, y + THUMB_H + 16, THUMB_W, [
            (f"{tag}", font(28, bold=True), ACCENT),
            (fname, font(28), TEXT),
            (spec, font(28), DIM),
            (note, font(28, bold=True), note_color),
        ], label_h)

    out = os.path.join(REFERENCE_DIR, "segments_reference.png")
    sheet.save(out)
    return out, missing


# ------------------------------------------------------------------- main ---

def main():
    os.makedirs(REFERENCE_DIR, exist_ok=True)
    c_out, c_missing = build_cards_sheet()
    s_out, s_missing = build_segments_sheet()
    for p in (c_out, s_out):
        size = os.path.getsize(p)
        print(f"{p}  ({size} bytes)")
        assert size > 0, f"empty output: {p}"
    if c_missing or s_missing:
        print("COULD NOT RENDER:", sorted(set(c_missing + s_missing)))
    else:
        print("all elements rendered OK")


if __name__ == "__main__":
    main()
