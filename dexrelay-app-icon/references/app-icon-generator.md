---
name: ios-app-icon-generator
description: Generates a complete iOS app icon set with all required sizes. Use when asked to create an app icon, design an iOS icon, generate app store artwork, or make an icon for an iPhone/iPad app. Follows a philosophy-first approach - first defining the visual identity and concept, then producing production-ready icons.
---

# iOS App Icon Generator

Create beautiful, production-ready iOS app icons through a two-phase creative process.

## Phase 1: Visual Philosophy

Before drawing anything, develop a 2-3 paragraph `Icon Philosophy` that articulates:

- core concept
- visual metaphor
- color psychology
- silhouette test

### Design Principles

- Simplicity: one focal element, no more than 2-3 colors, no text.
- Distinctiveness: make it stand out in a crowded home screen.
- Scalability: the smallest icon should still read.
- No photography: favor illustration, geometry, or abstraction.
- Optical balance: center visual weight, not just geometry.

## Phase 2: Icon Generation

Generate the icon as a self-contained HTML artifact with embedded SVG when browser-based review is useful.

The artifact should:

1. render the master icon at `1024x1024`
2. include an iOS-style rounded mask or superellipse approximation
3. preview all required sizes
4. support exporting PNG outputs

## Required Sizes

Generate these iOS app icon sizes:

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

## Suggested HTML Artifact Structure

```html
<!DOCTYPE html>
<html>
<head>
  <title>App Icon: [Name]</title>
</head>
<body>
  <!-- Philosophy -->
  <!-- Master SVG -->
  <!-- Preview grid -->
  <!-- Export/download logic -->
</body>
</html>
```

## SVG Guidance

- Use `viewBox="0 0 1024 1024"`.
- Design for the iOS mask, not a plain square.
- Use gradients sparingly.
- Keep stroke widths large enough to survive scaling.

## Squircle Guidance

The iOS icon silhouette is not a plain rounded rectangle. Use a superellipse-style mask or a close approximation when generating previews.

## Process

1. Ask about app purpose, name, and brand colors.
2. Write the icon philosophy.
3. Present 2-3 concept directions only if exploration is needed.
4. Converge on one direction.
5. Generate the full icon set.
6. Iterate based on feedback.

## Quality Bar

Aim for something that could plausibly ship in a polished App Store app. Avoid glossy skeuomorphism, hairline detail, generic clip-art, or lazy centered-symbol-on-gradient solutions.
