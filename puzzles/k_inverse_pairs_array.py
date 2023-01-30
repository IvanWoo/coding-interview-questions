# https://leetcode.com/problems/k-inverse-pairs-array/
"""
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.


Example 1:
Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.

Example 2:
Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.


Constraints:
1 <= n <= 1000
0 <= k <= 1000
"""


# O(n^3)
def k_inverse_pairs(n: int, k: int) -> int:
    MOD = 10**9 + 7

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(k + 1):
            dp[i][j] = sum(dp[i - 1][max(0, j - i + 1) : j + 1]) % MOD
    return dp[n][k]


# O(n^2)
def k_inverse_pairs(n: int, k: int) -> int:
    MOD = 10**9 + 7

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        prefix = [0] * (k + 1)
        for j in range(k + 1):
            prefix[j] = prefix[j - 1] + dp[i - 1][j]

        for j in range(k + 1):
            if j - i + 1 <= 0:
                dp[i][j] = prefix[j] % MOD
            else:
                dp[i][j] = (prefix[j] - prefix[j - i]) % MOD
    return dp[n][k]


if __name__ == "__main__":
    k_inverse_pairs(4, 3)
