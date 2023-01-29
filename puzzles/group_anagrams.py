"""
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
from collections import defaultdict


# O(N^2 * logN)
def group_anagrams(strs: list[str]) -> list[list[str]]:
    ans = defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()


# O(N^2)
def group_anagrams(strs: list[str]) -> list[list[str]]:
    ans = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
    return ans.values()
