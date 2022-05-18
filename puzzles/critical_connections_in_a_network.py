# https://leetcode.com/problems/critical-connections-in-a-network/
"""
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Example 2:
Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
 
Constraints:
2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
"""
from collections import defaultdict, deque
from puzzles.union_find import UF

# brute force: TLE
# at least O(n^2*log(n))
def critical_connections(n: int, connections: list[list[int]]) -> list[list[int]]:
    def is_critical(c_idx):
        uf = UF(n)
        for i, (u, v) in enumerate(connections):
            if i == c_idx:
                continue
            uf.union(u, v)
        for i in range(n):
            if not uf.connected(i, 0):
                return True
        return False

    res = []
    for i, c in enumerate(connections):
        if is_critical(i):
            res.append(c)
    return res


# Tarjan's strongly connected components algorithm
# https://www.youtube.com/watch?v=kYcUIEQqL2Y&t=0s
def critical_connections(n: int, connections: list[list[int]]) -> list[list[int]]:
    graph = defaultdict(deque)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(u, parents, low, disc, ans):
        nonlocal time, graph
        if disc[u] != -1:
            return

        low[u] = disc[u] = time
        time += 1
        for v in graph[u]:
            if disc[v] == -1:
                parents[v] = u
                dfs(v, parents, low, disc, ans)

                if low[v] > disc[u]:
                    ans.append([u, v])

                low[u] = min(low[u], low[v])
            elif parents[u] != v:
                low[u] = min(low[u], disc[v])

    time = 0
    # first discover time
    disc = [-1] * n
    # lowest vertex in subtree
    low = [-1] * n
    parents = [-1] * n
    ans = []
    for i in range(n):
        if disc[i] == -1:
            dfs(i, parents, low, disc, ans)
    return ans


if __name__ == "__main__":
    critical_connections(4, [[0, 1], [1, 2], [2, 0], [1, 3]])
