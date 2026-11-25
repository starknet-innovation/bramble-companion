# Working agreement

This file is for people and coding agents working in this repository.

- Read `README.md` before changing anything.
- Keep changes small: one purpose per branch and pull request.
- Run `./scripts/check.sh` before you push, and report which checks actually ran. It covers the
  Cargo workspace; `conformance/` and `contracts/` have their own commands in CI.
- A missing tool is a failure, not a reason to skip a check.
- Do not loosen a check, delete a test or lower a version pin to get a green run. Say what is
  failing instead.
- Unit tests sit in `#[cfg(test)]` modules next to the code; integration tests in each crate's
  `tests/`.
- `Cargo.lock` is committed and every Cargo command uses `--locked`. Change dependencies in
  their own change.
- Never commit secrets, keys or `.env` files.

## Agent instructions

Read [README.md](README.md) for project context and conventions.

Use the repository's existing manifests, scripts, and CI workflows to choose
build and validation commands for the files you change.

## Claude Code and Codex

These instructions apply to both agents. `CLAUDE.md` imports this file. Before
editing a directory, read its scoped `AGENTS.md` when present. Shared local skills
are discoverable under `.agents/skills`; `.claude/skills` provides compatibility.
Use the host's native tools for questions, planning, and delegation when a workflow
mentions a Claude tool name. Preserve the workflow's permission and review gates.
If a required capability is unavailable, report it instead of claiming it ran.
