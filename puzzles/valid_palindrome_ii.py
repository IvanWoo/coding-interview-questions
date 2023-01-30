# https://leetcode.com/problems/valid-palindrome-ii/
"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false


Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
"""


def valid_palindrome(s: str) -> bool:
    def is_valid(s, left, right, quota):
        if (right - left) <= 0:
            return True
        if s[left] == s[right]:
            return is_valid(s, left + 1, right - 1, quota)
        if not quota:
            return False
        return is_valid(s, left + 1, right, quota - 1) or is_valid(s, left, right - 1, quota - 1)

    return is_valid(s, 0, len(s) - 1, 1)


valid_palindrome("abc")
