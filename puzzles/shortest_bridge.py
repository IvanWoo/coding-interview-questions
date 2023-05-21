# https://leetcode.com/problems/shortest-bridge/
"""
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Example 1:
Input: A = [[0,1],[1,0]]
Output: 1

Example 2:
Input: A = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:
Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Constraints:
2 <= A.length == A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
"""
from collections import deque


def shortest_bridge(grid: list[list[int]]) -> int:
    def dis(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2) - 1

    def neighbors(x, y):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n:
                yield nx, ny

    def on_boundary(x, y):
        for nx, ny in neighbors(x, y):
            if grid[nx][ny] == 0:
                return True
        return False

    def get_labeled_island(label: int, visited):
        return [
            (r, c)
            for r in range(n)
            for c in range(n)
            if visited[r][c] == label and on_boundary(r, c)
        ]

    def label_island(n):
        visited = [[0] * n for _ in range(n)]
        counter = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0 or visited[i][j]:
                    continue
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    if visited[x][y]:
                        continue
                    visited[x][y] = counter
                    for nx, ny in neighbors(x, y):
                        if grid[nx][ny]:
                            q.append((nx, ny))
                counter += 1
        return visited

    n = len(grid)
    visited = label_island(n)

    island1 = get_labeled_island(1, visited)
    island2 = get_labeled_island(2, visited)

    ret = n * n
    for i1 in island1:
        for i2 in island2:
            ret = min(ret, dis(i1, i2))
    return ret
