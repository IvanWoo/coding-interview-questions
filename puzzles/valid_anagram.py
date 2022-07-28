# https://leetcode.com/problems/valid-anagram/
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    c_s = Counter(s)
    c_t = Counter(t)

    if c_s.keys() != c_t.keys():
        return False

    for k, v in c_s.items():
        if c_t[k] != v:
            return False
    return True


def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
