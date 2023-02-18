import pytest

from puzzles.invert_binary_tree import invert_tree
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([4, 2, 7, 1, 3, 6, 9]), make_tree([4, 7, 2, 9, 6, 3, 1])),
        (make_tree([2, 1, 3]), make_tree([2, 3, 1])),
        (make_tree([]), make_tree([])),
    ],
)
def test_invert_tree(root, expected):
    assert invert_tree(root) == expected
