import pytest
from puzzles.utils import TreeNode
from puzzles.longest_univalue_path import longest_univalue_path


@pytest.fixture
def tree():
    ts = {
        k: TreeNode(v)
        for k, v in [(1, 1), ("41", 4), ("42", 4), ("43", 4), ("51", 5), ("52", 5)]
    }
    ts[1].left = ts["41"]
    ts[1].right = ts["51"]
    ts["41"].left = ts["42"]
    ts["41"].right = ts["43"]
    ts["51"].left = ts["52"]
    return ts


def test_longest_univalue_path1(tree):
    assert longest_univalue_path(tree[1]) == 2
