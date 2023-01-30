import pytest

from puzzles.maximum_difference_between_node_and_ancestor import max_ancestor_diff
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]), 7),
        (make_tree([1, None, 2, None, 0, 3]), 3),
    ],
)
def test_max_ancestor_diff(root, expected):
    assert max_ancestor_diff(root) == expected
