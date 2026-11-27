#!/bin/sh
# The one place the Cargo workspace's checks are defined, matching the `test` job in
# .github/workflows/ci.yml. The commit hook calls it with --fast.
# Usage: ./scripts/check.sh [--fast]    --fast skips the tests.
#
# Not covered here: conformance/ (npm) and contracts/strk20-owner-example (Scarb), which have
# their own CI jobs, and desktop/, which is outside the workspace.
set -eu
cd "$(dirname "$0")/.."

cargo fmt --all --check
cargo build --locked --all-targets
cargo clippy --locked --all-targets -- -D warnings

if [ "${1:-}" = "--fast" ]; then
    exit 0
fi

cargo test --locked
