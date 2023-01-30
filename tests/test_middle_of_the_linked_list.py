import pytest

from puzzles.middle_of_the_linked_list import middle_node
from puzzles.utils import make_linked_list


@pytest.mark.parametrize(
    "head, expected",
    [
        (make_linked_list([1, 2, 3, 4, 5]), make_linked_list([3, 4, 5])),
        (make_linked_list([1, 2, 3, 4, 5, 6]), make_linked_list([4, 5, 6])),
    ],
)
def test_middle_node(head, expected):
    assert middle_node(head) == expected
