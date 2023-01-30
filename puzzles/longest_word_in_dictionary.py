# https://leetcode.com/problems/longest-word-in-dictionary/
"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Note:
All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class TrieNode:
    children: Dict[str, "TrieNode"] = field(default_factory=dict)
    isEnd = False


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def searchHelper(self, word: str, index: int, node: TrieNode, length: int) -> bool:
        if index >= len(word):
            return length
        if not node.children[word[index]].isEnd:
            return 0
        return self.searchHelper(
            word, index + 1, node.children[word[index]], length + 1
        )

    def search(self, word: str) -> bool:
        return self.searchHelper(word, 0, self.root, 0)


def longest_word(words: List[str]) -> str:
    wd = WordDictionary()
    max_length = 0
    ans = ""
    for word in words:
        wd.addWord(word)

    for word in words:
        length = wd.search(word)
        if length > max_length:
            max_length = length
            ans = word
        elif length == max_length:
            ans = min(ans, word)
    return ans


def longest_word(words: List[str]) -> str:
    valid = set([""])

    for word in sorted(words, key=lambda x: len(x)):
        if word[:-1] in valid:
            valid.add(word)

    return max(sorted(valid), key=lambda x: len(x))


if __name__ == "__main__":
    pass
