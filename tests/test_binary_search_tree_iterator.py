import pytest
from puzzles.utils import TreeNode
from puzzles.binary_search_tree_iterator import BSTIterator


@pytest.fixture
def root():
    return TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))


def test_binary_search_tree_iterator(root):
    bst = BSTIterator(root)
    assert bst.next() == 3
    assert bst.next() == 7
    assert bst.hasNext()
    assert bst.next() == 9
    assert bst.hasNext()
    assert bst.next() == 15
    assert bst.hasNext()
    assert bst.next() == 20
    assert not bst.hasNext()
