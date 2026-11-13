# RunMPC — Logo Guidelines

## 1. The logo
- **Idea:** in "run", the **u** and **n** share a stem and form one continuous **sine wave**, so the name carries a sound wave. The wave in Signal Orange is the brand's one recognisable detail.
- **Construction:** custom monoline lowercase lettering. It uses circles and straight stems only, with flat terminals and a 1.5 % overshoot on round forms. Every file is drawn as outlines, so no font is needed.
- **Versions:**
  - **Wordmark** (primary): `runmpc-wordmark-*.svg`
  - **Stacked** (square spaces): `runmpc-stacked-*.svg`
  - **Symbol**, the wave alone (favicon, avatar, app icon): `runmpc-symbol-*.svg`
  - **Small cut**, a heavier wave for 16–32 px: `runmpc-symbol-small.svg` / `favicon.*`
- **Colour variants of each version:**
  - `-color`: ink and orange, for light backgrounds
  - `-reversed`: white and orange, for dark backgrounds, drawn slightly thinner
  - `-black` and `-white`: one-colour versions

## 2. Clear space
Let **x** be the x-height of the wordmark, which is the height of the wave.
- Around the wordmark and stacked logo, keep at least **½ x** clear on every side.
- Around the symbol, keep at least **¼ of its width** clear.

The clear zone scales with the logo.

## 3. Minimum size
| Version | Screen | Print |
|---|---|---|
| Wordmark | 88 px wide | 22 mm wide |
| Stacked | 64 px wide | 16 mm wide |
| Symbol | 24 px (16–23 px: use the small cut / `favicon.*`) | 5 mm |

## 4. Colour
| Name | Use | HEX | RGB | CMYK (approx.) | Pantone (nearest) |
|---|---|---|---|---|---|
| **Signal Orange** | the wave, accents, brand surfaces | #FF4B2B | 255 75 43 | 0 80 85 0 | Warm Red C |
| **Studio Black** | wordmark, text, dark surfaces | #0E0E12 | 14 14 18 | 60 40 40 100 (rich black) | Black 6 C |
| **Text Orange** | orange text and links on light backgrounds | #CC3618 | 204 54 24 | 0 85 95 10 | 7597 C |
| **Paper** | light backgrounds | #F6F5F1 | 246 245 241 | 2 2 4 0 | — |
| **White** | | #FFFFFF | 255 255 255 | 0 0 0 0 | — |

The CMYK and Pantone values are approximations. Check them against a printed swatch before you print.

**Contrast (WCAG):**
- Studio Black on white: 19.3:1
- Signal Orange on Studio Black: 5.8:1
- Signal Orange on white: 3.3:1. That's fine for the logo and large graphics, but not for body text. Use Text Orange (#CC3618, 5.1:1) for orange text instead.

**Approved logo and background pairs:**
- colour logo on white or Paper
- reversed logo on Studio Black
- white logo on Signal Orange
- black logo on white

On photos, put the white or black logo on a calm area. Never put the orange logo on orange.

## 5. Typography (companion fonts for the site)
The logo is custom lettering, so don't recreate it by typing it.
- **Headlines:** Manrope, Bold or ExtraBold
- **Body and UI:** Inter, Regular, Medium or Semibold
- **Web fallback:** `system-ui, -apple-system, "Segoe UI", sans-serif`

Both fonts use the SIL Open Font License, which allows free commercial use.

## 6. Don'ts
- Don't stretch, squash or rotate it.
- Don't recolour the wave, or the letters, outside the palette.
- Don't put the orange wave on an orange background.
- Don't add shadows, outlines, gradients or effects.
- Don't respace or rearrange the letters, or swap the wave for a normal "un".
- Don't type "runmpc" in a font to stand in for the logo.
- Don't place it on busy images without a calm area or a container.

## 7. Files
- **Masters:** `final/export/*.svg`
- **Screen PNGs:** `final/export/*-1200.png`, `*-1000.png`, `*-512.png` and `*-1024.png`
- **Web icons:**
  - `favicon.ico`, `favicon.svg` and `favicon-16/32/48.png`
  - `apple-touch-icon.png`, `icon-192/512.png` and `maskable-512.png`
  - `site.webmanifest`
  - `head-snippet.html`, which you paste into `<head>`
- **Rebuild everything:** `python3 final/build_final.py`
