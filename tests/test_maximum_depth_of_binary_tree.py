import pytest

from puzzles.maximum_depth_of_binary_tree import max_depth
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([3, 9, 20, None, None, 15, 7]), 3),
        (make_tree([1, None, 2]), 2),
    ],
)
def test_max_depth(root, expected):
    assert max_depth(root) == expected
