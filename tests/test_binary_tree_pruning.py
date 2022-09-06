import pytest
from puzzles.utils import make_tree
from puzzles.binary_tree_pruning import prune_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([1, None, 0, 0, 1]), make_tree([1, None, 0, None, 1])),
        (make_tree([1, 0, 1, 0, 0, 0, 1]), make_tree([1, None, 1, None, 1])),
        (make_tree([1, 1, 0, 1, 1, 0, 1, 0]), make_tree([1, 1, 0, 1, 1, None, 1])),
        (make_tree([0]), None),
    ],
)
def test_prune_tree(root, expected):
    assert prune_tree(root) == expected
