# https://leetcode.com/problems/n-queens/
"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""


def solve_n_queens(n: int) -> list[list[str]]:
    res = []
    board = [["."] * n for _ in range(n)]

    def is_valid(board, row, col):
        # above upper
        for i in range(row):
            if board[i][col] == "Q":
                return False
        # right upper
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        # left upper
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        return True

    def backtrack(board, row):
        if row == n:
            res.append(["".join(r) for r in board])
            return
        for col in range(n):
            if not is_valid(board, row, col):
                continue
            board[row][col] = "Q"
            backtrack(board, row + 1)
            board[row][col] = "."

    backtrack(board, 0)
    return res


def solve_n_queens(n: int) -> list[list[str]]:
    def serialize(board: list[list[int]]) -> list[list[str]]:
        val = ["".join("Q" if c else "." for c in r) for r in board]
        return val

    def is_valid(board, row, col):
        # above upper
        for i in range(row):
            if board[i][col]:
                return False
        # right upper
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j]:
                return False
            i -= 1
            j += 1
        # left upper
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            i -= 1
            j -= 1
        return True

    def backtrack(board, row):
        nonlocal res
        if row == n:
            res.append(serialize(board))
            return
        for col in range(n):
            if not is_valid(board, row, col):
                continue
            board[row][col] = 1
            backtrack(board, row + 1)
            board[row][col] = 0

    res = []
    board = [[0] * n for _ in range(n)]
    backtrack(board, 0)
    return res


# generator
def solve_n_queens(n: int) -> list[list[str]]:
    def serialize(board: list[list[int]]) -> list[list[str]]:
        val = ["".join("Q" if c else "." for c in r) for r in board]
        return val

    def is_valid(board, row, col):
        # above upper
        for i in range(row):
            if board[i][col]:
                return False
        # right upper
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j]:
                return False
            i -= 1
            j += 1
        # left upper
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            i -= 1
            j -= 1
        return True

    def backtrack(board, row):
        if row == n:
            yield serialize(board)
            return
        for col in range(n):
            if not is_valid(board, row, col):
                continue
            board[row][col] = 1
            yield from backtrack(board, row + 1)
            board[row][col] = 0

    board = [[0] * n for _ in range(n)]
    return list(backtrack(board, 0))
