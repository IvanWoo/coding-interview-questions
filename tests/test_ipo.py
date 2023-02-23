import pytest

from puzzles.ipo import find_maximized_capital


@pytest.mark.parametrize(
    "k, w, profits, capital, expected",
    [
        (2, 0, [1, 2, 3], [0, 1, 1], 4),
        (1, 0, [1, 2, 3], [1, 1, 2], 0),
        (1, 2, [1, 2, 3], [1, 1, 2], 5),
    ],
)
def test_find_maximized_capital(k, w, profits, capital, expected):
    assert find_maximized_capital(k, w, profits, capital) == expected
