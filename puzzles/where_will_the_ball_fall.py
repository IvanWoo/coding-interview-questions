# https://leetcode.com/problems/where-will-the-ball-fall/
"""
You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.

Example 1:
Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
Output: [1,-1,-1,-1,-1]
Explanation: This example is shown in the photo.
Ball b0 is dropped at column 0 and falls out of the box at column 1.
Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.

Example 2:
Input: grid = [[-1]]
Output: [-1]
Explanation: The ball gets stuck against the left wall.

Example 3:
Input: grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
Output: [0,1,2,3,4,-1]
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is 1 or -1.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Position:
    row: int
    col: int
    # 0 is top, 1 is bottom
    dir: int


def find_ball(grid: list[list[int]]) -> list[int]:
    def nxt(cur_p: Position, pre_p: Optional[Position]) -> tuple[Position, Position]:
        cur_row, cur_col, cur_dir = cur_p.row, cur_p.col, cur_p.dir
        nxt_row = nxt_col = 0
        match (cur_p.dir, grid[cur_row][cur_col]):
            case (0, -1):
                nxt_row, nxt_col = cur_row, cur_col - 1
            case (0, 1):
                nxt_row, nxt_col = cur_row, cur_col + 1
            case (1, _):
                nxt_row, nxt_col = cur_row + 1, cur_col
        if not (0 <= nxt_row < rows and 0 <= nxt_col < cols):
            return None, cur_p
        if cur_dir == 1:
            nxt_dir = cur_dir ^ 1
        else:
            match (grid[cur_row][cur_col], grid[nxt_row][nxt_col]):
                case (-1, -1):
                    nxt_dir = cur_dir ^ 1
                case (1, 1):
                    nxt_dir = cur_dir ^ 1
                case _:
                    nxt_dir = cur_dir
        nxt_p = Position(nxt_row, nxt_col, nxt_dir)
        if nxt_p == pre_p:
            return None, cur_p
        return nxt_p, cur_p

    rows, cols = len(grid), len(grid[0])
    ans = [-1] * cols
    for c in range(cols):
        cur_p = Position(0, c, 0)
        pre_p = None
        while cur_p:
            cur_p, pre_p = nxt(cur_p, pre_p)
        if pre_p and pre_p.row == rows - 1 and pre_p.dir == 1:
            ans[c] = pre_p.col
    return ans


def find_ball(grid: list[list[int]]) -> list[int]:
    def find(c):
        for r in range(rows):
            n_c = c + grid[r][c]
            if n_c < 0 or n_c >= cols or grid[r][c] != grid[r][n_c]:
                return -1
            c = n_c
        return c

    rows, cols = len(grid), len(grid[0])
    return [find(c) for c in range(cols)]


if __name__ == "__main__":
    find_ball(
        [
            [1, 1, 1, -1, -1],
            [1, 1, 1, -1, -1],
            [-1, -1, -1, 1, 1],
            [1, 1, 1, 1, -1],
            [-1, -1, -1, -1, -1],
        ],
    )
