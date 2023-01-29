import pytest

from puzzles.power_of_three import is_power_of_three


@pytest.mark.parametrize(
    "n, expected",
    [
        (27, True),
        (0, False),
        (9, True),
        (243, True),
    ],
)
def test_is_power_of_three(n, expected):
    assert is_power_of_three(n) == expected
