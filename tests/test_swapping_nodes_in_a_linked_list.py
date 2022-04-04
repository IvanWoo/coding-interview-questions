import pytest
from puzzles.utils import ListNode
from puzzles.swapping_nodes_in_a_linked_list import swap_nodes


@pytest.fixture
def head():
    lns = {x: ListNode(x) for x in range(1, 6)}
    lns[1].next = lns[2]
    lns[2].next = lns[3]
    lns[3].next = lns[4]
    lns[4].next = lns[5]
    return lns[1]


@pytest.fixture
def ans():
    lns = {x: ListNode(x) for x in range(1, 6)}
    lns[1].next = lns[4]
    lns[4].next = lns[3]
    lns[3].next = lns[2]
    lns[2].next = lns[5]
    return lns[1]


def test_swap_nodes(head, ans):
    assert swap_nodes(head, 2) == ans
