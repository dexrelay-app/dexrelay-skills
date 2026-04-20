---
name: dexrelay-governance
description: Initialize, repair, and normalize per-project governance for Codex-managed repos. Use when creating a new project, adding a backend service, repairing missing project runbooks/governance files, rebuilding command-center registration after reinstall or moving to a different Mac, or updating unmanaged projects so the phone app can discover actions, ports, and service controls.
---

# DexRelay Project Governance

Keep the source of truth inside each project repo:

- `.dexrelay/project-runbook.json`
- `.dexrelay/project-governance.json`

Do not treat the iPhone app or command-center snapshot as the only source of project behavior. Those layers index and expose project state; they do not replace project-local metadata.

## Use This Skill When

- a new project is created
- a project adds a backend/server
- the phone app cannot find project actions or services
- governance files are missing or stale
- the user reinstalls the app, reinstalls DexRelay, or moves to another Mac and needs command-center state rebuilt

## Default Commands

From any Mac with DexRelay installed:

```bash
python3 "$HOME/Library/Application Support/DexRelay/runtime/scripts/governancectl.py" update-project --project-path "/abs/path/to/project"
python3 "$HOME/Library/Application Support/DexRelay/runtime/scripts/governancectl.py" update-unmanaged
python3 "$HOME/Library/Application Support/DexRelay/runtime/scripts/governancectl.py" update-all
```

## Rules

1. Prefer project-local `.dexrelay` metadata over inventing app-local state.
2. If a backend is introduced, ensure governance is updated before treating the service as managed.
3. If command center is out of sync, repair project files first, then rebuild the snapshot.
4. Do not introduce a parallel metadata tree unless the user explicitly asks for a migration plan.

## References

- DexRelay runtime script: `~/Library/Application Support/DexRelay/runtime/scripts/governancectl.py`
- Project governance guide: `docs/PROJECT_GOVERNANCE.md`
