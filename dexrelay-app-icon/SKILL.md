---
name: dexrelay-app-icon
description: Design, refine, and generate production-ready iOS app icon systems for iPhone and iPad apps. Use when creating a new app icon, redesigning an existing icon, building `AppIcon.appiconset` PNGs and `Contents.json`, defining an icon concept or philosophy, or checking whether an icon will read clearly at small iOS sizes and match the app's product/brand direction.
---

# DexRelay App Icon

## Overview

Create iOS app icons with a product-design workflow, not a one-off image export. Start from the app's purpose and visual identity, converge on one strong icon concept, then produce a complete `AppIcon.appiconset` that is ready for Xcode.

Keep the result Apple-appropriate: one dominant idea, strong silhouette, no tiny text, no decorative clutter, and consistent readability from `1024x1024` down to small settings/notification sizes.

When the user wants options, vary the icon by style family or metaphor instead of making small cosmetic tweaks to the same idea.

## Workflow

### 1. Establish the icon brief

Capture these inputs before drawing:

- app name
- app purpose
- current visual direction or brand theme
- existing colors to preserve or avoid
- whether the icon should feel editorial, playful, premium, technical, or utility-first

When the request is underspecified, write a short `Icon Brief` yourself with:

- concept
- visual metaphor
- palette
- constraints
- what must be avoided

### 2. Write the icon philosophy

Before generating assets, write 1-3 short paragraphs that define:

- the single idea the icon should communicate
- the main shape or metaphor
- why it will remain legible at small sizes
- how it connects to the app's existing interface and brand

This is not filler. It should drive the asset decisions.

If you need a fuller philosophy-first template or HTML preview approach, read [references/app-icon-generator.md](./references/app-icon-generator.md).

### 3. Choose one concept direction

Prefer one decisive direction over three weak ones. A strong iOS icon usually has:

- one focal symbol
- two or three colors at most
- a clear light/dark value structure
- a silhouette that still reads when mentally reduced to a black shape

Avoid:

- text labels inside the icon
- screenshots or photography
- thin linework
- generic gears, clouds, checkmarks, or default gradients unless the product truly warrants them

When the user asks for multiple options, vary one of these style families first:

- glyph: one symbolic mark with maximum reduction
- geometric: precise primitives with strong negative space
- monogram: one custom letterform when the brand truly depends on initials
- pictographic: simplified object or scene for consumer-facing products
- brutalist: stark, raw, high-contrast geometry for technical or indie tools
- gradient orb: restrained luminous depth for softer, expressive products

Default to `glyph` or `geometric` when the brief is ambiguous. They age better and survive reduction more reliably than decorative directions.

### 4. Produce the master icon

Create the icon at `1024x1024` first.

Use these rules:

- design for the iOS rounded icon mask, not a plain square
- keep the visual center optically balanced, not just geometrically centered
- leave enough breathing room around the main form so it does not choke at small sizes
- test whether the design still reads at roughly `32x32` and `20x20`
- keep the production mark to roughly `1-6` major shapes and `2-3` colors unless the brief clearly requires more

When the workflow calls for browser-based iteration or downloadable previews, follow the HTML/SVG artifact approach in [references/app-icon-generator.md](./references/app-icon-generator.md).

### 5. Export the iOS size set

Generate the required sizes for Xcode asset catalogs. At minimum, be prepared to supply:

- `1024x1024`
- `180x180`
- `167x167`
- `152x152`
- `120x120`
- `87x87`
- `80x80`
- `76x76`
- `60x60`
- `58x58`
- `40x40`
- `29x29`
- `20x20`

If the target project already has an `AppIcon.appiconset`, inspect its `Contents.json` and match the filenames and required slots instead of guessing.

When you already have a finished master `1024x1024` PNG, use `scripts/build_appiconset.py` to generate a complete `AppIcon.appiconset` folder with resized PNGs and a matching `Contents.json`.

### 6. Install into the app project

When applying the icon to a real iOS app:

1. Locate `Assets.xcassets/AppIcon.appiconset`
2. Replace or add the PNGs
3. Update `Contents.json` only if the filenames or required slots changed
4. Keep filenames simple and deterministic
5. Do not break existing idiom/scale mappings

### 7. Verify

Always verify with at least:

- asset catalog still resolves in Xcode
- app builds successfully
- icon looks balanced at small sizes
- icon matches the app's current UI direction
- the icon still communicates one clear idea at `29x29`

For project work, prefer an actual build over visual confidence alone.

## Output Rules

- State the chosen icon concept clearly.
- State the chosen style family when it meaningfully affects the result.
- Mention if the final design is an iteration of an existing icon rather than a full replacement.
- When you generate files, name the target `AppIcon.appiconset` path explicitly.
- If you are inferring missing brand direction, say so briefly.
- If the app UI already has a strong theme, make the icon feel like the same product family.

## Reference

- Use [scripts/build_appiconset.py](./scripts/build_appiconset.py) to turn a master `1024x1024` PNG into a complete Xcode-ready `AppIcon.appiconset`.
- Read [references/app-icon-generator.md](./references/app-icon-generator.md) when you need the longer philosophy-first workflow, required-size checklist, HTML artifact structure, or squircle guidance.
