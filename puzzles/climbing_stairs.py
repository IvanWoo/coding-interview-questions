# https://leetcode.com/problems/climbing-stairs/description/
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""
from functools import cache


def climb_stairs(n: int) -> int:
    @cache
    def helper(cur):
        if cur > n:
            return 0
        elif cur == n:
            return 1
        return helper(cur + 1) + helper(cur + 2)

    return helper(0)


def climb_stairs(n: int) -> int:
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a
