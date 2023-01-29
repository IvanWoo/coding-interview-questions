import pytest

from puzzles.lowest_common_ancestor_of_a_binary_tree import lowest_common_ancestor
from puzzles.utils import find_tree, make_tree


@pytest.mark.parametrize(
    "root, p, q, expected",
    [
        (make_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), 5, 1, 3),
        (make_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), 5, 4, 5),
        (make_tree([1, 2]), 1, 2, 1),
    ],
)
def test_lowest_common_ancestor(root, p, q, expected):
    p_tree = find_tree(root, p)
    q_tree = find_tree(root, q)
    assert lowest_common_ancestor(root, p_tree, q_tree).val == expected
