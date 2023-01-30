import pytest

from puzzles.keys_and_rooms import can_visit_all_rooms


@pytest.mark.parametrize(
    "rooms, expected",
    [
        ([[1], [2], [3], []], True),
        ([[1, 3], [3, 0, 1], [2], [0]], False),
    ],
)
def test_can_visit_all_rooms(rooms, expected):
    assert can_visit_all_rooms(rooms) == expected
