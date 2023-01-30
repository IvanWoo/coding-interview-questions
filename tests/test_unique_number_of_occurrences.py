import pytest

from puzzles.unique_number_of_occurrences import unique_occurrences


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 2, 1, 1, 3], True),
        ([1, 2], False),
        ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
    ],
)
def test_unique_occurrences(arr, expected):
    assert unique_occurrences(arr) == expected
