from copy import deepcopy

import pytest

from puzzles.find_a_corresponding_node_of_a_binary_tree_in_a_clone_of_that_tree import get_target_copy
from puzzles.utils import TreeNode


@pytest.fixture
def tree():
    return TreeNode(
        7,
        TreeNode(
            4,
        ),
        TreeNode(3, TreeNode(6, TreeNode(19))),
    )


@pytest.fixture
def tree_non_unique():
    return TreeNode(
        7,
        TreeNode(
            4,
        ),
        TreeNode(7, TreeNode(6, TreeNode(19))),
    )


def test_get_target_copy(tree):
    original = deepcopy(tree)
    cloned = deepcopy(tree)
    target = cloned.right
    assert get_target_copy(original, cloned, target) is target


def test_get_target_copy_non_unique(tree_non_unique):
    original = deepcopy(tree_non_unique)
    cloned = deepcopy(tree_non_unique)
    target = cloned.right
    assert get_target_copy(original, cloned, target) is target
