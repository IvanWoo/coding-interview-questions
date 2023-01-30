# https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
Input:
n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]]
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
import heapq
from collections import deque
from math import inf


# bfs: TLE
def find_cheapest_price(
    n: int, flights: list[list[int]], src: int, dst: int, k: int
) -> int:
    graph = [[inf] * n for _ in range(n)]
    for u, v, d in flights:
        graph[u][v] = d

    ans = inf
    visited = set()
    q = deque([(src, k, 0)])
    while q:
        cur, stop, cost = q.popleft()
        if stop < -1:
            continue
        if cur == dst:
            ans = min(ans, cost)
            continue
        if cur in visited and cost > ans:
            continue
        visited.add(cur)
        for nxt in range(n):
            if nxt == cur:
                continue
            nxt_cost = graph[cur][nxt]
            q.append((nxt, stop - 1, cost + nxt_cost))
    return ans if ans != inf else -1


# priority queue
def find_cheapest_price(
    n: int, flights: list[list[int]], src: int, dst: int, k: int
) -> int:
    graph = [[inf] * n for _ in range(n)]
    for u, v, d in flights:
        graph[u][v] = d

    visited = set()
    pq = [(0, src, k + 1)]
    while pq:
        cost, cur, stop = heapq.heappop(pq)
        if cost == inf:
            continue
        if cur == dst:
            return cost
        if (cur, stop) in visited:
            continue
        visited.add((cur, stop))
        if stop > 0:
            for nxt in range(n):
                heapq.heappush(pq, (cost + graph[cur][nxt], nxt, stop - 1))
    return -1


if __name__ == "__main__":
    find_cheapest_price(
        n=4,
        flights=[[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]],
        src=0,
        dst=3,
        k=1,
    )
