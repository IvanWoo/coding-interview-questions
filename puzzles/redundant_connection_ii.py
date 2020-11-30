# https://leetcode.com/problems/redundant-connection-ii/
# In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

# The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

# Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

# Example 1:

# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given directed graph will be like this:
#   1
#  / \
# v   v
# 2-->3
# Example 2:

# Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# Output: [4,1]
# Explanation: The given directed graph will be like this:
# 5 <- 1 -> 2
#      ^    |
#      |    v
#      4 <- 3
# Note:

# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
from typing import List


def find_redundant_directed_connection(edges: List[List[int]]) -> List[int]:
    class UF:
        def __init__(self, n) -> None:
            self.root = list(range(n + 1))
            self.size = [1] * (n + 1)

        def find(self, x):
            while self.root[x] != x:
                self.root[x] = self.root[self.root[x]]
                x = self.root[x]
            return x

        def union(self, u, v):
            root_u, root_v = self.find(u), self.find(v)
            if root_u == root_v:
                return False

            if self.size[root_u] > self.size[root_v]:
                self.root[root_v] = root_u
                self.size[root_u] += self.size[root_v]
            else:
                self.root[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            return True

    def detect_cycle(n, edges, skip_edge):
        uf = UF(n)
        for u, v in edges:
            if [u, v] == skip_edge:
                continue
            if not uf.union(u, v):
                return [u, v]
        return

    n = len(edges)
    two_indegrees_node = -1
    indegrees = [0] * (n + 1)
    for _, v in edges:
        indegrees[v] += 1
        if indegrees[v] == 2:
            two_indegrees_node = v
            break

    if two_indegrees_node == -1:
        return detect_cycle(n, edges, None)

    for i in reversed(range(n)):
        if edges[i][1] == two_indegrees_node:
            if detect_cycle(n, edges, edges[i]) is None:
                return edges[i]
