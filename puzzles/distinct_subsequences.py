# https://leetcode.com/problems/distinct-subsequences/
"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It's guaranteed the answer fits on a 32-bit signed integer.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag
 
Constraints:

0 <= s.length, t.length <= 1000
s and t consist of English letters.
"""
from functools import lru_cache


def num_distinct(s: str, t: str) -> int:
    @lru_cache(None)
    def helper(i, j):
        if j == len(t):
            return 1
        if i == len(s):
            return 0
        res = 0
        if s[i] == t[j]:
            res += helper(i + 1, j + 1)
        res += helper(i + 1, j)
        return res

    return helper(0, 0)


# dp
def num_distinct(s: str, t: str) -> int:
    row, col = len(s), len(t)
    dp = [[0] * (col + 1) for _ in range(row + 1)]
    for r in range(row + 1):
        dp[r][0] = 1

    for r in range(1, row + 1):
        for c in range(1, col + 1):
            dp[r][c] = dp[r - 1][c] + dp[r - 1][c - 1] * (s[r - 1] == t[c - 1])
    return dp[-1][-1]


if __name__ == "__main__":
    num_distinct(s="rabbbit", t="rabbit")
