# https://codingbat.com/prob/p198700
"""
Given three ints, a b c, one of them is small, one is medium and one is large. Return true if the three values are evenly spaced, so the difference between small and medium is the same as the difference between medium and large.


evenly_spaced(2, 4, 6) → true
evenly_spaced(4, 6, 2) → true
evenly_spaced(4, 6, 3) → false
"""


def evenly_spaced(a: int, b: int, c: int) -> bool:
    l = [a, b, c]
    l.sort()
    return (l[1] - l[0]) == (l[2] - l[1])
