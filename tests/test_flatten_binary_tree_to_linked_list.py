import pytest

from puzzles.flatten_binary_tree_to_linked_list import flatten
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            make_tree([1, 2, 5, 3, 4, None, 6]),
            make_tree([1, None, 2, None, 3, None, 4, None, 5, None, 6]),
        ),
        (make_tree([]), make_tree([])),
        (make_tree([0]), make_tree([0])),
    ],
)
def test_flatten(root, expected):
    flatten(root)
    assert root == expected
