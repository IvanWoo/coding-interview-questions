import pytest

from puzzles.can_place_flowers import can_place_flowers


@pytest.mark.parametrize(
    "flowerbed, n, expected",
    [
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
    ],
)
def test_can_place_flowers(flowerbed, n, expected):
    assert can_place_flowers(flowerbed, n) == expected
