# Rexy 360 1.0.3-beta — the user guide, and a tidier Edit

## New
- **User Guide** — every screen and panel explained, with pictures, in **Dark** and **Light**: [USER_GUIDE.md](USER_GUIDE.md) here, and as PDFs on the release page.
- **Ctrl+Shift+P takes screenshots of the whole app** — Dark and Light, Shoot and Edit: the window as it is, the whole app at full length with every panel open, and each panel on its own, into Pictures\Rexy 360 screenshots. Your theme, screen and panels go back as they were.

## Changed
- **The first linked shot dropped into an empty Edit goes to its start**, wherever you drop it — no dead gap before the song. Later shots still find their own place in the music.
- **Removing the last shot that uses the master music lets the Edit forget that song**, so the next shot you drop brings its own. Ctrl+Z brings back both.
- **New project starts clean** — a clip you import into a new project no longer brings the moves and audio it had in other projects. Existing projects are unchanged.
- **Soft Stops** fits a narrow panel: the + / − buttons go under the number instead of pushing the last column off the edge.

---

# Rexy 360 1.0.2-beta — wheels in mouse mode, YouTube cubemaps

## New
- **Mouse devices (Alt Inputs, Windows).** Hand wheels that only send a mouse signal over USB can now drive Rexy 360. Tick **listen** and every mouse shows up by name, with its x, y, wheel and buttons — **Bind** a control and move the one you want. Works like an absolute wheel: **range** sets how many counts cover a control, **Zero** re-centres.
- **Ctrl+M detaches the cursor** while the wheels drive: the pointer holds still (clicks and scrolling still work), the wheels keep moving the head. Ctrl+M again — or switching to another app — gives the cursor back. Also bindable in Functions.
- **YouTube 360 cubemaps** that download squeezed into 16:9 (with no 360 tag) are recognised and converted, instead of being refused as "not a 360 file".
- **Alt Inputs** are now in the order Mouse devices, OSC, MIDI, FreeD, NODO.

## Fixed
- Wheels (mouse devices and NODO) no longer pile up turns past the end of a control's range — turning back moves it straight away.
- No more "WiFi stall?" warnings for inputs that only send when moved (mice, NODO, MIDI).
- A sound mix could occasionally fail when a shot's sound started after the beginning of a render.

---

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
