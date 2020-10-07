# https://leetcode.com/problems/regular-expression-matching/
"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:
Input: s = "mississippi", p = "mis*is*p*."
Output: false
 
Constraints:

0 <= s.length <= 20
0 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
"""


def is_match(s: str, p: str) -> bool:
    l_s, l_p = len(s), len(p)
    dp = [[False] * (l_p + 1) for _ in range(l_s + 1)]
    dp[0][0] = True

    # first row
    for c in range(1, l_p + 1):
        if p[c - 1] == "*":
            dp[0][c] = dp[0][c - 2]

    for r in range(1, l_s + 1):
        for c in range(1, l_p + 1):
            if p[c - 1] == "." or s[r - 1] == p[c - 1]:
                dp[r][c] = dp[r - 1][c - 1]
            elif p[c - 1] == "*":
                if p[c - 2] == s[r - 1] or p[c - 2] == ".":
                    dp[r][c] = dp[r][c - 2] or dp[r - 1][c]
                else:
                    dp[r][c] = dp[r][c - 2]
    return dp[-1][-1]


def is_match(s: str, p: str) -> bool:
    if not p:
        return not s

    first_match = bool(s) and p[0] in {s[0], "."}

    if len(p) >= 2 and p[1] == "*":
        return is_match(s, p[2:]) or (first_match and is_match(s[1:], p))
    else:
        return first_match and is_match(s[1:], p[1:])


if __name__ == "__main__":
    is_match("ab", ".*")