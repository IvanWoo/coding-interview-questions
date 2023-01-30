# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
"""
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

Example 1:
Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation:
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

Example 2:
Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
"""
from collections import deque
from math import inf


# TLE
def shortest_path(grid: list[list[int]], k: int) -> int:
    def helper(x: int, y: int, r: int):
        nonlocal path
        if (x, y) == (m - 1, n - 1):
            return len(path)

        ans = inf
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if (nx, ny) in path:
                    continue
                if grid[nx][ny] and r == 0:
                    continue
                path.add((nx, ny))
                ans = min(ans, helper(nx, ny, r - grid[nx][ny]))
                path.remove((nx, ny))
        return ans

    m, n = len(grid), len(grid[0])
    path = set()
    ans = helper(0, 0, k)
    return -1 if ans == inf else ans


# bfs
def shortest_path(grid: list[list[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    q = deque()
    # (row, col, steps, k)
    q.append((0, 0, 0, k))
    seen = set()
    while q:
        r, c, steps, rk = q.popleft()
        if (r, c) == (m - 1, n - 1):
            return steps

        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and (nr, nc, rk) not in seen:
                seen.add((nr, nc, rk))
                if grid[nr][nc] == 1 and rk > 0:
                    q.append((nr, nc, steps + 1, rk - 1))
                elif grid[nr][nc] == 0:
                    q.append((nr, nc, steps + 1, rk))
    return -1
