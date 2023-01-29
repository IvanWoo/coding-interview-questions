import pytest

from puzzles.find_duplicate_file_in_system import find_duplicate


@pytest.mark.parametrize(
    "paths, expected",
    [
        (
            [
                "root/a 1.txt(abcd) 2.txt(efgh)",
                "root/c 3.txt(abcd)",
                "root/c/d 4.txt(efgh)",
                "root 4.txt(efgh)",
            ],
            [
                ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"],
                ["root/a/1.txt", "root/c/3.txt"],
            ],
        ),
        (
            [
                "root/a 1.txt(abcd) 2.txt(efgh)",
                "root/c 3.txt(abcd)",
                "root/c/d 4.txt(efgh)",
            ],
            [["root/a/2.txt", "root/c/d/4.txt"], ["root/a/1.txt", "root/c/3.txt"]],
        ),
    ],
)
def test_find_duplicate(paths, expected):
    assert sorted(find_duplicate(paths)) == sorted(expected)
