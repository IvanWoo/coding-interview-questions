import pytest

from puzzles.reducing_dishes import max_satisfaction


@pytest.mark.parametrize(
    "satisfaction, expected",
    [
        ([-1, -8, 0, 5, -9], 14),
        ([4, 3, 2], 20),
        ([-1, -4, -5], 0),
    ],
)
def test_max_satisfaction(satisfaction, expected):
    assert max_satisfaction(satisfaction) == expected
