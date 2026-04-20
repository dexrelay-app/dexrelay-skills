# ASC Deploy Map

## Sources

- Homepage: `https://asccli.app/`
- Main repo: `https://github.com/rudrankriyam/App-Store-Connect-CLI`
- Upstream skills repo: `https://github.com/rudrankriyam/app-store-connect-cli-skills`
- Apple build upload guide: `https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds`

Validated against:
- installed `asc --help` and subcommand help on this Mac
- current public homepage/docs surface at `https://asccli.app/`
- current Apple upload/distribution help

## Install and Auth

Install:

```bash
brew install asc
```

```bash
curl -fsSL https://asccli.sh/install | bash
```

Authenticate:

```bash
asc auth login \
  --name "MyApp" \
  --key-id "KEY_ID" \
  --issuer-id "ISSUER_ID" \
  --private-key /path/to/AuthKey.p8
```

Check auth:

```bash
asc auth status
asc auth doctor
```

Useful env vars:
- `ASC_APP_ID`
- `ASC_KEY_ID`
- `ASC_ISSUER_ID`
- `ASC_PRIVATE_KEY_PATH`
- `ASC_PRIVATE_KEY`
- `ASC_PRIVATE_KEY_B64`
- `ASC_DEFAULT_OUTPUT`
- `ASC_TIMEOUT` or `ASC_TIMEOUT_SECONDS`
- `ASC_UPLOAD_TIMEOUT` or `ASC_UPLOAD_TIMEOUT_SECONDS`
- `ASC_BYPASS_KEYCHAIN`

## Discovery Commands

Use these before mutation:

```bash
asc apps list --bundle-id "<BUNDLE_ID>"
asc apps view --id "<APP_ID>"
asc builds list --app "<APP_ID>" --output table
asc builds info --app "<APP_ID>" --latest --platform IOS
asc testflight groups list --app "<APP_ID>" --output table
asc encryption declarations list --app "<APP_ID>" --output table
```

Use help as the source of truth:

```bash
asc --help
asc publish --help
asc builds upload --help
asc testflight groups --help
asc signing fetch --help
xcodebuild -help
asc workflow --help
```

## High-Level Release Commands

TestFlight:

```bash
asc publish testflight \
  --app "<APP_ID>" \
  --ipa "/path/to/App.ipa" \
  --group "<GROUP_ID_OR_NAME>" \
  --wait
```

App Store upload:

```bash
asc publish appstore \
  --app "<APP_ID>" \
  --ipa "/path/to/App.ipa" \
  --version "<VERSION>"
```

App Store upload and submit:

```bash
asc publish appstore \
  --app "<APP_ID>" \
  --ipa "/path/to/App.ipa" \
  --version "<VERSION>" \
  --submit \
  --confirm
```

Metadata-aware release pipeline:

```bash
asc release stage \
  --app "<APP_ID>" \
  --version "<VERSION>" \
  --build-id "<BUILD_ID>" \
  --metadata-dir "./metadata/version/<VERSION>" \
  --confirm
```

Monitor status:

```bash
asc status --app "<APP_ID>"
```

## Preparation Commands

Create bundle IDs:

```bash
asc bundle-ids create \
  --identifier "com.example.app" \
  --name "Example" \
  --platform IOS
```

Create an internal TestFlight group:

```bash
asc testflight groups create \
  --app "<APP_ID>" \
  --name "Internal Testers" \
  --internal
```

Fetch or create App Store signing files:

```bash
asc signing fetch \
  --app "<APP_ID>" \
  --bundle-id "com.example.app" \
  --profile-type IOS_APP_STORE \
  --create-missing \
  --output "./signing"
```

## Lower-Level Commands

Upload an IPA:

```bash
asc builds upload --app "<APP_ID>" --ipa "/path/to/App.ipa" --wait
```

Find the latest build:

```bash
asc builds info --app "<APP_ID>" --latest --version "<VERSION>" --platform IOS
```

Find the next build number:

```bash
asc builds next-build-number \
  --app "<APP_ID>" \
  --version "<VERSION>" \
  --platform IOS \
  --initial-build-number 1 \
  --output json
```

Add a build to TestFlight groups:

```bash
asc builds add-groups --build-id "<BUILD_ID>" --group "<GROUP_ID_OR_NAME>"
```

Inspect TestFlight beta detail state:

