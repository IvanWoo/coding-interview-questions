import pytest

from puzzles.maximum_number_of_vowels_in_a_substring_of_given_length import max_vowels


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("abciiidef", 3, 3),
        ("aeiou", 2, 2),
        ("leetcode", 3, 2),
    ],
)
def test_max_vowels(s, k, expected):
    assert max_vowels(s, k) == expected
