# https://leetcode.com/problems/minesweeper/
"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.


Example 1:

Input:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:

Input:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:



Note:

The range of the input matrix's height and width is [1,50].
The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
The input board won't be a stage when game is over (some mines have been revealed).
For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.
"""
from typing import List


# TLE
def update_board(board: List[List[str]], click: List[int]) -> List[List[str]]:
    DIRS = [
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
    ]

    def get_around_mine(r, c):
        count = 0
        row, col = len(board), len(board[0])
        for i, j in DIRS:
            new_r, new_c = r + i, c + j
            if 0 <= new_r < row and 0 <= new_c < col and board[new_r][new_c] == "M":
                count += 1
        return count

    s_r, s_c = click
    if board[s_r][s_c] == "M":
        board[s_r][s_c] = "X"
        return board
    row, col = len(board), len(board[0])
    q = [(s_r, s_c)]
    while q:
        new_q = []
        while q:
            r, c = q.pop()
            num = get_around_mine(r, c)
            if num == 0:
                board[r][c] = "B"
                for i, j in DIRS:
                    new_r, new_c = r + i, c + j
                    if (
                        0 <= new_r < row
                        and 0 <= new_c < col
                        and board[new_r][new_c] == "E"
                    ):
                        new_q.append((new_r, new_c))
            else:
                board[r][c] = str(num)
        q = new_q
    return board


def update_board(board: List[List[str]], click: List[int]) -> List[List[str]]:
    d = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
    m, n = len(board), len(board[0])

    def dfs(B, i, j):
        if i < 0 or j < 0 or i >= m or j >= n:
            return
        if B[i][j] == "M":
            B[i][j] = "X"
        elif B[i][j] == "E":
            mine = sum(
                B[i + x][j + y] == "M"
                for x, y in d
                if 0 <= i + x < m and 0 <= j + y < n
            )
            B[i][j] = mine and str(mine) or "B"
            for x, y in d * (not mine):
                dfs(B, i + x, j + y)
        return B

    return dfs(board, *click)


if __name__ == "__main__":
    update_board(
        [
            ["E", "E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E", "E", "E", "M"],
            ["E", "E", "M", "E", "E", "E", "E", "E"],
            ["M", "E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "M", "M", "E", "E", "E", "E"],
        ],
        [0, 0],
    )
