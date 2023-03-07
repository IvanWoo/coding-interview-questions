import pytest

from puzzles.minimum_time_to_complete_trips import minimum_time


@pytest.mark.parametrize(
    "time, total_trips, expected",
    [
        ([1, 2, 3], 5, 3),
        ([2], 1, 2),
    ],
)
def test_minimum_time(time, total_trips, expected):
    assert minimum_time(time, total_trips) == expected
