# https://leetcode.com/problems/equal-row-and-column-pairs/description/
"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

Constraints:
n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
"""
from collections import defaultdict


# brute force
def equal_pairs(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    rs, cs = defaultdict(list), defaultdict(list)
    for r in range(rows):
        for c in range(cols):
            rs[r].append(grid[r][c])
            cs[c].append(grid[r][c])
    ret = 0
    for r in range(rows):
        for c in range(cols):
            if rs[r] == cs[c]:
                ret += 1
    return ret
