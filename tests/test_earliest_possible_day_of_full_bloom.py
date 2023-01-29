import pytest

from puzzles.earliest_possible_day_of_full_bloom import earliest_full_bloom


@pytest.mark.parametrize(
    "plant_time, grow_time, expected",
    [([1, 4, 3], [2, 3, 1], 9), ([1, 2, 3, 2], [2, 1, 2, 1], 9), ([1], [1], 2)],
)
def test_earliest_full_bloom(plant_time, grow_time, expected):
    assert earliest_full_bloom(plant_time, grow_time) == expected
