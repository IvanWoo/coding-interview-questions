import pytest

from puzzles.swap_nodes_in_pairs import swap_pairs
from puzzles.utils import make_linked_list


@pytest.mark.parametrize(
    "head, expected",
    [
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([], []),
        ([1], [1]),
    ],
)
def test_swap_pairs(head, expected):
    assert swap_pairs(make_linked_list(head)) == make_linked_list(expected)
