import pytest
from puzzles.maximum_length_of_repeated_subarray import find_length


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 2, 3, 2, 1], [3, 2, 1, 4, 7], 3),
        ([0, 1, 1, 1, 1], [1, 0, 1, 0, 1], 2),
    ],
)
def test_find_length(nums1, nums2, expected):
    assert find_length(nums1, nums2) == expected
