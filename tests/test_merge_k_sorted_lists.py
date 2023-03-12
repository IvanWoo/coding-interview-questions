import pytest

from puzzles.merge_k_sorted_lists import merge_k_lists
from puzzles.utils import make_linked_list


@pytest.mark.parametrize(
    "lists, expected",
    [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
    ],
)
def test_merge_k_lists(lists, expected):
    assert merge_k_lists([make_linked_list(l) for l in lists]) == make_linked_list(
        expected
    )
