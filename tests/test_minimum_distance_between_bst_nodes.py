import pytest

from puzzles.minimum_distance_between_bst_nodes import min_diff_in_bst
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([4, 2, 6, 1, 3]), 1),
        (make_tree([1, 0, 48, None, None, 12, 49]), 1),
    ],
)
def test_min_diff_in_bst(root, expected):
    assert min_diff_in_bst(root) == expected
