import pytest
from puzzles.candy import candy


@pytest.mark.parametrize(
    "ratings, expected",
    [
        ([1, 0, 2], 5),
        ([1, 2, 2], 4),
        ([1, 2, 87, 87, 87, 2, 1], 13),
        ([1, 6, 10, 8, 7, 3, 2], 18),
        ([1, 3, 4, 5, 2], 11),
    ],
)
def test_candy(ratings, expected):
    assert candy(ratings) == expected
