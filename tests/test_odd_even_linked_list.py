import pytest

from puzzles.odd_even_linked_list import odd_even_list
from puzzles.utils import make_linked_list


@pytest.mark.parametrize(
    "head, expected",
    [
        (make_linked_list([1, 2, 3, 4, 5]), make_linked_list([1, 3, 5, 2, 4])),
        (
            make_linked_list([2, 1, 3, 5, 6, 4, 7]),
            make_linked_list([2, 3, 6, 7, 1, 5, 4]),
        ),
        (
            make_linked_list([1, 2, 3, 4, 5, 6, 7, 8]),
            make_linked_list([1, 3, 5, 7, 2, 4, 6, 8]),
        ),
    ],
)
def test_odd_even_list(head, expected):
    assert odd_even_list(head) == expected
