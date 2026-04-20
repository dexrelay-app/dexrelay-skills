---
name: dexrelay-repair
description: Diagnose and repair DexRelay setup, direct bridge, helper, Tailscale fallback, and mobile recovery failures for the Codex phone app.
---

# DexRelay Repair

Use this skill when DexRelay is broken enough that the user needs a clean repair sequence instead of ad hoc debugging.

## Mental model

DexRelay now works like this:

1. `dexrelay pair` gives the phone a QR
2. the phone uses local Wi-Fi first when available
3. the phone uses Tailscale fallback after leaving Wi-Fi
4. the Mac runtime is kept alive by launchd, helper, watchdog, and keep-awake

So repair work should always preserve that mental model. Do not throw users back into raw host guessing unless the canonical repair path has actually failed.

## Default repair order

1. run `dexrelay status`
2. confirm whether the Mac runtime is healthy
3. confirm whether Tailscale is connected on the Mac
4. confirm whether the phone problem is:
   - local Wi-Fi only
   - away-from-home / Tailscale only
   - stale setup state
5. run `dexrelay repair`
6. rerun `dexrelay install` only if repair is insufficient

## Canonical commands

```bash
dexrelay status
```

```bash
dexrelay repair
```

```bash
dexrelay install
```

```bash
dexrelay uninstall
```

## What `dexrelay status` should tell you

Check these first:

- bridge launch agent
- helper launch agent
- watchdog launch agent
- keep-awake launch agent
- bridge socket
- helper socket
- Tailscale connected state
- helper-reported host information

Direct path ports:

- `4615` bootstrap/direct bridge
- `4616` setup helper

Optional relay path:

- `4620`

## Repair rules

- If the Mac runtime is unhealthy, use `dexrelay repair` before inventing manual restarts.
- If the user can connect on Wi-Fi but not after leaving Wi-Fi, suspect missing or disconnected phone-side Tailscale first.
- If the user is on LTE/5G and Tailscale is not available on the phone, the app should guide them into Tailscale recovery, not first-time onboarding.
- If the app is already paired to the Mac, do not send the user back to “install DexRelay on your Mac” unless the Mac runtime is actually gone.
- Bonjour or nearby-Mac discovery is only a same-Wi-Fi discovery helper. It is not the durable remote route.

## Tailscale-specific rules

- Prefer MagicDNS over raw `100.x.x.x` when both are available.
- Same-Wi-Fi onboarding should work without making Tailscale the first-run blocker.
- Away-from-home recovery should clearly say:
  - install Tailscale on this phone, or
  - open Tailscale on this phone

## When to escalate to reinstall

Only reinstall when:

- `dexrelay repair` fails
- the launch agents are missing or corrupted
- the helper is not recoverable
- the payload version mismatch is severe enough that in-place repair is not trustworthy

## Public references

- `https://dexrelay.app/dexrelaysetup`
- `https://dexrelay.app/dexrelay-skill.md`
