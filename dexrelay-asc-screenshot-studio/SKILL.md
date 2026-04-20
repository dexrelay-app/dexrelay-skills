---
name: dexrelay-asc-screenshot-studio
description: Capture, curate, validate, and upload App Store screenshots for iOS apps using deterministic simulator fixtures plus ASC CLI. Use when producing high-quality light/dark iPhone+iPad screenshot sets for TestFlight/App Store metadata.
---

# DexRelay ASC Screenshot Studio

## Overview

Use this skill to produce repeatable, App Store-ready screenshot sets with correct dimensions and reliable ASC uploads. Prefer deterministic app fixtures over manual clicking.

This skill is optimized for this repo and calls:
- `scripts/capture-ios-appstore-screenshots.sh`

## Workflow

1. Verify toolchain and active Xcode.
   - `xcodebuild -version`
   - `xcrun --sdk iphoneos --show-sdk-version`
   - `asc --version`

2. Ensure simulator platform exists for the active Xcode.
   - `xcrun simctl list runtimes`
   - If missing desired runtime: `xcodebuild -downloadPlatform iOS`

3. Generate deterministic screenshot assets.
   - Run the script with explicit project/scheme/runtime.
   - Default script output:
     - raw captures under `.../raw`
     - curated App Store sets under `.../appstore/<locale>/iphone` and `.../ipad`

4. Validate dimensions before upload.
   - iPhone: `APP_IPHONE_65`
   - iPad: `APP_IPAD_PRO_3GEN_129`

5. Upload using version-localization targeting.
   - Resolve version ID and localization ID first.
   - Upload each device set with `--replace` if refreshing assets.

## Canonical Commands

Generate best set:

```bash
bash scripts/capture-ios-appstore-screenshots.sh \
  --project CodexRemote.xcodeproj \
  --scheme CodexRemote \
  --configuration Debug \
  --runtime "iOS 18.5" \
  --output-root /tmp/dexrelay-appstore-screenshots \
  --locale en-US
```

Resolve version and localization:

```bash
asc versions list --app 6761513011 --output table
asc localizations list --version <VERSION_ID> --output json
```

Upload iPhone + iPad sets:

```bash
asc screenshots upload \
  --version-localization <LOCALIZATION_ID> \
  --path /tmp/dexrelay-appstore-screenshots/appstore/en-US/iphone \
  --device-type APP_IPHONE_65 \
  --replace

asc screenshots upload \
  --version-localization <LOCALIZATION_ID> \
  --path /tmp/dexrelay-appstore-screenshots/appstore/en-US/ipad \
  --device-type APP_IPAD_PRO_3GEN_129 \
  --replace
```

## Quality Rules

- Prefer deterministic fixtures (`snapshot-main`, `snapshot-detail`) for stable composition.
- Capture both light and dark mode, then curate to the strongest ordered narrative set.
- Keep status bar clean and consistent (time/network/battery).
- Do not upload unvalidated dimensions.
- Use version-localization upload mode when uploading a single locale folder.

## Troubleshooting

- `CoreSimulatorService version mismatch`:
  - Kill stale simulator services and rerun.
- `Unable to find destination generic/platform=iOS Simulator`:
  - Download iOS platform with `xcodebuild -downloadPlatform iOS`.
- `no locale directories found` in app-scoped screenshot upload:
  - Use `--version-localization` mode for direct folder uploads.
- Paths with spaces can break `simctl io screenshot` in some flows:
  - Use a no-space output root such as `/tmp/dexrelay-appstore-screenshots`.

## References

- Read [references/screenshot-playbook.md](references/screenshot-playbook.md) for a compact execution checklist.
