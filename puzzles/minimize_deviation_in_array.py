# https://leetcode.com/problems/minimize-deviation-in-array/description/
"""
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

Example 1:
Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.

Example 2:
Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.

Example 3:
Input: nums = [2,10,8]
Output: 3

Constraints:
n == nums.length
2 <= n <= 5 * 104
1 <= nums[i] <= 109
"""
import heapq
from math import inf

from sortedcontainers import SortedSet


def minimum_deviation(nums: list[int]) -> int:
    # dedup and normalize the nums to only have even numbers
    vals = [-(x * 2 if x % 2 != 0 else x) for x in set(nums)]

    min_v = -max(vals)
    heapq.heapify(vals)

    ans = inf
    while True:
        cur_max = -heapq.heappop(vals)
        ans = min(ans, cur_max - min_v)
        if ans == 0:
            break

        if cur_max % 2 == 1:
            break
        cur_max //= 2
        heapq.heappush(vals, -cur_max)
        min_v = min(min_v, cur_max)
    return ans


def minimum_deviation(nums: list[int]) -> int:
    vals = SortedSet([x * 2 if x % 2 != 0 else x for x in nums])
    ans = inf
    min_v = vals[0]

    while True:
        cur_max = vals.pop(-1)
        ans = min(ans, cur_max - min_v)
        if ans == 0:
            break

        if cur_max % 2 == 1:
            break
        cur_max //= 2
        vals.add(cur_max)
        min_v = min(min_v, cur_max)
    return ans
