import pytest

from puzzles.count_ways_to_build_good_strings import count_good_strings


@pytest.mark.parametrize(
    "low, high, zero, one, expected",
    [
        (3, 3, 1, 1, 8),
        (2, 3, 1, 2, 5),
    ],
)
def test_count_good_strings(low, high, zero, one, expected):
    assert count_good_strings(low, high, zero, one) == expected
