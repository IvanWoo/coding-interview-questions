# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""


# cheat
def str_str(haystack: str, needle: str) -> int:
    try:
        idx = haystack.index(needle)
    except ValueError:
        idx = -1
    return idx


def str_str(haystack: str, needle: str) -> int:
    n = len(haystack)
    m = len(needle)
    for i in range(n - m + 1):
        if haystack[i : i + m] == needle:
            return i
    return -1
