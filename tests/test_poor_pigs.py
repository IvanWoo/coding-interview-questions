import pytest

from puzzles.poor_pigs import poor_pigs


@pytest.mark.parametrize(
    "buckets, minutes_to_die, minutes_to_test, expected",
    [
        (1000, 15, 60, 5),
        (4, 15, 15, 2),
        (4, 15, 30, 2),
    ],
)
def test_poor_pigs(buckets, minutes_to_die, minutes_to_test, expected):
    assert poor_pigs(buckets, minutes_to_die, minutes_to_test) == expected
