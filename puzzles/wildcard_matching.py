# https://leetcode.com/problems/wildcard-matching/
"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""
from functools import lru_cache


# backtrack
def is_match(s: str, p: str) -> bool:
    l_s, l_p = len(s), len(p)
    ans = False

    @lru_cache(maxsize=None)
    def backtrack(i, j):
        nonlocal ans
        if ans:
            return
        if i == l_s:
            ans = j == l_p or p[j:] == "*" * (l_p - j)
            return
        if j == l_p:
            return
        if s[i] == p[j]:
            return backtrack(i + 1, j + 1)
        else:
            if p[j] == "?":
                backtrack(i + 1, j + 1)
            elif p[j] == "*":
                backtrack(i, j + 1)
                backtrack(i + 1, j)
                backtrack(i + 1, j + 1)
            else:
                return

    backtrack(0, 0)
    return ans


# dp
def is_match(s: str, p: str) -> bool:
    l_s, l_p = len(s), len(p)
    dp = [[False] * (l_p + 1) for _ in range(l_s + 1)]
    dp[0][0] = True

    # first row
    for c in range(1, l_p + 1):
        if p[c - 1] != "*":
            break
        dp[0][c] = True

    for r in range(1, l_s + 1):
        for c in range(1, l_p + 1):
            if p[c - 1] in {s[r - 1], "?"}:
                dp[r][c] = dp[r - 1][c - 1]
            elif p[c - 1] == "*":
                dp[r][c] = dp[r - 1][c] or dp[r][c - 1] or dp[r - 1][c - 1]
    return dp[-1][-1]


def is_match(s: str, p: str) -> bool:
    star_idx = -1
    match = 0
    i = j = 0
    while i < len(s):
        if j < len(p) and (p[j] == "?" or s[i] == p[j]):
            i += 1
            j += 1
            continue
        elif j < len(p) and p[j] == "*":
            star_idx = j
            match = i
            j += 1
        elif star_idx != -1:
            j = star_idx + 1
            match += 1
            i = match
        else:
            return False
    while j < len(p) and p[j] == "*":
        j += 1
    return j == len(p)
