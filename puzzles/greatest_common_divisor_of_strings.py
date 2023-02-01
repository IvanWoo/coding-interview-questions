# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""


def gcd_of_strings(str1: str, str2: str) -> str:
    def is_divisor(divisor: str, s: str) -> bool:
        size = len(divisor)
        idx = 0
        n = len(s)
        while idx < n:
            if s[idx : idx + size] != divisor:
                return False
            idx += size
        return True

    n = min(len(str1), len(str2))
    ans = ""
    for i in range(1, n + 1):
        divisor = str1[:i]
        if is_divisor(divisor, str1) and is_divisor(divisor, str2):
            ans = divisor
    return ans
