import pytest

from puzzles.restore_the_array import number_of_arrays


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("1000", 10000, 1),
        ("1000", 10, 0),
        ("1317", 2000, 8),
    ],
)
def test_number_of_arrays(s, k, expected):
    assert number_of_arrays(s, k) == expected
