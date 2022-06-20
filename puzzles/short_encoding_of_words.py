# https://leetcode.com/problems/short-encoding-of-words/
"""
A valid encoding of an array of words is any reference string s and array of indices indices such that:

words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

Example 1:
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"

Example 2:
Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].
 

Constraints:
1 <= words.length <= 2000
1 <= words[i].length <= 7
words[i] consists of only lowercase letters.
"""
from __future__ import annotations
from dataclasses import dataclass, field

# brute force
def minimum_length_encoding(words: list[str]) -> int:
    words.sort(key=len, reverse=True)
    res = []
    for suffix in words:
        if not any(word.endswith(suffix) for word in res):
            res.append(suffix)
    return sum(len(word) + 1 for word in res)


@dataclass
class TrieNode:
    children: dict[str, TrieNode] = field(default_factory=dict)


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]


def minimum_length_encoding(words: list[str]) -> int:
    def dfs(node: TrieNode, curr: int) -> int:
        if not node.children:
            return curr
        return sum(dfs(adj, curr + 1) for adj in node.children.values())

    trie = Trie()
    for word in set(words):
        trie.insert(word[::-1])
    return dfs(trie.root, 1)
