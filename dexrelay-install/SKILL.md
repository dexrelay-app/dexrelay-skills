---
name: dexrelay-install
description: Thin DexRelay install alias. Use when the user asks for DexRelay install specifically and you want the same behavior as dexrelay-setup, including Tailscale checks, install, verification, repair fallback, and governance refresh when needed.
---

# DexRelay Install

This is the narrow install-facing alias for `dexrelay-setup`.

If this skill triggers, use the full `dexrelay-setup` workflow and keep the user-facing language install-oriented.

Preferred install command:

```bash
brew install dexrelay-app/dexrelay/dexrelay && dexrelay install
```

Fallback:

```bash
curl -fsSL https://assets.dexrelay.app/install.sh | bash
```

Public references:

- `https://dexrelay.app/dexrelaysetup`
- `https://dexrelay.app/dexrelay-skill.md`
