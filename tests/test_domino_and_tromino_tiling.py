import pytest
from puzzles.domino_and_tromino_tiling import num_tilings


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 2),
        (3, 5),
        (4, 11),
        (5, 24),
        (6, 53),
        (7, 117),
    ],
)
def test_num_tilings(n, expected):
    assert num_tilings(n) == expected
