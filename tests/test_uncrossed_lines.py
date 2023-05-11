import pytest

from puzzles.uncrossed_lines import max_uncrossed_lines


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 4, 2], [1, 2, 4], 2),
        ([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2], 3),
        ([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1], 2),
    ],
)
def test_max_uncrossed_lines(nums1, nums2, expected):
    assert max_uncrossed_lines(nums1, nums2) == expected
