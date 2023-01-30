# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]
Output:
"apple"

Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]
Output:
"a"

Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""
from typing import List


def find_longest_word(s: str, d: List[str]) -> str:
    def is_valid(w1, w2):
        i1, i2 = 0, 0
        n1, n2 = len(w1), len(w2)
        while i1 < n1 and i2 < n2:
            if w1[i1] == w2[i2]:
                i1 += 1
                i2 += 1
            else:
                i1 += 1
        return i2 == n2

    d = sorted(d, key=lambda x: (-len(x), x))
    for word in d:
        if is_valid(s, word):
            return word
    return ""


if __name__ == "__main__":
    find_longest_word(s="abpcplea", d=["ale", "apple", "monkey", "plea"])
