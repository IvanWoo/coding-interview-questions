# https://leetcode.com/problems/erect-the-fence/
"""
You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed.

Return the coordinates of trees that are exactly located on the fence perimeter.

Example 1:
Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]

Example 2:
Input: points = [[1,2],[2,2],[4,2]]
Output: [[4,2],[2,2],[1,2]]

Constraints:
1 <= points.length <= 3000
points[i].length == 2
0 <= xi, yi <= 100
All the given points are unique.
"""


def outer_trees(trees: list[list[int]]) -> list[list[int]]:
    # monotone chain convex hull: https://algorithmist.com/wiki/Monotone_chain_convex_hull.py
    def cross(o, a, b):
        """
        Returns a positive value, if OAB makes a counter-clockwise turn,
        negative for clockwise turn, and zero if the points are collinear.
        """
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def one_side_hull(pts):
        res = []
        for p in pts:
            while len(res) >= 2 and cross(res[-2], res[-1], p) < 0:
                res.pop()
            res.append(p)
        return res

    if len(trees) <= 3:
        return trees
    pts = sorted([tuple(pt) for pt in trees])

    lower_hull = one_side_hull(iter(pts))
    upper_hull = one_side_hull(reversed(pts))

    return [[x, y] for x, y in set(lower_hull + upper_hull)]
