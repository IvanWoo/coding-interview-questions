# https://leetcode.com/problems/surrounded-regions/
"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""

from collections import deque
from typing import List
from puzzles.union_find import UF


def on_border(board, r, c):
    row, col = len(board), len(board[0])
    return any([r == 0, r == row - 1, c == 0, c == col - 1])


def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    if not board:
        return
    q = deque()
    row, col = len(board), len(board[0])
    for r in range(row):
        for c in range(col):
            if board[r][c] == "O" and on_border(board, r, c):
                q.append((r, c))

    while q:
        r, c = q.popleft()
        if 0 <= r < row and 0 <= c < col and board[r][c] == "O":
            board[r][c] = "D"
            q.extend([(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])
            # for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            #     q.append((r + i, c + j))

    for r in range(row):
        for c in range(col):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "D":
                board[r][c] = "O"

    return


def solve(board: List[List[str]]) -> None:
    if not board:
        return
    m, n = len(board), len(board[0])
    uf = UF(m * n + 1)
    dummy = m * n

    for i in range(m):
        if board[i][0] == "O":
            uf.union(i * n, dummy)
        if board[i][n - 1] == "O":
            uf.union(i * n + n - 1, dummy)

    for j in range(n):
        if board[0][j] == "O":
            uf.union(j, dummy)
        if board[m - 1][j] == "O":
            uf.union(n * (m - 1) + j, dummy)

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if board[i][j] == "O":
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x = i + di
                    y = j + dj
                    if board[x][y] == "O":
                        uf.union(x * n + y, i * n + j)

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if not uf.connected(dummy, i * n + j):
                board[i][j] = "X"
    return
