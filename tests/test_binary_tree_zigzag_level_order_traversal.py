import pytest

from puzzles.binary_tree_zigzag_level_order_traversal import zigzag_level_order
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([3, 9, 20, None, None, 15, 7]), [[3], [20, 9], [15, 7]]),
        (make_tree([1]), [[1]]),
        (make_tree([]), []),
    ],
)
def test_zigzag_level_order(root, expected):
    assert zigzag_level_order(root) == expected
