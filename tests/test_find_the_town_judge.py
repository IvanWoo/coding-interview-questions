import pytest

from puzzles.find_the_town_judge import find_judge


@pytest.mark.parametrize(
    "n, trusted, expected",
    [
        (2, [[1, 2]], 2),
        (3, [[1, 3], [2, 3]], 3),
        (3, [[1, 3], [2, 3], [3, 1]], -1),
    ],
)
def test_find_judge(n, trusted, expected):
    assert find_judge(n, trusted) == expected
