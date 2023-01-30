# https://leetcode.com/problems/n-th-tribonacci-number/
"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 


Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""
from functools import cache


@cache
def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


def tribonacci(n: int) -> int:
    dp = dict(zip([0, 1, 2], [0, 1, 1]))
    for v in range(3, n + 1):
        dp[v] = dp[v - 1] + dp[v - 2] + dp[v - 3]
    return dp[n]


def tribonacci(n: int) -> int:
    def helper(a, b, c, n):
        if n == 0:
            return a
        a, b, c = b, c, a + b + c
        return helper(a, b, c, n - 1)

    return helper(0, 1, 1, n)
