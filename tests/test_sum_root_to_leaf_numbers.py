import pytest
from puzzles.utils import TreeNode
from puzzles.sum_root_to_leaf_numbers import sum_numbers


@pytest.fixture
def tree():
    ts = {x: TreeNode(x) for x in [4, 9, 0, 5, 1]}

    ts[4].left = ts[9]
    ts[4].right = ts[0]
    ts[9].left = ts[5]
    ts[9].right = ts[1]
    return ts


def test_sum_numbers(tree):
    assert sum_numbers(tree[4]) == (495 + 491 + 40)
