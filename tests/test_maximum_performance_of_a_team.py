import pytest

from puzzles.maximum_performance_of_a_team import max_performance


@pytest.mark.parametrize(
    "n, speed, efficiency, k, expected",
    [
        (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2, 60),
        (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3, 68),
        (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4, 72),
    ],
)
def test_max_performance(n, speed, efficiency, k, expected):
    assert max_performance(n, speed, efficiency, k) == expected
