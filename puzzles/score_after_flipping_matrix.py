# https://leetcode.com/problems/score-after-flipping-matrix/
"""
We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

Example 1:
Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Note:
1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.
"""

from typing import List


def mat2int(A: List[List[int]]) -> int:
    row, col = len(A), len(A[0])
    ans = 0
    for c in range(col):
        ans += sum([a[c] for a in A]) * (2 ** (col - c - 1))
    return ans


def flip_col(A: List[List[int]], c) -> None:
    row, col = len(A), len(A[0])
    for r in range(row):
        A[r][c] = 0 if A[r][c] else 1
    return


def flip_row(A: List[List[int]], r) -> None:
    row, col = len(A), len(A[0])
    for c in range(col):
        A[r][c] = 0 if A[r][c] else 1
    return


def matrix_score(A: List[List[int]]) -> int:
    row, col = len(A), len(A[0])
    ans = 0
    for r in range(row):
        if A[r][0] == 0:
            flip_row(A, r)

    for c in range(col):
        if sum([a[c] for a in A]) <= row // 2:
            flip_col(A, c)

    return mat2int(A)


def matrix_score(A: List[List[int]]) -> int:
    row, col = len(A), len(A[0])
    ans = 0
    for c in range(col):
        counter = 0
        for r in range(row):
            counter += A[r][c] ^ A[r][0]
        ans += max(counter, row - counter) * (2 ** (col - c - 1))
    return ans
