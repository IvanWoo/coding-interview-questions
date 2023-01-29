import string

import pytest

from puzzles.remove_all_adjacent_duplicates_in_string_ii import remove_duplicates

long_string = string.ascii_lowercase * int(1e3)


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("abcd", 2, "abcd"),
        ("deeedbbcccbdaa", 3, "aa"),
        ("pbbcggttciiippooaais", 2, "ps"),
        ("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4, "ybth"),
        (long_string, 2, long_string),
    ],
)
def test_remove_duplicates(s, k, expected):
    assert remove_duplicates(s, k) == expected
