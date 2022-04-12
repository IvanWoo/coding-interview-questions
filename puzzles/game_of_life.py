# https://leetcode.com/problems/game-of-life/
"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:
Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""


def neighbors(board, r, c):
    rows, cols = len(board), len(board[0])
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            rr, cc = r + i, c + j
            if 0 <= rr < rows and 0 <= cc < cols:
                yield rr, cc


def game_of_life(board: list[list[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    nxt_ops = []
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            total = sum([board[rr][cc] for rr, cc in neighbors(board, r, c)])
            if board[r][c] == 1:
                if total < 2 or total > 3:
                    nxt_ops.append((r, c, 0))
            else:
                if total == 3:
                    nxt_ops.append((r, c, 1))
    for r, c, v in nxt_ops:
        board[r][c] = v
