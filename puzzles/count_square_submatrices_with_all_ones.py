# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.


Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:
Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.
"""
from typing import List


# TLE
def count_squares(matrix: List[List[int]]) -> int:
    def all_ones(matrix, r, c, w):
        for i in range(r, r + w):
            for j in range(c, c + w):
                if matrix[i][j] != 1:
                    return False
        return True

    row, col = len(matrix), len(matrix[0])
    res = 0

    for w in range(1, min(row, col) + 1):
        for r in range(row - w + 1):
            for c in range(col - w + 1):
                if all_ones(matrix, r, c, w):
                    res += 1
    return res


def count_squares(matrix: List[List[int]]) -> int:
    row, col = len(matrix), len(matrix[0])
    res = 0

    for r in range(row):
        for c in range(col):
            if not matrix[r][c]:
                continue
            if r != 0 and c != 0:
                matrix[r][c] += min(matrix[r - 1][c - 1], matrix[r - 1][c], matrix[r][c - 1])
            res += matrix[r][c]
    return res


if __name__ == "__main__":
    count_squares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]])
