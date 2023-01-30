import pytest

from puzzles.lowest_common_ancestor_of_a_binary_search_tree import (
    lowest_common_ancestor,
)
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, p, q, expected",
    [
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
        ([2, 1], 2, 1, 2),
    ],
)
def test_lowest_common_ancestor(root, p, q, expected):
    assert lowest_common_ancestor(make_tree(root), make_tree([p]), make_tree([q])).val == expected
