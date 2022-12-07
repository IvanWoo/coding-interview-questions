import pytest
from puzzles.utils import make_tree
from puzzles.range_sum_of_bst import range_sum_BST


@pytest.mark.parametrize(
    "root, low, high, expected",
    [
        (make_tree([10, 5, 15, 3, 7, None, 18]), 7, 15, 32),
        (make_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6]), 6, 10, 23),
    ],
)
def test_range_sum_BST(root, low, high, expected):
    assert range_sum_BST(root, low, high) == expected
