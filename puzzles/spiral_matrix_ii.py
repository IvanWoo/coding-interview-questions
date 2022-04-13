# https://leetcode.com/problems/spiral-matrix-ii/
"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
 
Constraints:
1 <= n <= 20
"""
from functools import cache


def generate_matrix(n: int) -> list[list[int]]:
    def nxt(i: int, j: int, dir_vec: tuple[int, int]):
        di, dj = dir_vec
        ii = i + di
        jj = j + dj
        return ii, jj

    @cache
    def rotate(dir_vec: tuple[int, int]):
        vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        return vectors[(vectors.index(dir_vec) + 1) % 4]

    matrix = [[0] * n for _ in range(n)]
    dir_vec = (0, 1)
    i = j = 0

    for val in range(1, n**2 + 1):
        matrix[i][j] = val
        ii, jj = nxt(i, j, dir_vec)

        if ii == n or jj == n or ii < 0 or jj < 0 or matrix[ii][jj] != 0:
            dir_vec = rotate(dir_vec)
        i, j = nxt(i, j, dir_vec)
    return matrix
