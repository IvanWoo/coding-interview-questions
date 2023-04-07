import pytest

from puzzles.number_of_enclaves import num_enclaves


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]], 3),
        ([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]], 0),
    ],
)
def test_num_enclaves(grid, expected):
    assert num_enclaves(grid) == expected
