# MPC hardware generations and Target device ids

Resolves [#11](https://github.com/wehday/runmpc/issues/11). Researched 2026-11-13.

## Answer in one paragraph

Akai itself splits standalone MPCs into two hardware generations. **Gen 1** is "MPC X · MPC X SE · MPC Live · MPC Live II · MPC One · MPC One+ · MPC Key 37 · MPC Key 61" [A1]. Community Authors add the **Force** to Gen 1, because it is the same 32-bit ARM platform [O1, H2]. **Gen 2** is the 64-bit, "Gen 2 8-core processor" line: MPC Live III, MPC XL, MPC One G2 and MPC Key 37 G2. Akai files all four under its "MPC > G2" collection [A2, A3]. The **MPC Sample** is a separate product with its own firmware (1.x, not MPC OS 3.x) [A4], so it belongs to neither generation. Akai has not released a Force successor: no "Force II" exists on akaipro.com [A2].

## Sources

Akai (first party):

- **A1**: "Legacy MPC Firmware (Gen 1)" entry on akaipro.com (`/mpcfirmwarelegacy.html`). Description: "Includes support for Generation One Hardware: MPC X · MPC X SE · MPC Live · MPC Live II · MPC One · MPC One+ · MPC Key 37 · MPC Key 61". The download files are named `MPC-3.x.x-Gen1-Update.img`.
- **A2**: the akaipro.com product catalogue, read from the site's Gatsby static data (`https://www.akaipro.com/page-data/sq/d/2008607954.json`, `allBuilderModels`). Each product has a name, URL, category path and `releaseDateValue`. These products carry the category `Products > Collections > MPC > G2`: MPC Key 37 G2, MPC ONE G2, MPC XL and MPC Live III. Force has no successor product in it.
- **A3**: product page data (`https://www.akaipro.com/page-data/<slug>/page-data.json`):
  - `mpc-xl`: "Powered by a new Gen 2 8-core processor with 16GB of RAM, MPC XL delivers four times the performance of previous MPCs."
  - `mpc-live-3`: "8-core processor with 8GB RAM", "Second Generation portable drum sampler".
  - `mpc-one-g2`: "The MPC for Beatmakers: Generation 2", "four times the processing performance of MPC One+".
  - `mpc-key-37-g2`: "The MPC for PLAYERS: Generation 2".
- **A4**: the MPC Sample has its own firmware line: "MPC Sample Firmware Updater 1.2.1" and "MPC Sample 1.3 Release Notes" on its product entry [A2].
- **A5**: "Legacy MPC Firmware (Gen 2)" entry (`/legacy-gen-2`). Description: "Includes support for Generation Two Hardware : MPC LIVE III". The files are named `MPC-3.x.0-Gen2-Update.img` (3.6 to 3.9). This entry predates the XL, One G2 and Key 37 G2 firmware listing.
- **A6**: [MPC 3.9.1 Release Notes](https://cdn.inmusicbrands.com/Software/MPC/MVSU391APC/MPC%203.9.1%20-%20Release%20Notes.pdf), Compatibility: "This release is for MPC Key 37 G2, MPC One G2, MPC XL, MPC Live III, MPC Key 37, MPC One+, MPC X Special Edition, MPC Key 61, MPC One, MPC Live II, MPC X, MPC X SE, MPC Live and Force (standalone only)."

Items (Author wording):

- **H1**: [HAKAI README](https://github.com/medampire/HAKAI), "Supported Devices".
- **H2**: [HAKAI releases](https://github.com/medampire/HAKAI/releases): v2026-11-09, v2026-11-12 and v2026-11-13 release notes. Also the shell scripts inside `HAKAI_Gen1_MPC_2026-11-13.zip` and `HAKAI_Gen2_MPC_2026-11-13.zip`, read by remote zip listing without downloading the payload.
- **K1**: [MPC-LiveXplore README](https://github.com/TheKikGen/MPC-LiveXplore).
- **K2**: [MPCLiveXplore-libs `src/tkgl_midimapper.c`](https://github.com/TheKikGen/MPCLiveXplore-libs/blob/main/src/tkgl_midimapper.c), `DeviceInfoBloc[]`. Also the [libs README](https://github.com/TheKikGen/MPCLiveXplore-libs) and the [bootstrap README](https://github.com/TheKikGen/MPC-LiveXplore-bootstrap).
- **O1**: [open-mpc FAQ](https://open-mpc.github.io/faq.html), "Gen1 or Gen2 build?".
- **O2**: [open-mpc catalogue](https://open-mpc.github.io/), the tested-device strings embedded in the page.
- **S1**: [SampQOL OS README](https://github.com/snarebes/SampQOL-OS).

## 1. Model list for `data/devices.json`

Colourway and bundle editions are not listed as separate devices: MPC One Retro Edition, MPC Live II BeatClub Edition, MPC Live II Retro and MPC Live III Retro. Each is the same hardware as its base model and should map to the base id. MPC Studio, Touch, Renaissance and older models are controllers or pre-standalone hardware, so they are left out.

```json
[
  { "id": "mpc-live",       "label": "MPC Live",       "family": "mpc-standalone" },
  { "id": "mpc-x",          "label": "MPC X",          "family": "mpc-standalone" },
  { "id": "force",          "label": "Force",          "family": "force" },
  { "id": "mpc-one",        "label": "MPC One",        "family": "mpc-standalone" },
  { "id": "mpc-live-ii",    "label": "MPC Live II",    "family": "mpc-standalone" },
  { "id": "mpc-key-61",     "label": "MPC Key 61",     "family": "mpc-standalone" },
  { "id": "mpc-x-se",       "label": "MPC X SE",       "family": "mpc-standalone" },
  { "id": "mpc-one-plus",   "label": "MPC One+",       "family": "mpc-standalone" },
  { "id": "mpc-key-37",     "label": "MPC Key 37",     "family": "mpc-standalone" },
  { "id": "mpc-live-iii",   "label": "MPC Live III",   "family": "mpc-standalone" },
  { "id": "mpc-xl",         "label": "MPC XL",         "family": "mpc-standalone" },
  { "id": "mpc-sample",     "label": "MPC Sample",     "family": "mpc-sample" },
  { "id": "mpc-one-g2",     "label": "MPC One G2",     "family": "mpc-standalone" },
  { "id": "mpc-key-37-g2",  "label": "MPC Key 37 G2",  "family": "mpc-standalone" }
]
```

### Generation, platform and dates

"Akai date" is the `releaseDateValue` from akaipro.com's catalogue [A2]. It is a CMS field, and for some products it looks like a page-publish date rather than a ship date. For example, MPC Live II shows 2020-05-01 and MPC XL shows 2026-01-20, the same day as both legacy-firmware entries. Treat it as an approximate year. Where Akai gives no date (legacy product pages), the year column is marked *not stated by Akai*.

| id | Akai name | Generation (source) | Platform | Akai date | Community product code [K2, H2] |
|---|---|---|---|---|---|
| mpc-live | MPC Live | Gen 1 [A1] | 32-bit ARM (armv7l), RK3288 per [K1] | not stated by Akai (legacy page) | ACV8 |
| mpc-x | MPC X | Gen 1 [A1] | same | not stated by Akai (legacy page) | ACV5 |
| force | Force | Gen 1 by community usage [O1, H2]; Akai's Gen 1 list [A1] covers MPCs only | 32-bit ARM; `armv7l` kernel output in [K1] | 2019-02-01 | ADA2 |
| mpc-one | MPC One | Gen 1 [A1] | 32-bit ARM | not stated by Akai (legacy page) | ACVA |
| mpc-live-ii | MPC Live II | Gen 1 [A1] | 32-bit ARM | 2020-05-01 | ACVB |
| mpc-key-61 | MPC Key 61 | Gen 1 [A1] | 32-bit ARM | 2022-06-23 | ACVM |
| mpc-x-se | MPC X Special Edition | Gen 1 [A1] | 32-bit ARM | 2023-04-26 | uncertain (ACV5S or ACVC, see ambiguities) |
| mpc-one-plus | MPC One+ | Gen 1 [A1] | 32-bit ARM (open-mpc lists a One+ test as armv7l [O2]) | 2023-05-30 | probably ACVA2, unconfirmed |
| mpc-key-37 | MPC Key 37 | Gen 1 [A1] | 32-bit ARM | 2024-02-06 | ACVR [K1] |
| mpc-live-iii | MPC Live III | Gen 2 [A5, A2] | 64-bit ARM (aarch64) [O1, H2], "8-core processor with 8GB RAM" [A3] | 2025-10-02 | not stated |
| mpc-xl | MPC XL | Gen 2 [A2, A3] | "Gen 2 8-core processor", 16 GB RAM [A3]; 64-bit [O1] | 2026-01-20 (see note) | uncertain (ACV5S or ACVC) |
| mpc-sample | MPC Sample | neither: own firmware 1.x [A4] | not stated by Akai | 2026-03-24 | not stated |
| mpc-one-g2 | MPC ONE G2 | Gen 2 [A2, A3] | 64-bit [O1]; "4x MPC One+" [A3] | 2026-06-18 | not stated |
| mpc-key-37-g2 | MPC Key 37 G2 | Gen 2 [A2, A3] | 64-bit [O1] | 2026-06-18 | not stated |

Akai does not name the SoC on any product page or in the release notes I read. "RK3288" comes from TheKikGen [K1], who expected the then-unreleased Force keyboard to use "the RK3288-based hardware core" shared by the MPC/Force range, and "Gen 2 8-core" is Akai's own wording [A3]. The 32-bit/64-bit split comes from open-mpc [O1] and HAKAI's scripts [H2]: the Gen1 runtime is "ARMv7" and the Gen2 VST payloads are "Gen2/AArch64".

Possible schema addition, not asked for: a `generation` field (`gen1`, `gen2`, or null for MPC Sample). It would let the site expand "Gen1" and "Gen2" phrases without hard-coding lists.

## 2. Phrase-to-device mapping for the seed Items

### HAKAI (medampire/HAKAI)

| Author wording | Where | Device ids |
|---|---|---|
| "HAKAI – Gen1 MPC & Force: For supported first-generation Akai MPC & Force standalone devices." | release notes v2026-11-12 and v2026-11-13 [H2] | mpc-live, mpc-live-ii, mpc-x, mpc-x-se, mpc-one, mpc-one-plus, mpc-key-37, mpc-key-61, force |
| "HAKAI – Gen2 MPC: For supported second-generation Akai MPC standalone devices." | same [H2] | mpc-live-iii, mpc-xl, mpc-one-g2, mpc-key-37-g2 |
| "MPC X / MPC X SE" | README Supported Devices [H1] | mpc-x, mpc-x-se |
| "MPC Live / Live II / Live III" | [H1] | mpc-live, mpc-live-ii, mpc-live-iii |
| "MPC One / One+ / One Gen2" | [H1] | mpc-one, mpc-one-plus, mpc-one-g2 |
| "MPC XL" | [H1] | mpc-xl |
| "MPC Key series" | [H1] | mpc-key-37, mpc-key-61, mpc-key-37-g2 (ambiguous, see below) |
| "Akai Force / Force II (both soon)" | [H1] | force only, and marked "soon" in the README. Force II is not a released product, so it gets no id. |

HAKAI's own wording conflicts on Force, and the sources disagree:

- v2026-11-09 says "HAKAI – Gen1 FORCE: Coming soon!"
- v2026-11-12 and later say "Gen1 MPC & Force".
- The README still says "Force / Force II (both soon)".
- The asset is still named `HAKAI_Gen1_MPC_*.zip`.

Recommendation: list `force` with a "per release notes from v2026-11-12" note, or hold it until the README agrees.

"Gen 2" here means Akai's Gen 2, not a firmware major version. HAKAI's Gen2 deploy script targets stock MPC OS 3.10.1 only ("HAKAI 3.10.1 stock-firmware deploy path") and ships "Gen2/AArch64 VST payloads". A code comment in the Gen2 script names product codes ACVC/ACV5/ACV5S as "X / X SE / XL", and both scripts branch on that same set of codes (for screen rotation).

### MPC-LiveXplore family (TheKikGen)

| Author wording | Where | Device ids |
|---|---|---|
| "Akai MPC Live / X / Force / One technical explorations and hacks" | MPC-LiveXplore README title and repo description [K1] | mpc-live, mpc-x, force, mpc-one (literal reading) |
| "Special libraries and code for MPC and Force devices" | libs README [K2] | see the code table below |
| "MPC / Force bootstrap scripts", "Bootstrap for Akai MPCs and Force" | bootstrap README and description [K2] | same as libs |

The libs code recognises these product codes in `DeviceInfoBloc[]` [K2]: ACV5 "MPC X", ACV8 "MPC Live", ADA2 "Force", ACVA "MPC One", ACVB "MPC Live 2", ACVM "MPC Keys 61", ACV5S "MPC XL" and ACVA2 "MPC ONE 2". With firm ids that gives mpc-x, mpc-live, force, mpc-one, mpc-live-ii and mpc-key-61. ACV5S and ACVA2 were added before the retail products were named, so their mapping to mpc-x-se, mpc-xl or mpc-one-plus is a guess (see ambiguities).

Everything TheKikGen ships is Gen 1, 32-bit only. The libs were last pushed 2023-12-13 and the bootstrap 2023-11-30, before any Gen 2 hardware existed. The newest SSH image in the README is for MPC 3.4.2, and the autorun hack is "until 3.9 version". Recommended mapping for all three Items: mpc-live, mpc-live-ii, mpc-x, mpc-one, mpc-key-61, force. Adding mpc-x-se, mpc-one-plus or mpc-key-37 would need a test report; the README never names them.

### open-mpc (open-mpc.github.io)

| Author wording | Where | Device ids |
|---|---|---|
| "Gen1 (32-bit): Live, Live II, One, X, Key 61/37, and the Force." | FAQ "Gen1 or Gen2 build?" [O1] | mpc-live, mpc-live-ii, mpc-one, mpc-x, mpc-key-61, mpc-key-37, force |
| "Gen2 (64-bit): Live III, One G2, Key G2, XL." | [O1] | mpc-live-iii, mpc-one-g2, mpc-key-37-g2, mpc-xl ("Key G2" can only be the Key 37 G2; no Key 61 G2 exists [A2]) |
| "Verified (Gen1, Gen2 or MPC Sample)", "MPC / Force" and "MPC Sample" catalogue tabs | FAQ and catalogue [O1, O2] | the MPC Sample is a third tier: mpc-sample |
| "One+, X, Live, Live III, Force" (the ticket's phrase) | matches the tested-device strings in the catalogue [O2]: "MPC One+", "Akai MPC X", "MPC Live", "MPC Live III (Gen2)", "Akai Force" | mpc-one-plus, mpc-x, mpc-live, mpc-live-iii, force |

The FAQ's Gen1 list leaves out One+ and X SE, which Akai classes as Gen 1 [A1]. The catalogue does record a One+ test ("MPC One+ 3.10.0.49 ... (armv7l)") [O2]. For a whole-catalogue Item like open-mpc, the Target devices should be the full Gen1 + Gen2 + Sample set. Per-plugin devices come from each plugin's tested data.

### SampQOL OS (snarebes/SampQOL-OS)

| Author wording | Where | Device ids |
|---|---|---|
| "SampQOL OS is a free mod for the Akai Professional MPC Sample." "Tested only with MPC Sample firmware 1.3.0 (full version number 1.3.0.12)." | README [S1] | mpc-sample |
| "MPC One, Live and X are not tested yet." | README [S1] | none. This is a statement that something is untested, not a claim of support. The MPC One, Live and X also run MPC OS 3.x, a different firmware from the MPC Sample's 1.3.0 [A4]. The sentence does not say which generation it means. |

## Ambiguities (not guessed)

1. **Product codes ACV5S, ACVC and ACVA2.** TheKikGen labelled ACV5S "MPC XL" in December 2022, from a firmware string [K1, K2]. The retail MPC XL only appeared in Akai's catalogue in 2026, and the MPC X SE in 2023. HAKAI's comment lists "X / X SE / XL" against ACVC|ACV5|ACV5S without pairing them [H2]. ACVA2 ("MPC ONE 2" in [K2]) is probably the One+, but no source confirms it. The codes are not needed for `devices.json`, so the table marks them uncertain.
2. **Release years.** Akai's `releaseDateValue` is a CMS field and some values look like publish dates (Live II, XL). Akai gives no date for MPC X, MPC Live or MPC One, whose pages are legacy. Firmware release notes do not state launch dates either. If exact years are needed, they need a separate source, such as Akai press releases or launch-day firmware notes.
3. **"MPC X SE" vs "MPC X Special Edition".** Akai's 3.9.1 notes list both names in one compatibility sentence [A6]. Akai's catalogue has only one product, "MPC X Special Edition" (`/mpc-x-se`) [A2]. Treated as one device.
4. **Force's generation.** Akai's "Generation One Hardware" list [A1] covers MPCs only. Grouping the Force with Gen1 comes from the Authors [O1, H2], based on its shared 32-bit platform. Akai ships Force firmware as a separate updater line [A2].
5. **HAKAI "MPC Key series"** does not say whether the Key 37 G2 is covered. The Gen2 package's release text ("second-generation Akai MPC") would include it by Akai's definition, but the README does not list it.
6. **HAKAI Force support** conflicts between the README and the release notes (see above).
7. **SampQOL "One, Live and X"**: the generation is unspecified, and the hardware runs different firmware. Not mapped.
