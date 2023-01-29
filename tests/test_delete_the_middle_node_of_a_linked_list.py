import pytest

from puzzles.delete_the_middle_node_of_a_linked_list import delete_middle
from puzzles.utils import make_linked_list


@pytest.mark.parametrize(
    "head, expected",
    [
        (make_linked_list([1, 3, 4, 7, 1, 2, 6]), make_linked_list([1, 3, 4, 1, 2, 6])),
        (make_linked_list([1, 2, 3, 4]), make_linked_list([1, 2, 4])),
        (make_linked_list([2, 1]), make_linked_list([2])),
    ],
)
def test_delete_middle(head, expected):
    assert delete_middle(head) == expected
