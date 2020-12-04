# https://leetcode.com/problems/word-break/
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
from typing import List

# TLE
def word_break(s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    n = len(s)
    res = False

    def helper(i):
        nonlocal res
        if res:
            return
        if i == n:
            res = True
            return
        for j in range(i + 1, n + 1):
            if s[i:j] in word_set:
                helper(j)

    helper(0)
    return res


# dp
def word_break(s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        # get all True value indexes
        ts = [k for k, v in enumerate(dp) if v]
        dp[i] = any([s[x:i] in word_set for x in ts])
    return dp[-1]


if __name__ == "__main__":
    word_break("applepenapple", ["apple", "pen", "app"])
