# LORETTA AVE — Grok Build Guide
**Step-by-step instructions for cutting the film. Compiled 2026-09-22.**

## The pipeline (how this actually works)

1. **Grok Imagine** generates the missing visual clips (6–15 seconds each, 16:9, 24fps).
2. **You pull the finished elements** — 11 video clips + audio, stored in the Higgsfield project gallery and in the element manifest.
3. **You assemble in CapCut** (free) — Grok doesn't do timelines. Lay audio first, cut visuals to it, add the text cards, export both masters.

Watch your Grok usage pool: video generations share a weekly quota with chat. Generate in batches, download every keeper immediately.

---

## PART 1 — Generate in Grok

Settings per clip: **16:9, 24fps, highest resolution your plan allows** (720p in-app; 1080p needs SuperGrok Plus or the API). 15 seconds max per generation — chain with Extend-from-Frame for longer beats. Prompt style: cinematic, photoreal, naturalistic. Never ask for text, logos, or words inside the image — all text is added in the edit.

**Copy-paste prompts:**

**Shot 2 — the flyover (critical, generate first):**
> Smooth low-altitude continuous drone flyover over a developing suburban corridor at dusk, Menifee California: graded earth pads, terraced lots, construction activity, golden-hour light raking across the dirt, Scott Road corridor, cinematic aerial cinematography, photoreal, no people in close-up, no text overlays

**Act I — dawn drive:**
> Pickup truck rolling past golden ranch land on a rural road at dawn, warm low sun, fence lines and open hills, cinematic tracking shot, photoreal

**Act I — car interior:**
> Interior of a pickup truck at dawn, driver's hands on the steering wheel, dashboard radio glowing, golden light through the windshield, hills rolling past the window, cinematic, photoreal

**Act I — roadside:**
> Man in his 30s standing at the roadside at dawn looking out over empty golden hills, wind in the dry grass, quiet contemplative mood, cinematic wide shot, photoreal

**Act III — builder's office (flyer beat):**
> Warm office interior morning, frustrated executive tossing a thin document flyer into a trash bin, papers on a desk, phone ringing in background, real workplace frustration, cinematic, photoreal

**Act III — package handoff:**
> Colleague handing a thick complete document package across an office desk, mood lifting, morning office light, cinematic, photoreal

**Act III — monitor study:**
> Over-the-shoulder of an executive studying maps and aerial imagery on a large dark monitor, finger tracing a line on screen, office morning light, cinematic, photoreal, screen content left dark and blank

**Act III — underwriting:**
> Over-the-shoulder of an executive working a financial spreadsheet on a monitor with an aerial site map beside it, typing, pausing, checking numbers, warm office, cinematic, photoreal, screen content left dark and blank

**Act IV — coffee room:**
> Two colleagues in an office coffee room in the morning, one pouring coffee while talking animatedly, genuine excitement, fast natural energy, cinematic, photoreal

**Act IV — studio table:**
> Architecture studio, team gathered around a table covered with grading plans and contour sheets, pointing and discussing, morning light, cinematic, photoreal

**Closer — conference room dialing:**
> Team filing into a conference room gathering around a speakerphone on the table, one person dialing, anticipation, cinematic, photoreal

**Closer — Hamza:** DO NOT generate. This is his real phone recording. No AI face, ever.

**After each generation:** download immediately. Check for the Grok watermark — if it's burned in, that clip fails QC. Reject anything with waxy skin, morphing faces, warping hands, or smeary textures and regenerate.

---

## PART 2 — Assemble in CapCut

### Timeline (total ~3:25)

