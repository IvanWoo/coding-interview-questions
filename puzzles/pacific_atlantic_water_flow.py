# https://leetcode.com/problems/pacific-atlantic-water-flow/
"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""
from typing import List
from collections import defaultdict


def pacific_atlantic(matrix: List[List[int]]) -> List[List[int]]:
    def helper(r, c):
        nonlocal memo, graph
        row, col = len(matrix), len(matrix[0])
        visited = set()
        q = [(r, c)]
        is_p, is_a = False, False
        while q:
            cur_row, cur_col = q.pop()
            if (cur_row, cur_col) in memo and memo[(cur_row, cur_col)]:
                return True
            if (cur_row, cur_col) in visited:
                continue
            visited.add((cur_row, cur_col))
            if cur_row == 0 or cur_col == 0:
                is_p = True
            if cur_row == row - 1 or cur_col == col - 1:
                is_a = True
            if is_p and is_a:
                return True
            q.extend(graph[(cur_row, cur_col)])
        return False

    if not matrix:
        return []
    res = []
    memo = dict()
    row, col = len(matrix), len(matrix[0])

    # build the graph
    graph = defaultdict(list)
    for r in range(row):
        for c in range(col):
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r, new_c = r + i, c + j
                if 0 <= new_r < row and 0 <= new_c < col:
                    if matrix[new_r][new_c] <= matrix[r][c]:
                        graph[(r, c)].append((new_r, new_c))

    for r in range(row):
        for c in range(col):
            is_connected = helper(r, c)
            memo[(r, c)] = is_connected
            if is_connected:
                res.append([r, c])
    return res


if __name__ == "__main__":
    pacific_atlantic(
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
    )
