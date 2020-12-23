# https://leetcode.com/problems/number-of-boomerangs/
"""
You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Return the number of boomerangs.

Example 1:
Input: points = [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].

Example 2:
Input: points = [[1,1],[2,2],[3,3]]
Output: 2

Example 3:
Input: points = [[1,1]]
Output: 0
 
Constraints:
n == points.length
1 <= n <= 500
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""
from typing import List
from collections import defaultdict


def number_of_boomerangs(points: List[List[int]]) -> int:
    def distance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return (x1 - x2) ** 2 + (y1 - y2) ** 2

    n = len(points)
    if n < 3:
        return 0
    hashmap = defaultdict(lambda: defaultdict(int))
    res = 0
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            d = distance(points[i], points[j])
            hashmap[i][d] += 1

    res = 0
    for i in range(n):
        for d, l in hashmap[i].items():
            if l >= 2:
                res += l * (l - 1)
    return res


if __name__ == "__main__":
    number_of_boomerangs([[0, 0], [1, 0], [2, 0]])
