# https://leetcode.com/problems/spiral-matrix/
"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []
    row, col = len(matrix), len(matrix[0])
    visited = [[False] * col for _ in range(row)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ans = []

    r, c = 0, 0
    i = 0
    for _ in range(row * col):
        ans.append(matrix[r][c])
        visited[r][c] = True
        dr, dc = directions[i]
        tr, tc = r + dr, c + dc
        if 0 <= tr <= row - 1 and 0 <= tc <= col - 1 and not visited[tr][tc]:
            r, c = tr, tc
        else:
            i = (i + 1) % 4
            dr, dc = directions[i]
            r, c = r + dr, c + dc
    return ans
