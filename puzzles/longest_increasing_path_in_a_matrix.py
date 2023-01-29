# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1
 

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
"""
from functools import cache


# brute force: TLE
def longest_increasing_path(matrix: list[list[int]]) -> int:
    ROWS = len(matrix)
    COLS = len(matrix[0])

    def get_val(pos):
        r, c = pos
        return matrix[r][c]

    def neighbors(pos):
        r, c = pos
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                nxt_pos = (nr, nc)
                if get_val(nxt_pos) > get_val(pos):
                    yield nxt_pos

    def dfs(pos, path):
        nonlocal ans
        for nxt_pos in neighbors(pos):
            if nxt_pos in path:
                continue
            dfs(nxt_pos, path + [pos])
        ans = max(ans, len(path))

    ans = 0
    for r in range(ROWS):
        for c in range(COLS):
            dfs((r, c), [(r, c)])

    return ans


# memo
def longest_increasing_path(matrix: list[list[int]]) -> int:
    ROWS = len(matrix)
    COLS = len(matrix[0])

    def get_val(pos):
        r, c = pos
        return matrix[r][c]

    def neighbors(pos):
        r, c = pos
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                nxt_pos = (nr, nc)
                if get_val(nxt_pos) > get_val(pos):
                    yield nxt_pos

    @cache
    def dfs(pos):
        longes = 1
        for nxt_pos in neighbors(pos):
            longes = max(longes, 1 + dfs(nxt_pos))
        return longes

    ans = 0
    for r in range(ROWS):
        for c in range(COLS):
            ans = max(ans, dfs((r, c)))

    return ans


if __name__ == "__main__":
    longest_increasing_path([[1]])
