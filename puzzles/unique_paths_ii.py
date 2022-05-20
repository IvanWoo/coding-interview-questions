# https://leetcode.com/problems/unique-paths-ii/
"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""


# backtrack: TLE
def unique_paths_with_obstacles(obstacleGrid: list[list[int]]) -> int:
    if obstacleGrid[0][0] == 1:
        return 0
    row, col = len(obstacleGrid), len(obstacleGrid[0])
    ans = 0

    def backtrack(x, y):
        nonlocal ans
        if x == col - 1 and y == row - 1:
            ans += 1
            return
        for dx, dy in [(1, 0), (0, 1)]:
            tx, ty = x + dx, y + dy
            if tx <= col - 1 and ty <= row - 1 and obstacleGrid[ty][tx] == 0:
                backtrack(tx, ty)

    backtrack(0, 0)
    return ans


# dp
def unique_paths_with_obstacles(obstacleGrid: list[list[int]]) -> int:
    def is_obs(r, c):
        return obstacleGrid[r][c] == 1

    row, col = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * col for _ in range(row)]

    # first row
    for i in range(col):
        if is_obs(0, i):
            break
        dp[0][i] = 1

    # first col
    for i in range(row):
        if is_obs(i, 0):
            break
        dp[i][0] = 1

    for r in range(1, row):
        for c in range(1, col):
            if not is_obs(r, c):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

    return dp[-1][-1]
