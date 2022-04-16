import pytest
from puzzles.utils import TreeNode
from puzzles.convert_bst_to_greater_tree import convert_BST


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(
                4,
                TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))),
                TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))),
            ),
            TreeNode(
                30,
                TreeNode(36, TreeNode(36), TreeNode(35, None, TreeNode(33))),
                TreeNode(21, TreeNode(26), TreeNode(15, None, TreeNode(8))),
            ),
        ),
        (TreeNode(0), TreeNode(0)),
        (TreeNode(0, None, TreeNode(1)), TreeNode(1, None, TreeNode(1))),
    ],
)
def test_convert_BST(root, expected):
    assert convert_BST(root) == expected
