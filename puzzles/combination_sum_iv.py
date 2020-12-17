# https://leetcode.com/problems/combination-sum-iv/
"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""
from typing import List

# backtrack: TLE
def combination_sum_4(nums: List[int], target: int) -> int:
    def backtrack(path, total):
        nonlocal res, visited
        if total > target:
            return
        elif total == target:
            p = tuple(path)
            if p not in visited:
                res += 1
                visited.add(p)
            return
        for n in nums:
            path.append(n)
            backtrack(path, total + n)
            path.pop()

    res = 0
    visited = set()
    backtrack([], 0)
    return res


# dp
def combination_sum_4(nums: List[int], target: int) -> int:
    nums = sorted(nums)
    dp = [1] + [0] * target
    for i in range(target + 1):
        for num in nums:
            if num > i:
                break
            dp[i] += dp[i - num]
    return dp[target]


if __name__ == "__main__":
    combination_sum_4([4, 2, 1], 32)
