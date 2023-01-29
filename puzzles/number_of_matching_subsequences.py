# https://leetcode.com/problems/number-of-matching-subsequences/
"""
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Example 1:
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

Example 2:
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
 
Constraints:
1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
"""
from bisect import bisect_left
from collections import defaultdict
from functools import cache


# brute force
def num_matching_subseq(s: str, words: list[str]) -> int:
    @cache
    def is_subseq(w: str, s: str):
        i, j = 0, 0
        while i < len(w) and j < len(s):
            if w[i] == s[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(w)

    ans = 0
    for w in words:
        if is_subseq(w, s):
            ans += 1
    return ans


def num_matching_subseq(s: str, words: list[str]) -> int:
    @cache
    def is_subseq(word: str) -> bool:
        nonlocal hashmap
        lower = 0
        for char in word:
            if char not in hashmap:
                return False
            idx_list = hashmap[char]
            n = len(idx_list)
            i = bisect_left(idx_list, lower)
            if i == n:
                return False
            lower = idx_list[i] + 1
        return True

    hashmap = defaultdict(list)
    for i, char in enumerate(s):
        hashmap[char].append(i)

    ans = 0
    for w in words:
        if is_subseq(w):
            ans += 1
    return ans
