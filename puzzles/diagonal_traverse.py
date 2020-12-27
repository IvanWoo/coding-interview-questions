# https://leetcode.com/problems/diagonal-traverse/
"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
"""
from typing import List
from collections import defaultdict


def find_diagonal_order(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []
    row, col = len(matrix), len(matrix[0])
    r, c = 0, 0
    direction = 1
    res = []
    while r < row and c < col:
        res.append(matrix[r][c])
        new_r = r - direction
        new_c = c + direction
        if new_r < 0 or new_r == row or new_c < 0 or new_c == col:
            if direction == 1:
                r += c == col - 1
                c += c < col - 1
            elif direction == -1:
                c += r == row - 1
                r += r < row - 1
            direction *= -1
        else:
            r, c = new_r, new_c
    return res


def find_diagonal_order(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []
    row, col = len(matrix), len(matrix[0])
    hashmap = defaultdict(list)
    for r in range(row):
        for c in range(col):
            hashmap[r + c].append(matrix[r][c])
    res = []
    for k, v in hashmap.items():
        if k % 2 == 1:
            res.extend(v)
        else:
            res.extend(v[::-1])
    return res


if __name__ == "__main__":
    find_diagonal_order([[1, 2], [3, 4]])
