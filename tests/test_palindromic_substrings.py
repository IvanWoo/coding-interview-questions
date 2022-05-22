import pytest
from puzzles.palindromic_substrings import count_substrings


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abc", 3),
        ("aaa", 6),
        ("a", 1),
        ("", 0),
        ("abcd", 4),
    ],
)
def test_count_substrings(s, expected):
    assert count_substrings(s) == expected
