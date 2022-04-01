import pytest
from puzzles.get_biggest_three_rhombus_sums_in_a_grid import get_biggest_three


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [
                [3, 4, 5, 1, 3],
                [3, 3, 4, 2, 3],
                [20, 30, 200, 40, 10],
                [1, 5, 5, 4, 1],
                [4, 3, 2, 2, 5],
            ],
            [228, 216, 211],
        ),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [20, 9, 8]),
        ([[7, 7, 7]], [7]),
    ],
)
def test_get_biggest_three(grid, expected):
    assert get_biggest_three(grid) == expected
