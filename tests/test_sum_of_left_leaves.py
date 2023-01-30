import pytest

from puzzles.sum_of_left_leaves import sum_of_left_leaves
from puzzles.utils import TreeNode


@pytest.fixture
def tree():
    ts = {i: TreeNode(i) for i in [3, 9, 20, 15, 7]}
    ts[3].left = ts[9]
    ts[3].right = ts[20]
    ts[20].left = ts[15]
    ts[20].right = ts[7]
    return ts


def test_sum_of_left_leaves(tree):
    assert sum_of_left_leaves(tree[3]) == 24
    assert sum_of_left_leaves(tree[20]) == 15
    assert sum_of_left_leaves(tree[9]) == 0
