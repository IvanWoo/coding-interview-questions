# https://leetcode.com/problems/number-of-islands/
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    ans = 0
    row, col = len(grid), len(grid[0])
    for r in range(row):
        for c in range(col):
            if grid[r][c] == "1":
                dfs(grid, r, c)
                ans += 1
    return ans


def dfs(grid, r, c):
    row, col = len(grid), len(grid[0])
    if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != "1":
        return
    grid[r][c] = "#"
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dfs(grid, r + i, c + j)
