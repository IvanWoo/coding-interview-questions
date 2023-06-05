import pytest

from puzzles.check_if_it_is_a_straight_line import check_straight_line


@pytest.mark.parametrize(
    "coordinates, expected",
    [
        ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]], True),
        ([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]], False),
    ],
)
def test_check_straight_line(coordinates, expected):
    assert check_straight_line(coordinates) == expected
