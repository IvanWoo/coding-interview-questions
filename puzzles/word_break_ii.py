# https://leetcode.com/problems/word-break-ii/
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""
from typing import List
from puzzles.word_break import word_break as is_breakable

# TLE
def word_break(s: str, wordDict: List[str]) -> List[str]:
    def helper(i, words):
        nonlocal res
        if i == len(s):
            res.append(" ".join(words))
        for j in range(i + 1, len(s) + 1):
            w = s[i:j]
            if w in word_set:
                helper(j, words + [w])

    word_set = set(wordDict)
    res = []
    helper(0, [])
    return res


# dp
def word_break(s: str, wordDict: List[str]) -> List[str]:
    # use this check to get rid of TLE on leetcode
    if not is_breakable(s, wordDict):
        return []

    n = len(s)
    word_set = set(wordDict)
    dp = [[] for _ in range(n + 1)]
    dp[0] = [""]

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i].extend([pre + " " + s[j:i] if pre else s[j:i] for pre in dp[j]])

    return dp[-1]


if __name__ == "__main__":
    word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"])
