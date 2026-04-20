---
name: dexrelay-xcode-cache-repair
description: Repair stale Xcode cache, PIF, DerivedData, SourcePackages, and build database issues in Apple projects. Use when xcodebuild or Xcode shows errors like unable to load transferred PIF, duplicate package GUIDs, build.db locked, or repeated DerivedData corruption.
---

# DexRelay Xcode Cache Repair

Use this skill when an Apple project has stale Xcode cache state instead of a real code problem.

Typical symptoms:

- `unable to load transferred PIF`
- `workspace contains multiple references with the same GUID`
- `build.db: database is locked`
- package graph corruption after branch changes
- builds that only recover after deleting DerivedData

## Default workflow

1. Prefer the repo's targeted repair script if it exists.
2. Avoid deleting all DerivedData unless the targeted fix fails.
3. Avoid running Xcode UI builds and CLI builds against the same DerivedData at the same time.
4. After repair, rerun one clean build to verify the project is healthy.

## Canonical repo command

From the repo root:

```sh
sh ./scripts/fix-xcode-pif.sh
```

This script should be preferred over manual cleanup because it only removes:

- project `SourcePackages`
- project `XCBuildData`
- stale workspace UI state

and then re-resolves packages.

## If the repo script is missing

Use the same logic manually for the affected project only:

1. Find the matching DerivedData folder.
2. Remove the project's `SourcePackages`.
3. Remove the project's `Build/Intermediates.noindex/XCBuildData`.
4. Clear stale workspace UI state if it is obviously tied to the broken project.
5. Re-resolve packages.

Do not default to wiping unrelated DerivedData for other apps.

## Build hygiene

- Do not run the repair script while a build is active.
- Prefer either Xcode UI or CLI, not both at once.
- For CLI builds, prefer an isolated derived data path such as:

```sh
xcodebuild -project 'CodexRemote.xcodeproj' -scheme CodexRemote -destination 'generic/platform=iOS Simulator' -derivedDataPath /tmp/CodexRemoteCLI build
```

This avoids collisions with Xcode's default DerivedData and reduces `build.db locked` errors.

## Expected closeout

After repair:

1. rerun one build
2. confirm whether the cache issue is gone
3. only escalate to broader DerivedData cleanup if the targeted repair did not work
