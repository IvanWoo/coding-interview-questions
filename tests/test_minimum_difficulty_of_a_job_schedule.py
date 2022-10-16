import pytest
from puzzles.minimum_difficulty_of_a_job_schedule import min_difficulty


@pytest.mark.parametrize(
    "job_difficulty, d, expected",
    [
        ([6, 5, 4, 3, 2, 1], 2, 7),
        ([9, 9, 9], 4, -1),
        ([1, 1, 1], 3, 3),
        ([4, 3, 2], 1, 4),
        ([7, 1, 7, 1, 7, 1], 3, 15),
    ],
)
def test_min_difficulty(job_difficulty, d, expected):
    assert min_difficulty(job_difficulty, d) == expected
