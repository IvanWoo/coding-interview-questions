import pytest

from puzzles.critical_connections_in_a_network import critical_connections


@pytest.mark.parametrize(
    "n, connections, expected",
    [
        (4, [[0, 1], [1, 2], [2, 0], [1, 3]], [[1, 3]]),
        (2, [[0, 1]], [[0, 1]]),
        (6, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]], [[1, 3]]),
        (5, [[1, 0], [2, 0], [3, 2], [4, 2], [4, 3], [3, 0], [4, 0]], [[0, 1]]),
    ],
)
def test_critical_connections(n, connections, expected):
    assert critical_connections(n, connections) == expected
