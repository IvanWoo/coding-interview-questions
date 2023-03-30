import pytest

from puzzles.scramble_string import is_scramble


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("greatly", "rgeat", False),
        ("great", "rgeat", True),
        ("abcde", "caebd", False),
        ("a", "a", True),
        ("abcdbdacbdac", "bdacabcdbdac", True),
    ],
)
def test_is_scramble(s1, s2, expected):
    assert is_scramble(s1, s2) == expected
