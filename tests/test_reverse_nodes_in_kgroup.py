import pytest

from puzzles.reverse_nodes_in_kgroup import reverse_kgroup
from puzzles.utils import ListNode


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
    lns[2].next = lns[1]
    lns[1].next = lns[4]
    lns[4].next = lns[3]
    lns[3].next = lns[5]

    return lns[2]


def test_reverse_kgroup_2(ls, ans):
    assert reverse_kgroup(ls, 2) == ans
