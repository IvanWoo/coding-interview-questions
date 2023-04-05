import pytest

from puzzles.minimize_maximum_of_array import minimize_array_value


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 7, 1, 6], 5),
        ([10, 1], 10),
        ([13, 13, 20, 0, 8, 9, 9], 16),
    ],
)
def test_minimize_array_value(nums, expected):
    assert minimize_array_value(nums) == expected
