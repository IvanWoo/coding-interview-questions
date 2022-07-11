#!/bin/sh
set -euo pipefail

main() {
    NEW_PUZZLE="$(git status | grep "new file" | wc -l)"
    if [ "$NEW_PUZZLE" -ge 1 ]; then
        PUZZLE_NAME="$(git status | grep "new file" | awk -F "puzzles/" '{print $2}' | awk -F "." '{print $1}' | sed -n '/./{p;q;}')"
        git commit -m "feat: add ${PUZZLE_NAME}"
    fi
    EDIT_PUZZLE="$(git status | grep "modified" | wc -l)"
    if [ "$EDIT_PUZZLE" -ge 1 ]; then
        PUZZLE_NAME="$(git status | grep "modified" | awk -F "puzzles/" '{print $2}' | awk -F "." '{print $1}' | sed -n '/./{p;q;}')"
        git commit -m "refactor: revisit ${PUZZLE_NAME}"
    fi

    git whatchanged -1 --format=oneline
}

main
