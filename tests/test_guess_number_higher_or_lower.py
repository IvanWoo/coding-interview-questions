from functools import partial

import pytest

from puzzles.guess_number_higher_or_lower import guess_number


def _guess(n: int, pick: int) -> bool:
    if n == pick:
        return 0
    elif n > pick:
        return -1
    elif n < pick:
        return 1


@pytest.mark.parametrize(
    "n, expected",
    [
        (10, 6),
        (1, 1),
        (2, 1),
    ],
)
def test_guess_number(n, expected):
    guess = partial(_guess, pick=expected)
    assert guess_number(n, guess) == expected
