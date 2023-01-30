# https://leetcode.com/problems/path-with-maximum-probability/
"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:
Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.

Constraints:
2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
There is at most one edge between every two nodes.
"""
import heapq
from collections import defaultdict
from typing import List


def max_probability(
    n: int, edges: List[List[int]], succProb: List[float], start: int, end: int
) -> float:
    graph = defaultdict(dict)
    for i in range(len(edges)):
        frm, to = edges[i]
        graph[frm][to] = succProb[i]
        graph[to][frm] = succProb[i]

    probabilities = {e: 0 for e in range(n)}
    probabilities[start] = 1
    # heappop will return the smallest value, but we need largest one in this problem
    # use negative value to do the trick
    pq = [(-1, start)]

    while pq:
        current_prob, edge = heapq.heappop(pq)
        current_prob = abs(current_prob)
        if current_prob < probabilities[edge]:
            continue

        for neighbor, succ_prob in graph[edge].items():
            prob = current_prob * succ_prob
            if prob > probabilities[neighbor]:
                probabilities[neighbor] = prob
                heapq.heappush(pq, (-prob, neighbor))

    return probabilities[end]


if __name__ == "__main__":
    max_probability(
        5,
        [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]],
        [0.37, 0.17, 0.93, 0.23, 0.39, 0.04],
        3,
        4,
    )
