# https://leetcode.com/problems/possible-bipartition/description/
"""
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.


Example 1:
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].

Example 2:
Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:
Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false

Constraints:
1 <= n <= 2000
0 <= dislikes.length <= 104
dislikes[i].length == 2
1 <= dislikes[i][j] <= n
ai < bi
All the pairs of dislikes are unique.
"""
from collections import defaultdict, deque


def possible_bipartition(n: int, dislikes: list[list[int]]) -> bool:
    def dfs(i, node_color):
        color[i] = node_color
        for nxt in graph[i]:
            if color[nxt] == node_color:
                return False
            if color[nxt] == -1:
                if not dfs(nxt, 1 - node_color):
                    return False
        return True

    graph = defaultdict(list)
    for u, v in dislikes:
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == -1:
            if not dfs(i, 0):
                return False
    return True


def possible_bipartition(n: int, dislikes: list[list[int]]) -> bool:
    def bfs(i):
        color[i] = 0
        q = deque([i])
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                if color[nxt] == color[cur]:
                    return False
                if color[nxt] == -1:
                    color[nxt] = 1 - color[cur]
                    q.append(nxt)
        return True

    graph = defaultdict(list)
    for u, v in dislikes:
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == -1:
            if not bfs(i):
                return False
    return True
