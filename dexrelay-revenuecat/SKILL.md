---
name: dexrelay-revenuecat
description: Implement, audit, or repair RevenueCat in iOS and SwiftUI apps. Use when adding subscriptions, entitlements, offerings, packages, paywalls, Customer Center, restore flows, entitlement gating, or subscription testing for another app that uses RevenueCat.
---

# DexRelay RevenueCat

Use this skill for Apple-platform apps that need RevenueCat wired correctly without scattering purchase logic across the UI. Prefer a centralized subscription manager, explicit entitlement gating, and first-class restore and paywall flows.

## Workflow

1. Inspect the app before editing.
   Identify the app entry point, purchase-related code, current feature surfaces to gate, and whether StoreKit or RevenueCat is already present.

2. Confirm the subscription model.
   Determine the entitlement IDs, product IDs, package identifiers, current offering strategy, and which features belong behind the paywall.
   For Apple apps, separate Apple-side product setup from RevenueCat-side catalog setup before touching code.

3. Install or verify the SDK.
   For SwiftUI apps, prefer Swift Package Manager with `RevenueCat` and `RevenueCatUI`.

4. Centralize purchase state.
   Add one observable purchase coordinator or subscription manager that owns:
   - SDK configuration
   - offerings fetch
   - customer info refresh
   - purchase
   - restore
   - entitlement checks
   - paywall and Customer Center presentation support

5. Gate features deliberately.
   Put paywall checks at user entry points for premium actions, not deep in unrelated helpers. Locked actions should show a clear lock state and open the paywall immediately.

6. Verify the full loop.
   Confirm fresh purchase, restore, locked state, unlocked state, startup refresh, and missing-offering behavior.

7. Split debug and production keys.
   Keep Test Store keys in debug-only config.
   Keep the real Apple public SDK key in release or TestFlight config.
   Never allow `test_...` keys in non-debug builds.

## Implementation Rules

- Prefer Swift Package Manager over manual dependency setup.
- Keep the RevenueCat SDK key and entitlement ID in one config surface.
- Do not ship a `test_...` key in release builds.
- Do not ship a `test_...` key in TestFlight builds.
- Do not hardcode entitlement strings across multiple views.
- Use one source of truth for `hasAccess` checks.
- Prefer async RevenueCat APIs and update UI on the main actor.
- Present RevenueCat paywalls with `RevenueCatUI.PaywallView` unless the app already has a custom paywall.
- Add Customer Center when the app has subscriptions users may need to manage in-app.
- Keep restore visible in settings or the paywall.
- If the app already has StoreKit code, integrate carefully instead of replacing it blindly.

## SwiftUI Pattern

For most apps, implement this shape:

- `SubscriptionManager.swift`
  Owns `Purchases.configure`, `customerInfo`, `offerings`, `purchase`, `restorePurchases`, `hasAccess`.
- `App.swift`
  Creates and injects the manager as an environment object and refreshes on app activation.
- Premium feature entry points
  Call `hasAccess`, show locked UI, and route to the paywall when needed.
- Settings or Billing screen
  Show current entitlement state, restore, paywall, prices, and Customer Center.

## RevenueCat Dashboard Expectations

Make sure the dashboard matches the app:

- The correct app exists in RevenueCat for the real Apple bundle ID, not only Test Store.
- Entitlement exists and matches the identifier used by the app.
- Products exist in App Store Connect and are imported into RevenueCat.
- The current offering contains the intended packages.
- Package mapping is explicit for monthly, annual, lifetime, or any custom identifiers.
- A paywall is attached to the offering if using RevenueCat paywalls.
- Customer Center is configured before exposing it to users.

## Apple + RevenueCat Rules

- Use `asc` or App Store Connect for real Apple products, pricing, availability, screenshots, and metadata.
- Use RevenueCat for entitlements, offerings, packages, paywalls, and customer state.
- RevenueCat secret API keys (`sk_...`) are for automation only. Never put them in the app.
- RevenueCat public SDK keys are platform app keys. The production iOS key usually starts with `appl_...`.
- If a RevenueCat project only has Test Store configured, add the real Apple app before expecting live StoreKit products to resolve.
- For StoreKit 2 based Apple apps, make sure the RevenueCat Apple app has both:
  - App Store Connect API key
  - In-App Purchase / Subscription key
- Keep build settings ready for separate debug and release SDK keys, for example `REVENUECAT_API_KEY = $(...)` in `Info.plist`.
- For TestFlight verification, always validate on a real device running TestFlight, not a local Release run from Xcode.
- If subscriptions or IAPs were newly created or edited in App Store Connect, allow propagation time (typically 15 minutes to 24 hours) before treating `offerings empty` / `products unavailable` as a code bug.

## Build Mode Matrix

- Debug: use RevenueCat Test Store key (`test_...`) only if intentional for local development.
- TestFlight (ad hoc/release config): use Apple RevenueCat app key (`appl_...`) and real ASC product IDs.
- App Store release: same key/path as TestFlight; never point release to Test Store.

## API Notes

- RevenueCat API v2 can create and update:
  - apps
  - entitlements
  - products
  - offerings
  - package and entitlement product attachments
- RevenueCat API v2 may not expose the public SDK key back to the agent. If it is not already in local config, ask the user for the `appl_...` key.
- If an offering already contains Test Store packages, attaching real Apple products to the same packages works, but clean up stale test products later if they create ambiguity.

## Verification Checklist

- Offerings load successfully.
- The expected entitlement activates after purchase.
- Restore works on a clean install.
- Locked UI downgrades correctly when no entitlement is active.
- Missing or empty offering states fail gracefully.
- Sandbox and production wording do not get mixed.

## References

- Read `references/ios-revenuecat-checklist.md` for a compact setup map, implementation checklist, and failure patterns.
- Read `../ios-subscriptions-codex-relay/references/asc-revenuecat-interop.md` when the work spans App Store Connect plus RevenueCat.
- When API details are version-sensitive, check the current official RevenueCat docs before coding.
