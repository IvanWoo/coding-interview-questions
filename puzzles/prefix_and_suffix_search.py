# https://leetcode.com/problems/prefix-and-suffix-search/
"""
Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.


Example 1:
Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".

Constraints:
1 <= words.length <= 15000
1 <= words[i].length <= 10
1 <= prefix.length, suffix.length <= 10
words[i], prefix and suffix consist of lower-case English letters only.
At most 15000 calls will be made to the function f.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TrieNode:
    children: dict[str, TrieNode] = field(default_factory=dict)
    prefix_idx: set[int] = field(default_factory=set)
    suffix_idx: set[int] = field(default_factory=set)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, idx: int, is_reverse: bool) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if is_reverse:
                node.suffix_idx.add(idx)
            else:
                node.prefix_idx.add(idx)

    def search(self, prefix: str) -> Optional[TrieNode]:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def intersect(self, prefix: str, suffix: str):
        p_node, s_node = self.search(prefix), self.search(suffix)
        if not p_node or not s_node:
            return -1

        merged = p_node.prefix_idx.intersection(s_node.suffix_idx)
        return max(merged) if merged else -1


class WordFilter:
    def __init__(self, words: list[str]):
        self.trie = Trie()
        # dedup to speed up the performance
        words = {word: i for (i, word) in enumerate(words)}
        for word, i in words.items():
            self.trie.insert(word, i, False)
            self.trie.insert(word[::-1], i, True)

    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.intersect(prefix, suffix[::-1])


if __name__ == "__main__":
    words = ["apple"]
    word_filter = WordFilter(words)
    prefix, suffix = "a", "e"
    word_filter.f(prefix, suffix)
