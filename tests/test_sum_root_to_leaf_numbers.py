import pytest

from puzzles.sum_root_to_leaf_numbers import sum_numbers
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        ([1, 2, 3], 25),
        ([4, 9, 0, 5, 1], 1026),
    ],
)
def test_sum_numbers(root, expected):
    assert sum_numbers(make_tree(root)) == expected
