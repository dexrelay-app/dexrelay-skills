# DexRelay Skills

This folder is the publishable source for `dexrelay-app/dexrelay-skills`.

These skills should always match the current DexRelay product model:

1. install DexRelay on the Mac
2. run `dexrelay pair`
3. scan the QR on the phone
4. use local Wi-Fi first
5. use Tailscale fallback away from Wi-Fi
6. use `dexrelay status` and `dexrelay repair` if something breaks

Expected repo shape:

- `README.md`
- `dexrelay-setup/SKILL.md`
- `dexrelay-install/SKILL.md`

Primary install target:

```text
https://github.com/dexrelay-app/dexrelay-skills/tree/main/dexrelay-setup
```

Install alias:

```text
https://github.com/dexrelay-app/dexrelay-skills/tree/main/dexrelay-install
```

Publish rule:

If DexRelay onboarding, repair behavior, or public install guidance changes, update these skill sources before the next release script publishes the skills repo.
