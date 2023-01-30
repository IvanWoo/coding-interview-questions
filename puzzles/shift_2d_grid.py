# https://leetcode.com/problems/shift-2d-grid/
"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Example 1:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2:
Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]

Constraints:
m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
"""


def shift_grid(grid: list[list[int]], k: int) -> list[list[int]]:
    def to_list(grid):
        res = []
        for row in grid:
            res.extend(row)
        return res

    def shift_list(l, k):
        if k == 0:
            return l
        return l[-k:] + l[:-k]

    def from_list(l, m, n):
        res = []
        for i in range(m):
            res.append(l[i * n : (i + 1) * n])
        return res

    m, n = len(grid), len(grid[0])
    l = to_list(grid)
    k = k % (m * n)
    l = shift_list(l, k)
    return from_list(l, m, n)
