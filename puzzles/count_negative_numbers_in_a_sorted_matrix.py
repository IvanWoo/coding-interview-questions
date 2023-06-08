# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100


Follow up: Could you find an O(n + m) solution?
"""
from bisect import bisect_right


def count_negatives(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    ret = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] < 0:
                ret += 1
    return ret


def count_negatives(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    ret = 0
    for r in range(rows):
        idx = bisect_right(grid[r], 0, key=lambda x: -1 * x)
        ret += cols - idx
    return ret


def count_negatives(grid: list[list[int]]) -> int:
    ret = 0
    n = len(grid[0])
    cur_row_neg_idx = n - 1
    for row in grid:
        while cur_row_neg_idx >= 0 and row[cur_row_neg_idx] < 0:
            cur_row_neg_idx -= 1
        ret += n - (cur_row_neg_idx + 1)
    return ret
