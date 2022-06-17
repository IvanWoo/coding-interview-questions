from typing import Optional
import pytest
from puzzles.utils import TreeNode, make_tree


@pytest.mark.parametrize(
    "vals, expected",
    [
        ([0, 0, None, 0, 0], TreeNode(0, TreeNode(0, TreeNode(0), TreeNode(0)), None)),
        (
            [0, 0, None, 0, None, 0, None, None, 0],
            TreeNode(
                0,
                TreeNode(0, TreeNode(0, TreeNode(0, None, TreeNode(0)), None), None),
                None,
            ),
        ),
    ],
)
def test_make_tree(vals: list[Optional[int]], expected: bool):
    assert make_tree(vals) == expected
