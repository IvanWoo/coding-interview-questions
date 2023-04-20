import pytest

from puzzles.maximum_width_of_binary_tree import width_of_binary_tree
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        ([1, 3, 2, 5, 3, None, 9], 4),
        ([1, 3, 2, 5, None, None, 9, 6, None, 7], 7),
        ([1, 3, 2, 5], 2),
        (
            [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                None,
                None,
                None,
                1,
                None,
                None,
                None,
                None,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                None,
                2,
                None,
                None,
                2,
                None,
                2,
            ],
            8,
        ),
    ],
)
def test_width_of_binary_tree(root, expected):
    assert width_of_binary_tree(make_tree(root)) == expected
