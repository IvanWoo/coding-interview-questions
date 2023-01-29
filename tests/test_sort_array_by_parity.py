import pytest

from puzzles.sort_array_by_parity import sort_array_by_parity


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 1, 2, 4], [2, 4, 3, 1]),
        ([0], [0]),
        ([1, 2, 3, 4], [2, 4, 1, 3]),
    ],
)
def test_sort_array_by_parity(nums: list[int], expected: list[int]) -> None:
    assert sort_array_by_parity(nums) == expected
