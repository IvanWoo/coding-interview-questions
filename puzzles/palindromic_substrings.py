# https://leetcode.com/problems/palindromic-substrings/
"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

# brute force: O(n^3)
def count_substrings(s: str) -> int:
    def is_palindromic(i, j):
        sub = s[i : j + 1]
        return sub == sub[::-1]

    res = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            res += is_palindromic(i, j)
    return res


# O(n^2)
def count_substrings(s: str) -> int:
    def count(l, r):
        nonlocal res
        while l >= 0 and r < n and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1

    res = 0
    n = len(s)
    # odd
    for i in range(n):
        count(i, i)
    # even
    for i in range(n):
        count(i, i + 1)

    return res
