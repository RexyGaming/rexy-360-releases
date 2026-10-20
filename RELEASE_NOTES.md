# Rexy 360 1.0.1-beta — cut to the music

## New
- **★ Master music.** In a clip's Audio panel (Shoot screen), star the track the edit should follow — or leave it on the clip's own sound.
- **Shots land on the music.** Drag a shot onto the Edit and it goes straight to where its In falls in the master song (🔗 linked) — shots made from one clip line up exactly as they were on the Shoot screen. The song runs along the bottom of the Edit (**★ Master**). **Right-click → Unlink** to move a shot freely, **Link** to put it back. The **♪** button changes the master or turns it off.
- **Free timeline with Snap.** Shots sit wherever you place them (gaps are black; where two overlap the later one wins). **⊐⊏ Snap** (on by default) makes drops and drags meet the shot before or after — no gaps, no overlaps.
- **Move thumbnails.** Every shot card in the Library shows its move — the vMoCo curves in their colours — updating live as you record.
- **Render part of an Edit.** On the Edit screen, **Set In / Set Out** (Export panel) or the **I / O** keys mark a stretch of the Edit; **Render now** renders just that, picture and music in step.
- **A tidier Edit screen.** The right-hand panel shows only the Library, Colour and Export there — the operating controls stay on the Shoot screen.
- **"Shot" is now "Shoot"** — the screen where you operate a clip (shots are still what you make there).

## Fixed
- Music on the Edit: a song imported into a clip's Audio panel is its master music without needing a ★, so it plays on the Edit.
- Set In / Set Out on the Edit screen set the same point twice (and changed the open shot).
- Double-clicking a clip or shot in the Library opens it again.
- NODO in no longer tries to open other serial ports (Bluetooth links) when no Receiver is plugged in.

---

# Rexy 360 1.0.0-beta — the first public beta

Rexy 360 turns 360° footage into operated camera shots: you drive a virtual remote head through the shot with real wheels, shape the moves, cut them together and render. Designed for **Rexy Wheels in joystick mode**; a gamepad works too.

## In this release

**Reframing and the head**
- Stitched 360 footage: equirectangular, YouTube's cubemap and squashed-16:9 360, Insta360 .insv (experimental — no lens calibration or FlowState). Proxies build in the background for smooth scrubbing; renders always use the full-resolution original.
- Pan / tilt / roll in **Absolute** or **Continuous** wheel modes, Horizon or Frame roll, Swoop, Unlimited tilt, soft stops, Autolevel, and Rexy Bridge's S / C / D / F tuning per axis.
- Inputs: **Rexy Wheels** (joystick mode), gamepads, keyboard, and Alt Inputs — **NODO Inertia Wheels** (straight from the USB Receiver), OSC, MIDI and FreeD — with calibration and the Filter Lab.

**Lenses and time**
- A lens library (real zooms and primes, custom lenses), frame shapes with guides, tiny-planet zoom.
- Speed ramps from 1 % to 10 000 %, a shutter angle for real motion blur, light trails, slow-motion frames by blending or optical flow.

**Virtual motion control**
- Record moves as takes; mark, anchor and reshape their curves; every take is a **shot** with its own In / Out and look; Save over another take; save / load `.rxmove` files (Rexy Bridge moves load too).
- **Audio → Move**: moves that pulse on the beat or follow the loudness of any track — layered, trimmed on the timeline, with Threshold and Smooth. Saving a move can **apply the music to it**, so the music-driven movement travels to another clip.

**Audio**
- Music and sound tracks on the film's time, fades, volume keys, **Sync to clip audio**, audio from a link.

**Rexy Studio — editing**
- Projects and a Library; an **Edit** timeline (magnetic main track), overlay tracks with eight blend modes, opacity and opacity keyframes, dissolves and dips, Edit undo, music linked to its shots, render the Edit.

**Colour**
- A grade per shot and one over the whole Edit: exposure, contrast, highlights, shadows, saturation, vibrance, temperature, tint — and **.cube LUTs** with a strength.

**Import and export**
- Open files, or import from **YouTube** (a whole video or just a section, From–To), Dropbox, Google Drive or a direct link — progress in the log.
- Render to **H.264**, **HEVC** or **ProRes** with a render queue (cancel any time), snapshots.
- Works with **any graphics card**: NVIDIA NVENC, Intel Quick Sync, AMD, Windows Media Foundation — or software H.264 when none is available.

**App**
- Update check at start-up and in About; one-click update on Windows.
- Resizable right-hand panel; mouse-wheel zoom on every timeline (Shift + wheel slides).

## Known limits

- The installers aren't code-signed yet (Windows: **More info → Run anyway**).
- macOS build coming soon.
- HEVC renders need a graphics-card encoder that does HEVC.
- Insta360 .insv and GoPro .360 support is experimental / not yet available — export an equirectangular video from Insta360 Studio or GoPro Player for best results.
- NODO Inertia Wheels support is built from NODO's published data format and tested with simulated wheels — please report how it works with yours.
