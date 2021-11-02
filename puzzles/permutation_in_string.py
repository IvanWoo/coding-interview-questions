# https://leetcode.com/problems/permutation-in-string/
"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.


Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
 
Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""
from collections import Counter, defaultdict


def check_inclusion(s1: str, s2: str) -> bool:
    lo, hi = 0, 0
    needs = Counter(s1)
    window = defaultdict(int)
    match = 0

    while hi < len(s2):
        c1 = s2[hi]
        if c1 in needs.keys():
            window[c1] += 1
            if window[c1] == needs[c1]:
                match += 1
        hi += 1

        while match == len(needs):
            if hi - lo == len(s1):
                return True
            c2 = s2[lo]
            if c2 in needs.keys():
                window[c2] -= 1
                if window[c2] < needs[c2]:
                    match -= 1
            lo += 1
    return False


if __name__ == "__main__":
    check_inclusion(s1="abc", s2="bbbca")
