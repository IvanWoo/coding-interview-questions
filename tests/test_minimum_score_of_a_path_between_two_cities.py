import pytest

from puzzles.minimum_score_of_a_path_between_two_cities import min_score


@pytest.mark.parametrize(
    "n, roads, expected",
    [
        (4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]], 5),
        (4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]], 2),
    ],
)
def test_min_score(n, roads, expected):
    assert min_score(n, roads) == expected
