import pytest
from puzzles.minimum_time_to_collect_all_apples_in_a_tree import min_time


@pytest.mark.parametrize(
    "n, edges, has_apple, expected",
    [
        (
            7,
            [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            [False, False, True, False, True, True, False],
            8,
        ),
        (
            7,
            [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            [False, False, False, False, False, False, False],
            0,
        ),
        (4, [[0, 2], [0, 3], [1, 2]], [False, True, False, False], 4),
        (4, [[0, 2], [0, 3], [1, 2]], [False, False, False, False], 0),
    ],
)
def test_min_time(n, edges, has_apple, expected):
    assert min_time(n, edges, has_apple) == expected
