# https://leetcode.com/problems/max-area-of-island/
"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.

Note: The length of each dimension in the given grid does not exceed 50.
"""

from collections import deque


def max_area_of_island(grid: list[list[int]]) -> int:
    def bfs(grid, r, c):
        row, col = len(grid), len(grid[0])

        ans = 0
        q = deque([(r, c)])
        while q:
            r, c = q.popleft()
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != 1:
                continue
            else:
                ans += 1
                grid[r][c] = "."
                for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    q.append((r + i, c + j))
        return ans

    if not grid:
        return 0

    ans = 0
    row, col = len(grid), len(grid[0])
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                ans = max(ans, bfs(grid, r, c))

    return ans


def max_area_of_island(grid: list[list[int]]) -> int:
    def neighbors(i, j):
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj]:
                yield ni, nj

    rows, cols = len(grid), len(grid[0])
    visited = [[0] * cols for _ in range(rows)]
    ans = 0
    for r in range(rows):
        for c in range(cols):
            if not grid[r][c]:
                continue
            queue = [(r, c)]
            count = 0
            while queue:
                new_queue = []
                while queue:
                    cr, cc = queue.pop()
                    if visited[cr][cc]:
                        continue
                    visited[cr][cc] = 1
                    count += 1
                    new_queue.extend(neighbors(cr, cc))
                ans = max(ans, count)
                queue = new_queue
    return ans
