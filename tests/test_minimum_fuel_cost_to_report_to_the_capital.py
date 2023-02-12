import pytest

from puzzles.minimum_fuel_cost_to_report_to_the_capital import minimum_fuel_cost


@pytest.mark.parametrize(
    "roads, seats, expected",
    [
        ([[0, 1], [0, 2], [0, 3]], 5, 3),
        ([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2, 7),
        ([], 1, 0),
        ([[0, 1], [0, 2], [1, 3], [1, 4]], 5, 4),
    ],
)
def test_minimum_fuel_cost(roads, seats, expected):
    assert minimum_fuel_cost(roads, seats) == expected
