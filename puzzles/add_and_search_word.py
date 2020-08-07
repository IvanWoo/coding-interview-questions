# https://leetcode.com/problems/add-and-search-word-data-structure-design/
"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""

from dataclasses import dataclass, field
from typing import Dict, Optional, Any


@dataclass
class TrieNode:
    children: Dict[str, "TrieNode"] = field(default_factory=dict)
    # we don't need to save the val, simply using a isEnd flag is enough
    value: Optional[Any] = None


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
        node.value = word

    def searchHelper(self, word: str, index: int, node: TrieNode) -> bool:
        if index == len(word):
            return node.value != None
        if word[index] == ".":
            return any(
                [
                    self.searchHelper(word, index + 1, node.children[child])
                    for child in node.children
                ]
            )
        if word[index] not in node.children:
            return False
        return self.searchHelper(word, index + 1, node.children[word[index]])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.searchHelper(word, 0, self.root)


if __name__ == "__main__":
    obj = WordDictionary()

    for word in ["bad", "dad", "mad", "pad"]:
        obj.addWord(word)

    for word in ["bad", ".ad", "b.."]:
        print(f"{obj.search(word)=}")
