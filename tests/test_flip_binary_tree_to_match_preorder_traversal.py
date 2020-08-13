import pytest
from puzzles.utils import TreeNode
from puzzles.flip_binary_tree_to_match_preorder_traversal import flip_match_voyage


@pytest.fixture
def tree():
    ts = {x: TreeNode(x) for x in range(1, 4)}
    ts[1].left = ts[2]
    ts[1].right = ts[3]
    return ts


def test_flip_match_voyage_1(tree):
    assert flip_match_voyage(tree[1], [1, 3, 2]) == [1]


def test_flip_match_voyage_2(tree):
    assert flip_match_voyage(tree[1], [1, 2, 3]) == []


def test_flip_match_voyage_3(tree):
    assert flip_match_voyage(tree[1], [3, 1, 2]) == [-1]

