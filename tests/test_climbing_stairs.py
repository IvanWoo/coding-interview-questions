import pytest
from puzzles.climbing_stairs import climb_stairs


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, 2),
        (3, 3),
        (35, 14930352),
    ],
)
def test_climb_stairs(n, expected):
    assert climb_stairs(n) == expected
