import pytest

from puzzles.reverse_linked_list_ii import reverse_between
from puzzles.utils import make_linked_list


@pytest.mark.parametrize(
    "head, m, n, ans",
    [
        (
            make_linked_list([1, 2, 3, 4, 5]),
            2,
            4,
            make_linked_list([1, 4, 3, 2, 5]),
        ),
        (make_linked_list([5]), 1, 1, make_linked_list([5])),
    ],
)
def test_reverse_between(head, m, n, ans):
    assert reverse_between(head, m, n) == ans
