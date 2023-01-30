# https://leetcode.com/problems/longest-string-chain/
"""
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

Example 1:
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Example 2:
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

Example 3:
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.

Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.
"""
from collections import defaultdict
from functools import cache
from math import inf


# TLE
def longest_str_chain(words: list[str]) -> int:
    @cache
    def is_valid(w1: str, w2: str) -> bool:
        i, j, can_insert = len(w1) - 1, len(w2) - 1, True
        while i >= 0 and j >= 0:
            if w1[i] != w2[j]:
                if can_insert:
                    j -= 1
                    can_insert = False
                    continue
                return False

            i -= 1
            j -= 1
        return True

    def helper(w: str, steps: int) -> None:
        nonlocal groups, res
        res = max(res, steps)
        for next_w in groups[len(w) + 1]:
            if is_valid(w, next_w):
                helper(next_w, steps + 1)

    groups = defaultdict(list)
    min_len, max_len = inf, -inf
    for w in words:
        min_len = min(min_len, len(w))
        max_len = max(max_len, len(w))
        groups[len(w)].append(w)

    res = 1
    for l in range(min_len, max_len):
        for w in groups[l]:
            potential = max_len - l
            if potential < res:
                continue
            helper(w, 1)
    return res


def longest_str_chain(words: list[str]) -> int:
    @cache
    def is_valid(w1: str, w2: str) -> bool:
        i, j, can_insert = len(w1) - 1, len(w2) - 1, True
        while i >= 0 and j >= 0:
            if w1[i] != w2[j]:
                if can_insert:
                    j -= 1
                    can_insert = False
                    continue
                return False

            i -= 1
            j -= 1
        return True

    @cache
    def helper(w: str, steps: int) -> int:
        nonlocal next_words
        vals = [helper(next_w, steps + 1) for next_w in next_words[w]]
        return max(vals) if vals else steps

    groups = defaultdict(list)
    min_len, max_len = inf, -inf
    for w in words:
        min_len = min(min_len, len(w))
        max_len = max(max_len, len(w))
        groups[len(w)].append(w)

    next_words = defaultdict(list)
    for l in range(min_len, max_len):
        for w in groups[l]:
            for next_w in groups[l + 1]:
                if is_valid(w, next_w):
                    next_words[w].append(next_w)

    res = 1
    for l in range(min_len, max_len):
        for w in groups[l]:
            potential = max_len - l
            if potential < res:
                continue
            res = max(res, helper(w, 1))
    return res


def longest_str_chain(words: list[str]) -> int:
    dp = {w: 1 for w in words}

    res = 1
    for w in sorted(words, key=len):
        for i in range(len(w)):
            prev = w[:i] + w[i + 1 :]
            if prev in dp:
                dp[w] = max(dp[w], dp[prev] + 1)
        res = max(res, dp[w])
    return res
