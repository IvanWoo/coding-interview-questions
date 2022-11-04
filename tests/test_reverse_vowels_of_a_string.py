import pytest
from puzzles.reverse_vowels_of_a_string import reverse_vowels


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Sore was I ere I saw Eros.", "SorE was I ere I saw eros."),
        ("aA", "Aa"),
        ("hello", "holle"),
        ("leetcode", "leotcede"),
    ],
)
def test_reverse_vowels(s, expected):
    assert reverse_vowels(s) == expected
