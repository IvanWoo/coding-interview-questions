# https://leetcode.com/problems/number-of-operations-to-make-network-connected/
"""
There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return -1.

Example 1:
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

Example 2:
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2

Example 3:
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.

Example 4:
Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
Output: 0


Constraints:
1 <= n <= 10^5
1 <= connections.length <= min(n*(n-1)/2, 10^5)
connections[i].length == 2
0 <= connections[i][0], connections[i][1] < n
connections[i][0] != connections[i][1]
There are no repeated connections.
No two computers are connected by more than one cable.
"""
from typing import List


def make_connected(n: int, connections: List[List[int]]) -> int:
    class UF:
        def __init__(self, n) -> None:
            self.root = list(range(n))
            self.size = [1] * n
            self.count = n
            self.redundant = 0

        def find(self, x):
            while self.root[x] != x:
                self.root[x] = self.root[self.root[x]]
                x = self.root[x]
            return x

        def union(self, u, v):
            root_u, root_v = self.find(u), self.find(v)
            if root_u == root_v:
                self.redundant += 1
                return
            if self.size[root_u] > self.size[root_v]:
                self.root[root_v] = root_u
                self.size[root_u] += self.size[root_v]
            else:
                self.root[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            self.count -= 1

    uf = UF(n)
    for u, v in connections:
        uf.union(u, v)
    if uf.redundant < uf.count - 1:
        return -1
    return uf.count - 1
