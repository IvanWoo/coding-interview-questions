import pytest

from puzzles.maximum_level_sum_of_a_binary_tree import max_level_sum
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        ([1, 7, 0, 7, -8, None, None], 2),
        ([989, None, 10250, 98693, -89388, None, None, None, -32127], 2),
    ],
)
def test_max_level_sum(root, expected):
    assert max_level_sum(make_tree(root)) == expected
