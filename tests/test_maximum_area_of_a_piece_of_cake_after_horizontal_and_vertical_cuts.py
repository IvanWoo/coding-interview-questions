import pytest

from puzzles.maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts import (
    max_area,
)


@pytest.mark.parametrize(
    "h, w, horizontal_cuts, vertical_cuts, expected",
    [
        (5, 4, [1, 2, 4], [1, 3], 4),
        (5, 4, [3, 1], [1], 6),
        (5, 4, [3], [3], 9),
        (1000000000, 1000000000, [2], [2], 81),
    ],
)
def test_max_area(h, w, horizontal_cuts, vertical_cuts, expected):
    assert max_area(h, w, horizontal_cuts, vertical_cuts) == expected
