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
from collections import defaultdict


def num_islands(grid: list[list[str]]) -> int:
    def dfs(grid, r, c):
        if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != "1":
            return
        grid[r][c] = "#"
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dfs(grid, r + i, c + j)

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


def num_islands(grid: list[list[str]]) -> int:
    def dfs(r, c):
        nonlocal visited
        visited[(r, c)] = 1
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if visited[(nr, nc)]:
                    continue
                if grid[nr][nc] == "1":
                    dfs(nr, nc)

    visited = defaultdict(int)
    ans = 0
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if visited[(r, c)]:
                continue
            if grid[r][c] == "0":
                continue
            elif grid[r][c] == "1":
                ans += 1
                dfs(r, c)
    return ans


def num_islands(grid: list[list[str]]) -> int:
    class UF:
        def __init__(self):
            self.parent = {}

        def insert(self, x):
            self.parent[x] = x

        def find(self, x):
            while self.parent[x] != x:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x

        def union(self, u, v):
            root_u = self.find(u)
            root_v = self.find(v)
            self.parent[root_u] = root_v

    uf = UF()
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                uf.insert((r, c))
                if r >= 1 and grid[r - 1][c] == "1":
                    uf.union((r, c), (r - 1, c))
                if c >= 1 and grid[r][c - 1] == "1":
                    uf.union((r, c), (r, c - 1))

    ans = 0
    for k, v in uf.parent.items():
        if k == v:
            ans += 1
    return ans


if __name__ == "__main__":
    num_islands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
