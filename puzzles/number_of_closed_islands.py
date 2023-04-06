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


def closed_island(grid: list[list[int]]) -> int:
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


def closed_island(grid: list[list[int]]) -> int:
    def dfs(r, c):
        grid[r][c] = -1
        is_close = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                is_close.append(dfs(nr, nc))

        return (r not in (0, rows - 1) and c not in (0, cols - 1)) and all(is_close)

    ret = 0
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and dfs(r, c):
                ret += 1
    return ret


def closed_island(grid: list[list[int]]) -> int:
    def dfs(r, c):
        if (r, c) in visited:
            return False
        visited.add((r, c))
        is_close = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and grid[nr][nc] == 0
                and (nr, nc) not in visited
            ):
                is_close.append(dfs(nr, nc))

        return (r not in (0, rows - 1) and c not in (0, cols - 1)) and all(is_close)

    ret = 0
    visited = set()
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and dfs(r, c):
                ret += 1
    return ret
