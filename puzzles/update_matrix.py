# https://leetcode.com/problems/01-matrix/
"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.


Example 1:
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""
from typing import List


# bfs
def update_matrix(matrix: List[List[int]]) -> List[List[int]]:
    row, col = len(matrix), len(matrix[0])
    visited = [[False] * col for _ in range(row)]
    res = [[float("inf")] * col for _ in range(row)]
    q = []
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == 0:
                q.append((r, c, 0))
    while q:
        new_q = []
        while q:
            cur_r, cur_c, distance = q.pop()
            if visited[cur_r][cur_c]:
                continue
            visited[cur_r][cur_c] = True
            res[cur_r][cur_c] = distance
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r, new_c = cur_r + i, cur_c + j
                if 0 <= new_r < row and 0 <= new_c < col:
                    new_q.append((new_r, new_c, distance + 1))
        q = new_q
    return res
