import pytest

from puzzles.longest_zigzag_path_in_a_binary_tree import longest_zigzag
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1, None, 1],
            3,
        ),
        ([1, 1, 1, None, 1, None, None, 1, 1, None, 1], 4),
        ([1], 0),
    ],
)
def test_longest_zigzag(root, expected):
    assert longest_zigzag(make_tree(root)) == expected
