# https://leetcode.com/problems/swim-in-rising-water/
"""
On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?


Example 1:
Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:
Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

Note:
2 <= N <= 50.
grid[i][j] is a permutation of [0, ..., N*N - 1].
"""
import heapq
from typing import List


class UF:
    def __init__(self):
        self.parent = dict()
        self.value = dict()

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.value[x] = 1

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def is_connected(self, u, v):
        return self.find(u) == self.find(v)

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return
        if self.value[root_u] > self.value[root_v]:
            self.parent[root_v] = root_u
            self.value[root_u] += self.value[root_v]
        else:
            self.parent[root_u] = root_v
            self.value[root_v] += self.value[root_u]


# union find: O(N^3)
def swim_in_water(grid: List[List[int]]) -> int:
    uf = UF()
    row, col = len(grid), len(grid[0])
    max_t = 0
    for r in range(row):
        for c in range(col):
            uf.add((r, c))
            max_t = max(max_t, grid[r][c])

    for t in range(grid[row - 1][col - 1], max_t + 2):
        if uf.is_connected((0, 0), (row - 1, col - 1)):
            return t - 1
        for r in range(row):
            for c in range(col):
                if grid[r][c] > t:
                    continue
                for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_r, new_c = r + i, c + j
                    if (
                        0 <= new_r < row
                        and 0 <= new_c < col
                        and grid[new_r][new_c] <= t
                    ):
                        uf.union((r, c), (new_r, new_c))


# union find + binary search: O(N^2*logN)
def swim_in_water(grid: List[List[int]]) -> int:
    def is_connected(t):
        uf = UF()
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                uf.add((r, c))

        for r in range(row):
            for c in range(col):
                if grid[r][c] > t:
                    continue
                for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_r, new_c = r + i, c + j
                    if (
                        0 <= new_r < row
                        and 0 <= new_c < col
                        and grid[new_r][new_c] <= t
                    ):
                        uf.union((r, c), (new_r, new_c))
                        if uf.is_connected((0, 0), (row - 1, col - 1)):
                            return True
        return False

    row, col = len(grid), len(grid[0])
    lo = max(grid[0][0], grid[-1][-1])
    hi = 0
    for r in range(row):
        for c in range(col):
            hi = max(hi, grid[r][c])
    while lo <= hi:
        mid = (lo + hi) // 2
        if is_connected(mid):
            hi = mid - 1
        else:
            lo = mid + 1
    return lo


# Dijkstra’s: O(N^2*logN)
def swim_in_water(grid: List[List[int]]) -> int:
    row, col = len(grid), len(grid[0])
    res = 0
    pq = [(grid[0][0], 0, 0)]
    visited = set([(0, 0)])
    while pq:
        t, r, c = heapq.heappop(pq)
        res = max(res, t)
        if r == row - 1 and c == col - 1:
            return res
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r, new_c = r + i, c + j
            if 0 <= new_r < row and 0 <= new_c < col and (new_r, new_c) not in visited:
                visited.add((new_r, new_c))
                heapq.heappush(pq, (grid[new_r][new_c], new_r, new_c))


if __name__ == "__main__":
    swim_in_water([[0, 2], [1, 3]])
