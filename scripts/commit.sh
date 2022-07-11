#!/bin/sh
set -euo pipefail

grep_file() {
    local grep_str="$1"
    local commit_prefix="$2"
    TARGET="$(git status | grep $grep_str | wc -l)"
    if [ "$TARGET" -ge 1 ]; then
        PUZZLE_NAME="$(git status | grep $grep_str | awk -F "puzzles/" '{print $2}' | awk -F "." '{print $1}' | sed -n '/./{p;q;}')"
        git commit -m "$commit_prefix ${PUZZLE_NAME}"
    fi
}

commit_new_file() {
    grep_file "new file" "feat: add"
}

commit_modified_file() {
    grep_file "modified" "refactor: revisit"
}

main() {
    local cmd="$1"
    case "$cmd" in
    new)
        commit_new_file
        ;;
    modified)
        commit_modified_file
        ;;
    *)
        echo "Usage: $0 {new|modified}"
        exit 1
        ;;
    esac

    git whatchanged -1 --format=oneline
}

main
