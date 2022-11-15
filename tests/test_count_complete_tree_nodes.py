import pytest
from puzzles.utils import make_tree
from puzzles.count_complete_tree_nodes import count_nodes


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([1, 2, 3, 4, 5, 6]), 6),
        (make_tree([]), 0),
        (make_tree([1]), 1),
    ],
)
def test_count_nodes(root, expected):
    assert count_nodes(root) == expected
