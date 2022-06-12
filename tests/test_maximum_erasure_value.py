import pytest
from puzzles.maximum_erasure_value import maximum_unique_subarray


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([4, 2, 4, 5, 6], 17),
        ([5, 2, 1, 2, 5, 2, 1, 2, 5], 8),
    ],
)
def test_maximum_unique_subarray(nums, expected):
    assert maximum_unique_subarray(nums) == expected
