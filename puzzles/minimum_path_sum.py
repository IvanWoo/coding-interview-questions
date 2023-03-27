# https://leetcode.com/problems/minimum-path-sum/
"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
"""
from functools import cache
from math import inf


def min_path_sum(grid: list[list[int]]) -> int:
    @cache
    def helper(r, c):
        if r == 0 and c == 0:
            return grid[r][c]
        if r < 0 or c < 0:
            return inf
        return grid[r][c] + min(helper(r - 1, c), helper(r, c - 1))

    row, col = len(grid), len(grid[0])
    return helper(row - 1, col - 1)


def min_path_sum(grid: list[list[int]]) -> int:
    row, col = len(grid), len(grid[0])
    dp = [[inf for _ in range(col + 1)] for _ in range(row + 1)]
    dp[1][1] = grid[0][0]
    for r in range(1, row + 1):
        for c in range(1, col + 1):
            if r == c == 1:
                continue
            dp[r][c] = grid[r - 1][c - 1] + min(dp[r - 1][c], dp[r][c - 1])
    return dp[row][col]
