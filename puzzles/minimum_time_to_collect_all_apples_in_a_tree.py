# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
"""
Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend in order to collect all apples in the tree starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [fromi, toi] means that exists an edge connecting the vertices fromi and toi. Additionally, there is a boolean array hasApple, where hasApple[i] = True means that vertex i has an apple, otherwise, it does not have any apple.

Example 1:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False]
Output: 8
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.

Example 2:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.

Example 3:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,False,False,False,False,False]
Output: 0

Constraints:

1 <= n <= 10^5
edges.length == n-1
edges[i].length == 2
0 <= fromi, toi <= n-1
fromi < toi
hasApple.length == n
"""
from collections import defaultdict


def min_time(n: int, edges: list[list[int]], has_apple: list[bool]) -> int:
    visited = set()
    tree = defaultdict(set)
    for u, v in edges:
        tree[u].add(v)
        tree[v].add(u)

    def dfs(node):
        if node in visited:
            return 0
        visited.add(node)
        count = int(has_apple[node]) * 2
        if node == 0:
            count = 0
        count += sum([dfs(c) for c in tree[node]])
        if count > 0 and node != 0 and not has_apple[node]:
            count += 2
        return count

    return dfs(0)
