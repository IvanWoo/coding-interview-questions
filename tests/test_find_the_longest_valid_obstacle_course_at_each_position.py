import pytest

from puzzles.find_the_longest_valid_obstacle_course_at_each_position import (
    longest_obstacle_course_at_each_position,
)


@pytest.mark.parametrize(
    "obstacles, expected",
    [
        ([1, 2, 3, 2], [1, 2, 3, 3]),
        ([2, 2, 1], [1, 2, 1]),
        ([3, 1, 5, 6, 4, 2], [1, 1, 2, 3, 2, 2]),
        ([5, 1, 5, 5, 1, 3, 4, 5, 1, 4], [1, 1, 2, 3, 2, 3, 4, 5, 3, 5]),
    ],
)
def test_longest_obstacle_course_at_each_position(obstacles, expected):
    assert longest_obstacle_course_at_each_position(obstacles) == expected
