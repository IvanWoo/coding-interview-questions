import pytest

from puzzles.delete_node_in_a_linked_list import delete_node
from puzzles.utils import make_linked_list


@pytest.mark.parametrize(
    "head, node_val, expected",
    [
        (make_linked_list([4, 5, 1, 9]), 5, make_linked_list([4, 1, 9])),
        (make_linked_list([4, 5, 1, 9]), 1, make_linked_list([4, 5, 9])),
    ],
)
def test_delete_node(head, node_val, expected):
    node = head
    while node.val != node_val:
        node = node.next
    delete_node(node)
    assert head == expected
