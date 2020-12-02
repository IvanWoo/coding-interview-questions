# https://leetcode.com/problems/min-cost-to-connect-all-points/
"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Example 3:
Input: points = [[0,0],[1,1],[1,0],[-1,1]]
Output: 4

Example 4:
Input: points = [[-1000000,-1000000],[1000000,1000000]]
Output: 4000000

Example 5:
Input: points = [[0,0]]
Output: 0

Constraints:
1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
"""
from typing import List
import heapq
from puzzles.union_find import UF

# TLE: O(n ^ 3)
def min_cost_connect_points(points: List[List[int]]) -> int:
    def get_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    if not points:
        return 0

    n = len(points)
    weights = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            weights[i][j] = get_distance(points[i], points[j])

    uf = UF(n)
    res = 0
    reach = set([0])
    unreach = set(range(1, n))
    while len(unreach) != 0:
        u, v, min_weight = None, None, float("inf")
        for x in reach:
            for y in unreach:
                if not uf.connected(x, y):
                    w = weights[x][y]
                    if w < min_weight:
                        u, v = x, y
                        min_weight = w
        uf.union(u, v)
        reach.add(v)
        unreach.remove(v)
        res += min_weight
    return res


# Min Spanning Tree, Prim's Algorithm: O(n ^ 2)
def min_cost_connect_points(points: List[List[int]]) -> int:
    def get_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    if not points:
        return 0

    n = len(points)
    res = 0
    # init edges with first point
    visited = set([0])
    edges = [(get_distance(points[0], points[i]), 0, i) for i in range(1, n)]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to in visited:
            continue
        visited.add(to)
        res += cost
        for i in range(n):
            if i not in visited:
                heapq.heappush(edges, (get_distance(points[to], points[i]), to, i))
    return res


if __name__ == "__main__":
    min_cost_connect_points([[0, 0], [1, 1], [1, 0], [-1, 1]])
