import pytest
from puzzles.utils import TreeNode
from puzzles.insert_into_bst import insert_into_bst


@pytest.fixture
def tree_input():
    ts = {x: TreeNode(x) for x in [1, 2, 3, 4, 7]}
    ts[4].left = ts[2]
    ts[4].right = ts[7]
    ts[2].left = ts[1]
    ts[2].right = ts[3]
    return ts


@pytest.fixture
def tree_ans():
    ts = {x: TreeNode(x) for x in [1, 2, 3, 4, 5, 7]}
    ts[4].left = ts[2]
    ts[4].right = ts[7]
    ts[2].left = ts[1]
    ts[2].right = ts[3]
    ts[7].left = ts[5]
    return ts


def test_insert_into_bst(tree_input, tree_ans):
    assert insert_into_bst(tree_input[4], 5) == tree_ans[4]
