#!/bin/sh
set -euo pipefail
cd "$(git rev-parse --show-toplevel)" || exit 1

# Default git configuration
git config --local --bool pull.rebase true
git config --local --bool core.autocrlf false
git config --local core.hooksPath .githooks/
