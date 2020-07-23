import pytest
from puzzles.utils import TreeNode
from puzzles.bst_find_modes import FindModes


def test_find_modes():
    n1 = TreeNode(1)
    n22 = TreeNode(2)
    n23 = TreeNode(2)
    n1.right = n22
    n22.left = n23
    fm1 = FindModes()
    assert fm1.find_modes(n1) == [2]

    n2 = TreeNode(2)
    n12 = TreeNode(1)
    n2.left = n12
    fm2 = FindModes()
    assert fm2.find_modes(n2) == [1, 2]

