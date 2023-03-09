import pytest

from puzzles.linked_list_cycle_ii import detect_cycle
from puzzles.utils import connect_linked_list, make_linked_list


@pytest.mark.parametrize(
    "head, pos",
    [
        ([3, 2, 0, -4], 1),
        ([1, 2], 0),
        ([1], -1),
    ],
)
def test_detect_cycle(head, pos):
    ll = make_linked_list(head)
    expected = None
    if pos != -1:
        expected = connect_linked_list(ll, head[-1], head[pos])

    assert detect_cycle(ll) == expected
