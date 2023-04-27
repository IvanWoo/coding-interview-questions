import pytest

from puzzles.bulb_switcher import bulb_switch


@pytest.mark.parametrize(
    "n, expected",
    [
        (3, 1),
        (0, 0),
        (1, 1),
    ],
)
def test_bulb_switch(n, expected):
    assert bulb_switch(n) == expected
