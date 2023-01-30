# https://leetcode.com/problems/minimum-falling-path-sum/
"""
Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.

Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation:
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.

Constraints:

1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100
"""
from collections import defaultdict
from functools import cache
from math import inf


# TLE
def min_falling_path_sum(A: list[list[int]]) -> int:
    row, col = len(A), len(A[0])
    ans = float("inf")

    @cache
    def backtrack(r, c, path_sum):
        nonlocal ans
        if r >= row:
            ans = min(ans, path_sum)
            return
        for i in [-1, 0, 1]:
            if 0 <= c + i < col:
                backtrack(r + 1, c + i, path_sum + A[r][c])

    for c in range(col):
        backtrack(0, c, 0)
    return ans


# DP
def min_falling_path_sum(A: list[list[int]]) -> int:
    row, col = len(A), len(A[0])
    dp = [[0] * col for _ in range(row)]

    for c in range(col):
        dp[0][c] = A[0][c]

    for r in range(1, row):
        for c in range(col):
            if c == 0:
                dp[r][c] = min(dp[r - 1][c], dp[r - 1][c + 1]) + A[r][c]
            elif c == col - 1:
                dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c]) + A[r][c]
            else:
                dp[r][c] = (
                    min(dp[r - 1][c - 1], dp[r - 1][c], dp[r - 1][c + 1]) + A[r][c]
                )

    return min(dp[row - 1])


def min_falling_path_sum(matrix: list[list[int]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    dp = defaultdict(lambda: inf)
    # init the value
    for c in range(cols):
        dp[(0, c)] = matrix[0][c]

    for r in range(1, rows):
        for c in range(cols):
            dp[(r, c)] = matrix[r][c] + min(
                [dp[(r - 1, c - 1)], dp[(r - 1, c)], dp[(r - 1, c + 1)]]
            )

    return min([dp[(rows - 1, c)] for c in range(cols)])


if __name__ == "__main__":
    min_falling_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
