import pytest

from puzzles.deepest_leaves_sum import deepest_leaves_sum
from puzzles.utils import TreeNode


@pytest.fixture
def tree():
    return TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(4, TreeNode(7), None),
            TreeNode(5),
        ),
        TreeNode(3, None, TreeNode(6, None, TreeNode(8))),
    )


def test_deepest_leaves_sum(tree):
    assert deepest_leaves_sum(tree) == 15
