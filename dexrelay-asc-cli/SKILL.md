---
name: dexrelay-asc-cli
description: Deploy any iOS app to TestFlight or the App Store with ASC CLI. Use when Codex needs to install or verify `asc`, authenticate with App Store Connect API keys, inspect app/build/version state, build and export an IPA from Xcode, upload builds, distribute to TestFlight groups, submit an App Store version, monitor release status, or create repo-local `.asc/workflow.json` automations driven by the ASC CLI itself.
---

# DexRelay ASC CLI

## Overview

Use this skill to drive App Store Connect releases with `asc` instead of ad hoc browser work. Treat `asc --help` and `asc <command> --help` as the source of truth for exact flags, and use this skill to choose the right command family and execution order.

## Workflow

1. Verify the toolchain first.
   - Confirm `asc` exists: `asc --help`
   - Confirm auth: `asc auth status`
   - Confirm auth health: `asc auth doctor`
   - If `asc` is missing, install it with either:
     - `brew install asc`
     - `curl -fsSL https://asccli.sh/install | bash`

2. Resolve app context before acting.
   - Prefer an explicit app ID with `--app` or `ASC_APP_ID`.
   - Discover state before mutation:
     - `asc apps list --bundle-id "<BUNDLE_ID>"`
     - `asc apps view --id "<APP_ID>"`
     - `asc builds list --app "<APP_ID>" --output table`
     - `asc builds info --app "<APP_ID>" --latest --platform IOS`
     - `asc testflight groups list --app "<APP_ID>" --output table`
     - `asc encryption declarations list --app "<APP_ID>" --output table`

3. Prepare Apple-side state before uploading.
   - Ensure bundle IDs exist:
     - `asc bundle-ids create --identifier "com.example.app" --name "Example" --platform IOS`
   - Ensure TestFlight groups exist:
     - `asc testflight groups create --app "<APP_ID>" --name "Internal Testers" --internal`
   - Prepare App Store signing files when needed:
     - `asc signing fetch --app "<APP_ID>" --bundle-id "com.example.app" --profile-type IOS_APP_STORE --create-missing`
   - If `asc apps list --bundle-id "<BUNDLE_ID>"` returns no app record, do not assume the installed public CLI can create one. Use App Store Connect web UI unless the installed `asc` build explicitly exposes an app-creation surface in `asc --help`.

4. Build deterministically when the repo contains source.
   - Use `xcodebuild archive` and `xcodebuild -exportArchive` unless the installed `asc` help explicitly exposes a supported Xcode wrapper.
   - Use `-allowProvisioningUpdates` for archive and export.
   - If Xcode Accounts are not signed in on the Mac, pass App Store Connect API-key auth directly to `xcodebuild`:
     - `-authenticationKeyPath`
     - `-authenticationKeyID`
     - `-authenticationKeyIssuerID`
  - Set a new build number before upload. Use `asc builds next-build-number --app "<APP_ID>" --version "<VERSION>" --platform IOS --initial-build-number 1`.

5. Validate before destructive release actions.
   - Dry-run App Store flows where supported.
   - Inspect output in JSON for automation.
   - Use `--confirm` for submit or other destructive operations.

## Auth Rules

- Prefer keychain-backed login:
  - `asc auth login --name "MyApp" --key-id "KEY_ID" --issuer-id "ISSUER_ID" --private-key /path/to/AuthKey.p8`
- Use environment variables only when keychain-backed auth is not practical:
  - `ASC_KEY_ID`
  - `ASC_ISSUER_ID`
  - `ASC_PRIVATE_KEY_PATH`, `ASC_PRIVATE_KEY`, or `ASC_PRIVATE_KEY_B64`
- Re-check credentials with `asc auth status` before blaming release failures on build artifacts.

## Output and Discovery Rules

- Always inspect help before inventing flags:
  - `asc --help`
  - `asc publish --help`
  - `asc builds upload --help`
  - `asc testflight groups --help`
  - `asc signing fetch --help`
  - `xcodebuild -help`
- Prefer long flags and explicit IDs.
- Prefer `--output json` for machine steps and `--output table` for human inspection.
- Use `--paginate` when the user wants all results.
- If a command family has changed, follow the current `--help` output instead of older examples.

## Common Paths

### TestFlight from an existing IPA

Use the high-level path first:

```bash
asc publish testflight \
  --app "<APP_ID>" \
  --ipa "/path/to/App.ipa" \
  --group "<GROUP_ID_OR_NAME>" \
  --wait
```

Add `--notify` to notify testers and `--test-notes` plus `--locale` when you need What to Test notes.

### TestFlight from repo source

1. Resolve the next build number:
   - `asc builds next-build-number --app "<APP_ID>" --version "<VERSION>" --platform IOS --initial-build-number 1 --output json`
