# https://leetcode.com/problems/n-queens-ii/
"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1

Constraints:
1 <= n <= 9
"""


def total_n_queens(n: int) -> int:
    def is_valid(board, row, col):
        for r in range(row):
            if board[r][col]:
                return False

        r, c = row, col
        while 0 <= r < n and 0 <= c < n:
            if board[r][c]:
                return False
            r -= 1
            c -= 1

        r, c = row, col
        while 0 <= r < n and 0 <= c < n:
            if board[r][c]:
                return False
            r -= 1
            c += 1
        return True

    def backtrack(board, row):
        nonlocal res
        if row == n:
            res += 1
            return

        for col in range(n):
            if not is_valid(board, row, col):
                continue
            board[row][col] = 1
            backtrack(board, row + 1)
            board[row][col] = 0

    res = 0
    board = [[0] * n for _ in range(n)]
    backtrack(board, 0)
    return res
