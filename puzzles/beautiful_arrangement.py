# https://leetcode.com/problems/beautiful-arrangement/
"""
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.


Example 1:
Input: n = 2
Output: 2
Explanation:
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1

Example 2:
Input: n = 1
Output: 1


Constraints:
1 <= n <= 15
"""
from functools import lru_cache


# backtrack
def count_arrangement(n: int) -> int:
    def is_valid_last(perm):
        n = len(perm)
        return perm[-1] % n == 0 or n % perm[-1] == 0

    def backtrack(perm):
        nonlocal res
        if perm:
            if not is_valid_last(perm):
                return
        if len(perm) == n:
            res += 1
            return
        for i in range(1, n + 1):
            if visited[i]:
                continue
            visited[i] = True
            backtrack(perm + [i])
            visited[i] = False

    res = 0
    visited = [False] * (n + 1)
    backtrack([])
    return res


# dp + bitmasks
def count_arrangement(n: int) -> int:
    @lru_cache(None)
    def dfs(bm, pos):
        if pos == 0:
            return 1

        total = 0
        for i in range(n):
            if (bm & (1 << i) == 0) and ((i + 1) % pos == 0 or pos % (i + 1) == 0):
                total += dfs(bm ^ (1 << i), pos - 1)
        return total

    return dfs(0, n)


if __name__ == "__main__":
    count_arrangement(2) == 2
