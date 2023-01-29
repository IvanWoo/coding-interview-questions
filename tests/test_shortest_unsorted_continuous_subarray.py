import pytest

from puzzles.shortest_unsorted_continuous_subarray import find_unsorted_subarray


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 6, 4, 8, 10, 9, 15], 5),
        ([1, 2, 3, 4], 0),
        ([1], 0),
    ],
)
def test_find_unsorted_subarray(nums: list[int], expected: int) -> None:
    assert find_unsorted_subarray(nums) == expected
