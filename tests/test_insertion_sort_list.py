import pytest
from puzzles.utils import ListNode
from puzzles.insertion_sort_list import insertion_sort_list


@pytest.fixture
def ans():
    lns = {x: ListNode(x) for x in range(1, 6)}
    lns[1].next = lns[2]
    lns[2].next = lns[3]
    lns[3].next = lns[4]
    lns[4].next = lns[5]

    return lns


@pytest.fixture
def ls():
    lns = {x: ListNode(x) for x in range(1, 6)}
    lns[1].next = lns[4]
    lns[4].next = lns[3]
    lns[3].next = lns[2]
    lns[2].next = lns[5]

    return lns


def test_insertion_sort_list_1(ls, ans):
    assert insertion_sort_list(ls[1]) == ans[1]


def test_insertion_sort_list_2(ls, ans):
    assert insertion_sort_list(ls[4]) == ans[2]
