# https://leetcode.com/problems/evaluate-division/
"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""
from collections import defaultdict, deque

# union find
def calc_equation(
    equations: list[list[str]], values: list[float], queries: list[list[str]]
) -> list[float]:
    root = {}

    # xr = x/parent(x), pr = parent(x)/root(x), update xr to xr*pr = x/root(x)
    def find(x):
        p, xr = root.setdefault(x, (x, 1.0))
        if x != p:
            r, pr = find(p)
            root[x] = (r, xr * pr)
        return root[x]

    # if root(x) = root(y), equations "x / y" doable as (x/root(x)) / (y/root(y)) = xr / yr
    def union(x, y, ratio):
        px, xr = find(x)
        py, yr = find(y)
        if not ratio:
            return xr / yr if px == py else -1.0
        if px != py:
            root[px] = (py, yr / xr * ratio)

    for (x, y), v in zip(equations, values):
        union(x, y, v)
    return [union(x, y, 0) if x in root and y in root else -1.0 for x, y in queries]


# bfs
def calc_equation(
    equations: list[list[str]], values: list[float], queries: list[list[str]]
) -> list[float]:
    graph = defaultdict(dict)
    for (x, y), v in zip(equations, values):
        graph[x][y] = v
        graph[y][x] = 1 / v

    def bfs(src, dst):
        if not (src in graph and dst in graph):
            return -1
        q, visited = deque([(src, 1)]), set()
        while q:
            x, v = q.popleft()
            if x == dst:
                return v
            visited.add(x)
            for y in graph[x]:
                if y not in visited:
                    q.append((y, v * graph[x][y]))
        return -1

    return [bfs(s, d) for s, d in queries]


if __name__ == "__main__":
    calc_equation(
        equations=[["a", "b"], ["b", "c"]],
        values=[2.0, 3.0],
        queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
    )
