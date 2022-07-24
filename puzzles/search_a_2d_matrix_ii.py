# https://leetcode.com/problems/search-a-2d-matrix-ii/
"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matrix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109
"""

from bisect import bisect_left

# brute force
def search_matrix(matrix: list[list[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == target:
                return True
    return False


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    first_col = [row[0] for row in matrix]
    last_col = [row[-1] for row in matrix]
    r1 = bisect_left(last_col, target)
    r2 = bisect_left(first_col, target)

    for r in range(r1, min(r2 + 1, len(matrix))):
        row = matrix[r]
        idx = bisect_left(row, target)
        if row[idx] == target:
            return True
    return False


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    r, c = rows - 1, 0
    while r >= 0 and c < cols:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            c += 1
        else:
            r -= 1
    return False


# as long as the r, c is monotonic, this algo will work
def search_matrix(matrix: list[list[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    r, c = 0, cols - 1
    while r < rows and c >= 0:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            r += 1
        else:
            c -= 1
    return False


if __name__ == "__main__":
    search_matrix([[1, 4], [2, 5]], 2)
