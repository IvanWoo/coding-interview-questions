# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

Example 1:
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].

Constraints:
0 <= low <= high <= 10^9
"""


def count_odds(low: int, high: int) -> int:
    def is_odd(x: int) -> bool:
        return x % 2 == 1

    ol, oh = is_odd(low), is_odd(high)
    match (ol, oh):
        case (False, True):
            return (high + 1 - low) // 2
        case (True, False):
            return (high + 1 - low) // 2
        case (False, False):
            return (high - low) // 2
        case (True, True):
            return (high + 1 - low) // 2 + 1
