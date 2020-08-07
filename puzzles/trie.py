# https://leetcode.com/problems/implement-trie-prefix-tree/
"""
208. Implement Trie (Prefix Tree)
Medium

3435

52

Add to List

Share
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""
from __future__ import annotations
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, Optional, Any

# https://docs.python.org/3/library/dataclasses.html#mutable-default-values
@dataclass
class TrieNode:
    children: Dict[str, TrieNode] = field(default_factory=dict)
    value: Optional[Any] = None


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.value = word

    def searchPrefix(self, word: str) -> TrieNode:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.searchPrefix(word)
        return node != None and node.value == word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.searchPrefix(prefix)
        return node != None


if __name__ == "__main__":
    obj = Trie()
    word = "hello"
    prefix = "hey"
    obj.insert(word)
    print(f"{obj.search(word)=}")
    print(f"{obj.startsWith(prefix)=}")

