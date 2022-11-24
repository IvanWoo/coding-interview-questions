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
from collections import Counter
from itertools import chain


def exist(board: list[list[str]], word: str) -> bool:
    def backtrack(r, c, idx, visited):
        if board[r][c] != word[idx]:
            return False
        if idx == len(word) - 1:
            return True
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                visited.add((nr, nc))
                if backtrack(nr, nc, idx + 1, visited):
                    return True
                visited.remove((nr, nc))

    source = Counter(list(chain(*board)))
    target = Counter(word)
    if not source >= target:
        return False
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0, set([(r, c)])):
                return True

    return False


if __name__ == "__main__":
    exist(
        [
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
        ],
        "AAAAAAAAAAAABAA",
    )
