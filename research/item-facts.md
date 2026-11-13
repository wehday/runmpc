# Item facts for the 20 seed Items

Research for [#2](https://gitea.wehday.com/wehday/run-mpc/issues/2). All sources accessed 2026-11-13.

Method: each Item's own README, release notes and site were read. Licence, last push, archived flag and releases come from the GitHub REST API (`/repos/<o>/<r>`, `/releases`). For repos where the API reports no licence, `LICENSE`, `LICENSE.md`, `LICENSE.txt` and `COPYING` were checked on the default branch. "unknown" means the Item's own page does not say. Nothing here is inferred from third-party write-ups.

Status rule: **active** = pushed within the last 30 days and no beta/experimental warning; **beta** = the Item's own page calls itself beta, alpha or experimental; **inactive** = no push for over a year (none of these repos has the GitHub "archived" flag set).

## Summary table

| Item | Author | Target devices | Firmware requirement | Install method | Licence | Status | Proposed Category |
|---|---|---|---|---|---|---|---|
| MPC-LiveXplore | TheKikGen | MPC Live / X / One, Force | Modded SSH images for MPC 2.14, MPC 3.4.2.13, Force 3.3.0; autorun hack "until 3.9" | Modded firmware image (USB update); bootstrap SD image flashed with Etcher | none (no licence file) | active (pushed 2026-11-11) | Research |
| MPCLiveXplore-libs | TheKikGen | MPC and Force | Needs an SSH-modded image; version unknown | LD_PRELOAD library run over SSH | CC0-1.0 | inactive (last push 2023-12-13) | Dev library |
| MPC-LiveXplore-bootstrap | TheKikGen | MPC and Force | Needs the modded image from MPC-LiveXplore; version unknown | Modded image, then `tkgl_bootstrap_[ProjectData]` folder on SD card / USB stick | none (no licence file) | inactive (last push 2023-11-30) | Boot / Firmware |
| HAKAI | medampire | MPC X / X SE, Live / II / III, One / One+ / One Gen2, XL, Key series; Force / Force II "soon" | unknown (release notes: "make sure your device and firmware version are compatible") | Per-release package for Gen1 or Gen2 with included instructions; exFAT storage | none (proprietary freeware; no redistribution) | active (release 2026-11-13) | Mod |
| mpc-boot-thingy | garrettjwilke | MPC Sample | unknown | USB web tool (`mpc-sample.local/testapp`) or `autoboot` folder on SD card | none (no licence file) | active (v1.1.1, 2026-11-11) | Boot / Firmware |
| open-mpc | open-mpc (GitHub org); maintainer unknown | Standalone MPC and Force (One+, X, Live, Live III, Force named) | Plugin Manager for MPC OS 3.10.1; installer zips for 3.9.1 and earlier | On-device OpenMPC Plugin Manager; device patches over SSH | unknown (site repo has no licence file) | active (pushed 2026-11-13) | Plugin |
| Melodee | Kerem Kiliç (Ellic Studio), keremimo | MPC Sample | 1.3.0.12 | SD card autorun | AGPL-3.0-only | active (v0.1.0, 2026-11-12) | App |
| Am MOD | AlekseyMalykh | MPC Sample | 1.3.0.12 | SD card autorun; Windows / Python installer | MIT | active (r29a, 2026-11-13) | Mod |
| SampQOL OS | Snare Bes (snarebes) | MPC Sample (One, Live, X "not tested yet") | 1.3.0 (1.3.0.12) | SD card autorun | proprietary freeware (custom LICENSE, all rights reserved) | beta (v0.2.0, 2026-11-08) | Mod |
| sample-base | Kerem Kiliç (Ellic Studio), keremimo | MPC Sample | 1.3.0.12 | SD card autorun (release zip) or SSH `device.py` | AGPL-3.0-only | active (v0.1.0, 2026-11-11) | Dev library |
| Gridzilla | The Sound Factory NJ | MPC Sample (page title) | unknown | unknown | unknown (page title says "Free Download") | unknown | unknown (see notes) |
| mpc-minimod | ioma8 | MPC Sample | 1.3.0.12 only | SD card autorun | none (no licence file) | active (v0.9.0, 2026-11-12) | Mod |
| kaosample-beta | Omar Huertas LLC / kaosbeatz | MPC Sample | 1.3.0.12 | SD card autorun | none (closed; "Don't re-upload the zip") | beta (v0.36-beta, 2026-11-07) | Mod |
| LoopPad | Lars Öholm (larsoholm) | MPC Sample | unknown | Via mpc-boot-thingy only; build from source (no binary releases) | MIT | beta ("alpha-quality", pushed 2026-11-05) | App |
| beat-train-mpc-sample | drose030 | MPC Sample | 1.3.0.x | SD card autorun (exFAT card) | MIT | active (v1.6, 2026-11-07) | Game |
| mpc-furnace | garrettjwilke | MPC Sample | unknown | SD card autorun or mpc-boot-thingy | none (no licence file) | active (v1.0.0, 2026-10-31) | App |
| mpc-gen1recomp | garrettjwilke | MPC Sample | unknown | SD card autorun or mpc-boot-thingy; SSH deploy | none (no licence file) | active (v1.0.1, 2026-11-11) | Game |
| mpc-cavestory | garrettjwilke | MPC Sample | unknown | SD card autorun or mpc-boot-thingy | none (no licence file) | active (v1.0.0, 2026-10-31) | Game |
| mpc-tic80 | garrettjwilke | MPC Sample | unknown | SD card autorun or mpc-boot-thingy | none (no licence file) | active (v1.0.0, 2026-10-31) | Game |
| mpc-sample-ui-toolkit | garrettjwilke | MPC Sample | unknown | Linked into apps; example zips via autorun or mpc-boot-thingy | CC0-1.0 | active (pushed 2026-11-10) | Dev library |

## Screenshots

Only images that appear on the Item's own page. Direct URLs checked to return an image.

| Item | Screenshot URL |
|---|---|
| Am MOD | https://raw.githubusercontent.com/AlekseyMalykh/am-mod/HEAD/docs/media/chords.gif |
| Melodee | https://raw.githubusercontent.com/keremimo/melodee-sample/HEAD/docs/images/melodee-promo.png |
| mpc-minimod | https://raw.githubusercontent.com/ioma8/mpc-minimod/HEAD/docs/images/menu.png |
| beat-train-mpc-sample | https://raw.githubusercontent.com/drose030/beat-train-mpc-sample/HEAD/docs/images/library.png |
| HAKAI | banner only, not a screenshot: https://raw.githubusercontent.com/medampire/HAKAI/HEAD/assets/HAKAI_Banner.png |
| MPC-LiveXplore | only YouTube video thumbnails (e.g. https://img.youtube.com/vi/Ivp53UNk8ck/0.jpg for IamForce2) |
| all others | none on the Item's page |

## Per-Item notes

### MPC-LiveXplore
- Repo: https://github.com/TheKikGen/MPC-LiveXplore
- A research and news log plus wiki: SSH-enabled firmware images, IamForce, VNC4MPC, autorun hack, hardware ID findings. Downloads are hosted on Google Drive, not in the repo.
- Firmware facts are per hack: SSH images for "Force 3.3.0, MPC 2.14" and "MPC 3.4.2.13"; "Autorun Hack (until 3.9 version)".
- No licence file. The repo is a hub for several things; it could also be split into separate Items (IamForce2, SSH images).

### MPCLiveXplore-libs
- Repo: https://github.com/TheKikGen/MPCLiveXplore-libs (CC0-1.0)
- LD_PRELOAD libraries: tkgl_midimapper (and IamForce2 plugins), tkgl_anyctrl, tkgl_ctrldump. "You need SSH images update to use these libraries." Build needs glibc 2.30 and an ARM cross toolchain.

### MPC-LiveXplore-bootstrap
- Repo: https://github.com/TheKikGen/MPC-LiveXplore-bootstrap
- Boot-time module launcher (rtpmidid, iamforce2, vnc4mpc, smbnetfs, arp_overlay...). Requires the modded image; copy `tkgl_bootstrap_[ProjectData]` to SD card / USB stick (ext4 preferred), or burn a ready-made image from Google Drive.

### HAKAI
- Repo / releases: https://github.com/medampire/HAKAI/releases
- Distribution-only repo: "Source code for proprietary HAKAI components is not publicly distributed." Free; donations via Ko-fi (`hakaidev`).
- Releases ship `HAKAI_Gen1_MPC_*.zip` ("first-generation Akai MPC & Force") and `HAKAI_Gen2_MPC_*.zip` ("second-generation Akai MPC"). v2026-11-13 notes require exFAT storage.
- No firmware version stated: "Compatibility may vary depending on hardware and firmware versions."
- Contents are described only as "ready-to-use payloads", "custom applications, plugins, tools and system enhancements". Category Mod is the best fit but contents are not itemised.

### mpc-boot-thingy
- Repo: https://github.com/garrettjwilke/mpc-boot-thingy
- Boot menu for the MPC Sample that lets several autorun apps and mods coexist. Install: USB web tool at `mpc-sample.local/testapp` / `192.168.155.1/testapp`, or copy the `autoboot` folder to the SD card. Apps go into `autorun/apps/` as zips or through its web tool.
- README links a YouTube video only (no embedded image).
- Its README lists other apps not in the seed list: `jeffwebb-to/mpc-sample-tracker`.

### open-mpc
- Site: https://open-mpc.github.io/index.html ; repo https://github.com/open-mpc/open-mpc.github.io
- A community plugin catalogue and Plugin Manager for MPC OS, not a single plugin. The catalogue data is a copy of `sd88me/mpc-vst-plugins`. Individual plugins are credited to sd88me, mmiroshnikov, Retroloop USA / IAMTHEBAND LLC, Padbangers.
- Plugin Manager is described for MPC OS 3.10.1; other installer zips for 3.9.1 and earlier. Device patches run as root shell scripts over SSH.
- The only image on the page is for the MPC Link companion app, not OpenMPC, so no screenshot is recorded.

### Melodee
- Repo: https://github.com/keremimo/melodee-sample (AGPL-3.0-only; boot animation logo excluded)
- 16-track groovebox that replaces the stock app; VST3/VST2/Open MPC plug-in host. Built on sample-base. "On any other firmware Melodee does not start."

### Am MOD
- Repo: https://github.com/AlekseyMalykh/am-mod (MIT)
- Patches a RAM copy of the stock app; checks the app's SHA-256 and refuses other firmware. Card must be exFAT (FAT32 experimental from r26e). Windows installer `.exe` and a Python installer. Many features marked "trial" (not yet hardware-checked).

### SampQOL OS
- Repo: https://github.com/snarebes/SampQOL-OS ; manual https://snarebes.github.io/SampQOL-OS/
- "This is beta software." Closed source; "freeware, not open source"; "Do not upload or share the zip". Also distributed via beatops.io.

### sample-base
- Repo: https://github.com/keremimo/sample-base (AGPL-3.0-only)
- JUCE 9 application base for MPC Sample AC50 1.3.0.12, with demos. Melodee is built on it. Release zip is the demos; the main audience is developers.

### Gridzilla
- Page: https://www.thesoundfactorynj.com/gridzilla
- The page is a Wix site that renders little text without JavaScript. Fetched content gives only the title "GRIDZILLA for MPC Sample | "Free Download" | The Sound Factory NJ", no download link, no version, no install steps. The fetch summariser described it as a "sample pack"; mpc-boot-thingy's README describes it as "modern daw-like sequencing UI/UX...super custom workflow". These conflict, so Category is left unknown. Needs a manual browser check.
- No product image identified.

### mpc-minimod
- Repo: https://github.com/ioma8/mpc-minimod
- Small mod (AutoTrim, octave shift, HPSS, Spectral Chop, Live Looper). Built on the same author's `ioma8/mpc-sample-sdk` (a candidate Dev library Item). No licence file.

### kaosample-beta
- Repo: https://github.com/omarhuertasllc-ops/kaosample-beta
- "Beta. Not fully tested on real hardware yet." Runs in RAM from the `autorun` folder; switches itself off on other firmware. Repo has "no Akai firmware and no source code". Releases are GitHub pre-releases with a PDF user guide.

### LoopPad
- Repo: https://github.com/larsoholm/LoopPad (MIT)
- "alpha-quality community software"; v0.6.0 line in development. No binary releases: the README says redistribution waits on mpc-ui-toolkit licence clarity. Requires mpc-boot-thingy for recovery because it has no exit/power-off of its own.

### beat-train-mpc-sample
- Repo: https://github.com/drose030/beat-train-mpc-sample (MIT)
- Drum game using Clone Hero song folders. Copy `autorun` and `BeatTrain` folders to an exFAT card.

### mpc-furnace
- Repo: https://github.com/garrettjwilke/mpc-furnace
- No README; description "furnace tracker for the MPC Sample". Release v1.0.0 notes: "Copy that folder to the card, or add the zip with mpc-boot-thingy." Furnace is a chiptune tracker, so Category App.

### mpc-gen1recomp
- Repo: https://github.com/garrettjwilke/mpc-gen1recomp
- Native Pokémon Red/Blue/Yellow runtime. Ships no ROMs; the user supplies them over USB storage mode.

### mpc-cavestory
- Repo: https://github.com/garrettjwilke/mpc-cavestory
- Port of doukutsu-rs. The user supplies the Cave Story `data/` folder at build time; release v1.0.0 has a zip. README links `github.com/home-less/mpc-boot-thingy`, not `garrettjwilke/mpc-boot-thingy`.

### mpc-tic80
- Repo: https://github.com/garrettjwilke/mpc-tic80
- No README; description "play tic80 games on your MPC Sample". Release v1.0.0 has the same autorun / boot-thingy note as mpc-furnace.

### mpc-sample-ui-toolkit
- Repo: https://github.com/garrettjwilke/mpc-ui-toolkit (the issue calls it "mpc-sample-ui-toolkit"; the repo is `mpc-ui-toolkit`)
- C drawing and widget library for the 320×240 panel, plus autorun packaging script. GitHub reports CC0-1.0 now; LoopPad's README says the version it used had no explicit licence, so the licence was likely added recently.

## Cross-cutting findings

- **Target devices split in two.** 15 Items are MPC Sample only (firmware 1.3.0.12 where stated). 5 Items (MPC-LiveXplore, -libs, -bootstrap, HAKAI, open-mpc) target the Linux MPC OS / Force line.
- **Licence gaps.** 11 Items have no licence file (mpc-boot-thingy, mpc-furnace, mpc-gen1recomp, mpc-cavestory, mpc-tic80, MPC-LiveXplore, MPC-LiveXplore-bootstrap, HAKAI, open-mpc, mpc-minimod, kaosample-beta). Gridzilla's licence is unknown. 3 are closed freeware with redistribution limits (HAKAI, SampQOL OS, kaosample-beta). Only 7 have an open licence: MIT (Am MOD, LoopPad, beat-train), AGPL-3.0-only (Melodee, sample-base), CC0-1.0 (MPCLiveXplore-libs, mpc-ui-toolkit).
- **Copyrighted game data.** mpc-gen1recomp and mpc-cavestory require user-supplied commercial game data.
- **Not single Items.** open-mpc is itself a catalogue and plugin manager; MPC-LiveXplore is a hub for several hacks.
- **Candidates found along the way** (not researched): `ioma8/mpc-sample-sdk`, `jeffwebb-to/mpc-sample-tracker`, `orrpunk-art/virtual-mpc-sample`, `orrpunk-art/mpc-sample-root-ssh`, `drose030/trackyard`.

## Sources (accessed 2026-11-13)

- https://github.com/TheKikGen/MPC-LiveXplore
- https://github.com/TheKikGen/MPCLiveXplore-libs
- https://github.com/TheKikGen/MPC-LiveXplore-bootstrap
- https://github.com/medampire/HAKAI and https://github.com/medampire/HAKAI/releases
- https://github.com/garrettjwilke/mpc-boot-thingy and https://github.com/garrettjwilke/mpc-boot-thingy/releases
- https://open-mpc.github.io/index.html and https://github.com/open-mpc/open-mpc.github.io
- https://github.com/keremimo/melodee-sample
- https://github.com/AlekseyMalykh/am-mod
- https://github.com/snarebes/SampQOL-OS (README and LICENSE)
- https://github.com/keremimo/sample-base
- https://www.thesoundfactorynj.com/gridzilla
- https://github.com/ioma8/mpc-minimod
- https://github.com/omarhuertasllc-ops/kaosample-beta
- https://github.com/larsoholm/LoopPad
- https://github.com/drose030/beat-train-mpc-sample
- https://github.com/garrettjwilke/mpc-furnace and https://github.com/garrettjwilke/mpc-furnace/releases
- https://github.com/garrettjwilke/mpc-gen1recomp
- https://github.com/garrettjwilke/mpc-cavestory
- https://github.com/garrettjwilke/mpc-tic80 and https://github.com/garrettjwilke/mpc-tic80/releases
- https://github.com/garrettjwilke/mpc-ui-toolkit
- GitHub REST API `https://api.github.com/repos/<owner>/<repo>` and `/releases` for each repo above
