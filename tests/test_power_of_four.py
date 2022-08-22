import pytest
from puzzles.power_of_four import is_power_of_four


@pytest.mark.parametrize(
    "n, expected",
    [
        (16, True),
        (5, False),
        (1, True),
        (-1, False),
        (8, False),
        (0, False),
    ],
)
def test_is_power_of_four(n, expected):
    assert is_power_of_four(n) == expected
