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
from typing import List


def is_valid(board, r, c):
    row, col = len(board), len(board[0])
    return 0 <= r < row and 0 <= c < col


def is_alive(board, r, c):
    count = 0
    for i, j in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if is_valid(board, r + i, c + j):
            count += board[r + i][c + j]
    if board[r][c]:
        return count in [2, 3]
    else:
        return count == 3


def game_of_life(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    row, col = len(board), len(board[0])
    pos = []
    for r in range(row):
        for c in range(col):
            if is_alive(board, r, c):
                if board[r][c] == 0:
                    pos.append((r, c))
            else:
                if board[r][c] == 1:
                    pos.append((r, c))

    for r, c in pos:
        board[r][c] = 0 if board[r][c] else 1
