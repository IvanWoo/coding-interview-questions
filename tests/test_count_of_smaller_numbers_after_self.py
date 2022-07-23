import pytest
from puzzles.count_of_smaller_numbers_after_self import count_smaller


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([5, 2, 6, 1], [2, 1, 1, 0]),
        ([-1], [0]),
        ([-1, -1], [0, 0]),
    ],
)
def test_count_smaller(nums, expected):
    assert count_smaller(nums) == expected
