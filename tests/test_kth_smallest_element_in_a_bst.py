import pytest

from puzzles.kth_smallest_element_in_a_bst import kth_smallest
from puzzles.utils import TreeNode


@pytest.mark.parametrize(
    "root, k, expected",
    [
        (
            TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2))),
            1,
            1,
        ),
        (
            TreeNode(
                5, TreeNode(3, TreeNode(2, TreeNode(1), None), TreeNode(4)), TreeNode(6)
            ),
            3,
            3,
        ),
    ],
)
def test(root, k, expected):
    assert kth_smallest(root, k) == expected
