import pytest

from puzzles.find_k_closest_elements import find_closest_elements


@pytest.mark.parametrize(
    "arr, k, x, expected",
    [
        ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
        ([1, 1, 1, 10, 10, 10], 1, 9, [10]),
    ],
)
def test_find_closest_elements(arr, k, x, expected):
    assert find_closest_elements(arr, k, x) == expected
