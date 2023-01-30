import pytest

from puzzles.remove_duplicates_from_sorted_array import remove_duplicates


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 2], 2, [1, 2, None]),
        (
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
            5,
            [0, 1, 2, 3, 4, None, None, None, None, None],
        ),
    ],
)
def test_remove_duplicates(nums, k, expected):
    assert remove_duplicates(nums) == k
    for i in range(k):
        assert nums[i] == expected[i]
