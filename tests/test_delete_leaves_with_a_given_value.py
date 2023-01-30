import pytest

from puzzles.delete_leaves_with_a_given_value import remove_leaf_nodes
from puzzles.utils import TreeNode


@pytest.fixture
def tree_input():
    ts = {
        k: TreeNode(v)
        for k, v in [(1, 1), (2, 2), (3, 3), (4, 4), ("21", 2), ("22", 2)]
    }
    ts[1].left = ts[2]
    ts[1].right = ts[3]
    ts[2].left = ts["21"]
    ts[3].left = ts["22"]
    ts[3].right = ts[4]
    return ts


@pytest.fixture
def tree_ans():
    ts = {x: TreeNode(x) for x in [1, 3, 4]}
    ts[1].right = ts[3]
    ts[3].right = ts[4]
    return ts


def test_remove_leaf_nodes(tree_input, tree_ans):
    assert remove_leaf_nodes(tree_input[1], 2) == tree_ans[1]
