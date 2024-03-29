# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
"""
You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Remove x from the array nums.
Return the maximum score after performing m operations.

Example 1:
Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.

Example 2:
Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score.
The total score is 50 + 15 - 9 + 4 + 42 = 102.


Constraints:
n == nums.length
m == multipliers.length
1 <= m <= 103
m <= n <= 105
-1000 <= nums[i], multipliers[i] <= 1000
"""
from functools import cache


# brute force
def maximum_score(nums: list[int], multipliers: list[int]) -> int:
    def helper(lo: int, hi: int, idx: int, score: int):
        nonlocal ans
        if idx >= m:
            ans = max(ans, score)
            return
        helper(lo + 1, hi, idx + 1, nums[lo] * multipliers[idx] + score)
        helper(lo, hi - 1, idx + 1, nums[hi] * multipliers[idx] + score)

    ans = 0
    n = len(nums)
    m = len(multipliers)
    helper(0, n - 1, 0, 0)
    return ans


def maximum_score(nums: list[int], multipliers: list[int]) -> int:
    @cache
    def helper(lo: int, hi: int, idx: int):
        if idx >= m:
            return 0
        score = max(
            helper(lo + 1, hi, idx + 1) + nums[lo] * multipliers[idx],
            helper(lo, hi - 1, idx + 1) + nums[hi] * multipliers[idx],
        )
        return score

    n = len(nums)
    m = len(multipliers)
    return helper(0, n - 1, 0)


def maximum_score(nums: list[int], multipliers: list[int]) -> int:
    @cache
    def helper(ops: int, left: int):
        if ops >= m:
            return 0
        l = helper(ops + 1, left + 1) + nums[left] * multipliers[ops]
        r = helper(ops + 1, left) + nums[n - 1 - (ops - left)] * multipliers[ops]
        return max(l, r)

    n, m = len(nums), len(multipliers)
    return helper(0, 0)


def maximum_score(nums: list[int], multipliers: list[int]) -> int:
    n, m = len(nums), len(multipliers)
    dp = [[0] * (m + 1) for _ in range(m + 1)]
    for op in reversed(range(m)):
        for left in reversed(range(op + 1)):
            dp[op][left] = max(
                multipliers[op] * nums[left] + dp[op + 1][left + 1],
                multipliers[op] * nums[n - 1 - (op - left)] + dp[op + 1][left],
            )
    return dp[0][0]


if __name__ == "__main__":
    maximum_score(
        [1, 2, 3],
        [3, 2, 1],
    )
