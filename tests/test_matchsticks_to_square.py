import pytest
from puzzles.matchsticks_to_square import makesquare


@pytest.mark.parametrize(
    "sticks, expected",
    [
        ([1, 1, 2, 2, 2], True),
        ([3, 3, 3, 3, 4], False),
        ([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3], True),
    ],
)
def test_makesquare(sticks, expected):
    assert makesquare(sticks) == expected
