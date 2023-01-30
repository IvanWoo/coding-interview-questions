import pytest

from puzzles.network_delay_time import network_delay_time


@pytest.mark.parametrize(
    "times, n, k, expected",
    [
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
        ([[1, 2, 1]], 2, 1, 1),
        ([[1, 2, 1]], 2, 2, -1),
    ],
)
def test_network_delay_time(times, n, k, expected):
    assert network_delay_time(times, n, k) == expected
