# https://leetcode.com/problems/out-of-boundary-paths/
"""
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

Example 1:
Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:
Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

Note:
Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].
"""
from functools import cache

# TLE
def find_paths(m: int, n: int, N: int, i: int, j: int) -> int:
    def backtrack(x, y, left, path):
        if tuple(path) in visited:
            return
        if 0 <= x < m and 0 <= y < n:
            if left == 0:
                return
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                backtrack(new_x, new_y, left - 1, path + [(new_x, new_y)])
        else:
            visited.add(tuple(path))

    visited = set()
    backtrack(i, j, N, [(i, j)])
    return int(len(visited) % (10**9 + 7))


def find_paths(m: int, n: int, N: int, i: int, j: int) -> int:
    @cache
    def helper(x, y, left):
        if 0 <= x < m and 0 <= y < n:
            if left == 0:
                return 0
            total = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                total += helper(new_x, new_y, left - 1)
            return total
        else:
            return 1

    return int(helper(i, j, N) % (10**9 + 7))


def find_paths(m: int, n: int, max_move: int, start_row: int, start_column: int) -> int:
    @cache
    def helper(i, j, move):
        ans = 0
        if move > max_move:
            return 0
        if 0 <= i < m and 0 <= j < n:
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                ans += helper(ni, nj, move + 1)
        else:
            ans += 1
        return ans

    MOD = 10**9 + 7

    ans = 0
    ans = helper(start_row, start_column, 0)
    return ans % MOD


if __name__ == "__main__":
    find_paths(m=2, n=1, N=2, i=0, j=0)
