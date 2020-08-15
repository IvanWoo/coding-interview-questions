# https://leetcode.com/problems/word-search/
"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    row, col = len(board), len(board[0])
    visited = [[False] * col for _ in range(row)]

    ans = [False]

    def backtrack(i, r, c, visited):
        if ans[0]:
            return
        if i == len(word):
            ans[0] = True
            return
        for r_i, c_i in [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]:
            if r_i >= row or r_i < 0 or c_i >= col or c_i < 0 or visited[r_i][c_i]:
                continue
            if board[r_i][c_i] == word[i]:
                visited[r_i][c_i] = True
                backtrack(i + 1, r_i, c_i, visited)
                visited[r_i][c_i] = False

    for r in range(row):
        for c in range(col):
            if board[r][c] == word[0]:
                visited[r][c] = True
                backtrack(1, r, c, visited[:])
                visited[r][c] = False

    return ans[0]

