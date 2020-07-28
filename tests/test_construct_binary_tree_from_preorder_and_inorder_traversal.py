import pytest
from puzzles.utils import TreeNode
from puzzles.construct_binary_tree_from_preorder_and_inorder_traversal import build_tree


@pytest.fixture
def tree_15():
    ts = {i: TreeNode(i) for i in range(1, 6)}
    ts[1].left = ts[2]
    ts[1].right = ts[3]
    ts[2].left = ts[4]
    ts[2].right = ts[5]
    return ts


def test_build_tree(tree_15):
    preorder = [1, 2, 4, 5, 3]
    inorder = [4, 2, 5, 1, 3]
    assert build_tree(preorder, inorder) == tree_15[1]
