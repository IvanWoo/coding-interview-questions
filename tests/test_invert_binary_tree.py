import pytest

from puzzles.invert_binary_tree import invert_tree
from puzzles.utils import TreeNode


@pytest.fixture
def tree():
    ts = {i: TreeNode(i) for i in [1, 2, 3, 4, 6, 7, 9]}
    ts[4].left = ts[2]
    ts[4].right = ts[7]
    ts[2].left = ts[1]
    ts[2].right = ts[3]
    ts[7].left = ts[6]
    ts[7].right = ts[9]
    return ts


@pytest.fixture
def inverted_tree():
    ts = {i: TreeNode(i) for i in [1, 2, 3, 4, 6, 7, 9]}
    ts[4].left = ts[7]
    ts[4].right = ts[2]
    ts[2].left = ts[3]
    ts[2].right = ts[1]
    ts[7].left = ts[9]
    ts[7].right = ts[6]
    return ts


def test_invert_tree(tree, inverted_tree):
    assert invert_tree(tree[4]) == inverted_tree[4]
