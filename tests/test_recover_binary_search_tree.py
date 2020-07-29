import pytest
from puzzles.utils import TreeNode
from puzzles.recover_binary_search_tree import recover_tree


@pytest.fixture
def tree_input():
    ts = {x: TreeNode(x) for x in range(1, 5)}
    ts[3].left = ts[1]
    ts[3].right = ts[4]
    ts[4].left = ts[2]
    return ts


@pytest.fixture
def tree_ans():
    ts = {x: TreeNode(x) for x in range(1, 5)}
    ts[2].left = ts[1]
    ts[2].right = ts[4]
    ts[4].left = ts[3]
    return ts


def test_recover_tree(tree_input, tree_ans):
    recover_tree(tree_input[3])
    # 3 and 2 are keys reference the TreeNode rather than vals
    assert tree_input[3] == tree_ans[2]
