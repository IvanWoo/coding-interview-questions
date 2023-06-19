import pytest

from puzzles.find_the_highest_altitude import largest_altitude


@pytest.mark.parametrize(
    "gain, expected",
    [
        ([-5, 1, 5, 0, -7], 1),
        ([-4, -3, -2, -1, 4, 3, 2], 0),
    ],
)
def test_largest_altitude(gain, expected):
    assert largest_altitude(gain) == expected
