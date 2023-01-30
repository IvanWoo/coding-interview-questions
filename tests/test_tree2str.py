import pytest

from puzzles.tree2str import tree2str
from puzzles.utils import TreeNode


@pytest.fixture
def tree_14():
    ts = {i: TreeNode(i) for i in range(1, 5)}
    ts[1].left = ts[2]
    ts[1].right = ts[3]
    ts[2].left = ts[4]
    return ts


def test_tree2str(tree_14):
    assert tree2str(tree_14[1]) == "1(2(4))(3)"
