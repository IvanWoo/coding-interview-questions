import pytest

from puzzles.rectangle_area import compute_area


@pytest.mark.parametrize(
    "ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, expected",
    [
        (-3, 0, 3, 4, 0, -1, 9, 2, 45),
        (0, -1, 9, 2, -3, 0, 3, 4, 45),
        (-2, -2, 2, 2, -2, -2, 2, 2, 16),
        (-2, -2, 2, 2, 3, 3, 4, 4, 17),
        (-2, -2, 2, 2, -1, -1, 1, 1, 16),
    ],
)
def test_compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, expected):
    assert compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) == expected
