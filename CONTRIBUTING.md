# Contributing

## Set up

Install stable Rust with Clippy and rustfmt, then turn on the commit hook once per clone:

```sh
git config core.hooksPath .githooks
```

## Check your change

```sh
./scripts/check.sh          # format, build, Clippy with warnings denied, tests
./scripts/check.sh --fast   # the same without tests; this is what the commit hook runs
```

CI runs the same commands on every pull request, plus the independent conformance check and
the owner-contract tests. A change is ready when CI passes.

## Where things go

- Workspace crates: `crates/<name>/src/`, with unit tests in `#[cfg(test)]` modules.
- Integration tests: `crates/<name>/tests/`.
- Conformance vectors and their independent check: `conformance/`.
- The reference owner contract: `contracts/strk20-owner-example/`.

## Pull requests

Keep each pull request to one purpose. Say what changed, why, and which checks you ran.
