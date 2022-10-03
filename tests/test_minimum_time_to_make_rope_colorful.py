import pytest
from puzzles.minimum_time_to_make_rope_colorful import min_cost


@pytest.mark.parametrize(
    "colors, needed_time, expected",
    [
        ("abaac", [1, 2, 3, 4, 5], 3),
        ("abc", [1, 2, 3], 0),
        ("aabaa", [1, 2, 3, 4, 1], 2),
    ],
)
def test_min_cost(colors, needed_time, expected):
    assert min_cost(colors, needed_time) == expected
