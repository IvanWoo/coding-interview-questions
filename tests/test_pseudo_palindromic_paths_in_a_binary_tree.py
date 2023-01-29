import pytest

from puzzles.pseudo_palindromic_paths_in_a_binary_tree import pseudo_palindromic_paths
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([2, 3, 1, 3, 1, None, 1]), 2),
        (make_tree([2, 1, 1, 1, 3, None, None, None, None, None, 1]), 1),
        (make_tree([9]), 1),
    ],
)
def test_pseudo_palindromic_paths(root, expected):
    assert pseudo_palindromic_paths(root) == expected
