---
name: dexrelay-xcode-build
description: Get an Apple project building when Xcode's Play button fails. Use when a project needs the right scheme, simulator/device destination, team ID, automatic signing, provisioning profile selection, or a practical fallback from device build to simulator build so the user can run the app instead of manually fighting Xcode settings.
---

# DexRelay Xcode Build

Use this skill when the user's real problem is not optimization but "I opened the project and it won't build."

This skill is a first-build and build-recovery workflow for Apple projects. It should quickly answer:

1. what should be built
2. where it should be built
3. which signing settings are blocking it
4. whether the correct fix is device provisioning, simulator fallback, or targeted Xcode cleanup

## Use This Skill When

- pressing Play in Xcode fails on a fresh project checkout
- Xcode cannot find a signing team or provisioning profile
- the project opens but does not know which simulator or device to use
- a user wants the app running as fast as possible, even if that means simulator first
- a repo was copied from another developer and still points at the wrong team or bundle identifier

## Core Rules

- Prefer getting the app running over preserving broken default settings.
- If device signing is blocked, try simulator first unless the task explicitly requires a physical device capability.
- Reuse project evidence before guessing: nearby Apple projects, existing provisioning settings, bundle ID patterns, and any checked-in Xcode config.
- Do not invent a production signing setup when a local automatic-signing fix is enough.
- When a change affects code signing or bundle identifiers, report exactly what changed.

## Workflow

### 1. Discover the build target

Inspect:

- `.xcodeproj` and `.xcworkspace`
- available schemes
- app targets versus test targets
- platform: iOS, macOS, watchOS, tvOS

Prefer the main app scheme. Ignore test-only schemes unless the user asked to run tests.

### 2. Decide simulator vs device first

Default decision:

- Use simulator when the goal is simply "get it running"
- Use device only when the app needs real-device capabilities such as push, camera, HealthKit, Bluetooth, NFC, or the user explicitly asked for device install

If the project can run on simulator, prefer proving that path first. That avoids blocking on signing when signing is not necessary.

### 3. Inspect signing state

Check the project for:

- `DEVELOPMENT_TEAM`
- `CODE_SIGN_STYLE`
- `PRODUCT_BUNDLE_IDENTIFIER`
- `PROVISIONING_PROFILE_SPECIFIER`
- `CODE_SIGN_IDENTITY`
- per-configuration overrides in `project.pbxproj` or `.xcconfig` files

Also inspect neighboring Apple projects in the same parent workspace or nearby directories when the current project is missing a usable team ID. A practical heuristic is:

1. look for sibling repos or folders owned by the same developer
2. search their `project.pbxproj` and `.xcconfig` files for `DEVELOPMENT_TEAM`
3. reuse the same team only when it is clearly the user's local Apple team and not a checked-in company-specific release configuration

If multiple nearby team IDs exist, prefer the one already used by the most similar personal iOS project.

### 4. Fix the minimum necessary signing settings

For local development, prefer:

- `CODE_SIGN_STYLE = Automatic`
- a valid `DEVELOPMENT_TEAM`
- no stale `PROVISIONING_PROFILE_SPECIFIER` forcing a missing manual profile

Common fixes:

- remove stale manual provisioning specifier for Debug
- set a valid team ID for the app target and extension targets
- keep Release-specific signing untouched when only Debug is broken
- if the bundle identifier collides with another installed app under the same team, use a temporary debug-safe suffix only if needed to get the app running locally

### 5. Build the easiest viable path

Try in this order:

1. simulator build
2. simulator run
3. device build if the task requires it
4. device run after signing is confirmed

If simulator works and device does not, say that plainly and isolate the remaining problem to provisioning instead of treating the whole project as broken.

### 6. Escalate only when the failure is a different class of problem

Use nearby skills only when appropriate:

- `dexrelay-xcode-cache-repair` for PIF, DerivedData, or package-state corruption
- `spm-build-analysis` for package graph issues
- `xcode-project-analyzer` for true project-configuration inefficiencies, not first-build blocking

## Preferred Tactics

- Use Xcode build tooling or `xcodebuildmcp` to discover schemes and simulator targets before editing files
- Prefer isolated DerivedData paths for CLI verification
- Keep device-signing changes scoped to Debug/local development unless the user asks for broader normalization
- If the project has extensions, widgets, or watch targets, make sure their team settings do not remain broken after fixing the main app target

## Reporting

Report in this order:

1. chosen scheme and destination
2. whether simulator or device path was selected and why
3. the exact signing/build issue found
4. the exact fix applied
5. current status: builds on simulator, runs on simulator, builds on device, or still blocked

When still blocked, state the remaining blocker precisely:

- missing Apple account/team on this Mac
- profile/certificate unavailable for device builds
- bundle ID collision
- cache/package corruption
- real compile error unrelated to signing

## Good Outcome

The expected outcome is not "all signing is perfect." The expected outcome is:

- the user knows the correct scheme
- the app builds in the easiest viable destination
- signing is repaired enough for the requested destination
- any remaining device-only blocker is explicit and narrowly scoped
