from cmath import exp

import pytest

from puzzles.ransom_note import can_construct


@pytest.mark.parametrize(
    "random_note, magazine, expected",
    [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
    ],
)
def test_can_construct(random_note, magazine, expected):
    assert can_construct(random_note, magazine) == expected
