# https://codingbat.com/prob/p117019
"""
Given 2 int values greater than 0, return whichever value is nearest to 21 without going over. Return 0 if they both go over.


blackjack(19, 21) → 21
blackjack(21, 19) → 21
blackjack(19, 22) → 19
"""


def blackjack(a: int, b: int) -> int:
    valids = [i for i in [a, b] if 21 - i >= 0]
    return max(valids) if valids != [] else 0
