import pytest
from puzzles.utils import make_tree
from puzzles.binary_tree_right_side_view import right_side_view


@pytest.mark.parametrize(
    "tree,expected",
    [
        (make_tree([1, 2, 3, None, 5, None, 4]), [1, 3, 4]),
        (make_tree([1, 3]), [1, 3]),
        (make_tree([]), []),
    ],
)
def test_right_side_view(tree, expected):
    assert list(right_side_view(tree)) == expected
