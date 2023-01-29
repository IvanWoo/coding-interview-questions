# https://leetcode.com/problems/sudoku-solver/
"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""
import copy
from typing import List


def solve_sudoku(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    def get_bucket(n):
        if n < 3:
            return 0
        elif n < 6:
            return 3
        else:
            return 6

    def get_sub_sqr(row, col):
        return get_bucket(row), get_bucket(col)

    def is_valid(board, row, col, val):
        for c in range(9):
            if c == col:
                continue
            if board[row][c] == val:
                return False

        for r in range(9):
            if r == row:
                continue
            if board[r][col] == val:
                return False

        s_r, s_c = get_sub_sqr(row, col)
        for r in range(s_r, s_r + 3):
            for c in range(s_c, s_c + 3):
                if r == row and c == col:
                    continue
                if board[r][c] == val:
                    return False

        return True

    def backtrack(board, row, col):
        nonlocal res
        if res:
            return True
        if row >= 9:
            res = copy.deepcopy(board)
            return True
        elif col >= 9:
            return backtrack(board, row + 1, 0)
        if board[row][col] != ".":
            return backtrack(board, row, col + 1)
        for val in range(1, 10):
            if not is_valid(board, row, col, str(val)):
                continue
            board[row][col] = str(val)
            if backtrack(board, row, col + 1):
                return True
            board[row][col] = "."
        return False

    res = []
    backtrack(board, 0, 0)
    for r in range(9):
        for c in range(9):
            board[r][c] = res[0][r][c]
    return


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    solve_sudoku(board)
    ans = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]
    print(f"{board == ans=}")
