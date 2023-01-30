# https://leetcode.com/problems/count-servers-that-communicate/
"""
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

Example 1:
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Example 3:
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.


Constraints:
m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
"""

from collections import Counter
from typing import List

from puzzles.union_find import UF


# union find
def count_servers(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    uf = UF(rows * cols)

    def convert(r, c):
        return r * cols + c

    for r in range(rows):
        for c in range(cols):
            if not grid[r][c]:
                continue
            for rr in range(r + 1, rows):
                if grid[rr][c]:
                    uf.union(convert(r, c), convert(rr, c))
            for cc in range(c + 1, cols):
                if grid[r][cc]:
                    uf.union(convert(r, c), convert(r, cc))

    def compact(uf):
        for i in range(rows * cols):
            uf.parent[i] = uf.find(i)
        return uf

    uf = compact(uf)
    parent = uf.parent
    count = Counter(parent)
    return sum(v for v in count.values() if v > 1)


# matrix
def count_servers(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    res = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        if sum(grid[r]) <= 1:
            continue
        for c in range(cols):
            if grid[r][c]:
                res[r][c] = 1

    for c in range(cols):
        if sum(grid[r][c] for r in range(rows)) <= 1:
            continue
        for r in range(rows):
            if grid[r][c]:
                res[r][c] = 1

    return sum(sum(row) for row in res)
