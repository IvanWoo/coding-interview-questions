import pytest
from puzzles.utils import TreeNode
from puzzles.binary_tree_pruning import prune_tree


@pytest.fixture
def tree_input():
    ts = {k: TreeNode(v) for k, v in [("11", 1), ("12", 1), ("01", 0), ("02", 0)]}
    ts["11"].left = ts["01"]
    ts["01"].left = ts["02"]
    ts["01"].right = ts["12"]
    return ts


@pytest.fixture
def tree_ans():
    ts = {k: TreeNode(v) for k, v in [("11", 1), ("12", 1), ("01", 0), ("02", 0)]}
    ts["11"].left = ts["01"]
    ts["01"].right = ts["12"]
    return ts


def test_prune_tree(tree_input, tree_ans):
    assert prune_tree(tree_input["11"]) == tree_ans["11"]
