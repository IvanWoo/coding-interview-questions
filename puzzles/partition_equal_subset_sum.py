# https://leetcode.com/problems/partition-equal-subset-sum/
"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.


Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 
Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""
from typing import List


# brute force: O(2^n)
def can_partition(nums: List[int]) -> bool:
    nums_sum = sum(nums)
    if nums_sum % 2 != 0:
        return False
    target = nums_sum // 2
    res = False

    def helper(i, target):
        n = len(nums)
        nonlocal res
        if res:
            return
        if target < 0:
            return
        elif target == 0:
            res = True
            return
        if i >= n - 1:
            return
        for j in range(i + 1, n):
            helper(j, target - nums[i])
            helper(j, target)

    helper(0, target)
    return res


# dp
def can_partition(nums: List[int]) -> bool:
    nums_sum = sum(nums)
    if nums_sum % 2 != 0:
        return False
    target = nums_sum // 2
    s = set([0])
    for n in nums:
        sum_with_n = []
        for i in s:
            if i + n == target:
                return True
            elif i + n < target:
                sum_with_n.append(i + n)
        s.update(sum_with_n)
    return False


if __name__ == "__main__":
    can_partition([1, 2, 5])
