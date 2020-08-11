# https://leetcode.com/problems/redundant-connection/
# In this problem, a tree is an undirected graph that is connected and has no cycles.

# The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

# Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
#   1
#  / \
# 2 - 3
# Example 2:
# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: The given undirected graph will be like this:
# 5 - 1 - 2
#     |   |
#     4 - 3
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

from collections import defaultdict
from typing import List, Dict, Set


def find(start: int, target: int, prev: int, graph: Dict[int, List[int]]) -> bool:
    if start == target:
        return True
    return any(
        find(child, target, start, graph) for child in graph.get(start) if child != prev
    )


def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    graph: Dict[int, List[int]] = defaultdict(list)
    for u, v in edges:
        if u in graph and v in graph and find(u, v, None, graph):
            return [u, v]
        graph[u].append(v)
        graph[v].append(u)
    return []


# disjoint set union
class DSU:
    def __init__(self, edges):
        self.parent = [0] * (len(edges) + 1)

    def find(self, x):
        if self.parent[x] == 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False
        self.parent[root_u] = root_v
        return True


def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    dsu = DSU(edges)
    for u, v in edges:
        if not dsu.union(u, v):
            return [u, v]
    return

