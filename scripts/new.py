import argparse
import pathlib

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
ROOT_DIR = SCRIPT_DIR.parent.resolve()
PUZZLES_DIR = ROOT_DIR / "puzzles"
TESTS_DIR = ROOT_DIR / "tests"


def _normalize_name(name):
    res = name.strip().lower()
    pairs = [(" ", "_"), ("-", "_"), ("'", "")]
    for old, new in pairs:
        res = res.replace(old, new)
    return res


def _create_new_puzzle(name):
    file_path = PUZZLES_DIR / f"{name}.py"
    if file_path.exists():
        print(f"Puzzle already exists: {name}")
        return
    print(f"Creating new puzzle: {name}")
    with file_path.open("w") as f:
        f.write("")


def _create_new_test(name):
    file_path = TESTS_DIR / f"test_{name}.py"
    if file_path.exists():
        print(f"Test already exists: {name}")
        return
    print(f"Creating new test: {name}")
    with file_path.open("w") as f:
        f.write(f"import pytest\n\nfrom puzzles.{name} import *\n\n")


def create(name):
    name = _normalize_name(name)
    _create_new_puzzle(name)
    _create_new_test(name)


def main():
    parser = argparse.ArgumentParser(description="Create a new puzzle")
    parser.add_argument("name", help="The name of the new puzzle")
    args = parser.parse_args()

    create(args.name)


if __name__ == "__main__":
    main()
