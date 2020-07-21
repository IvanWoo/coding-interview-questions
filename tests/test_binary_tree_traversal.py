import pytest
from puzzles.binary_tree_traversal import (
    inorder_traversal,
    preorder_traversal,
    postorder_traversal,
)
from utils import TreeNode


@pytest.fixture
def tree_13():
    ts = {i: TreeNode(i) for i in range(1, 4)}
    ts[1].right = ts[2]
    ts[2].left = ts[3]
    return ts


@pytest.fixture
def tree_15():
    ts = {i: TreeNode(i) for i in range(1, 6)}
    ts[1].left = ts[2]
    ts[1].right = ts[3]
    ts[2].left = ts[4]
    ts[2].right = ts[5]
    return ts


def test_inorder_traversal_13(tree_13):
    assert inorder_traversal(tree_13[1]) == [1, 3, 2]


def test_inorder_traversal_15(tree_15):
    assert inorder_traversal(tree_15[1]) == [4, 2, 5, 1, 3]


def test_preorder_traversal_13(tree_13):
    assert preorder_traversal(tree_13[1]) == [1, 2, 3]


def test_preorder_traversal_15(tree_15):
    assert preorder_traversal(tree_15[1]) == [1, 2, 4, 5, 3]


def test_postorder_traversal_13(tree_13):
    assert postorder_traversal(tree_13[1]) == [3, 2, 1]


def test_postorder_traversal_15(tree_15):
    assert postorder_traversal(tree_15[1]) == [4, 5, 2, 3, 1]
