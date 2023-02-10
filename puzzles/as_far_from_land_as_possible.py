# https://leetcode.com/problems/as-far-from-land-as-possible/
"""
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

Example 1:
Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:
Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""
from collections import defaultdict, deque
from math import inf


# brute force: TLE
def max_distance(grid: list[list[int]]) -> int:
    def cal_distance(x0: int, y0: int, x1: int, y1: int) -> int:
        return abs(x0 - x1) + abs(y0 - y1)

    n = len(grid)
    islands = set()
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                islands.add((r, c))
    ans = -1
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                continue
            min_dis = inf
            for x1, y1 in islands:
                min_dis = min(min_dis, cal_distance(r, c, x1, y1))
            if min_dis != inf:
                ans = max(ans, min_dis)
    return ans


# bfs
def max_distance(grid: list[list[int]]) -> int:
    def neighbors(r, c):
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = dr + r, dc + c
            if 0 <= nr < n and 0 <= nc < n:
                yield (nr, nc)

    n = len(grid)
    matrix = defaultdict(int)
    visited = set()
    q = deque()
    for r in range(n):
        for c in range(n):
            if grid[r][c]:
                q.append((r, c, 0))
    while q:
        r, c, steps = q.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        matrix[(r, c)] = steps
        for nr, nc in neighbors(r, c):
            q.append((nr, nc, steps + 1))
    ans = max([matrix[(r, c)] for r in range(n) for c in range(n)])
    return ans or -1
