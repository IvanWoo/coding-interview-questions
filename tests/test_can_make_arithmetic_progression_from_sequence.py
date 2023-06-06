import pytest

from puzzles.can_make_arithmetic_progression_from_sequence import (
    can_make_arithmetic_progression,
)


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([3, 5, 1], True),
        ([1, 2, 4], False),
    ],
)
def test_can_make_arithmetic_progression(arr, expected):
    assert can_make_arithmetic_progression(arr) == expected
