# https://leetcode.com/problems/longest-uncommon-subsequence-ii/
"""
Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc", "eae"
Output: 3
Note:

All the given strings' lengths will not exceed 10.
The length of the given list will be in the range of [2, 50].
"""

from collections import Counter, deque
from typing import List


def is_sub(s1, s2):
    if len(s1) > len(s2):
        return False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        t = s2[j:].find(s1[i])
        if t == -1:
            return False
        j += t + 1
        i += 1
    return i == len(s1)


def find_LUS_length(strs: List[str]) -> int:
    c = Counter(strs)
    dups = [k for k, v in c.items() if v > 1]
    strs = [k for k, v in c.items() if v == 1]
    pots = deque()
    for x in strs:
        if any([is_sub(x, dup) for dup in dups]):
            continue
        pots.append(x)
    return max([len(x) for x in pots]) if len(pots) > 0 else -1
