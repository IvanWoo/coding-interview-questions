# https://leetcode.com/problems/valid-square/
"""
Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

A valid square has four equal sides with positive length and four equal angles (90-degree angles).

Example 1:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true

Example 2:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false

Example 3:
Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true

Constraints:
p1.length == p2.length == p3.length == p4.length == 2
-104 <= xi, yi <= 104
"""
import itertools
from typing import List


def valid_square(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    def distance(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def dot(v1, v2):
        return v1[0] * v2[0] + v1[1] * v2[1]

    def vector(p1, p2):
        return (p1[0] - p2[0], p1[1] - p2[1])

    def is_valid(p1, p2, p3, p4):
        d = distance(p1, p2)
        v1 = vector(p1, p2)
        v2 = vector(p2, p3)
        return (
            d > 0
            and distance(p2, p3) == d
            and distance(p3, p4) == d
            and distance(p4, p1) == d
            and dot(v1, v2) == 0
        )

    if p1 != p2 != p3 != p4:
        for p in itertools.permutations([p1, p2, p3, p4]):
            if is_valid(*p):
                return True
    return False


if __name__ == "__main__":
    valid_square([0, 1], [1, 1], [1, 1], [1, 0])
