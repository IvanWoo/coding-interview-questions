import pytest

from puzzles.partition_list import partition
from puzzles.utils import make_linked_list


@pytest.mark.parametrize(
    "head, x, expected",
    [
        (make_linked_list([1, 4, 3, 2, 5, 2]), 3, make_linked_list([1, 2, 2, 4, 3, 5])),
        (make_linked_list([2, 1]), 2, make_linked_list([1, 2])),
    ],
)
def test_partition(head, x, expected):
    assert partition(head, x) == expected
