# https://leetcode.com/problems/reverse-string/
"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.
"""


def reverse_string(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    n = len(s)
    left, right = 0, n - 1
    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1