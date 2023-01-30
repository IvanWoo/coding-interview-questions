import pytest

from puzzles.longest_subsequence_with_limited_sum import answer_queries


@pytest.mark.parametrize(
    "nums, queries, expected",
    [
        ([4, 5, 2, 1], [3, 10, 21], [2, 3, 4]),
        ([2, 3, 4, 5], [1], [0]),
    ],
)
def test_answer_queries(nums, queries, expected):
    assert answer_queries(nums, queries) == expected
