from ssl import HAS_ALPN

import pytest

from puzzles.path_sum import has_path_sum
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, target_sum, expected",
    [
        (make_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22, True),
        (make_tree([1, 2, 3]), 5, False),
        (make_tree([]), 0, False),
        (make_tree([1, 2]), 1, False),
    ],
)
def test_has_path_sum(root, target_sum, expected):
    assert has_path_sum(root, target_sum) == expected
