# https://leetcode.com/problems/ones-and-zeroes/
"""
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

Example 1:
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:
Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 
Constraints:
1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
"""
from typing import List
from collections import Counter
from functools import lru_cache

# brute force: O(2^n)
def find_max_form(strs: List[str], m: int, n: int) -> int:
    def helper(path, choices, m, n):
        nonlocal res
        res = max(res, len(path))
        for i in range(len(choices)):
            option = choices[i]
            c = Counter(option)
            if c["0"] <= m and c["1"] <= n:
                helper(
                    path + [option],
                    choices[:i] + choices[i + 1 :],
                    m - c["0"],
                    n - c["1"],
                )

    zeros = sum([s.count("0") for s in strs])
    ones = sum([s.count("1") for s in strs])
    if zeros <= m and ones <= n:
        return len(strs)
    res = 0
    helper([], strs, m, n)
    return res


# recursive + memo
def find_max_form(strs: List[str], m: int, n: int) -> int:
    @lru_cache(None)
    def helper(i, m, n):
        if i == -1 or (m == 0 and n == 0):
            return 0
        c = Counter(strs[i])
        if c["0"] <= m and c["1"] <= n:
            result_0 = helper(i - 1, m, n)
            result_1 = helper(i - 1, m - c["0"], n - c["1"]) + 1
            result = max(result_0, result_1)
        else:
            result = helper(i - 1, m, n)
        return result

    return helper(len(strs) - 1, m, n)


# dp
def find_max_form(strs: List[str], m: int, n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    def count(s):
        c = Counter(s)
        return c["0"], c["1"]

    for z, o in [count(s) for s in strs]:
        for x in range(m, -1, -1):
            for y in range(n, -1, -1):
                if x >= z and y >= o:
                    dp[x][y] = max(1 + dp[x - z][y - o], dp[x][y])
    return dp[m][n]


if __name__ == "__main__":
    find_max_form(strs=["10", "0001", "111001", "1", "0"], m=5, n=3)
