import pytest

from puzzles.make_array_strictly_increasing import make_array_increasing


@pytest.mark.parametrize(
    "arr1, arr2, expected",
    [
        ([1, 5, 3, 6, 7], [1, 3, 2, 4], 1),
        ([1, 5, 3, 6, 7], [4, 3, 1], 2),
        ([1, 5, 3, 6, 7], [1, 6, 3, 3], -1),
    ],
)
def test_make_array_increasing(arr1, arr2, expected):
    assert make_array_increasing(arr1, arr2) == expected
