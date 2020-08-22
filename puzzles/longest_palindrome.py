# https://leetcode.com/problems/longest-palindromic-substring/
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""

# brute force O(n^3)
def longest_palindrome_bf(s: str) -> str:
    longest = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub_s = s[i:j]
            if sub_s == sub_s[::-1]:
                longest = sub_s if len(sub_s) > len(longest) else longest
    return longest


def expand_around_center(s: str, left: int, right: int) -> int:
    while left >= 0 and right <= (len(s) - 1) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1 : right]


def longest_palindrome(s: str) -> str:
    longest = ""
    for i in range(len(s)):
        s1 = expand_around_center(s, i, i)
        s2 = expand_around_center(s, i, i + 1)
        print(s1, s2)
        sub_s = s1 if len(s1) > len(s2) else s2
        if len(sub_s) > len(longest):
            longest = sub_s
    return longest
