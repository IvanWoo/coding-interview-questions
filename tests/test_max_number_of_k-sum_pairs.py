import pytest

from puzzles.max_number_of_k_sum_pairs import max_operations


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 3, 4], 5, 2),
        ([3, 1, 3, 4, 3], 6, 1),
        ([1, 1, 1, 1, 1], 2, 2),
    ],
)
def test_max_operations(nums, k, expected):
    assert max_operations(nums, k) == expected
