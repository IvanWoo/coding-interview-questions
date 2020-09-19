import pytest
from puzzles.utils import TreeNode
from puzzles.maximum_difference_between_node_and_ancestor import max_ancestor_diff


@pytest.fixture
def tree_input():
    ts = {x: TreeNode(x) for x in [8, 3, 10, 1, 6, 14, 4, 7, 13]}
    ts[8].left = ts[3]
    ts[8].right = ts[10]
    ts[3].left = ts[1]
    ts[3].right = ts[6]
    ts[6].left = ts[4]
    ts[6].right = ts[7]
    ts[10].right = ts[14]
    ts[14].left = ts[13]
    return ts


def test_max_ancestor_diff(tree_input):
    assert max_ancestor_diff(tree_input[8]) == 7
