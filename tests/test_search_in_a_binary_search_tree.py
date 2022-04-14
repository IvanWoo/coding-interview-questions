import pytest
from puzzles.utils import TreeNode
from puzzles.search_in_a_binary_search_tree import search_BST


@pytest.fixture
def root():
    return TreeNode(
        4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))
    )


@pytest.fixture
def root_expected():
    return TreeNode(2, TreeNode(1), TreeNode(3))


@pytest.fixture
def root_empty():
    return None


def test_search_BST(root, root_expected):
    assert search_BST(root, 2) == root_expected


def test_search_BST_empty(root, root_empty):
    assert search_BST(root, 5) == root_empty
