import pytest
from puzzles.utils import TreeNode
from puzzles.recover_binary_search_tree import recover_tree


@pytest.mark.parametrize(
    "tree, ans",
    [
        (
            TreeNode(1, TreeNode(3, None, TreeNode(2)), None),
            TreeNode(3, TreeNode(1, None, TreeNode(2)), None),
        ),
        (
            TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2), None)),
            TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3), None)),
        ),
    ],
)
def test_recover_tree(tree, ans):
    recover_tree(tree)
    assert tree == ans
