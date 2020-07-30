import pytest
from puzzles.utils import TreeNode
from puzzles.binary_tree_right_side_view import right_side_view


@pytest.fixture
def tree():
    ts = {x: TreeNode(x) for x in range(1, 6)}
    ts[1].left = ts[2]
    ts[1].right = ts[3]
    ts[2].left = ts[5]
    ts[3].left = ts[4]
    return ts


def test_right_side_view(tree):
    assert list(right_side_view(tree[1])) == [1, 3, 4]

