import pytest
from puzzles.reduce_array_size_to_the_half import min_set_size


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([3, 3, 3, 3, 5, 5, 5, 2, 2, 7], 2),
        ([7, 7, 7, 7, 7, 7], 1),
    ],
)
def test_min_set_size(arr, expected):
    assert min_set_size(arr) == expected
