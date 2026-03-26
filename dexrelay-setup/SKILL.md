---
name: dexrelay-setup
description: Install, repair, and normalize DexRelay on a Mac for the Codex phone app. Use when the user wants Codex to handle first-time DexRelay setup, Tailscale checks, helper and relay verification, host discovery, self-healing repair, reinstall fallback, or project governance refresh after DexRelay comes online.
---

# DexRelay Setup

Use this skill when the user wants one DexRelay operator skill that can bring a Mac up from zero, recover a broken setup, and repair the project-side metadata DexRelay depends on after install.

Prefer this skill over narrower install-only or repair-only flows when the user says things like:

- set up DexRelay
- install DexRelay
- fix DexRelay
- reconnect the phone app to my Mac
- re-onboard after reinstall
- repair governance or command-center discovery after DexRelay setup

## Scope

This skill covers four areas:

1. Tailscale prerequisite and host identity
2. DexRelay install and onboarding runtime health
3. DexRelay repair and reinstall fallback
4. project governance refresh so the phone app can discover project actions and services

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
5. run `dexrelay repair` if the install is unhealthy
6. fall back to reinstall only when repair is insufficient
7. refresh project governance if DexRelay is up but projects or actions are missing

## 1. Tailscale prerequisite

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

## 2. Install DexRelay

Preferred install command:

```bash
brew tap dexrelay-app/dexrelay && brew install dexrelay && dexrelay install
```

Fallback when Homebrew is unavailable or blocked:

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

## 3. Verify health after install or before repair

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

## 4. Surface the right host for the phone

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

## 5. Repair flow

If DexRelay exists but is unhealthy, use:

```bash
dexrelay repair
```

Use this path when:

- helper is stale
- relay is not listening
- watchdog did not recover services
- Tailscale dropped and DexRelay did not come back cleanly

Only fall back to reinstall when `dexrelay repair` is not enough.

Useful related command:

```bash
dexrelay uninstall
```

## 6. Governance refresh

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
- project-local `.codex` metadata is missing or outdated
- a backend or service was added and the phone app does not discover it

Prefer project-local governance files over inventing app-local state.

## Phone-side handoff

Once the Mac is healthy, the user should only need to:

1. open DexRelay `Setup`
2. scan for the Mac or enter the MagicDNS host manually
3. connect to `ws://<mac-host>:4615`
4. continue the relay login flow

## Public references

Use these when the user needs the public install or repair explanation:

- `https://dexrelay.app/dexrelaysetup`
- `https://dexrelay.app/dexrelay-skill.md`
