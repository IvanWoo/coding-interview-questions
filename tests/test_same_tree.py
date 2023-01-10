import pytest
from puzzles.utils import make_tree
from puzzles.same_tree import is_same_tree


@pytest.mark.parametrize(
    "p, q, expected",
    [
        (make_tree([1, 2, 3]), make_tree([1, 2, 3]), True),
        (make_tree([1, 2]), make_tree([1, None, 2]), False),
        (make_tree([1, 2, 1]), make_tree([1, 1, 2]), False),
    ],
)
def test_is_same_tree(p, q, expected):
    assert is_same_tree(p, q) == expected
