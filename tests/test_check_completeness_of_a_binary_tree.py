import pytest

from puzzles.check_completeness_of_a_binary_tree import is_complete_tree
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        ([1, 2, 3, 4, 5, 6], True),
        ([1, 2, 3, 4, 5, None, 7], False),
    ],
)
def test_is_complete_tree(root, expected):
    assert is_complete_tree(make_tree(root)) == expected
