import pytest

from puzzles.kth_missing_positive_number import find_kth_positive


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([2, 3, 4, 7, 11], 5, 9),
        ([1, 2, 3, 4], 2, 6),
    ],
)
def test_find_kth_positive(arr, k, expected):
    assert find_kth_positive(arr, k) == expected
