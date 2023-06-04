import pytest

from puzzles.number_of_provinces import find_circle_num


@pytest.mark.parametrize(
    "is_connected, expected",
    [
        ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
    ],
)
def test_find_circle_num(is_connected, expected):
    assert find_circle_num(is_connected) == expected
