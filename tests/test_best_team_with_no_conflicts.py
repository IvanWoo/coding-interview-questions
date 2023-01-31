import pytest

from puzzles.best_team_with_no_conflicts import best_team_score


@pytest.mark.parametrize(
    "scores, ages, expected",
    [
        ([1, 3, 5, 10, 15], [1, 2, 3, 4, 5], 34),
        ([4, 5, 6, 5], [2, 1, 2, 1], 16),
        ([12, 2, 13, 40], [1, 1, 1, 1], 67),
        ([1, 2, 3, 5], [8, 9, 10, 1], 6),
        ([1, 3, 7, 3, 2, 4, 10, 7, 5], [4, 5, 2, 1, 1, 2, 4, 1, 4], 29),
    ],
)
def test_best_team_score(scores, ages, expected):
    assert best_team_score(scores, ages) == expected
