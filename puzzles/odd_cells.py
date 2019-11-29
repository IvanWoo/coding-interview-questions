# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

from typing import List


def odd_cells(n: int, m: int, indices: List[List[int]]) -> int:
    rows = [0] * n
    cols = [0] * m
    for r, c in indices:
        rows[r] += 1
        cols[c] += 1

    ans = 0
    for row in range(n):
        for col in range(m):
            x = rows[row] + cols[col]
            ans += x % 2
    return ans

