import pytest

from puzzles.swap_nodes_in_pairs import swap_pairs
from puzzles.utils import ListNode


@pytest.fixture
def ls():
    lns = {x: ListNode(x) for x in range(1, 5)}
    lns[1].next = lns[2]
    lns[2].next = lns[3]
    lns[3].next = lns[4]

    return lns[1]


@pytest.fixture
def ans():
    lns = {x: ListNode(x) for x in range(1, 5)}
    lns[2].next = lns[1]
    lns[1].next = lns[4]
    lns[4].next = lns[3]

    return lns[2]


def test_swap_pairs(ls, ans):
    assert swap_pairs(ls) == ans
