from tkinter.tix import Tree
import pytest
from puzzles.utils import TreeNode
from puzzles.increasing_order_search_tree import increasing_BST


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6)),
            TreeNode(
                2,
                None,
                TreeNode(
                    3,
                    None,
                    TreeNode(4, None, TreeNode(5, None, TreeNode(6))),
                ),
            ),
        ),
        (
            TreeNode(5, TreeNode(1), TreeNode(7)),
            TreeNode(1, None, TreeNode(5, None, TreeNode(7))),
        ),
    ],
)
def test(root, expected):
    assert increasing_BST(root) == expected
