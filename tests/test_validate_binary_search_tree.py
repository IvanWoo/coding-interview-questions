import pytest

from puzzles.utils import make_tree
from puzzles.validate_binary_search_tree import is_valid_bst


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([2, 1, 3]), True),
        (make_tree([5, 1, 4, None, None, 3, 6]), False),
        (make_tree([5, 4, 6, None, None, 3, 7]), False),
        (make_tree([5, 4, 6, None, None, 5, 7]), False),
    ],
)
def test_is_valid_bst(root, expected):
    assert is_valid_bst(root) == expected
