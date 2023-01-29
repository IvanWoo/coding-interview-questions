import pytest

from puzzles.all_nodes_distance_k_in_binary_tree import distance_k
from puzzles.utils import TreeNode


@pytest.fixture
def tree():
    ts = {x: TreeNode(x) for x in range(9)}
    ts[3].left = ts[5]
    ts[3].right = ts[1]
    ts[5].left = ts[6]
    ts[5].right = ts[2]
    ts[2].left = ts[7]
    ts[2].right = ts[4]
    ts[1].left = ts[0]
    ts[1].right = ts[8]
    return ts


def test_distance_k(tree):
    assert sorted(distance_k(tree[3], TreeNode(5), 2)) == sorted([7, 4, 1])
