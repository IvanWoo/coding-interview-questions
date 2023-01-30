# https://leetcode.com/problems/word-subsets/
"""
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

Example 1:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]

Constraints:
1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
"""
from collections import Counter, defaultdict
from functools import reduce


# brute force: O(MN)
def word_subsets(words1: list[str], words2: list[str]) -> list[str]:
    w2_counters = [Counter(w2) for w2 in set(words2)]

    def is_valid(w: str):
        w1_c = Counter(w)
        for w2_c in w2_counters:
            for k, v in w2_c.items():
                if k not in w1_c:
                    return False
                if w1_c[k] < v:
                    return False
        return True

    ans = []
    for w1 in words1:
        if is_valid(w1):
            ans.append(w1)
    return ans


# O(M + N)
def word_subsets(words1: list[str], words2: list[str]) -> list[str]:
    criterial = defaultdict(int)
    for w2 in words2:
        w2_c = Counter(w2)
        for k, v in w2_c.items():
            criterial[k] = max(criterial[k], v)

    def is_valid(w: str):
        w1_c = Counter(w)
        for k, v in criterial.items():
            if k not in w1_c:
                return False
            if w1_c[k] < v:
                return False
        return True

    return [w1 for w1 in words1 if is_valid(w1)]


def word_subsets(words1: list[str], words2: list[str]) -> list[str]:
    # https://github.com/python/cpython/blob/d92b19e1b500247f9a62b12b9da889b99fe333f6/Lib/collections/__init__.py#L850-L854
    criterial = reduce(lambda a, b: Counter(a) | Counter(b), words2)
    return [w1 for w1 in words1 if Counter(w1) >= criterial]
