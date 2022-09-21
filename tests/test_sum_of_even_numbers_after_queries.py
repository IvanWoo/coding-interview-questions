import pytest
from puzzles.sum_of_even_numbers_after_queries import sum_even_after_queries


@pytest.mark.parametrize(
    "nums, queries, expected",
    [
        ([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]], [8, 6, 2, 4]),
        ([1], [[4, 0]], [0]),
    ],
)
def test_sum_even_after_queries(nums, queries, expected):
    assert sum_even_after_queries(nums, queries) == expected
