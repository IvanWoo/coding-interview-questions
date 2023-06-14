import pytest

from puzzles.minimum_absolute_difference_in_bst import get_minimum_difference
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        ([4, 2, 6, 1, 3], 1),
        ([1, 0, 48, None, None, 12, 49], 1),
        ([236, 104, 701, None, 227, None, 911], 9),
        ([0, None, 100000], 100000),
    ],
)
def test_get_minimum_difference(root, expected):
    assert get_minimum_difference(make_tree(root)) == expected
