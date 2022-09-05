from typing import Optional
import pytest
from puzzles.utils import TreeNode, make_tree
from puzzles.utils import NaryNode, make_nary_node


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
def test_make_tree(vals: list[Optional[int]], expected: TreeNode):
    assert make_tree(vals) == expected


@pytest.mark.parametrize(
    "vals, expected",
    [
        (
            [1, None, 3, 2, 4, None, 5, 6],
            NaryNode(
                1, [NaryNode(3, [NaryNode(5), NaryNode(6)]), NaryNode(2), NaryNode(4)]
            ),
        )
    ],
)
def test_make_nary_node(vals, expected):
    print(make_nary_node(vals))
    assert make_nary_node(vals) == expected
