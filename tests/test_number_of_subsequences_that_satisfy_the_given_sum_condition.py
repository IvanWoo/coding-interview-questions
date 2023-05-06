import pytest

from puzzles.number_of_subsequences_that_satisfy_the_given_sum_condition import (
    num_subseq,
)


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([3, 5, 6, 7], 9, 4),
        ([3, 3, 6, 8], 10, 6),
        ([2, 3, 3, 4, 6, 7], 12, 61),
    ],
)
def test_num_subseq(nums, target, expected):
    assert num_subseq(nums, target) == expected
