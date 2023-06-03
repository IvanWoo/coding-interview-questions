import pytest

from puzzles.time_needed_to_inform_all_employees import num_of_minutes


@pytest.mark.parametrize(
    "n, head_id, manager, inform_time, expected",
    [
        (1, 0, [-1], [0], 0),
        (6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0], 1),
        (
            11,
            4,
            [5, 9, 6, 10, -1, 8, 9, 1, 9, 3, 4],
            [0, 213, 0, 253, 686, 170, 975, 0, 261, 309, 337],
            2560,
        ),
    ],
)
def test_num_of_minutes(n, head_id, manager, inform_time, expected):
    assert num_of_minutes(n, head_id, manager, inform_time) == expected
