import pytest
from puzzles.utils import make_tree
from puzzles.binary_tree_inorder_traversal import inorder_traversal


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([1, None, 2, 3]), [1, 3, 2]),
        (make_tree([1]), [1]),
        (make_tree([]), []),
    ],
)
def test_inorder_traversal(root, expected):
    assert inorder_traversal(root) == expected