```bash
asc builds build-beta-detail view --build-id "<BUILD_ID>"
```

Clear export compliance when needed:

```bash
asc encryption declarations create \
  --app "<APP_ID>" \
  --app-description "Uses standard TLS and platform security libraries." \
  --contains-proprietary-cryptography=false \
  --contains-third-party-cryptography=true \
  --available-on-french-store=true
```

```bash
asc encryption declarations assign-builds \
  --id "<DECLARATION_ID>" \
  --build "<BUILD_ID>"
```

Validate before submit:

```bash
asc validate --app "<APP_ID>" --version "<VERSION>"
```

Create a submission:

```bash
asc versions attach-build --app "<APP_ID>" --version "<VERSION>" --build-id "<BUILD_ID>"
asc review submissions create --app "<APP_ID>" --version "<VERSION>" --confirm
```

## Xcode Path

Archive:

```bash
xcodebuild \
  -project "<PROJECT>.xcodeproj" \
  -scheme "<SCHEME>" \
  -configuration Release \
  -destination "generic/platform=iOS" \
  -archivePath ".asc/artifacts/App.xcarchive" \
  -allowProvisioningUpdates \
  archive
```

Export:

```bash
xcodebuild \
  -exportArchive \
  -archivePath ".asc/artifacts/App.xcarchive" \
  -exportPath ".asc/artifacts/export" \
  -exportOptionsPlist ".asc/export-options-app-store-connect.plist" \
  -allowProvisioningUpdates
```

If Xcode Accounts are unavailable on the Mac, add App Store Connect API-key auth:

```bash
xcodebuild \
  -exportArchive \
  -archivePath ".asc/artifacts/App.xcarchive" \
  -exportPath ".asc/artifacts/export" \
  -exportOptionsPlist ".asc/export-options-app-store-connect.plist" \
  -allowProvisioningUpdates \
  -authenticationKeyPath "/path/to/AuthKey_XXXX.p8" \
  -authenticationKeyID "KEY_ID" \
  -authenticationKeyIssuerID "ISSUER_ID"
```

Minimal export options plist:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>method</key>
  <string>app-store-connect</string>
  <key>signingStyle</key>
  <string>automatic</string>
  <key>teamID</key>
  <string>YOUR_TEAM_ID</string>
  <key>uploadSymbols</key>
  <true/>
</dict>
</plist>
```

## Verified Workflow File Shape

Use `.asc/workflow.json` when the repo should own a reusable release pipeline.

Recommended sequence:
1. `asc builds next-build-number`
2. `xcodebuild archive`
3. `xcodebuild -exportArchive`
4. `asc builds upload`
5. `asc builds add-groups`

Validation and execution:

```bash
asc workflow validate
asc workflow run --dry-run testflight_beta VERSION:1.2.3
asc workflow run testflight_beta VERSION:1.2.3
```

## TestFlight Operations

List beta groups:

```bash
asc testflight groups list --app "<APP_ID>" --paginate
```

## Troubleshooting

- If auth-related requests fail, run `asc auth status` and `asc auth doctor` before changing build code.
- If a version/build combination is rejected, resolve the next build number with `asc builds next-build-number`.
- If `asc publish testflight` appears stuck, verify whether the build already uploaded:
  - `asc builds list --app "<APP_ID>"`
  - `asc builds uploads list --app "<APP_ID>"`

## RevenueCat Notes (DexRelay)

- Do not use RevenueCat `test_` API keys in TestFlight or Release builds.
- Keep offerings and entitlements mapped to App Store product IDs exactly:
  - `com.cocotofy.dexrelay.monthly`
  - `com.cocotofy.dexrelay.yearly`
  - `com.cocotofy.dexrelay.lifetime`
- If products show unavailable right after metadata setup, allow Apple propagation time (typically 15 minutes to 24 hours), then retest on a real device with a TestFlight build.
  - If the build is already present, switch to `asc builds add-groups`.
- If internal or external TestFlight says `MISSING_EXPORT_COMPLIANCE`, create and assign an encryption declaration before retrying group assignment.
- If submit preflight fails, inspect metadata and app info, then retry:
  - `asc apps view --id "<APP_ID>" --output json --pretty`
- If you are automating, pin `--output json` instead of relying on TTY defaults.
- If examples from older docs conflict with current behavior, trust `asc <command> --help`.
