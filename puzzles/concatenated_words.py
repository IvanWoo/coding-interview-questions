# https://leetcode.com/problems/concatenated-words/description/
"""
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example 1:
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Example 2:
Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
 
Constraints:
1 <= words.length <= 104
1 <= words[i].length <= 30
words[i] consists of only lowercase English letters.
All the strings of words are unique.
1 <= sum(words[i].length) <= 105
"""
from functools import cache


# brute force: TLE
def find_all_concatenated_words_in_a_dict(words: list[str]) -> list[str]:
    @cache
    def is_concatenated(w: str, idx: int) -> bool:
        if not w:
            return True
        return any([is_concatenated(w[len(char) :], idx) for char in words[:idx] if w.startswith(char)])

    words.sort(key=len)
    ans = []
    for i, w in enumerate(words):
        if is_concatenated(w, i):
            ans.append(w)
    return ans


def find_all_concatenated_words_in_a_dict(words: list[str]) -> list[str]:
    @cache
    def dfs(w: str) -> bool:
        for i in range(1, len(w)):
            prefix = w[:i]
            suffix = w[i:]
            if prefix in d and suffix in d:
                return True
            if prefix in d and dfs(suffix):
                return True
            if suffix in d and dfs(prefix):
                return True
        return False

    d = set(words)
    ans = []
    for w in words:
        if dfs(w):
            ans.append(w)
    return ans
