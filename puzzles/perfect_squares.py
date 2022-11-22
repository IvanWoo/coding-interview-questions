# https://leetcode.com/problems/perfect-squares/
"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
from collections import deque
from math import inf

# BFS: use too much memory
def num_squares(n: int) -> int:
    squares = [x**2 for x in range(1, int(n**0.5) + 1)]
    q = deque([(n, 0)])
    while q:
        left, count = q.popleft()
        for sqr in squares:
            if sqr == left:
                return count + 1
            if sqr > left:
                break
            q.append((left - sqr, count + 1))


# DP: TLE
def num_squares(n: int) -> int:
    dp = [0] + [inf] * n
    for i in range(1, n + 1):
        dp[i] = (
            min(dp[i - s] for s in (x**2 for x in range(1, int(i**0.5) + 1))) + 1
        )
    return dp[n]


# BFS
def num_squares(n: int) -> int:
    squares = [x**2 for x in range(1, int(n**0.5) + 1)]
    count = 1
    queue = {n}
    while queue:
        temp = set()
        for x in queue:
            for y in squares:
                if x == y:
                    return count
                elif x < y:
                    break
                elif x > y:
                    temp.add(x - y)
        queue = temp
        count += 1


if __name__ == "__main__":
    num_squares(12)
