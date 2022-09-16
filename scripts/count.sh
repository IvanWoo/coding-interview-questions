#!/bin/sh
set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="${BASE_DIR}/.."

count_files() {
    local t=$1
    echo "$t:"
    ls ./$t/ | grep '^[a-z]' | wc -l
}

main() {
    cd "${REPO_DIR}"
    types=(puzzles tests docs)
    for t in "${types[@]}"; do
        count_files $t
    done
}

main
