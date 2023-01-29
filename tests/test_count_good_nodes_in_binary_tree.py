from cmath import exp

import pytest

from puzzles.count_good_nodes_in_binary_tree import good_nodes
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([3, 1, 4, 3, None, 1, 5]), 4),
        (make_tree([3, 3, None, 4, 2]), 3),
        (make_tree([1]), 1),
    ],
)
def test_good_nodes(root, expected):
    assert good_nodes(root) == expected
