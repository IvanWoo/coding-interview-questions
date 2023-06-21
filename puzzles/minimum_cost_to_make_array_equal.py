# https://leetcode.com/problems/minimum-cost-to-make-array-equal/description/
"""
You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.

Example 1:
Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the array equal with a smaller cost.

Example 2:
Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
Output: 0
Explanation: All the elements are already equal, so no operations are needed.

Constraints:
n == nums.length == cost.length
1 <= n <= 105
1 <= nums[i], cost[i] <= 106
"""
from math import inf


# brute force: O(n^2)
def min_cost(nums: list[int], cost: list[int]) -> int:
    unique_nums = set(nums)
    ret = inf
    for target in unique_nums:
        ret = min(ret, sum([abs(target - n) * c for n, c in zip(nums, cost)]))
    return ret


def min_cost(nums: list[int], cost: list[int]) -> int:
    def get_cost(target):
        return sum([abs(target - n) * c for n, c in zip(nums, cost)])

    lo, hi = min(nums), max(nums)
    ret = get_cost(nums[0])
    while lo < hi:
        mid = (lo + hi) // 2
        c1 = get_cost(mid)
        c2 = get_cost(mid + 1)
        ret = min(c1, c2)

        if c1 > c2:
            lo = mid + 1
        else:
            hi = mid
    return ret
