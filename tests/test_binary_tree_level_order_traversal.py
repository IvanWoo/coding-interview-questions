import pytest
from puzzles.utils import TreeNode
from puzzles.binary_tree_level_order_traversal import level_order


@pytest.fixture
def tree():
    ts = {x: TreeNode(x) for x in [3, 7, 9, 15, 20]}
    ts[3].left = ts[9]
    ts[3].right = ts[20]
    ts[20].left = ts[15]
    ts[20].right = ts[7]
    return ts


def test_level_order(tree):
    assert level_order(tree[3]) == [[3], [9, 20], [15, 7]]