2. Archive:
   - `xcodebuild -project "<PROJECT>.xcodeproj" -scheme "<SCHEME>" -configuration Release -destination "generic/platform=iOS" -archivePath ".asc/artifacts/App.xcarchive" -allowProvisioningUpdates archive`
3. Export:
   - `xcodebuild -exportArchive -archivePath ".asc/artifacts/App.xcarchive" -exportPath ".asc/artifacts/export" -exportOptionsPlist ".asc/export-options-app-store-connect.plist" -allowProvisioningUpdates`
4. Upload:
   - Prefer `asc publish testflight --app "<APP_ID>" --ipa ".asc/artifacts/export/App.ipa" --group "<GROUP_ID_OR_NAME>" --wait`
   - If the high-level publish flow stalls or needs more control, use:
     - `asc builds upload --app "<APP_ID>" --ipa ".asc/artifacts/export/App.ipa" --wait`
     - `asc builds add-groups --build-id "<BUILD_ID>" --group "<GROUP_ID_OR_NAME>"`
5. If TestFlight says the build is not internally testable, inspect export compliance:
   - `asc builds build-beta-detail view --build-id "<BUILD_ID>"`
   - If state is `MISSING_EXPORT_COMPLIANCE`, create and assign a declaration:
     - `asc encryption declarations create --app "<APP_ID>" --app-description "Uses standard TLS and platform security libraries." --contains-proprietary-cryptography=false --contains-third-party-cryptography=true --available-on-french-store=true`
     - `asc encryption declarations assign-builds --id "<DECLARATION_ID>" --build "<BUILD_ID>"`

### App Store upload and submit

Prefer one of these:

```bash
asc publish appstore \
  --app "<APP_ID>" \
  --ipa "/path/to/App.ipa" \
  --version "<VERSION>"
```

```bash
asc publish appstore \
  --app "<APP_ID>" \
  --ipa "/path/to/App.ipa" \
  --version "<VERSION>" \
  --submit \
  --confirm
```

Or use the canonical staged release pipeline when metadata lives in the repo:

```bash
asc release stage \
  --app "<APP_ID>" \
  --version "<VERSION>" \
  --build-id "<BUILD_ID>" \
  --metadata-dir "./metadata/version/<VERSION>" \
  --dry-run
```

```bash
asc release stage \
  --app "<APP_ID>" \
  --version "<VERSION>" \
  --build-id "<BUILD_ID>" \
  --metadata-dir "./metadata/version/<VERSION>" \
  --confirm
```

### Low-level App Store submission

Use this when you need more control:

```bash
asc validate --app "<APP_ID>" --version "<VERSION>"
asc versions attach-build --app "<APP_ID>" --version "<VERSION>" --build-id "<BUILD_ID>"
asc review submissions create --app "<APP_ID>" --version "<VERSION>" --confirm
asc status --app "<APP_ID>"
```

### RevenueCat + TestFlight guardrails

- Never ship `test_` RevenueCat API keys in TestFlight/Release builds.
- Keep RevenueCat offerings mapped to exact ASC product IDs:
  - `com.cocotofy.dexrelay.monthly`
  - `com.cocotofy.dexrelay.yearly`
  - `com.cocotofy.dexrelay.lifetime`
- If offerings are empty right after ASC metadata changes, wait for Apple propagation (typically 15 minutes to 24 hours), then retest on TestFlight (not Simulator/local release run).

## Repo Automation

Use `asc workflow` when the repo should own the release process.

1. Create `.asc/export-options-app-store-connect.plist`
2. Create `.asc/workflow.json`
3. Validate:
   - `asc workflow validate`
4. Preview:
   - `asc workflow run --dry-run testflight_beta VERSION:1.2.3`
5. Execute:
   - `asc workflow run testflight_beta VERSION:1.2.3`

Prefer a workflow shape of:
- `asc builds next-build-number`
- `xcodebuild archive`
- `xcodebuild -exportArchive`
- `asc builds upload`
- `asc builds add-groups`

## Operating Rules

- Do not guess IDs if list commands can resolve them first.
- Do not submit to App Store review without either `--dry-run` or a prior validation pass unless the user explicitly wants direct execution.
- Do not assume old aliases are canonical; prefer current surfaces such as `asc testflight groups list`.
- Do not assume the installed CLI still ships `asc xcode` wrappers. Verify first.
- When `asc publish testflight` does not finish cleanly, switch to `asc builds upload` plus `asc builds add-groups` instead of guessing.
- Do not rely on browser-only steps when the CLI can do the job.

## References

- Read [references/asc-deploy-map.md](references/asc-deploy-map.md) for the command map, validated source-to-TestFlight workflow, and troubleshooting cues.
