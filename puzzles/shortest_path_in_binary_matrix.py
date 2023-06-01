# https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""
from collections import deque
from math import inf


def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
    def neighbors(r, c):
        for dr, dc in [
            (-1, 0),
            (0, -1),
            (0, 1),
            (1, 0),
            (1, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
        ]:
            yield r + dr, c + dc

    n = len(grid)
    visited = [[0] * n for _ in range(n)]
    q = [(0, 0, 1)]
    while q:
        new_q = deque()
        for r, c, path in q:
            if grid[r][c] or visited[r][c]:
                continue
            visited[r][c] = 1
            if r == n - 1 and c == n - 1:
                return path
            for nr, nc in neighbors(r, c):
                if 0 <= nr < n and 0 <= nc < n:
                    new_q.append((nr, nc, path + 1))
        q = new_q
    return -1


def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
    n = len(grid)
    if grid[0][0] != 0:
        return -1

    dp = [[inf] * n for _ in range(n)]
    q = deque([(0, 0, 1)])
    while q:
        r, c, steps = q.popleft()
        if steps >= dp[r][c]:
            continue

        dp[r][c] = min(dp[r][c], steps)
        if r == c == n - 1:
            continue
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and grid[nr][nc] == 0
                    and dp[nr][nc] == inf
                ):
                    q.append((nr, nc, steps + 1))

    return dp[-1][-1] if dp[-1][-1] != inf else -1
