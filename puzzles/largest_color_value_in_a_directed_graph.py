# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/
"""
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

Example 1:
Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).

Example 2:
Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.

Constraints:
n == colors.length
m == edges.length
1 <= n <= 105
0 <= m <= 105
colors consists of lowercase English letters.
0 <= aj, bj < n
"""
from collections import defaultdict


def largest_path_value(colors: str, edges: list[list[int]]) -> int:
    n = len(colors)
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    # Topological sort
    in_degree = [0] * n
    for u, v in edges:
        in_degree[v] += 1
    queue = [u for u in range(n) if in_degree[u] == 0]
    color_count = [[0] * 26 for _ in range(n)]
    ret = 0
    visited = 0
    while queue:
        u = queue.pop()
        visited += 1
        color_count[u][ord(colors[u]) - ord("a")] += 1
        ret = max(ret, max(color_count[u]))
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
            for i in range(26):
                color_count[v][i] = max(color_count[v][i], color_count[u][i])
    return ret if visited == n else -1
