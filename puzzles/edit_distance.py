# https://leetcode.com/problems/edit-distance/
"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
from functools import cache


# recursion
def min_distance(word1: str, word2: str) -> int:
    @cache
    def helper(w1, w2):
        n1, n2 = len(w1), len(w2)
        if n1 == 0 or n2 == 0:
            return max(n1, n2)
        if w1[0] == w2[0]:
            return helper(w1[1:], w2[1:])
        return min(helper(w1[1:], w2), helper(w1, w2[1:]), helper(w1[1:], w2[1:])) + 1

    return helper(word1, word2)


# dp
def min_distance(word1: str, word2: str) -> int:
    n1, n2 = len(word1) + 1, len(word2) + 1
    dp = [[0] * n1 for _ in range(n2)]

    # first row
    dp[0] = list(range(n1))

    # first col
    for r in range(n2):
        dp[r][0] = r

    for r in range(1, n2):
        for c in range(1, n1):
            dp[r][c] = min(
                dp[r - 1][c - 1] + int(word1[c - 1] != word2[r - 1]),
                dp[r - 1][c] + 1,
                dp[r][c - 1] + 1,
            )

    return dp[-1][-1]
