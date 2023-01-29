# https://leetcode.com/problems/sum-of-distances-in-tree/description/
"""
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

Example 1:
Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

Example 2:
Input: n = 1, edges = []
Output: [0]

Example 3:
Input: n = 2, edges = [[1,0]]
Output: [1,1]
 

Constraints:
1 <= n <= 3 * 104
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
The given input represents a valid tree.
"""
from collections import defaultdict, deque
from functools import cache


# TLE: O(n^2)
def sum_of_distances_in_tree(n: int, edges: list[list[int]]) -> list[int]:
    @cache
    def dist(start, end):
        q = deque([(start, 0)])
        visited = set([start])
        while q:
            cur, steps = q.popleft()
            if cur == end:
                return steps
            for nxt in graph[cur]:
                if nxt not in visited:
                    q.append((nxt, steps + 1))
                    visited.add(nxt)

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    res = [0] * n
    for i in range(n):
        res[i] = sum([dist(i, j) for j in range(n)])
    return res


# O(n)
def sum_of_distances_in_tree(n: int, edges: list[list[int]]) -> list[int]:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # post-order
    def dfs(node, parent):
        for child in graph[node]:
            if child != parent:
                dfs(child, node)
                count[node] += count[child]
                res[node] += res[child] + count[child]

    # pre-order
    def dfs2(node, parent):
        for child in graph[node]:
            if child != parent:
                res[child] = res[node] - count[child] + (n - count[child])
                dfs2(child, node)

    count = [1] * n
    res = [0] * n
    dfs(0, None)
    dfs2(0, None)
    return res
