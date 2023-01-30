# https://leetcode.com/problems/power-of-three/
"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:
Input: n = 27
Output: true

Example 2:
Input: n = 0
Output: false

Example 3:
Input: n = 9
Output: true

Constraints:
-231 <= n <= 231 - 1

Follow up: Could you solve it without loops/recursion?
"""
from math import log


def is_power_of_three(n: int) -> bool:
    if n <= 0:
        return False
    val = round(log(n, 3))
    return 3**val == n


def is_power_of_three(n: int) -> bool:
    def helper(n: int):
        if n <= 0:
            return False
        if n == 1:
            return True
        div, residual = divmod(n, 3)
        if residual:
            return False
        return helper(div)

    return helper(n)
