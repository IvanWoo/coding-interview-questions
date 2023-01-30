from cmath import exp

import pytest

from puzzles.average_of_levels_in_binary_tree import average_of_levels
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([3, 9, 20, None, None, 15, 7]), [3.00000, 14.50000, 11.00000]),
        (make_tree([3, 9, 20, 15, 7]), [3.00000, 14.50000, 11.00000]),
    ],
)
def test_average_of_levels(root, expected):
    assert average_of_levels(root) == expected
