from cmath import exp
import pytest
from puzzles.kth_largest_element_in_an_array import find_kth_largest


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([3, 2, 1, 5, 6, 4], 1, 6),
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 1, 5, 6, 4], 6, 1),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ],
)
def test_find_kth_largest(nums, k, expected):
    assert find_kth_largest(nums, k) == expected
