import pytest

from puzzles.find_duplicate_subtrees import find_duplicate_subtrees
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        ([1, 2, 3, 4, None, 2, 4, None, None, 4], [[2, 4], [4]]),
        ([2, 1, 1], [[1]]),
        ([2, 2, 2, 3, None, 3, None], [[2, 3], [3]]),
        ([0, 0, 0, 0, None, None, 0, None, None, None, 0], [[0]]),
    ],
)
def test_find_duplicate_subtrees(root, expected):
    # TODO: make the assert order insensitive
    assert find_duplicate_subtrees(make_tree(root)) == [make_tree(x) for x in expected]
