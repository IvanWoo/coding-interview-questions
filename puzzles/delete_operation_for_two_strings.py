# https://leetcode.com/problems/delete-operation-for-two-strings/
"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4

Constraints:
1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
"""


def min_distance(word1: str, word2: str) -> int:
    rows, cols = len(word1) + 1, len(word2) + 1
    dp = [[0] * cols for _ in range(rows)]
    for col in range(cols):
        dp[0][col] = col
    for row in range(rows):
        dp[row][0] = row

    for row in range(1, rows):
        for col in range(1, cols):
            c1, c2 = word1[row - 1], word2[col - 1]
            if c1 == c2:
                dp[row][col] = dp[row - 1][col - 1]
            else:
                dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1
    return dp[-1][-1]
