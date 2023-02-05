# https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.


Example 1:
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
from collections import Counter, defaultdict


def find_anagrams(s: str, p: str) -> list[int]:
    target = Counter(p)
    n = len(p)
    ans = []
    for i in range(len(s) - n + 1):
        if Counter(s[i : i + n]) == target:
            ans.append(i)
    return ans


def find_anagrams(s: str, p: str) -> list[int]:
    needs = Counter(p)
    window = defaultdict(int)
    res = []
    lo, hi = 0, 0
    match = 0

    while hi < len(s):
        c1 = s[hi]
        if c1 in needs.keys():
            window[c1] += 1
            if window[c1] == needs[c1]:
                match += 1
        hi += 1

        while match == len(needs):
            if hi - lo == len(p):
                res.append(lo)
            c2 = s[lo]
            if c2 in needs.keys():
                window[c2] -= 1
                if window[c2] < needs[c2]:
                    match -= 1
            lo += 1
    return res
