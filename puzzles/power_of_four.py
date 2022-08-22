# https://leetcode.com/problems/power-of-four/
"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true
 

Constraints:
-231 <= n <= 231 - 1
 
Follow up: Could you solve it without loops/recursion?
"""
from math import log


def is_power_of_four(n: int) -> bool:
    def helper(n: int):
        if n == 0:
            return False
        if n == 1:
            return True
        new_n, left = divmod(n, 4)
        if left:
            return False
        return helper(new_n)

    return helper(n)


def is_power_of_four(n: int) -> bool:
    if n <= 0:
        return False
    v = log(n, 4)
    return v.is_integer()
