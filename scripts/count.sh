#!/bin/sh
set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="${BASE_DIR}/.."

main() {
    cd "${REPO_DIR}"
    echo "puzzles:"
    ls ./puzzles/ | grep '^[a-z]' | wc -l
    echo "tests:"
    ls ./tests/ | grep '^[a-z]' | wc -l
}

main
