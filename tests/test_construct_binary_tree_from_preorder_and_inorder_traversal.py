import pytest

from puzzles.construct_binary_tree_from_preorder_and_inorder_traversal import build_tree
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "preorder, inorder, expected",
    [
        (
            [3, 9, 20, 15, 7],
            [9, 3, 15, 20, 7],
            make_tree([3, 9, 20, None, None, 15, 7]),
        ),
        (
            [3, 9],
            [9, 3],
            make_tree([3, 9]),
        ),
        ([-1], [-1], make_tree([-1])),
    ],
)
def test_build_tree(preorder, inorder, expected):
    assert build_tree(preorder, inorder) == expected
