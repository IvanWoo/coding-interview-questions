import pytest

from puzzles.reordered_power_of_2 import reordered_power_of_2


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, True),
        (10, False),
        (2, True),
        (46, True),
    ],
)
def test_reordered_power_of_2(n, expected):
    assert reordered_power_of_2(n) == expected
