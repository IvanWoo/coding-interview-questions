# https://techdevguide.withgoogle.com/paths/advanced/working-in-multiple-languages-palindrome-permutation-2/#!
"""
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:
Input: "aabb"
Output: ["abba", "baab"]

Example 2:
Input: "abc"
Output: []

Example 3:
Input: "aaabbb"
Output: []
"""
from collections import Counter
from itertools import permutations
from typing import List, Optional


def mirror(s: str, center: str) -> str:
    return s + center + s[::-1]


def palindrome_permutation(s: str) -> Optional[List[str]]:
    c = Counter(s)
    # only one element can has odd totals
    if len([v for v in c.values() if v % 2 != 0]) > 1:
        return []

    center = [k for k, v in c.items() if v % 2 != 0]
    center = center[0] if len(center) == 1 else ""

    perm_list = []
    for k, v in c.items():
        for n in range(v // 2):
            perm_list.insert(0, k)

    unique_perm = set(["".join(x) for x in permutations(perm_list)])
    return sorted([mirror(x, center) for x in unique_perm])
