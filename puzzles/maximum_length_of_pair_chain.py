# https://leetcode.com/problems/maximum-length-of-pair-chain/
"""
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:

Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:

The number of given pairs will be in the range [1, 1000].
"""
from functools import lru_cache
from typing import List


# TLE
def find_longest_chain(pairs: List[List[int]]) -> int:
    ans = 0
    n = len(pairs)
    pairs = sorted(pairs)

    def helper(i, chain):
        nonlocal ans
        ans = max(ans, len(chain))
        for j in range(i + 1, n):
            if not chain:
                helper(j, [pairs[j]])
            elif pairs[j][0] > chain[-1][1]:
                helper(j, chain + [pairs[j]])

    helper(-1, [])
    return ans


# TLE
def find_longest_chain(pairs: List[List[int]]) -> int:
    ans = 0
    n = len(pairs)
    pairs = sorted(pairs)

    @lru_cache(None)
    def helper(i, len_chain, max_val):
        nonlocal ans
        ans = max(ans, len_chain)
        for j in range(i + 1, n):
            if not len_chain:
                helper(j, 1, pairs[j][1])
            elif pairs[j][0] > max_val:
                helper(j, len_chain + 1, pairs[j][1])

    helper(-1, 0, None)
    return ans


# DP: O(n^2)
def find_longest_chain(pairs: List[List[int]]) -> int:
    n = len(pairs)
    pairs = sorted(pairs)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if pairs[i][0] > pairs[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp[-1]


# DP: O(n^2)
def find_longest_chain(pairs: List[List[int]]) -> int:
    n = len(pairs)
    pairs = sorted(pairs)

    rights = [p[1] for p in pairs]
    dp = [1] * n

    for i in range(1, n):
        pres = [dp[k] for k, v in enumerate(rights[:i]) if v < pairs[i][0]]
        dp[i] += max(pres) if pres else 0

    return dp[-1]


# greedy
def find_longest_chain(pairs: List[List[int]]) -> int:
    cur, ans = float("-inf"), 0

    for head, tail in sorted(pairs, key=lambda x: x[1]):
        if cur < head:
            cur = tail
            ans += 1

    return ans


if __name__ == "__main__":
    find_longest_chain([[1, 2], [2, 3], [3, 4]])
