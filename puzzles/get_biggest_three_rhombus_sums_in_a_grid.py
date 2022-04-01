# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/
"""
ou are given an m x n integer matrix grid​​​.

A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:


Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.

Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.


Example 1:
Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
Output: [228,216,211]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 20 + 3 + 200 + 5 = 228
- Red: 200 + 2 + 10 + 4 = 216
- Green: 5 + 200 + 4 + 2 = 211

Example 2:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: [20,9,8]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 4 + 2 + 6 + 8 = 20
- Red: 9 (area 0 rhombus in the bottom right corner)
- Green: 8 (area 0 rhombus in the bottom middle)

Example 3:
Input: grid = [[7,7,7]]
Output: [7]
Explanation: All three possible rhombus sums are the same, so return [7].
 

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 105
"""
import heapq


def interpolate_points(p1, p2, direction):
    x1, y1 = p1
    x2, y2 = p2
    dx, dy = direction
    for step in range(1, abs(x1 - x2)):
        x, y = x1 + step * dx, y1 + step * dy
        if (x, y) == p2:
            break
        yield (x, y)


class Grid:
    def __init__(self, grid) -> None:
        self.grid = grid

    def in_range(self, p):
        rows, cols = len(self.grid), len(self.grid[0])
        r, c = p
        return 0 <= r < rows and 0 <= c < cols

    def interpolate_sum(self, p1, p2, direction) -> int:
        res = 0
        for x, y in interpolate_points(p1, p2, direction):
            res += self.grid[x][y]
        return res

    def get_sum(self, n, w, e, s):
        res = 0
        for p1, p2, direction in [
            (n, w, (1, -1)),
            (n, e, (1, 1)),
            (s, w, (-1, -1)),
            (s, e, (-1, 1)),
        ]:
            res += self.interpolate_sum(p1, p2, direction)

        for x, y in [n, w, e, s]:
            res += self.grid[x][y]
        return res

    def rhombus_sums(self, r, c):
        rows, cols = len(self.grid), len(self.grid[0])
        diag = int((rows**2 + cols**2) ** 0.5)
        n = (r, c)
        for l in range(1, diag):
            w = (r + l, c - l)
            e = (r + l, c + l)
            s = (r + l * 2, c)
            if all([self.in_range(p) for p in (w, e, s)]):
                yield self.get_sum(n, w, e, s)


def get_biggest_three(grid: list[list[int]]) -> list[int]:
    g = Grid(grid)
    res = []
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            heapq.heappush(res, -grid[r][c])
            for s in g.rhombus_sums(r, c):
                heapq.heappush(res, -s)
    ans = []
    while len(ans) != 3:
        if not res:
            break
        v = -heapq.heappop(res)
        if v in ans:
            continue
        ans.append(v)
    return ans
