---
name: dexrelay-install
description: Thin DexRelay install alias. Use when the user asks for DexRelay install specifically and you want the same behavior as dexrelay-setup, including QR pairing readiness and repair fallback.
---

# DexRelay Install

This is the narrow install-facing alias for `dexrelay-setup`.

Preferred install command:

```bash
brew tap dexrelay-app/dexrelay && brew install dexrelay && dexrelay install
```

Fallback:

```bash
curl -fsSL https://assets.dexrelay.app/install.sh | bash
```

Next step after install:

```bash
dexrelay pair
```

Repair flow:

```bash
dexrelay status
dexrelay repair
```

Uninstall:

```bash
dexrelay uninstall
```

Public references:

- `https://dexrelay.app/help`
- `https://dexrelay.app/dexrelaysetup`
- `https://dexrelay.app/dexrelay-skill.md`
