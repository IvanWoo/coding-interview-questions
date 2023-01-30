# https://leetcode.com/problems/longest-palindromic-substring/
"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""
from functools import cache


# brute force: O(n^3)
def longest_palindrome(s: str) -> str:
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    if not s:
        return ""

    n = len(s)
    res = s[0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            if j - i <= len(res):
                continue
            sub_s = s[i:j]
            if is_palindrome(sub_s):
                res = sub_s
    return res


# Memory Limit Exceeded
def longest_palindrome(s: str) -> str:
    @cache
    def is_palindrome(start: int, end: int) -> bool:
        if start >= end:
            return True
        if s[start] != s[end]:
            return False
        return is_palindrome(start + 1, end - 1)

    if not s:
        return ""

    n = len(s)
    res = s[0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            if j - i <= len(res):
                continue
            sub_s = s[i:j]
            if is_palindrome(i, j - 1):
                res = sub_s
    return res


# TLE
def longest_palindrome(s: str) -> str:
    n = len(s)
    ans = ""
    max_len = 0
    dp = [[False] * n for _ in range(n)]
    for i in reversed(range(n)):
        for j in range(i, n):
            res = s[i] == s[j]
            if j - i > 2:
                res = res and dp[i + 1][j - 1]
            dp[i][j] = res
            if dp[i][j]:
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    ans = s[i : j + 1]

    return ans


def longest_palindrome(s: str) -> str:
    def expand(start: int, end: int) -> str:
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start + 1 : end]

    n = len(s)
    res = ""
    for i in range(n):
        s1 = expand(i, i)
        s2 = expand(i, i + 1)

        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            if l1 > len(res):
                res = s1
        else:
            if l2 > len(res):
                res = s2
    return res


if __name__ == "__main__":
    longest_palindrome("aaaa")
