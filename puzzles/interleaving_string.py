# https://leetcode.com/problems/interleaving-string/
"""
Given s1, s2, and s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:
0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lower-case English letters.
"""

from functools import lru_cache


def is_interleave(s1: str, s2: str, s3: str) -> bool:
    n1, n2, n3 = len(s1), len(s2), len(s3)
    if n1 + n2 != n3:
        return False

    @lru_cache
    def helper(i1, i2, i3):
        if (i1, i2, i3) == (n1, n2, n3):
            return True
        elif i1 == n1:
            return s3[i3:] == s2[i2:]
        elif i2 == n2:
            return s3[i3:] == s1[i1:]
        else:
            if s1[i1] != s3[i3] and s2[i2] != s3[i3]:
                return False
            elif s1[i1] == s3[i3] and s2[i2] == s3[i3]:
                return any([helper(i1 + 1, i2, i3 + 1), helper(i1, i2 + 1, i3 + 1)])
            elif s1[i1] == s3[i3]:
                return helper(i1 + 1, i2, i3 + 1)
            elif s2[i2] == s3[i3]:
                return helper(i1, i2 + 1, i3 + 1)

    return helper(0, 0, 0)


# space O(m*n)
def is_interleave(s1: str, s2: str, s3: str) -> bool:
    n1, n2, n3 = len(s1), len(s2), len(s3)
    if n1 + n2 != n3:
        return False

    dp = [[None] * (n1 + 1) for _ in range(n2 + 1)]
    dp[0][0] = True

    # first row
    for c in range(1, n1 + 1):
        dp[0][c] = s1[c - 1] == s3[c - 1] and dp[0][c - 1]

    # first col
    for r in range(1, n2 + 1):
        dp[r][0] = s2[r - 1] == s3[r - 1] and dp[r - 1][0]

    for r in range(1, n2 + 1):
        for c in range(1, n1 + 1):
            dp[r][c] = (s3[r + c - 1] == s1[c - 1] and dp[r][c - 1]) or (
                s3[r + c - 1] == s2[r - 1] and dp[r - 1][c]
            )

    return dp[-1][-1]


# space O(m)
def is_interleave(s1: str, s2: str, s3: str) -> bool:
    n1, n2, n3 = len(s1), len(s2), len(s3)
    if n1 + n2 != n3:
        return False

    dp = [None] * (n1 + 1)
    dp[0] = True

    # first row
    for c in range(1, n1 + 1):
        dp[c] = s1[c - 1] == s3[c - 1] and dp[c - 1]

    for r in range(1, n2 + 1):
        for c in range(n1 + 1):
            if c == 0:
                dp[c] = dp[c] and s3[r + c - 1] == s2[r - 1]
            else:
                dp[c] = (s3[r + c - 1] == s1[c - 1] and dp[c - 1]) or (
                    s3[r + c - 1] == s2[r - 1] and dp[c]
                )

    return dp[-1]
