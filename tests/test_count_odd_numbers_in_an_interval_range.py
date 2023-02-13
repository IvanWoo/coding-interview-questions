import pytest

from puzzles.count_odd_numbers_in_an_interval_range import count_odds


@pytest.mark.parametrize(
    "low, high, expected",
    [
        (3, 7, 3),
        (8, 10, 1),
        (21, 22, 1),
        (1, 1, 1),
        (2, 2, 0),
    ],
)
def test_count_odds(low, high, expected):
    assert count_odds(low, high) == expected
