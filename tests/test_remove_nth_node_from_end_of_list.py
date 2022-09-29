import pytest
from puzzles.utils import make_linked_list
from puzzles.remove_nth_node_from_end_of_list import remove_nth_from_end


@pytest.mark.parametrize(
    "head, n, expected",
    [
        (make_linked_list([1, 2, 3, 4, 5]), 2, make_linked_list([1, 2, 3, 5])),
        (make_linked_list([1]), 1, make_linked_list([])),
        (make_linked_list([1, 2]), 1, make_linked_list([1])),
    ],
)
def test_remove_nth_from_end(head, n, expected):
    assert remove_nth_from_end(head, n) == expected
