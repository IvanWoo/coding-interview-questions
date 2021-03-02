# https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

Constraints:
The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""
from typing import List
import heapq


# bfs
def find_cheapest_price(
    n: int, edges: List[List[int]], src: int, dst: int, k: int
) -> int:
    graph = [[float("inf")] * n for _ in range(n)]
    for u, v, d in edges:
        graph[u][v] = d

    ans = float("inf")
    q = set([(src, 0, 0)])
    while q:
        new_q = set()
        while q:
            pos, cost, stop = q.pop()
            if stop > k or cost >= ans:
                continue
            for new_pos in range(n):
                if new_pos == dst:
                    ans = min(ans, cost + graph[pos][new_pos])
                    continue
                new_q.add((new_pos, cost + graph[pos][new_pos], stop + 1))
        q = new_q
    return ans if ans != float("inf") else -1


def find_cheapest_price(
    n: int, edges: List[List[int]], src: int, dst: int, k: int
) -> int:
    graph = [[float("inf")] * n for _ in range(n)]
    for u, v, d in edges:
        graph[u][v] = d

    pq = [(0, src, k + 1)]
    while pq:
        cost, pos, left_stop = heapq.heappop(pq)
        if cost == float("inf"):
            continue
        if pos == dst:
            return cost
        if left_stop > 0:
            for new_pos in range(n):
                heapq.heappush(pq, (cost + graph[pos][new_pos], new_pos, left_stop - 1))
    return -1


if __name__ == "__main__":
    find_cheapest_price(
        n=4,
        edges=[[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]],
        src=0,
        dst=3,
        k=1,
    )
