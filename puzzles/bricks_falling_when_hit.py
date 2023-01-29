# https://leetcode.com/problems/bricks-falling-when-hit/
"""
You are given an m x n binary grid, where each 1 represents a brick and 0 represents an empty space. A brick is stable if:

It is directly connected to the top of the grid, or
At least one other brick in its four adjacent cells is stable.
You are also given an array hits, which is a sequence of erasures we want to apply. Each time we want to erase the brick at the location hits[i] = (rowi, coli). The brick on that location (if it exists) will disappear. Some other bricks may no longer be stable because of that erasure and will fall. Once a brick falls, it is immediately erased from the grid (i.e., it does not land on other stable bricks).

Return an array result, where each result[i] is the number of bricks that will fall after the ith erasure is applied.

Note that an erasure may refer to a location with no brick, and if it does, no bricks drop.


Example 1:
Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
Output: [2]
Explanation: Starting with the grid:
[[1,0,0,0],
 [1,1,1,0]]
We erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,1,1,0]]
The two underlined bricks are no longer stable as they are no longer connected to the top nor adjacent to another stable brick, so they will fall. The resulting grid is:
[[1,0,0,0],
 [0,0,0,0]]
Hence the result is [2].

Example 2:
Input: grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
Output: [0,0]
Explanation: Starting with the grid:
[[1,0,0,0],
 [1,1,0,0]]
We erase the underlined brick at (1,1), resulting in the grid:
[[1,0,0,0],
 [1,0,0,0]]
All remaining bricks are still stable, so no bricks fall. The grid remains the same:
[[1,0,0,0],
 [1,0,0,0]]
Next, we erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,0,0,0]]
Once again, all remaining bricks are still stable, so no bricks fall.
Hence the result is [0,0].
 

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[i][j] is 0 or 1.
1 <= hits.length <= 4 * 104
hits[i].length == 2
0 <= xi <= m - 1
0 <= yi <= n - 1
All (xi, yi) are unique.
"""
from typing import List


# TLE
def hit_bricks(grid: List[List[int]], hits: List[List[int]]) -> List[int]:
    class UF:
        def __init__(self) -> None:
            self.parent = dict()
            self.top = set()

        def add(self, x):
            if x not in self.parent:
                self.parent[x] = x
                if x[0] == 0:
                    self.top.add(x)

        def remove(self, x):
            if x[0] == 0:
                self.top.remove(x)

        def find(self, x):
            while self.parent[x] != x:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x

        def is_stable(self, x):
            return self.find(x) in self.top

        def union(self, u, v):
            root_u, root_v = self.find(u), self.find(v)
            if root_u == root_v:
                return
            if root_v in self.top:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u

    def get_falling():
        nonlocal grid
        row, col = len(grid), len(grid[0])
        uf = UF()
        for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    uf.add((r, c))
                    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        new_r, new_c = r + i, c + j
                        if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c]:
                            uf.add((new_r, new_c))
                            uf.union((r, c), (new_r, new_c))
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] and not uf.is_stable((r, c)):
                    res += 1
                    grid[r][c] = 0
        return res

    res = [0] * len(hits)
    for i, pos in enumerate(hits):
        r, c = pos
        grid[r][c] = 0
        res[i] = get_falling()
    return res


def hit_bricks(grid: List[List[int]], hits: List[List[int]]) -> List[int]:
    class UF:
        def __init__(self, size) -> None:
            self.parent = list(range(size))
            self.size = [1] * size

        def find(self, x):
            while self.parent[x] != x:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x

        def union(self, u, v):
            root_u, root_v = self.find(u), self.find(v)
            if root_u == root_v:
                return
            if self.size[root_v] > self.size[root_u]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]

    def get_pos(r, c):
        return r * col + c + 1

    def union_around(uf, r, c):
        cur_pos = get_pos(r, c)
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r, new_c = r + i, c + j
            if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] == 1:
                uf.union(cur_pos, get_pos(new_r, new_c))
        if r == 0:
            uf.union(0, cur_pos)

    row, col = len(grid), len(grid[0])
    uf = UF(row * col + 1)

    # mark hits
    for r, c in hits:
        if grid[r][c] == 1:
            grid[r][c] = 2

    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                union_around(uf, r, c)

    num_bricks_left = uf.size[uf.find(0)]
    num_bricks_dropped = [0] * len(hits)

    for i in reversed(range(len(hits))):
        r, c = hits[i]
        if grid[r][c] == 2:
            grid[r][c] = 1
            union_around(uf, r, c)
            new_num_bricks_left = uf.size[uf.find(0)]
            num_bricks_dropped[i] = max(0, new_num_bricks_left - num_bricks_left - 1)
            num_bricks_left = new_num_bricks_left
    return num_bricks_dropped


if __name__ == "__main__":
    hit_bricks([[1, 0, 1], [1, 1, 1]], [[0, 0], [0, 2], [1, 1]])
