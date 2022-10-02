# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
"""
You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

Example 1:
Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.

Example 2:
Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:
Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 109 + 7.
 
Constraints:
1 <= n, k <= 30
1 <= target <= 1000
"""
from functools import cache


def num_rolls_to_target(n: int, k: int, target: int) -> int:
    @cache
    def helper(cur_sum, left):
        if cur_sum > target:
            return 0
        if left == 0:
            return int(cur_sum == target)
        ans = 0
        for v in range(1, k + 1):
            ans += helper(cur_sum + v, left - 1)
        return ans

    MOD = 10**9 + 7
    return helper(0, n) % MOD


def num_rolls_to_target(n: int, k: int, target: int) -> int:
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    for v in range(1, k + 1):
        if v > target:
            continue
        dp[1][v] = 1

    for used in range(2, n + 1):
        for cur_sum in range(1, target + 1):
            for v in range(1, k + 1):
                if cur_sum - v >= 0:
                    dp[used][cur_sum] += dp[used - 1][cur_sum - v]

    MOD = 10**9 + 7
    return dp[n][target] % MOD


if __name__ == "__main__":
    num_rolls_to_target(2, 6, 7)
