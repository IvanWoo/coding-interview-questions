import pytest

from puzzles.ones_and_zeroes import find_max_form


@pytest.mark.parametrize(
    "strs, m, n, expected",
    [
        (["10", "0001", "111001", "1", "0"], 5, 3, 4),
        (["10", "0", "1"], 1, 1, 2),
        (
            [
                "0",
                "1101",
                "01",
                "00111",
                "1",
                "10010",
                "0",
                "0",
                "00",
                "1",
                "11",
                "0011",
            ],
            63,
            36,
            12,
        ),
    ],
)
def test_find_max_form(strs, m, n, expected):
    assert find_max_form(strs, m, n) == expected
