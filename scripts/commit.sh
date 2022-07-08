#!/bin/sh
set -euo pipefail

main() {
    PUZZLE_NAME="$(git status | grep "new file" | awk -F "puzzles/" '{print $2}' | awk -F "." '{print $1}' | sed -n '/./{p;q;}')"
    if [ -z "${PUZZLE_NAME}" ]; then
        echo "No puzzle name found."
        exit 1
    fi
    git commit -m "feat: add ${PUZZLE_NAME}"
    git log --oneline | head -n 1
}

main
