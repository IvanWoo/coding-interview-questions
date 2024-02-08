import pytest

from puzzles.two_sum_iv_input_is_a_bst import find_target
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, k, expected",
    [
        (make_tree([5, 3, 6, 2, 4, None, 7]), 9, True),
        (make_tree([5, 3, 6, 2, 4, None, 7]), 28, False),
    ],
)
def test_find_target(root, k, expected):
    assert find_target(root, k) == expected
