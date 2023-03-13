import pytest

from puzzles.symmetric_tree import is_symmetric
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([1, 2, 2, 3, 4, 4, 3]), True),
        (make_tree([1, 2, 2, None, 3, None, 3]), False),
    ],
)
def test_is_symmetric(root, expected):
    assert is_symmetric(root) == expected
