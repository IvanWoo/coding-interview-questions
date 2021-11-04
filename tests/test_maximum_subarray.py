import pytest
from puzzles.maximum_subarray import maximum_subarray


@pytest.mark.parametrize(
    ("nums", "expected"), [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6), ([5, 4, -1, 7, 8], 23)]
)
def test_maximum_subarray(nums, expected):
    assert maximum_subarray(nums) == expected
