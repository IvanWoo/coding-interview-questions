import pytest

from puzzles.maximum_width_of_binary_tree import width_of_binary_tree
from puzzles.utils import TreeNode


@pytest.fixture
def tree_17():
    ts = {x: TreeNode(x) for x in range(1, 8)}
    ts[1].left = ts[2]
    ts[1].right = ts[3]
    ts[2].left = ts[4]
    ts[3].right = ts[5]
    ts[4].left = ts[6]
    ts[5].right = ts[7]
    return ts


@pytest.fixture
def tree_16():
    ts = {x: TreeNode(x) for x in range(1, 7)}
    ts[1].left = ts[3]
    ts[1].right = ts[2]
    ts[3].left = ts[5]
    ts[3].right = ts[4]
    ts[2].right = ts[6]
    return ts


def test_width_of_binary_tree_17(tree_17):
    assert width_of_binary_tree(tree_17[1]) == 8


def test_width_of_binary_tree_16(tree_16):
    assert width_of_binary_tree(tree_16[1]) == 4
