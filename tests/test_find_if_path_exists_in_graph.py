import pytest
from puzzles.find_if_path_exists_in_graph import valid_path


@pytest.mark.parametrize(
    "n, edges, source, destination, expected",
    [
        (3, [[0, 1], [1, 2], [2, 0]], 0, 2, True),
        (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5, False),
        (1, [], 0, 0, True),
    ],
)
def test_valid_path(n, edges, source, destination, expected):
    assert valid_path(n, edges, source, destination) == expected
