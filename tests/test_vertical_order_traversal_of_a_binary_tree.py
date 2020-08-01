import pytest
from puzzles.utils import TreeNode
from puzzles.vertical_order_traversal_of_a_binary_tree import vertical_traversal


@pytest.fixture
def tree():
    ts = {x: TreeNode(x) for x in range(12)}
    ts[0].left = ts[2]
    ts[0].right = ts[1]

    ts[2].left = ts[3]

    ts[3].left = ts[4]
    ts[3].right = ts[5]

    ts[4].right = ts[7]
    ts[7].left = ts[10]
    ts[7].right = ts[8]

    ts[5].left = ts[6]
    ts[6].left = ts[11]
    ts[6].right = ts[9]
    return ts


def test_vertical_traversal(tree):
    assert vertical_traversal(tree[0]) == [
        [4, 10, 11],
        [3, 6, 7],
        [2, 5, 8, 9],
        [0],
        [1],
    ]
