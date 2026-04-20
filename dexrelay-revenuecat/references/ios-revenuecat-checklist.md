# iOS RevenueCat Checklist

## Use This Reference When

- Creating a new RevenueCat integration in an iPhone or iPad app
- Repairing a broken entitlement or offering setup
- Auditing whether the app-side implementation matches the RevenueCat dashboard

## App Store Connect

- Create the products first.
- Put renewable subscriptions in a subscription group.
- Use clear product IDs and keep them stable.
- If lifetime access is offered, model it separately as a non-consumable.

## RevenueCat Dashboard

- Create the entitlement first.
- Import the App Store products.
- Add them to an offering.
- Map packages so app code can resolve monthly, yearly, lifetime, or custom IDs.
- Attach a paywall to the offering if using RevenueCat paywalls.
- Configure Customer Center before presenting it in the app.

## App-Side Checklist

- Add `RevenueCat` and `RevenueCatUI` with Swift Package Manager.
- Configure RevenueCat once at app startup.
- Fetch `customerInfo` and `offerings`.
- Listen for customer info updates.
- Expose:
  - `hasAccess`
  - `purchase`
  - `restorePurchases`
  - `managementURL`
  - `currentOffering`
- Route locked actions into the paywall.
- Keep a Billing screen with restore and status.

## Failure Patterns

- Entitlement ID in code does not match RevenueCat.
- Product IDs exist in App Store Connect but are not imported into RevenueCat.
- Offering exists but has no current offering set.
- Package identifiers do not match app expectations.
- Paywall is presented before `Purchases.configure`.
- Purchase logic lives in multiple views and drifts.
- Restore exists only in hidden or hard-to-reach UI.

## Good Defaults

- Central `SubscriptionManager` on the main actor
- One place for RevenueCat config keys
- One place for entitlement checks
- One place for paywall presentation decisions
- First-class restore and Customer Center surfaces
