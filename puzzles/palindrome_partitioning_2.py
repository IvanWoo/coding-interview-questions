# https://leetcode.com/problems/palindrome-partitioning-ii/
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


from typing import List


def compute_all_pals(s: str) -> List[List[bool]]:
    n = len(s)
    is_pal: List[List[bool]] = [[True] * (n + 1) for _ in range(n + 1)]
    for i in range(n, 0, -1):
        for j in range(i + 1, n + 1):
            is_pal[i][j] = s[i - 1] == s[j - 1] and is_pal[i + 1][j - 1]
    return is_pal


def min_cut(s: str) -> int:
    n = len(s)
    is_pal = compute_all_pals(s)
    # print(is_pal)

    dp = [n] * (n + 2)
    dp[n + 1] = 0

    for i in range(n, 0, -1):
        for j in range(i, n + 1):
            if is_pal[i][j]:
                dp[i] = min(dp[i], dp[j + 1] + 1)
    # print(dp)
    return dp[1] - 1


if __name__ == "__main__":
    print(min_cut("aab"))

