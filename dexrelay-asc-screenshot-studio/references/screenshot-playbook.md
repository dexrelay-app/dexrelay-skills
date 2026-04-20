# Screenshot Playbook (ASC + Simulator)

## Goal

Produce repeatable, submission-safe App Store screenshots for iPhone + iPad, including light and dark variants, then upload to the current version localization.

## Device Targets

- iPhone upload target: `APP_IPHONE_65` (1242x2688 / 1284x2778)
- iPad upload target: `APP_IPAD_PRO_3GEN_129` (2048x2732 / 2064x2752)

## Fast Path

1. Build and capture:
   - `bash scripts/capture-ios-appstore-screenshots.sh ...`
2. Validate:
   - `asc screenshots validate --path <iphone_dir> --device-type APP_IPHONE_65`
   - `asc screenshots validate --path <ipad_dir> --device-type APP_IPAD_PRO_3GEN_129`
3. Upload:
   - resolve `version-localization id`
   - upload both sets with `--replace`

## Required ASC Calls

- Get version ID:
  - `asc versions list --app <APP_ID> --output table`
- Get localization ID:
  - `asc localizations list --version <VERSION_ID> --output json`
- Upload screenshots:
  - `asc screenshots upload --version-localization <LOC_ID> --path <DIR> --device-type <TYPE> --replace`

## Common Failure Patterns

- Simulator service mismatch after Xcode switch:
  - restart simulator services and retry.
- Missing iOS platform in active Xcode:
  - `xcodebuild -downloadPlatform iOS`
- Wrong ASC upload path mode:
  - use `--version-localization` for direct locale folder uploads.
- Path quoting issues on screenshot output:
  - prefer no-space temp roots (`/tmp/...`).
