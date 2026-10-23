# Rexy 360

**A 360° reframing studio for camera operators.** Drive a virtual remote head through your 360 footage with real wheels — pan, tilt, roll, zoom — shape the moves, cut them together and render.

Rexy 360 is designed for use with **Rexy Wheels in joystick mode**, and can be operated with a **gamepad** too. NODO Inertia Wheels, OSC, MIDI, FreeD and the keyboard can drive it as well.

This repository is the **download page and documentation** for Rexy 360. (The application is closed source, and free during the beta.)

---

## ⬇️ Download

**[→ Download the latest release](../../releases/latest)**

- **Windows 10 / 11 (64-bit)** — grab `Rexy360-Setup-<version>.exe` and run it.
- **macOS 12 or later** — `Rexy360-<version>-arm64.dmg` for Apple Silicon (M1 and later), `Rexy360-<version>-x64.dmg` for Intel Macs. Open the .dmg and drag **Rexy 360** to Applications. (Not sure which Mac you have? Apple menu → About This Mac: "Chip: Apple M…" = Apple Silicon.)

> **Heads-up — the installers aren't code-signed yet.** Windows shows a blue **"Windows protected your PC"** dialog — click **More info → Run anyway**. On a Mac, the first time you open it **right-click (or Control-click) Rexy 360 → Open → Open**; if macOS still refuses, go to System Settings → Privacy & Security and click **Open Anyway**. This is expected for a beta and is not a warning about the app itself.

> **Mac — controllers:** the first time Rexy 360 reads a gamepad or Rexy Wheels, macOS asks for **Input Monitoring** — allow it (System Settings → Privacy & Security → Input Monitoring), then restart Rexy 360.

Rexy 360 checks for updates when it starts (and from **About → Check for updates**); on Windows a new version downloads in the background and the top bar offers **Restart to update**; on a Mac the top bar shows **⬇ Download**, which opens this page for the new version.

### What you need

- A **stitched 360° video** (equirectangular — e.g. exported from Insta360 Studio or GoPro Player). YouTube 360 videos can be imported straight from a link.
- A graphics card with **WebGL 2** (any recent one). **NVIDIA is recommended** — Rexy 360 also uses Intel Quick Sync, AMD or Windows' own encoder, and falls back to software H.264 when none is available (HEVC renders need a graphics-card encoder). On a Mac, Rexy 360 uses Apple VideoToolbox — every Mac can render H.264, HEVC and ProRes.
- 16 GB RAM or more is comfortable for 5.7K footage.

---

## 📖 Documentation

- **[Getting Started](GETTING_STARTED.md)** — open a clip, bind your wheels, record a move, render (start here).
- **[Release notes](RELEASE_NOTES.md)** — what's in each version.

## What it does

- **360 reframing** — equirectangular (plus YouTube's cubemap and squashed 16:9, Insta360 .insv experimental), proxies for smooth scrubbing, renders from the full-resolution original.
- **A virtual remote head** — Absolute or Continuous wheel modes, Horizon or Frame roll, Swoop, Unlimited tilt, soft stops, Autolevel, per-axis tuning.
- **Lenses** — a lens library of real zooms and primes, any frame shape (16:9, 9:16, 1:1 …) with guides, tiny-planet zoom.
- **Time** — speed ramps 1 %–10 000 %, shutter-angle motion blur, light trails, slow-motion by frame blending or optical flow.
- **Virtual motion control** — record moves as takes, mark, anchor and reshape them; every take is a shot with its own In / Out and look.
- **Audio** — music and sound tracks, sync to the clip's sound, and **Audio → Move**: moves that pulse with the beat or follow the loudness.
- **Rexy Studio editing** — projects and a library, an Edit timeline with overlays and blend modes, keyframes, dissolves, linked music.
- **Colour** — a grade per shot and over the whole Edit, and .cube LUTs.
- **Import / export** — files, Dropbox, Google Drive, YouTube (whole or a section); H.264, HEVC or ProRes.

## Feedback

Beta feedback, bugs and ideas: **rob@realprogear.com**.

---

© 2026 Real Pro Gear Ltd. Designed by Robert Portazier. Free during the beta under the [licence](LICENSE.txt); third-party components are listed in [THIRD_PARTY_NOTICES.txt](THIRD_PARTY_NOTICES.txt).
