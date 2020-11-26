from puzzles.unique_binary_search_trees_ii import generate_trees
import pytest
from puzzles.utils import TreeNode


@pytest.fixture
def results():
    return [
        TreeNode(
            val=1,
            left=None,
            right=TreeNode(
                val=2, left=None, right=TreeNode(val=3, left=None, right=None)
            ),
        ),
        TreeNode(
            val=1,
            left=None,
            right=TreeNode(
                val=3, left=TreeNode(val=2, left=None, right=None), right=None
            ),
        ),
        TreeNode(
            val=2,
            left=TreeNode(val=1, left=None, right=None),
            right=TreeNode(val=3, left=None, right=None),
        ),
        TreeNode(
            val=3,
            left=TreeNode(
                val=1, left=None, right=TreeNode(val=2, left=None, right=None)
            ),
            right=None,
        ),
        TreeNode(
            val=3,
            left=TreeNode(
                val=2, left=TreeNode(val=1, left=None, right=None), right=None
            ),
            right=None,
        ),
    ]


def test_generate_trees(results):
    assert generate_trees(3) == results
