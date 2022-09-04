import pytest
from puzzles.utils import make_tree
from puzzles.vertical_order_traversal_of_a_binary_tree import vertical_traversal


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([3, 9, 20, None, None, 15, 7]), [[9], [3, 15], [20], [7]]),
        (make_tree([1, 2, 3, 4, 5, 6, 7]), [[4], [2], [1, 5, 6], [3], [7]]),
        (make_tree([1, 2, 3, 4, 6, 5, 7]), [[4], [2], [1, 5, 6], [3], [7]]),
    ],
)
def test_vertical_traversal(root, expected):
    assert vertical_traversal(root) == expected
