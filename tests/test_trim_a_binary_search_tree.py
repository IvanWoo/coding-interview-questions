import pytest
from puzzles.utils import TreeNode
from puzzles.trim_a_binary_search_tree import trim_BST


@pytest.mark.parametrize(
    "root, low, high, expected",
    [
        (TreeNode(1, TreeNode(0), TreeNode(2)), 1, 2, TreeNode(1, None, TreeNode(2))),
        (
            TreeNode(3, TreeNode(0, None, TreeNode(2, TreeNode(1), None)), TreeNode(4)),
            1,
            3,
            TreeNode(3, TreeNode(2, TreeNode(1), None), None),
        ),
    ],
)
def test_trim_BST(root, low, high, expected):
    assert trim_BST(root, low, high) == expected
