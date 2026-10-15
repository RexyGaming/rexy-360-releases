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
