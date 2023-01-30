import pytest

from puzzles.sum_of_subarray_minimums import sum_subarray_mins


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 1], 3),
        ([3, 1, 2, 4], 17),
        ([11, 81, 94, 43, 3], 444),
    ],
)
def test_sum_subarray_mins(arr, expected):
    assert sum_subarray_mins(arr) == expected
