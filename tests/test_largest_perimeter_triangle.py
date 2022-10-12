import pytest
from puzzles.largest_perimeter_triangle import largest_perimeter


@pytest.mark.parametrize("nums, expected", [([2, 1, 2], 5), ([1, 2, 1], 0)])
def test_largest_perimeter(nums, expected):
    assert largest_perimeter(nums) == expected
