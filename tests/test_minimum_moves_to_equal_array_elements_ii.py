import pytest
from puzzles.minimum_moves_to_equal_array_elements_ii import min_moves_2


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3], 2),
        ([1, 10, 2, 9], 16),
        ([1, 0, 0, 8, 6], 14),
        ([1, 2, 0, 0, 8, 6], 15),
    ],
)
def test_min_moves_2(nums, expected):
    assert min_moves_2(nums) == expected
