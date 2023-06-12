import pytest

from puzzles.summary_ranges import summary_ranges


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
    ],
)
def test_summary_ranges(nums, expected):
    assert summary_ranges(nums) == expected
