import pytest

from puzzles.distribute_coins_in_binary_tree import distribute_coins
from puzzles.utils import TreeNode


@pytest.fixture
def tree1():
    root = TreeNode(0)
    root.left = TreeNode(3)
    root.right = TreeNode(0)
    return root


@pytest.fixture
def tree2():
    root = TreeNode(0)
    root.left = TreeNode(0)
    root.right = TreeNode(3)
    return root


@pytest.fixture
def tree3():
    root = TreeNode(3)
    root.left = TreeNode(0)
    root.right = TreeNode(0)
    return root


def test_distribute_coins_1(tree1):
    assert distribute_coins(tree1) == 3


def test_distribute_coins_2(tree2):
    assert distribute_coins(tree2) == 3


def test_distribute_coins_3(tree3):
    assert distribute_coins(tree3) == 2
