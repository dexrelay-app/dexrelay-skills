---
name: dexrelay-token-cost-reduction
description: Reduce Codex token cost and future edit scope when starting a project or planning a large refactor. Use when scaffolding a new codebase, setting project structure, splitting oversized files, isolating hot edit surfaces, or reorganizing code so future Codex work stays narrow, local, and cheap in tokens.
---

# DexRelay Token Cost Reduction

Optimize the codebase for narrow future edits.

Before a major DexRelay refactor, read:

1. `docs/DEXRELAY_ARCHITECTURE.md`
2. `docs/CODEX_CONTEXT_MAP.md`

Do not split hot files without understanding where they sit in the iPhone app ↔ bridge ↔ app-server topology.

Default goal order:

1. Reduce token cost for future Codex turns
2. Preserve or improve runtime performance
3. Improve compile-time and incremental-build behavior
4. Improve maintainability only when it does not fight the first three goals

## Principles

- Split by edit surface, not by arbitrary line count.
- Isolate hot paths separately from low-churn admin code.
- Keep files aligned to user-visible features: transcript, composer, header, sidebar, thread activity, networking, persistence, models.
- Prefer moving cohesive blocks into neighboring files over inventing deep abstractions.
- Avoid spreading a single feature across many tiny files if that increases lookup cost.
- Preserve behavior during structural refactors unless the user also asked for product changes.

## Where to Cut First

For UI-heavy apps:

- Extract the hottest scrolling surface first.
- Then extract the header/meta/activity surfaces that churn independently.
- Then extract composer/input flows.
- Keep shared support types, modifiers, and representables in a separate support file.

For large view models:

- Split by responsibility: thread activity, runtime state sync, transport/networking, persistence, project actions, approvals, deployment.
- Keep fast-changing selected-item logic separate from global settings and setup flows.

For general app code:

- Keep models and enums stable and centralized.
- Keep feature-local helpers near the feature unless multiple features truly share them.
- Move cross-file helpers from `private` only when required by the split.

## Project-Start Workflow

When used at the start of a project:

1. Identify the likely high-churn surfaces.
2. Create file boundaries around those surfaces immediately.
3. Keep the entry view/controller thin.
4. Keep app state split by domain rather than one giant store.
5. Prefer a folder/file layout that lets future Codex work open only 1-3 files for a task.

## Refactor Workflow

When used on an existing codebase:

1. Measure the largest files and the hottest edit surfaces.
2. Find the runtime hot path separately from the compile hot path.
3. Split first where both are improved together.
4. Verify project membership/build after every structural move.
5. Stop broadening access control more than necessary.

## Heuristics

- A file above roughly 1500-2500 lines is a candidate, but only split if there is a clean boundary.
- If a future task would require loading an unrelated 5k-10k line file, the structure is too coarse.
- If live state changes can invalidate a whole scrolling screen, isolate the scrolling subtree.
- If one file is edited on most turns, split it by the actual task clusters visible in git history or current work.

## Deliverables

For each application of this skill, aim to leave:

- smaller, feature-aligned files
- thinner entry files
- fewer unrelated dependencies per file
- explicit note of what was optimized for token cost versus runtime performance

## Do Not Optimize For

- aesthetic folder purity
- abstraction for its own sake
- micro-files that increase navigation cost
- widespread renames unless they materially reduce future edit scope

## Output Pattern

When finishing, summarize:

- what boundaries were introduced
- why those boundaries reduce future token cost
- whether the change also helps runtime or compile performance
- what the next highest-value split would be
