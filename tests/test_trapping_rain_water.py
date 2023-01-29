import pytest

from puzzles.trapping_rain_water import trap


@pytest.mark.parametrize(
    "height, expected",
    [
        ([1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2], 15),
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([0] * 10, 0),
        (list(range(10)), 0),
        (list(range(10, 0, -1)), 0),
    ],
)
def test_trap(height, expected):
    assert trap(height) == expected
