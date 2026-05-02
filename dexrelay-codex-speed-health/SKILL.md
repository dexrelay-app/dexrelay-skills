---
name: dexrelay-codex-speed-health
description: Inspect and safely maintain local Codex state through DexRelay. Use when Codex feels slow, when sessions/logs/worktrees have grown, or when the user wants to run `dexrelay codex-fast` from the Mac or phone settings.
---

# DexRelay Codex Speed Health

Use DexRelay's bundled Codex local-state maintenance tool.

Default command:

```bash
dexrelay codex-fast report
```

Safe cleanup command:

```bash
dexrelay codex-fast apply
```

Rules:

- Run report first. It is read-only and privacy-safe by default.
- Explain that cleanup creates a backup and archives old sessions/logs/worktrees instead of deleting them.
- Tell the user to create handoff docs for important old chats before cleanup.
- If cleanup says Codex is running, ask the user to close Codex on the Mac and retry.
- Do not run cleanup automatically during install, app launch, or repair.
