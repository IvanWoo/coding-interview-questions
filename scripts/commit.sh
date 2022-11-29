#!/bin/sh
set -euo pipefail

_check_count() {
    echo "Check count for $1"
    if [ $(git status | grep "$1" | wc -l) -eq 0 ]; then
        echo "Count of target files($1) is 0"
        exit 1
    fi
}

commit_new_file() {
    _check_count "new file"
    PUZZLE_NAME="$(git status | grep "new file" | awk -F "puzzles/" '{print $2}' | awk -F "." '{print $1}' | sed -n '/./{p;q;}')"
    if [ -z "${PUZZLE_NAME}" ]; then
        echo "No puzzle name found."
        exit 1
    fi
    git commit -m "feat: add ${PUZZLE_NAME}"
}

commit_modified_file() {
    _check_count "modified"
    PUZZLE_NAME="$(git status | grep "modified" | awk -F "puzzles/" '{print $2}' | awk -F "." '{print $1}' | sed -n '/./{p;q;}')"
    if [ -z "${PUZZLE_NAME}" ]; then
        echo "No puzzle name found."
        exit 1
    fi
    git commit -m "refactor: revisit ${PUZZLE_NAME}"
}

usage() {
    echo "Usage: $0 [new|modified]"
    echo "  new: commit new files"
    echo "  modified: commit modified files"
    exit 1
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
        usage
        exit 1
        ;;
    esac

    git whatchanged -1 --format=oneline
}

if [ $# -eq 0 ]; then
    usage
    exit 1
fi

main "$@"
