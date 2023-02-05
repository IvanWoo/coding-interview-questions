import pytest

from puzzles.find_all_anagrams_in_a_string import find_anagrams


@pytest.mark.parametrize(
    "s, p, expected",
    [
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
        ("baa", "aa", [1]),
    ],
)
def test_find_anagrams(s, p, expected):
    assert find_anagrams(s, p) == expected
