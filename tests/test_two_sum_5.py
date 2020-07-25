import pytest
from puzzles.utils import TreeNode
from puzzles.two_sum_5 import find_target


@pytest.fixture
def tree():
    ts = {i: TreeNode(i) for i in range(2, 8)}
    ts[5].left = ts[3]
    ts[5].right = ts[6]
    ts[3].left = ts[2]
    ts[3].right = ts[4]
    ts[6].right = ts[7]
    return ts


def test_findTarget(tree):
    assert find_target(tree[5], 9) == True
    assert find_target(tree[5], 13) == True
    assert find_target(tree[5], 28) == False
