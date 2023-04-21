import pytest

from puzzles.profitable_schemes import profitable_schemes


@pytest.mark.parametrize(
    "n, min_profit, group, profit, expected",
    [
        (5, 3, [2, 2], [2, 3], 2),
        (10, 5, [2, 3, 5], [6, 7, 8], 7),
    ],
)
def test_profitable_schemes(n, min_profit, group, profit, expected):
    assert profitable_schemes(n, min_profit, group, profit) == expected
