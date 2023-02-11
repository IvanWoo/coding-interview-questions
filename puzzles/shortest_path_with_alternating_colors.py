# https://leetcode.com/problems/shortest-path-with-alternating-colors/
"""
Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).

Example 1:
Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]

Example 2:
Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]

Example 3:
Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]

Example 4:
Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]

Example 5:
Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]


Constraints:
1 <= n <= 100
red_edges.length <= 400
blue_edges.length <= 400
red_edges[i].length == blue_edges[i].length == 2
0 <= red_edges[i][j], blue_edges[i][j] < n
"""
from collections import defaultdict, deque
from math import inf


def shortest_alternating_paths(
    n: int, red_edges: list[list[int]], blue_edges: list[list[int]]
) -> list[int]:
    def bfs(start_color):
        ans = [float("inf")] * n
        q = set([(0, 0, start_color)])
        visited = set()
        while q:
            new_q = set()
            while q:
                cur_node, cur_cost, cur_color = q.pop()

                if (cur_node, cur_color) in visited:
                    continue
                visited.add((cur_node, cur_color))

                ans[cur_node] = min(ans[cur_node], cur_cost)
                nxt_color = cur_color ^ 1
                for nxt_node in graph[nxt_color][cur_node]:
                    new_q.add((nxt_node, cur_cost + 1, nxt_color))
            q = new_q
        return ans

    graph = [defaultdict(list), defaultdict(list)]
    for u, v in red_edges:
        graph[0][u].append(v)
    for u, v in blue_edges:
        graph[1][u].append(v)

    red_ans = bfs(0)
    blue_ans = bfs(1)
    ans = [min(red_ans[i], blue_ans[i]) for i in range(n)]
    ans = [x if x != float("inf") else -1 for x in ans]
    return ans


def shortest_alternating_paths(
    n: int, red_edges: list[list[int]], blue_edges: list[list[int]]
) -> list[int]:
    red = defaultdict(list)
    blue = defaultdict(list)
    for u, v in red_edges:
        red[u].append(v)
    for u, v in blue_edges:
        blue[u].append(v)
    choices = [red, blue]
    ans = [inf] * n

    for flag in [0, 1]:
        visited = set()
        q = deque([(0, 0, flag)])
        while q:
            cur, steps, flag = q.popleft()
            if (cur, flag) in visited:
                continue
            visited.add((cur, flag))
            ans[cur] = min(ans[cur], steps)
            for nxt in choices[flag][cur]:
                q.append((nxt, steps + 1, flag ^ 1))
    return [x if x != inf else -1 for x in ans]
