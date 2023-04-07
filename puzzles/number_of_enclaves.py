# https://leetcode.com/problems/number-of-enclaves/
"""
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example 2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
"""


# TLE
def num_enclaves(grid: list[list[int]]) -> int:
    def count(path: list[tuple[int, int]]) -> int:
        for r, c in path:
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                return 0
        return len(path)

    def dfs(r: int, c: int) -> list[tuple[int, int]]:
        if not grid[r][c] or (r, c) in visited:
            return []
        visited.add((r, c))
        path = [(r, c)]
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                path.extend(dfs(nr, nc))
        return path

    rows, cols = len(grid), len(grid[0])
    visited = set()
    ret = 0
    for r in range(rows):
        for c in range(cols):
            ret += count(dfs(r, c))
    return ret


def num_enclaves(grid: list[list[int]]) -> int:
    def dfs(r, c):
        if not grid[r][c]:
            return
        grid[r][c] = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                dfs(nr, nc)

    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                dfs(r, c)

    return sum([sum(r) for r in grid])


def num_enclaves(grid: list[list[int]]) -> int:
    def dfs(r, c):
        if not grid[r][c] or (r, c) in visited:
            return
        visited.add((r, c))
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                dfs(nr, nc)

    visited = set()
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                dfs(r, c)

    ret = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] and (r, c) not in visited:
                ret += 1
    return ret
