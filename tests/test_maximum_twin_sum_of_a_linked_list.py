import pytest

from puzzles.maximum_twin_sum_of_a_linked_list import pair_sum
from puzzles.utils import make_linked_list


@pytest.mark.parametrize(
    "head, expected",
    [
        ([5, 4, 2, 1], 6),
        ([4, 2, 2, 3], 7),
        ([1, 100000], 100001),
    ],
)
def test_pair_sum(head, expected):
    assert pair_sum(make_linked_list(head)) == expected
