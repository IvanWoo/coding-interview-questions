import pytest

from puzzles.convert_sorted_list_to_binary_search_tree import sorted_list_to_BST
from puzzles.utils import make_linked_list, make_tree


@pytest.mark.parametrize(
    "head, expected",
    [
        (make_linked_list([-10, -3, 0, 5, 9]), make_tree([0, -3, 9, -10, None, 5])),
        (None, None),
    ],
)
def test_sorted_list_to_BST(head, expected):
    assert sorted_list_to_BST(head) == expected
