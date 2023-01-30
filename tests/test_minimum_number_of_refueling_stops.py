import pytest

from puzzles.minimum_number_of_refueling_stops import min_refuel_stops


@pytest.mark.parametrize(
    "target, start_fuel, stations, expected",
    [
        (1, 1, [], 0),
        (100, 1, [[10, 100]], -1),
        (100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]], 2),
        (100, 50, [[25, 30]], -1),
    ],
)
def test_min_refuel_stops(target, start_fuel, stations, expected):
    assert min_refuel_stops(target, start_fuel, stations) == expected
