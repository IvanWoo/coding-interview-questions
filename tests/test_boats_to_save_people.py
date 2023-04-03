import pytest

from puzzles.boats_to_save_people import num_rescue_boats


@pytest.mark.parametrize(
    "people, limit, expected",
    [
        ([1, 2], 3, 1),
        ([3, 2, 2, 1], 3, 3),
        ([3, 5, 3, 4], 5, 4),
        (
            [2, 49, 10, 7, 11, 41, 47, 2, 22, 6, 13, 12, 33, 18, 10, 26, 2, 6, 50, 10],
            50,
            11,
        ),
    ],
)
def test_num_rescue_boats(people, limit, expected):
    assert num_rescue_boats(people, limit) == expected
