# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
"""
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:
Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.


Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
"""
from functools import cache


# brute force: TLE
def min_operations(nums: list[int], x: int) -> int:
    @cache
    def helper(lo, hi, val, steps):
        if val == 0:
            return steps
        if val < 0:
            return float("inf")
        if lo > hi:
            return float("inf")

        return min(
            helper(lo + 1, hi, val - nums[lo], steps + 1),
            helper(lo, hi - 1, val - nums[hi], steps + 1),
        )

    res = helper(0, len(nums) - 1, x, 0)
    return res if res != float("inf") else -1


def min_operations(nums: list[int], x: int) -> int:
    def prefix_sum(arr: list[int]):
        res = [0] + arr[:]
        for i in range(1, len(res)):
            res[i] += res[i - 1]
        return res

    def do(h1: dict[int, int], h2: dict[int, int]) -> None:
        nonlocal res
        n = len(nums)
        for v1, i in h1.items():
            target = x - v1
            if target in h2:
                j = h2[target]
                if (i + j) > n:
                    continue
                res = min(res, i + j)

    left = {v: k for (k, v) in enumerate(prefix_sum(nums))}
    right = {v: k for (k, v) in enumerate(prefix_sum(nums[::-1]))}

    res = float("inf")
    do(left, right)
    do(right, left)

    return res if res != float("inf") else -1


def min_operations(nums: list[int], x: int) -> int:
    n, total = len(nums), sum(nums)
    lo, hi, window, res = 0, 0, 0, 0
    target = total - x
    if total < x:
        return -1
    if total == x:
        return n
    while hi < n:
        n1 = nums[hi]
        hi += 1
        window += n1
        while window > target:
            n2 = nums[lo]
            lo += 1
            window -= n2
        if window == target:
            res = max(res, hi - lo)
    return n - res if res != 0 else -1


if __name__ == "__main__":
    min_operations([1, 1, 4, 2, 3], 5)
