# https://leetcode.com/problems/check-if-it-is-a-straight-line/description/
"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:
2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""
from math import inf


def check_straight_line(coordinates: list[list[int]]) -> bool:
    def cal_k(i1, i2):
        x1, y1 = coordinates[i1]
        x2, y2 = coordinates[i2]
        return (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else inf

    n = len(coordinates)
    coordinates.sort()
    k = cal_k(0, 1)
    return all([cal_k(0, i) == k for i in range(1, n)])