| Time | Visual | Audio |
|---|---|---|
| 0:00–0:06 | Black → dawn truck (your Grok clip) | Radio fades up mid-sentence over black: *"...Menifee, named one of America's top boomtowns —"* |
| 0:06–0:20 | Car interior + roadside hills (Grok clips) | `radio_broadcast.wav` continues under |
| 0:20–0:30 | Roadside stop, man looking at hills | Wind bed. Card: **BUT THIS ISN'T A STORY ABOUT LAND.** |
| 0:30–0:38 | `kenburns_map.mp4` (parcel map draws itself) | Card: **IT'S ABOUT WHAT THE DATA SAW.** |
| 0:38–0:50 | `datastorm.mp4` — hard cuts, loudest 12s | Riser. Mid-storm card: **HE HELPED PUT 1,000+ HOMES INTO THE DEVELOPMENT PHASE IN THIS CORRIDOR** |
| 0:50–0:58 | `b2_extrude_trim.mp4` (map rises to 3D) | Sub drop. Card: **0 LORETTA AVE. 40.56 GROSS ACRES. MENIFEE, CA.** |
| 0:58–1:05 | `contour_dive.mp4` | Card: **232 PROPOSED LOTS. FOUR PARCELS. ONE PLAN.** |
| 1:05–1:22 | Builder office flyer beat (Grok) | `dialogue_builder_flyer.wav`: *"It would take me too long to underwrite this deal."* Phone ringing bed. |
| 1:22–1:32 | Package handoff (Grok) | Card: **THEN HAMZA'S PACKAGE LANDED.** |
| 1:32–1:47 | Monitor study (Grok) | `dialogue_builder_1.wav`: *"This is the corridor. Hamza brought us the data before anyone else saw it."* |
| 1:47–2:02 | Underwriting (Grok) | `dialogue_builder_2.wav` / `dialogue_builder_3.wav` — working the numbers |
| 2:02–2:08 | Builder at window (Grok or `loretta_shot01_knoll_reveal_ai_h264.mp4`) | Quiet beat. Card: **THE BUILDERS SAW IT TOO.** |
| 2:08–2:21 | Coffee room (Grok) | `dialogue_colleague_1/2/3.wav` — rapid-fire excitement |
| 2:21–2:29 | Studio table (Grok) | `dialogue_architect.wav`: *"The proposed lot layout is on the table. Let's walk through it."* |
| 2:29–2:36 | `eng_detail.mp4` | `dialogue_engineer.wav`: *"This is how you build before it exists."* |
| 2:36–2:39 | Team agreement beat | Card: **THEN CAME THE VISION.** |
| 2:39–2:47 | `orbit_trim.mp4` | Music opens fully (`starlight_trail.mp3` blooms 2:39–2:42) |
| 2:47–2:52 | `sweep_trim.mp4` | Music open |
| 2:52–2:59 | `street_trim.mp4` | Card: **BEFORE IT EXISTS.** |
| 2:59–3:04 | Driver bookend — gets in truck, drives on (Grok) | Music resolves under, then out |
| 3:04–3:12 | Conference room dialing (Grok) | `dialogue_teammember_dial.wav`: *"Hamza Nasir."* Ringing tone. |
| 3:12–3:20 | **Hamza's real clip** — answers, camera pushes in, he smiles | `dialogue_team_phone.wav` through phone-speaker EQ: *"Hamza — it's us. We just got through the package. We've got questions for you."* |
| 3:20–3:25 | Black. 0.5s silence, then cards. | **HE BUILDS BEFORE IT EXISTS.** / **AVAILABLE ON LOOPNET.** (Moby ending track under, when supplied — Starlight Trail excerpt as temp.) |

### Text cards
Gold text on near-black, simple elegant font. Exact wording in the table above — copy character-for-character. No APNs on screen — parcel outlines only, never parcel numbers. Lot count: always "232 PROPOSED."

### Audio order of operations
1. Lay `premix.wav` (dialogue) and `radio_broadcast.wav` on the timeline first.
2. Cut visuals to match the voices — not the other way around.
3. `starlight_trail.mp3` underneath: −12dB under Act II → whisper under Acts III–IV → bloom at 2:39 → out by 3:03.
4. Wind/office/phone beds from `audio/sfx/` under the roadside and office beats.

### Export
- **16:9 master:** 1920×1080, 24fps → `loretta_ave_16x9.mp4`
- **9:16 master:** 1080×1920, 24fps → reframe each clip vertically in CapCut (never crop the finished 16:9), own text-card layout → `loretta_ave_9x16.mp4`

### QC before calling it done
- Watch both masters end to end, in motion, no skipping.
- No Grok watermark visible anywhere. No AI artifacts (waxy skin, morphing, warping).
- Every card's spelling and numbers verified: 232 PROPOSED, road names. No APN numbers appear anywhere on screen.
- No dialogue from Hamza. No generated face claiming to be him.
- The only call to action in the film is **AVAILABLE ON LOOPNET.**
