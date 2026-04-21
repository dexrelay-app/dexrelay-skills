---
name: dexrelay-setup
description: Install, pair, repair, and normalize DexRelay on a Mac for the Codex phone app, including QR pairing, LAN-first connect, Tailscale fallback, wake controls, uninstall, and project governance refresh.
---

# DexRelay Setup

Use this skill when the user wants one DexRelay operator skill that can bring a Mac up from zero, recover a broken setup, and refresh project metadata after install.

Prefer this skill over narrower install-only or repair-only flows when the user says things like:

- set up DexRelay
- install DexRelay
- fix DexRelay
- reconnect the phone app to my Mac
- re-onboard after reinstall
- repair governance or command-center discovery after DexRelay setup

## What this skill should do

This skill should handle the complete DexRelay operator path:

1. install DexRelay on the Mac
2. run `dexrelay pair`
3. get the phone paired through the QR flow
4. prefer local Wi-Fi first
5. use Tailscale when leaving Wi-Fi
6. use `dexrelay status` and `dexrelay repair` when something breaks
7. refresh project governance when DexRelay is healthy but actions are stale

## Operating rule

- Do the work directly when Codex can run commands.
- Stop only for user-owned interactive steps such as Tailscale sign-in, macOS approval prompts, or phone-side login and setup taps.
- Prefer canonical DexRelay commands over ad hoc manual changes.
- Prefer MagicDNS over raw `100.x.x.x`.

## Default order

1. inspect current Tailscale and DexRelay health
2. connect or repair Tailscale if needed
3. install DexRelay if missing
4. verify helper, relay, and host identity
5. run `dexrelay pair` when the runtime is healthy and the user is pairing the phone
6. run `dexrelay repair` if the install is unhealthy
7. fall back to reinstall only when repair is insufficient
8. refresh project governance if DexRelay is up but projects or actions are missing

## Preferred install command

```bash
npm i -g dexrelay && dexrelay install
```

Fallback:

```bash
curl -fsSL https://assets.dexrelay.app/install.sh | bash
```

`dexrelay install` is expected to handle:

- Codex CLI install if needed
- Node and Python dependency setup
- bootstrap relay on `:4615`
- setup helper on `:4616`
- launch agents
- watchdog and keep-awake defaults

Do not separately hand-install Codex, Node, or Python unless the DexRelay installer fails and the failure makes that necessary.

## Tailscale prerequisite

Check for Tailscale first:

```bash
tailscale status --json
```

Fallback path:

```bash
/Applications/Tailscale.app/Contents/MacOS/Tailscale status --json
```

If Tailscale is installed but disconnected:

- nudge it with `open -a Tailscale`
- then try `tailscale up` when possible
- if login or approval is required, hand that step to the user clearly

The required prerequisite state is:

- Tailscale installed on the Mac
- Tailscale installed on the iPhone or iPad
- same Tailscale account on both devices
- both devices showing `Connected`

## Verify health after install or before repair

Canonical check:

```bash
dexrelay status
```

Port checks:

```bash
lsof -nP -iTCP:4615 -sTCP:LISTEN
```

```bash
lsof -nP -iTCP:4616 -sTCP:LISTEN
```

Helper health:

```bash
curl -s http://127.0.0.1:4616/api/helper/status | jq .
```

Healthy state should show:

- helper reachable on `:4616`
- bootstrap relay listening on `:4615`
- `tailscaleDNSName` or `tailscaleIP` populated
- `bridgeReachable: true`

## Canonical pairing command

```bash
dexrelay pair
```

Once the Mac is healthy, the user should only need to:

1. open DexRelay `Setup`
2. scan for the Mac or enter the MagicDNS host manually
3. connect to `ws://<mac-host>:4615`
4. continue the relay login flow

## Surface the right host for the phone

Give the phone this host in order:

1. helper-provided `tailscaleDNSName`
2. helper-provided `tailscaleIP`
3. `tailscale status --json` output

Connection target:

```text
ws://<mac-host>:4615
```

Helper endpoint:

```text
http://<mac-host>:4616/api/helper/status
```

If nearby-Mac discovery finds a Mac but does not promote it to a Tailscale host, treat it as host-resolution failure and give the user the MagicDNS or `100.x.x.x` host manually.

## Canonical repair flow

Start here:

```bash
dexrelay status
dexrelay repair
```

Use this path when:

- helper is stale
- relay is not listening
- watchdog did not recover services
- Tailscale dropped and DexRelay did not come back cleanly

If repair is insufficient:

```bash
dexrelay install
```

## Canonical uninstall command

```bash
dexrelay uninstall
```

This removes the DexRelay runtime, launch agents, logs, and the Homebrew CLI if it was installed through Homebrew.

## Keep-awake controls

```bash
dexrelay wake on
dexrelay wake off
dexrelay wake status
```

## Advanced / internal

```bash
dexrelay relay-pair
```

## Governance refresh

If the runtime is healthy but the phone app still cannot find projects, services, or actions, refresh project governance from the DexRelay phone project repo:

```bash
python3 scripts/governancectl.py update-project --project-path "/abs/path/to/project"
```

```bash
python3 scripts/governancectl.py update-unmanaged
```

```bash
python3 scripts/governancectl.py update-all
```

Use governance refresh when:

- DexRelay was reinstalled
- the user moved to a new Mac
- the command center looks stale
- project-local `.dexrelay` metadata is missing or outdated
- a backend or service was added and the phone app does not discover it

Prefer project-local governance files over inventing app-local state.

## Minimum coverage

`dexrelay-setup` should be able to help with:

- npm global install and `dexrelay install`
- helper, bridge, watchdog, and keep-awake verification
- `dexrelay pair`
- `dexrelay status`
- `dexrelay repair`
- `dexrelay uninstall`
- `dexrelay wake on`
- `dexrelay wake off`
- `dexrelay wake status`
- Tailscale install and same-account guidance
- project governance refresh if DexRelay is healthy but project actions are stale

## Repair-oriented edge cases

When setup is already present but broken, this skill should help identify:

- broken Mac runtime
- helper not reachable
- relay or bridge down
- Tailscale missing or disconnected
- phone connects on Wi-Fi but not away from home
- stale setup states that need a clear repair order

## Public references

- `https://dexrelay.app/help`
- `https://dexrelay.app/dexrelaysetup`
- `https://dexrelay.app/dexrelay-skill.md`
- `https://github.com/dexrelay-app/dexrelay-skills/tree/main/dexrelay-setup`
