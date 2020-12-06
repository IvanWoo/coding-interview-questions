# https://leetcode.com/problems/regions-cut-by-slashes/
# In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

# (Note that backslash characters are escaped, so a \ is represented as "\\".)

# Return the number of regions.


# Example 1:
# Input:
# [
#   " /",
#   "/ "
# ]
# Output: 2
# Explanation: The 2x2 grid is as follows:

# Example 2:
# Input:
# [
#   " /",
#   "  "
# ]
# Output: 1
# Explanation: The 2x2 grid is as follows:

# Example 3:
# Input:
# [
#   "\\/",
#   "/\\"
# ]
# Output: 4
# Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
# The 2x2 grid is as follows:

# Example 4:
# Input:
# [
#   "/\\",
#   "\\/"
# ]
# Output: 5
# Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
# The 2x2 grid is as follows:

# Example 5:
# Input:
# [
#   "//",
#   "/ "
# ]
# Output: 3
# Explanation: The 2x2 grid is as follows:


# Note:
# 1 <= grid.length == grid[0].length <= 30
# grid[i][j] is either '/', '\', or ' '.
from typing import List


def regions_by_slashes(grid: List[str]) -> int:
    class UF:
        def __init__(self):
            self.count = 0
            self.parent = dict()

        def add(self, x):
            self.count += 1
            self.parent[x] = x

        def find(self, x):
            while self.parent[x] != x:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x

        def union(self, u, v):
            root_u, root_v = self.find(u), self.find(v)
            if root_u == root_v:
                return
            self.parent[root_u] = root_v
            self.count -= 1

    uf = UF()
    row, col = len(grid), len(grid[0])
    for r in range(row):
        for c in range(col):
            # cut every grid into 4 pieces and index them as
            # left, top, right, bottom = 0, 1, 2, 3
            for i in range(4):
                uf.add((r, c, i))
            if grid[r][c] == " ":
                uf.union((r, c, 0), (r, c, 1))
                uf.union((r, c, 1), (r, c, 2))
                uf.union((r, c, 2), (r, c, 3))
            elif grid[r][c] == "\\":
                uf.union((r, c, 0), (r, c, 3))
                uf.union((r, c, 1), (r, c, 2))
            elif grid[r][c] == "/":
                uf.union((r, c, 0), (r, c, 1))
                uf.union((r, c, 2), (r, c, 3))
            if r != 0:
                uf.union((r, c, 1), (r - 1, c, 3))
            if c != 0:
                uf.union((r, c, 0), (r, c - 1, 2))
    return uf.count
