## What and why

<!-- One purpose per PR (AGENTS.md). Link the issue it closes. -->

## Checks

- [ ] `./scripts/check.sh` passes locally (say which checks ran if any were skipped)
- [ ] If this touches key derivation, account addresses, signing or the krusty-kms pin: the
      conformance vectors still match and were cross-checked against Bramble's
      (`conformance/`, `crates/wallet-core/tests/conformance.rs`)
- [ ] If this touches `desktop/` (outside the workspace and CI): built locally, and the GUI
      change was checked by launching the app
