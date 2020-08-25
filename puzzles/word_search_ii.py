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
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, Optional, Any

# https://docs.python.org/3/library/dataclasses.html#mutable-default-values
@dataclass
class TrieNode:
    children: Dict[str, TrieNode] = field(default_factory=dict)
    is_end: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> TrieNode:
        node = self.root
        for char in word:
            node = node.children.get(char)
            if not node:
                return False
        return node.is_end


def find_words(board, words):
    row, col = len(board), len(board[0])
    res = []
    trie = Trie()
    node = trie.root
    for word in words:
        trie.insert(word)

    for r in range(row):
        for c in range(col):
            dfs(board, node, r, c, "", res)
    return res


def dfs(board, node, r, c, path, res):
    row, col = len(board), len(board[0])
    if node.is_end:
        res.append(path)
        node.is_end = False

    if r < 0 or r >= row or c < 0 or c >= col:
        return

    temp = board[r][c]
    node = node.children.get(temp)
    if not node:
        return
    board[r][c] = "#"
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dfs(board, node, r + i, c + j, path + temp, res)
    board[r][c] = temp

