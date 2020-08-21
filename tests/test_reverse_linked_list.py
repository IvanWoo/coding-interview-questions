import pytest
from puzzles.utils import ListNode
from puzzles.reverse_linked_list import reverse_list


@pytest.fixture
def ls():
    lns = {x: ListNode(x) for x in range(1, 6)}
    lns[1].next = lns[2]
    lns[2].next = lns[3]
    lns[3].next = lns[4]
    lns[4].next = lns[5]

    return lns[1]


@pytest.fixture
def ans():
    lns = {x: ListNode(x) for x in range(1, 6)}
    lns[5].next = lns[4]
    lns[4].next = lns[3]
    lns[3].next = lns[2]
    lns[2].next = lns[1]

    return lns[5]


def test_reverse_list(ls, ans):
    assert reverse_list(ls) == ans
