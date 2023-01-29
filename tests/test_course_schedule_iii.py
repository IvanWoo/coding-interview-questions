import pytest

from puzzles.course_schedule_iii import schedule_course


@pytest.mark.parametrize(
    "courses, expected",
    [
        ([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]], 3),
        ([[1, 2]], 1),
        ([[3, 2], [4, 3]], 0),
        ([[3, 3], [4, 3]], 1),
    ],
)
def test_schedule_course(courses, expected):
    assert schedule_course(courses) == expected
