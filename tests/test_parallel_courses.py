import pytest
from puzzles.parallel_courses import parallel_courses


@pytest.mark.parametrize(
    "n, relations, expected",
    [
        (3, [[1, 3], [2, 3]], 2),
        (3, [[1, 2], [2, 3], [3, 1]], -1),
        (4, [[1, 2], [1, 3], [3, 2], [2, 4], [3, 4]], 4),
        (6, [[2, 3], [4, 5], [5, 6]], 3),
    ],
)
def test_parallel_courses(n, relations, expected):
    assert parallel_courses(n, relations) == expected
