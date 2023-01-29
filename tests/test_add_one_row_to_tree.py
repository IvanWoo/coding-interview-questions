import pytest

from puzzles.add_one_row_to_tree import add_one_row
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, val, depth, expected",
    [
        (
            make_tree([4, 2, 6, 3, 1, 5]),
            1,
            2,
            make_tree([4, 1, 1, 2, None, None, 6, 3, 1, 5]),
        ),
        (
            make_tree([4, 2, 6, 3, 1, 5]),
            1,
            1,
            make_tree([1, 4, None, 2, 6, 3, 1, 5]),
        ),
        (
            make_tree([4, 2, None, 3, 1]),
            1,
            3,
            make_tree([4, 2, None, 1, 1, 3, None, None, 1]),
        ),
    ],
)
def test_add_one_row(root, val, depth, expected):
    assert add_one_row(root, val, depth) == expected
