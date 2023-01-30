# https://leetcode.com/problems/domino-and-tromino-tiling/description/
"""
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.


Example 1:
Input: n = 3
Output: 5
Explanation: The five different ways are show above.

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 1000
"""


def num_tilings(n: int) -> int:
    MOD = 10**9 + 7
    cache_d = {0: 1, 1: 1, 2: 2}
    cache_t = {0: 0, 1: 0, 2: 1}

    def get_d(x: int):
        if x in cache_d:
            return cache_d[x]
        cache_d[x] = get_d(x - 1) + get_d(x - 2) + get_t(x - 1) * 2
        return cache_d[x]

    def get_t(x: int):
        if x in cache_t:
            return cache_t[x]
        cache_t[x] = get_d(x - 2) + get_t(x - 1)
        return cache_t[x]

    ans = get_d(n)
    return ans % MOD
