"""
1055.Shortest Way to Form String
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

Example 1:
Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

Example 2:
Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.

Example 3:
Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".


Constraints:
Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.
"""

from bisect import bisect_left
from collections import defaultdict


def shortest_way_to_form_string(source: str, target: str) -> int:
    # form the hashmap of source
    hashmap = defaultdict(list)
    for k, v in enumerate(source):
        hashmap[v].append(k)
    # map through target
    res = 0
    lower_boundary = 0
    for char in target:
        if char not in hashmap:
            return -1
        index_list = hashmap[char]
        i = bisect_left(index_list, lower_boundary)
        if i == len(index_list):
            lower_boundary = index_list[0] + 1
            res += 1
        else:
            lower_boundary = index_list[i] + 1
    return res + 1
