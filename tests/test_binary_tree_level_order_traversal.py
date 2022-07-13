import pytest
from puzzles.utils import make_tree
from puzzles.binary_tree_level_order_traversal import level_order


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([3, 9, 20, None, None, 15, 7]), [[3], [9, 20], [15, 7]]),
        (make_tree([1]), [[1]]),
        (make_tree([]), []),
    ],
)
def test_level_order(root, expected):
    assert level_order(root) == expected
