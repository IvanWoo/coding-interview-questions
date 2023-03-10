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


if __name__ == "__main__":
    shortest_path_binary_matrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]])
