# https://leetcode.com/problems/network-delay-time/
"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 
Constraints:
1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""
import heapq
from collections import defaultdict


# Dijkstra’s algorithm: shortest path
# min heap BFS
def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    costs = {i + 1: float("inf") for i in range(n)}
    costs[k] = 0
    pq = [(0, k)]
    while pq:
        current_cost, current_vertex = heapq.heappop(pq)
        if current_cost > costs[current_vertex]:
            continue

        for neighbor, distance in graph[current_vertex]:
            cost = current_cost + distance
            if cost < costs[neighbor]:
                costs[neighbor] = cost
                heapq.heappush(pq, (cost, neighbor))

    res = -1
    for cost in costs.values():
        res = max(res, cost)
    if res == float("inf"):
        return -1
    return res


if __name__ == "__main__":
    network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
