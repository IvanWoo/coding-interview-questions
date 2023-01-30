import pytest

from puzzles.count_and_say import count_and_say


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, "1"),
        (2, "11"),
        (3, "21"),
        (4, "1211"),
        (5, "111221"),
        (6, "312211"),
    ],
)
def test_count_and_say(n, expected):
    assert count_and_say(n) == expected
