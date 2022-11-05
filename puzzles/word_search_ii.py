# https://leetcode.com/problems/word-search-ii/
"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""
from __future__ import annotations
from dataclasses import dataclass, field

# https://docs.python.org/3/library/dataclasses.html#mutable-default-values
@dataclass
class TrieNode:
    children: dict[str, TrieNode] = field(default_factory=dict)
    end: str = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = word


def find_words(board, words):
    def backtrack(node, r, c):
        nonlocal res, visited
        if not node:
            return
        if node.end:
            res.add(node.end)

        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        temp = board[r][c]
        node = node.children.get(temp)
        if (r, c) in visited:
            return
        visited.add((r, c))
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            backtrack(node, nr, nc)
        visited.remove((r, c))

    rows, cols = len(board), len(board[0])
    visited = set()
    res = set()
    trie = Trie()
    node = trie.root
    for word in words:
        trie.insert(word)

    for r in range(rows):
        for c in range(cols):
            backtrack(node, r, c)
    return res
