import pytest
from puzzles.numbers_with_same_consecutive_differences import nums_same_consec_diff


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (3, 7, [181, 292, 707, 818, 929]),
        (2, 1, [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]),
    ],
)
def test_nums_same_consec_diff(n, k, expected):
    assert sorted(nums_same_consec_diff(n, k)) == sorted(expected)
