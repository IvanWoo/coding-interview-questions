import pytest
from puzzles.minimum_time_to_collect_all_apples_in_a_tree import min_time


def test_min_time():
    assert (
        min_time(
            7,
            [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            [False, False, True, False, True, True, False],
        )
        == 8
    )
    assert (
        min_time(
            7,
            [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            [False, False, False, False, False, False, False],
        )
        == 0
    )

    assert min_time(4, [[0, 2], [0, 3], [1, 2]], [False, True, False, False],) == 4
