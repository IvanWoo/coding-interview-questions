import pytest
from puzzles.maximum_points_you_can_obtain_from_cards import max_score


@pytest.mark.parametrize(
    "card_points, k, expected",
    [
        ([1, 2, 3, 4, 5, 6, 1], 3, 12),
        ([2, 2, 2], 2, 4),
        ([9, 7, 7, 9, 7, 7, 9], 7, 55),
        ([96, 90, 41, 82, 39, 74, 64, 50, 30], 8, 536),
    ],
)
def test_max_score(card_points, k, expected):
    assert max_score(card_points, k) == expected
