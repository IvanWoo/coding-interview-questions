import pytest

from puzzles.construct_binary_tree_from_inorder_and_postorder_traversal import (
    build_tree,
)
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "inorder, postorder, expected",
    [
        (
            [9, 3, 15, 20, 7],
            [9, 15, 7, 20, 3],
            make_tree([3, 9, 20, None, None, 15, 7]),
        ),
        ([-1], [-1], make_tree([-1])),
    ],
)
def test_build_tree(inorder, postorder, expected):
    assert build_tree(inorder, postorder) == expected
