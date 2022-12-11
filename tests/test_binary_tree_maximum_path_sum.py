import pytest
from puzzles.utils import make_tree
from puzzles.binary_tree_maximum_path_sum import max_path_sum


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([1, 2, 3]), 6),
        (make_tree([-10, 9, 20, None, None, 15, 7]), 42),
        (make_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 48),
    ],
)
def test_max_path_sum(root, expected):
    assert max_path_sum(root) == expected
