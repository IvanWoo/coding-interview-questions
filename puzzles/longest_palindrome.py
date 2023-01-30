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
def longest_palindrome(s: str) -> str:
    n = len(s)
    longest = ""
    for i in range(n):
        for j in range(i, n):
            sub_s = s[i : j + 1]
            if len(sub_s) > len(longest) and sub_s == sub_s[::-1]:
                longest = sub_s
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
        sub_s = s1 if len(s1) > len(s2) else s2
        if len(sub_s) > len(longest):
            longest = sub_s
    return longest


if __name__ == "__main__":
    longest_palindrome("babad")
