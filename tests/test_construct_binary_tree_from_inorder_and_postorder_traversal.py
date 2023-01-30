import pytest

from puzzles.construct_binary_tree_from_inorder_and_postorder_traversal import (
    build_tree,
)
from puzzles.utils import TreeNode


@pytest.fixture
def tree_15():
    ts = {i: TreeNode(i) for i in range(1, 6)}
    ts[1].left = ts[2]
    ts[1].right = ts[3]
    ts[2].left = ts[4]
    ts[2].right = ts[5]
    return ts


def test_build_tree(tree_15):
    inorder = [4, 2, 5, 1, 3]
    postorder = [4, 5, 2, 3, 1]
    assert build_tree(inorder, postorder) == tree_15[1]
