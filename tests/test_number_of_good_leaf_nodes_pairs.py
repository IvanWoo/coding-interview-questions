import pytest
from puzzles.utils import TreeNode
from puzzles.number_of_good_leaf_nodes_pairs import count_pairs


@pytest.fixture
def tree():
    ts = {x: TreeNode(x) for x in range(1, 5)}
    ts[1].left = ts[2]
    ts[1].right = ts[3]
    ts[2].right = ts[4]
    return ts


def test_count_pairs(tree):
    assert count_pairs(tree[1], 3) == 1
    assert count_pairs(tree[1], 2) == 0
    assert count_pairs(tree[1], 1) == 0
