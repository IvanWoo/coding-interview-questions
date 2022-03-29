from importlib import import_module
import pytest
from puzzles.search_in_rotated_sorted_array import search


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
    ],
)
def test_search(nums, target, expected):
    assert search(nums, target) == expected
