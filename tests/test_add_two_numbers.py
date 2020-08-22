import pytest
from puzzles.utils import ListNode
from puzzles.add_two_numbers import add_two_numbers


@pytest.fixture
def ls():
    lns = {x: ListNode(x) for x in range(1, 7)}
    lns[1].next = lns[2]
    lns[2].next = lns[3]

    lns[4].next = lns[5]
    lns[5].next = lns[6]

    return lns[1], lns[4]


@pytest.fixture
def ans():
    lns = {x: ListNode(x) for x in [5, 7, 9]}
    lns[5].next = lns[7]
    lns[7].next = lns[9]
    return lns[5]


def test_add_two_numbers(ls, ans):
    assert add_two_numbers(*ls) == ans
