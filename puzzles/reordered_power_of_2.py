# https://leetcode.com/problems/reordered-power-of-2/
"""
ou are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

Example 1:
Input: n = 1
Output: true

Example 2:
Input: n = 10
Output: false

Constraints:
1 <= n <= 109
"""
from itertools import permutations
from math import floor, log, ceil
from collections import Counter


def reordered_power_of_2(n: int) -> bool:
    def comb(n: int) -> list[str]:
        for p in permutations([c for c in str(n)], len(str(n))):
            yield "".join(p)

    def valid(candidate: str) -> bool:
        if candidate.startswith("0"):
            return False
        power = floor(log(int(candidate), 2))
        return 2**power == int(candidate)

    for c in comb(n):
        if valid(c):
            return True
    return False


def reordered_power_of_2(n: int) -> bool:
    source = Counter(str(n))
    boundary = 10**9 + 1
    targets = [Counter(str(2**v)) for v in range(ceil(log(boundary, 2)))]
    return any(t == source for t in targets)


if __name__ == "__main__":
    reordered_power_of_2(46)
