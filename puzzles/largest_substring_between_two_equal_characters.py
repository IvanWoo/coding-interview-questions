# https://leetcode.com/problems/largest-substring-between-two-equal-characters/
"""
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
Example 4:

Input: s = "cabbac"
Output: 4
Explanation: The optimal substring here is "abba". Other non-optimal substrings include "bb" and "".

Constraints:

1 <= s.length <= 300
s contains only lowercase English letters.
"""
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class MinMax:
    _min: float = float("inf")
    _max: float = float("-inf")


def max_length_between_equal_characters(s: str) -> int:
    hashmap = defaultdict(MinMax)
    ans = -1
    for i, c in enumerate(s):
        hashmap[c]._min = min(hashmap[c]._min, i)
        hashmap[c]._max = max(hashmap[c]._max, i)
        ans = max(ans, hashmap[c]._max - hashmap[c]._min - 1)
    return ans


def max_length_between_equal_characters(s: str) -> int:
    hashmap = dict()
    ans = -1
    for i, c in enumerate(s):
        if c not in hashmap:
            hashmap[c] = i
        else:
            ans = max(ans, i - hashmap[c] - 1)
    return ans