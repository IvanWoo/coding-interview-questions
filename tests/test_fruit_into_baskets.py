import pytest

from puzzles.fruit_into_baskets import total_fruit


@pytest.mark.parametrize(
    "fruits, expected",
    [
        ([1, 2, 1], 3),
        ([0, 1, 2, 2], 3),
        ([1, 2, 3, 2, 2], 4),
        ([1, 0, 1, 4, 1, 4, 1, 2, 3], 5),
    ],
)
def test_total_fruit(fruits, expected):
    assert total_fruit(fruits) == expected
