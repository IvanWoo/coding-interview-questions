import pytest
from puzzles.triangle import minimum_total


@pytest.mark.parametrize(
    "triangle, expected",
    [
        ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
        ([[-10]], -10),
    ],
)
def test_minimum_total(triangle, expected):
    assert minimum_total(triangle) == expected
