import pytest
from puzzles.utils import TreeNode
from puzzles.construct_binary_search_tree_from_preorder_traversal import (
    bst_from_preorder,
)


@pytest.fixture
def tree42():
    ts = {x: TreeNode(x) for x in [4, 2]}
    ts[4].left = ts[2]
    return ts


@pytest.fixture
def tree():
    ts = {x: TreeNode(x) for x in [8, 5, 1, 7, 10, 12]}
    ts[8].left = ts[5]
    ts[8].right = ts[10]
    ts[5].left = ts[1]
    ts[5].right = ts[7]
    ts[10].right = ts[12]
    return ts


def test_bst_from_preorder(tree):
    assert bst_from_preorder([8, 5, 1, 7, 10, 12]) == tree[8]


def test_bst_from_preorder_42(tree42):
    assert bst_from_preorder([4, 2]) == tree42[4]
