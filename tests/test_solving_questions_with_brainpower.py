import pytest

from puzzles.solving_questions_with_brainpower import most_points


@pytest.mark.parametrize(
    "questions, expected",
    [
        ([[3, 2], [4, 3], [4, 4], [2, 5]], 5),
        ([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 7),
    ],
)
def test_most_points(questions, expected):
    assert most_points(questions) == expected
