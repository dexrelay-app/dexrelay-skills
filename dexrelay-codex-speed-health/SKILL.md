---
name: dexrelay-codex-speed-health
description: Inspect and safely maintain local DexRelay agent state. Use when Codex feels slow, sessions/logs/worktrees have grown, stale iOS build temp folders accumulate, or the user wants to run `dexrelay agent-speedup` from the Mac or phone settings.
---

# DexRelay Agent Speedup

Use DexRelay's bundled agent maintenance tool.

Default command:

```bash
dexrelay agent-speedup report
```

Safe cleanup command:

```bash
dexrelay agent-speedup apply
```

Rules:

- Run report first. It is read-only and privacy-safe by default.
- Explain that cleanup creates a backup and archives old Codex sessions/logs/worktrees.
- Explain that stale iOS build temp cleanup only removes DexRelay/Codex-named temp folders.
- Tell the user to create handoff docs for important old chats before cleanup.
- If cleanup says Codex is running, ask the user to close Codex on the Mac and retry.
- Do not run cleanup automatically during install, app launch, or repair.
- `dexrelay codex-fast` remains a legacy alias, but prefer `dexrelay agent-speedup`.
