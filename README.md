# DexRelay Skills

This folder is the publishable source for `dexrelay-app/dexrelay-skills`.

Expected repo shape:

- `README.md`
- `dexrelay-setup/SKILL.md`
- `dexrelay-install/SKILL.md`

Recommended install target:

```bash
https://github.com/dexrelay-app/dexrelay-skills/tree/main/dexrelay-setup
```

Install-oriented alias:

```bash
https://github.com/dexrelay-app/dexrelay-skills/tree/main/dexrelay-install
```

The primary skill is `dexrelay-setup`. `dexrelay-install` is a narrow alias for users who search for install-specific wording.

## Install in Codex

Preferred skill:

```text
https://github.com/dexrelay-app/dexrelay-skills/tree/main/dexrelay-setup
```

Install alias:

```text
https://github.com/dexrelay-app/dexrelay-skills/tree/main/dexrelay-install
```

If the user is already in Codex, the simplest path is to use the built-in `skill-installer` skill and point it at one of the GitHub URLs above.

Equivalent GitHub repo form:

```text
repo: dexrelay-app/dexrelay-skills
path: dexrelay-setup
```

or:

```text
repo: dexrelay-app/dexrelay-skills
path: dexrelay-install
```

## What to install

- Install `dexrelay-setup` for the full setup, repair, and governance workflow.
- Install `dexrelay-install` only if you want the narrow install-oriented alias.

## Existing users

If a Mac still has the old tap from `chetanankola/dexrelay`, remove it once before using the shorter DexRelay install command:

```bash
brew untap chetanankola/dexrelay
```
