import pytest
from puzzles.contains_duplicate_ii import contains_nearby_duplicate


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 0, 1, 1], 0, False),
        ([1, 2, 3, 1, 2, 3], 2, False),
    ],
)
def test_contains_nearby_duplicate(nums, k, expected):
    assert contains_nearby_duplicate(nums, k) == expected
