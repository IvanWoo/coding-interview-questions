import pytest
from puzzles.most_stones_removed_with_same_row_or_column import remove_stones


@pytest.mark.parametrize(
    "stones, expected",
    [
        ([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]], 5),
        ([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]], 3),
        ([[0, 0]], 0),
    ],
)
def test_remove_stones(stones, expected):
    assert remove_stones(stones) == expected
