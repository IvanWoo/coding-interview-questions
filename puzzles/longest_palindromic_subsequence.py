# https://leetcode.com/problems/longest-palindromic-subsequence/
"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:
"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".


Example 2:
Input:
"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".


Constraints:
1 <= s.length <= 1000
s consists only of lowercase English letters.
"""


# brute force
def longest_palindrome_subseq(s: str) -> int:
    def palindrome_len(s, start, end):
        if start > end:
            return 0
        elif start == end:
            return 1
        elif s[start] == s[end]:
            return 2 + palindrome_len(s, start + 1, end - 1)
        else:
            return max(
                palindrome_len(s, start + 1, end), palindrome_len(s, start, end - 1)
            )

    n = len(s)
    res = 0
    for i in range(n):
        for j in range(i, n):
            res = max(res, palindrome_len(s, i, j))
    return res


# dp
def longest_palindrome_subseq(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # due to the nature of this dp matrix, we need to reverse the row-wise iteration
    for i in reversed(range(n)):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 1
                continue
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][-1]


if __name__ == "__main__":
    longest_palindrome_subseq("bbbab")
