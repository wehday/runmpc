# Item facts for the five candidate Items

Research for [#13](https://github.com/wehday/runmpc/issues/13). All sources accessed 2026-11-13.

Method: same as [item-facts.md](https://github.com/wehday/runmpc/blob/research/item-facts/research/item-facts.md). Each Item's own README and release notes were read. Licence, last push, archived flag, releases and tags come from the GitHub REST API (`/repos/<o>/<r>`, `/releases`, `/tags`). Author names come from `/users/<login>`. For the repo where the API reports no licence, the root listing was checked for any `LICENSE*` or `COPYING` file. Screenshot URLs were fetched and checked to return HTTP 200 with an `image/*` content type. Device ids come from the 14-id list in [hardware-generations.md](https://github.com/wehday/runmpc/blob/research/hardware-generations/research/hardware-generations.md). "unknown" means the Item's own page does not say.

None of the five repos has the GitHub "archived" flag set. None publishes a funding file, socials or support links; the authors' GitHub profiles list no website or Twitter.

## Summary table

| Item | Author | One-line summary | Category | Target devices | Firmware requirement | Install method | Licence | Maturity | Latest release / push |
|---|---|---|---|---|---|---|---|---|---|
| mpc-sample-sdk | Jakub Kolcar (ioma8) | Rust SDK for writing MPC Sample mods: typed events, firmware hooks, audio, drawing and an SD autorun packager. | dev-library | mpc-sample | 1.3.0.12 | build-from-source | MIT | stable (no beta wording; pre-1.0, see notes) | tag v0.5.3, 2026-11-12 (no GitHub releases); pushed 2026-11-12 |
| mpc-sample-tracker (MPCTRACKER) | Jeff (jeffwebb-to) | ProTracker-style 8-track pattern tracker for the MPC Sample that runs from the SD card and opens .mod files. | app | mpc-sample | 1.3.0.12 | sd-autorun, build-from-source | MIT | beta ("expect rough edges", see notes) | v0.1.0, 2026-11-10 |
| virtual-mpc-sample | punkart (orrpunk-art) | MPC Sample stock firmware running in QEMU with the whole device in a browser panel, for testing mods off-device. | dev-library | mpc-sample (emulated; runs on a computer) | user supplies the 1.3.0.12 update image; other versions not supported yet | build-from-source | MIT (kernel patches GPL-2.0) | beta ("young project", see notes) | no releases; pushed 2026-11-01 |
| mpc-sample-root-ssh | puckcv per README; repo owner punkart (orrpunk-art) | SD autorun kit that starts the MPC Sample's built-in SSH server for temporary root access over USB, using your own keys. | dev-library (see notes) | mpc-sample | 1.3.0.12 (AC50/AZ07); others unverified | sd-autorun | none (no licence file) | stable (validated on one unit, see notes) | v1.2.0, 2026-10-19 |
| Trackyard | David Rose (drose030) | Desktop app that turns MP3/WAV songs into drum charts for Beat-Train on the MPC Sample and Clone Hero. | app (runs on a computer, see notes) | mpc-sample (output only) | none on the computer; output targets Beat-Train, which needs 1.3.0.x | installer, build-from-source | MIT (ADTOF model CC BY-NC-SA 4.0) | stable (no beta wording) | v1.2.0, 2026-11-07 |

## Screenshots

Only images on the Item's own page. Each URL returned HTTP 200 with an image content type.

| Item | Screenshot URL |
|---|---|
| mpc-sample-tracker | https://raw.githubusercontent.com/jeffwebb-to/mpc-sample-tracker/HEAD/docs/screenshots/pattern.png |
| mpc-sample-tracker | https://raw.githubusercontent.com/jeffwebb-to/mpc-sample-tracker/HEAD/docs/screenshots/samples.png |
| mpc-sample-tracker | https://raw.githubusercontent.com/jeffwebb-to/mpc-sample-tracker/HEAD/docs/screenshots/song.png |
| mpc-sample-tracker | https://raw.githubusercontent.com/jeffwebb-to/mpc-sample-tracker/HEAD/docs/screenshots/intro-name.png |
| virtual-mpc-sample | https://raw.githubusercontent.com/orrpunk-art/virtual-mpc-sample/HEAD/docs/img/panel.jpg |
| virtual-mpc-sample | https://raw.githubusercontent.com/orrpunk-art/virtual-mpc-sample/HEAD/docs/img/screen-factory-library.png |
| virtual-mpc-sample | https://raw.githubusercontent.com/orrpunk-art/virtual-mpc-sample/HEAD/docs/img/screen-trim.png |
| virtual-mpc-sample | https://raw.githubusercontent.com/orrpunk-art/virtual-mpc-sample/HEAD/docs/img/stock-map.jpg |
| Trackyard | https://raw.githubusercontent.com/drose030/trackyard/HEAD/docs/images/editor.png |
| mpc-sample-sdk | none on the Item's page |
| mpc-sample-root-ssh | none on the Item's page |

Note: the virtual-mpc-sample screenshots show the stock Akai app's screens. The README says they are "shown for documentation and interoperability".

## Download channel

| Item | Channel |
|---|---|
| mpc-sample-sdk | Source only. Used as a Cargo git dependency (`git = "https://github.com/ioma8/mpc-sample-sdk", branch = "main"`). Versions are git tags, not GitHub releases. |
| mpc-sample-tracker | GitHub release asset `mpctracker-v0.1.0-sd-card.zip` |
| virtual-mpc-sample | Source only (`git clone`). No releases; prebuilt downloads are on the roadmap. |
| mpc-sample-root-ssh | GitHub release assets `mpc-sample-root-ssh-v1.2.0.zip` plus `SHA256SUMS-v1.2.0.txt` |
| Trackyard | GitHub release assets `Trackyard-1.2.0-arm64.dmg` and `Trackyard-Setup-1.2.0.exe`; or source install with `uv` |

## Per-Item notes

### mpc-sample-sdk
- Repo: https://github.com/ioma8/mpc-sample-sdk (MIT). Author Jakub Kolcar (GitHub name for `ioma8`).
- "The universal mod SDK for the Akai MPC Sample 1.3.0.12, written in Rust." A mod is a Rust `cdylib` that is `LD_PRELOAD`ed into the stock app. "`install` refuses a missing app, a different firmware and a build where no site could be patched."
- `build-mod.sh` cross-builds the `.so` and, with `--pack` and a firmware hash, writes the SD `autorun` zip. So the SDK itself is build-from-source, and the mods it produces are sd-autorun.
- The same author's mpc-minimod (already in the seed list) is built on it.
- Maturity: no beta or experimental wording. It is pre-1.0 and the README warns that "`v0.2.0` contains API-breaking safety corrections". Tags run v0.1.9 to v0.5.3.
- Created 2026-11-09.

### mpc-sample-tracker (MPCTRACKER)
- Repo: https://github.com/jeffwebb-to/mpc-sample-tracker (MIT). Author shown on GitHub as "Jeff" (`jeffwebb-to`); no surname given.
- Copy the `autorun` and `tracker` folders to the SD card root. The autorun script stops the sampler app, runs the tracker from RAM and restarts the sampler on quit (SHIFT + STOP). "Nothing is written to the device's own storage."
- Firmware badge and text: 1.3.0.12. "It was developed against the virtual-mpc-sample emulator on firmware 1.3.0.12. It starts and plays sound on a real unit. The rest of the testing on hardware is still to be done, so expect rough edges."
- Building needs Docker and the `mpclab-tools` image from virtual-mpc-sample.
- The README asks users to put only music they have rights to in `demo/`; the release ships a built-in drum kit, so no third-party content is required.

### virtual-mpc-sample
- Repo: https://github.com/orrpunk-art/virtual-mpc-sample (MIT, except `kernel/patches/` under GPL-2.0). Author shown on GitHub as "punkart". README also in Russian and Chinese.
- Runs the unmodified stock MPC Sample firmware 1.3.0.12 in QEMU with a browser panel (screen, pads, knobs, SD card, USB-C, root SSH inside the VM). Purpose: "Build and test mods without risking the device."
- **Requires proprietary vendor data.** "No firmware and no factory content are in this repository: you need your own copy of the firmware update and, for the factory library, your own MPC Sample." The user extracts partitions from inMusic's `MPCSAMPLE-1.3.0.12-update.img`; the build checks them against `inputs.sha256`. This is the same pattern as the game Items that need user-supplied commercial game data.
- Not on-device software: it runs on macOS (only Apple Silicon tested), with Linux and Windows "code paths exist".
- Maturity: no "beta" label. The README says "Treat it as you would any young project: read what you run" and lists Windows/Linux runs and a firmware extractor as roadmap items.
- States it was developed with Claude in Claude Code.

### mpc-sample-root-ssh
- Repo: https://github.com/orrpunk-art/mpc-sample-root-ssh. No licence: the API reports none and the repo root has no `LICENSE*` or `COPYING` file.
- **Author ambiguity.** The README opens "By **puckcv** on MPC-Forums". The repo is owned by `orrpunk-art` ("punkart"), the same account as virtual-mpc-sample. Whether puckcv and punkart are the same person is not stated.
- **Security-sensitive.** What it does: an SD autorun package that, when the card is inserted, starts the device's own OpenSSH server with root login over the USB-C network link (`192.168.155.1`). Login is public-key only, using keys the user generates with the included setup scripts; password login and forwarding are disabled. Everything is set up under `/run`, so it is gone after a reboot. It does not flash firmware or change the stock app. The README warns: "A root shell can modify the device: this kit supplies access, not a recovery guarantee." It also tells users never to publish a prepared SD folder or private keys.
- Firmware: "Akai MPC Sample AC50/AZ07, firmware 1.3.0.12". "Other firmware versions and beta builds have not been verified." The Windows setup script has not been run on Windows by the author.
- Maturity: no beta wording. v1.2.0 notes report "two full cold boots ... successful root SSH on both boots", and say "This is validation on one MPC Sample, not on every firmware/device."
- Category: it is neither a feature mod nor a library. dev-library is the closest fit because its audience is people building or debugging mods; research is the alternative.

### Trackyard
- Repo: https://github.com/drose030/trackyard (MIT). Author David Rose (`drose030`), also the author of seed Item beat-train-mpc-sample.
- **Not on-device software.** It is a desktop app (macOS Apple Silicon `.dmg`, Windows `.exe`, or a Python install on Mac/Linux). It separates drums from a song, finds the beat grid and writes a chart. "Everything runs on your computer. Beat-Train on the MPC only plays the finished song folder." Save as to the SD card puts the song in `BeatTrain/Songs/`.
- Target device mpc-sample applies only to its output. It also writes charts for Clone Hero, which is not MPC software.
- Installers are unsigned; the README gives the macOS "Open Anyway" and Windows "Run anyway" steps.
- Licence note: the code is MIT, but the drum transcription model ADTOF is "CC BY-NC-SA 4.0, **non-commercial**". "ADTOF's licence allows private use." The first conversion downloads about 160 MB of model weights.
- Requires no commercial game data; the user supplies their own songs.

## Listing-policy flags

| Item | Flag |
|---|---|
| mpc-sample-root-ssh | Security-sensitive: grants a temporary root shell over USB. No licence file. Author attribution unclear (puckcv vs. orrpunk-art). |
| virtual-mpc-sample | Needs the user's own copy of Akai's proprietary firmware image (and factory content). Runs on a computer, not on the device. |
| Trackyard | Runs on a computer, not on the device; a companion to Beat-Train. Bundled model is non-commercial (CC BY-NC-SA 4.0). |
| mpc-sample-sdk | None. Developer audience only; no prebuilt download. |
| mpc-sample-tracker | None. |

## Ambiguities

1. **Category for host-side tools.** virtual-mpc-sample and Trackyard run on a computer. The Category list has no "desktop tool" value. dev-library (emulator) and app (Trackyard) are proposed; whether host-side companions belong in the catalogue at all is a policy call.
2. **Category for mpc-sample-root-ssh.** dev-library proposed; research is the alternative.
3. **Maturity for MPCTRACKER and virtual-mpc-sample.** Neither uses the word "beta". "Expect rough edges" and "young project" were read as beta. Read strictly, both are "unknown".
4. **mpc-sample-root-ssh Author.** README names puckcv (MPC-Forums); the repo is under orrpunk-art.
5. **mpc-sample-sdk release date.** No GitHub releases; the date given is the commit date of tag v0.5.3.

## Sources (accessed 2026-11-13)

- https://github.com/ioma8/mpc-sample-sdk (README, `docs/22-build-and-install.md`, tags, LICENSE)
- https://github.com/jeffwebb-to/mpc-sample-tracker (README, release v0.1.0)
- https://github.com/orrpunk-art/virtual-mpc-sample (README)
- https://github.com/orrpunk-art/mpc-sample-root-ssh (README, releases v1.1.0 and v1.2.0)
- https://github.com/drose030/trackyard (README, releases v1.0.0 to v1.2.0)
- GitHub REST API: `/repos/<o>/<r>`, `/repos/<o>/<r>/releases`, `/repos/<o>/<r>/tags`, `/repos/<o>/<r>/contents`, `/users/<login>` for each of the above
