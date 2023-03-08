import pytest

from puzzles.koko_eating_bananas import min_eating_speed


@pytest.mark.parametrize(
    "piles, h, expected",
    [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
    ],
)
def test_min_eating_speed(piles, h, expected):
    assert min_eating_speed(piles, h) == expected
