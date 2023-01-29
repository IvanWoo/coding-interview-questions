import pytest

from puzzles.maximum_score_from_performing_multiplication_operations import maximum_score


@pytest.mark.parametrize(
    "nums, multipliers, expected",
    [
        ([1, 2, 3], [3, 2, 1], 14),
        ([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6], 102),
    ],
)
def test_maximum_score(nums, multipliers, expected):
    assert maximum_score(nums, multipliers) == expected
