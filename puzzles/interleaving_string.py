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
