import pytest

from puzzles.optimal_partition_of_string import partition_string


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abacaba", 4),
        ("ssssss", 6),
    ],
)
def test_partition_string(s, expected):
    assert partition_string(s) == expected
