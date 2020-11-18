# https://leetcode.com/problems/number-of-closed-islands/
"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
"""
from typing import List


def closed_island(grid: List[List[int]]) -> int:
    row, col = len(grid), len(grid[0])
    visited = [[False] * col for _ in range(row)]
    res = 0

    def helper(stack):
        nonlocal res
        valid = True

        while stack:
            r, c = stack.pop()
            if visited[r][c]:
                continue
            visited[r][c] = True
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r, new_c = r + i, c + j
                if not visited[new_r][new_c] and grid[new_r][new_c] == 0:
                    if 1 <= new_r < row - 1 and 1 <= new_c < col - 1:
                        stack.append((new_r, new_c))
                    else:
                        valid = False
        if valid:
            res += 1

        return

    for r in range(1, row - 1):
        for c in range(1, col - 1):
            if not visited[r][c] and grid[r][c] == 0:
                helper([(r, c)])
    return res


if __name__ == "__main__":
    closed_island(
        [
            [1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0],
        ]
    )
