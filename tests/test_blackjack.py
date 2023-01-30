import pytest

from puzzles.blackjack import blackjack


def test_blackjack():
    assert blackjack(19, 21) == 21
    assert blackjack(21, 19) == 21
    assert blackjack(19, 22) == 19
    assert blackjack(1, 22) == 1
    assert blackjack(22, 23) == 0
