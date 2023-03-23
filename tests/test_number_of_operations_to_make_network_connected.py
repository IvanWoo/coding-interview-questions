import pytest

from puzzles.number_of_operations_to_make_network_connected import make_connected


@pytest.mark.parametrize(
    "n, connections, expected",
    [
        (4, [[0, 1], [0, 2], [1, 2]], 1),
        (6, [[0, 1], [0, 2], [0, 3], [1, 2]], -1),
        (5, [[0, 1], [0, 2], [3, 4], [2, 3]], 0),
        (6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]], 2),
    ],
)
def test_make_connected(n, connections, expected):
    assert make_connected(n, connections) == expected
