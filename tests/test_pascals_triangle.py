import pytest

from puzzles.pascals_triangle import generate


@pytest.mark.parametrize(
    "num_rows, expected",
    [
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]]),
        (2, [[1], [1, 1]]),
    ],
)
def test_generate(num_rows, expected):
    assert generate(num_rows) == expected
