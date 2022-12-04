# https://leetcode.com/problems/minimum-average-difference/
"""
You are given a 0-indexed integer array nums of length n.

The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

Note:
The absolute difference of two numbers is the absolute value of their difference.
The average of n elements is the sum of the n elements divided (integer division) by n.
The average of 0 elements is considered to be 0.

Example 1:
Input: nums = [2,5,3,9,5,3]
Output: 3
Explanation:
- The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
- The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
- The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
- The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
- The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
- The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
The average difference of index 3 is the minimum average difference so return 3.

Example 2:
Input: nums = [0]
Output: 0
Explanation:
The only index is 0 so return 0.
The average difference of index 0 is: |0 / 1 - 0| = |0 - 0| = 0.

Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 105
"""
from math import inf

# TLE
def minimum_average_difference(nums: list[int]) -> int:
    def avg(ns: list[int]) -> int:
        if not ns:
            return 0
        return sum(ns) // len(ns)

    min_avg_diff = inf
    idx = None
    n = len(nums)
    for i in range(n):
        tail, head = nums[: i + 1], nums[i + 1 :]
        avg_diff = abs(avg(tail) - avg(head))
        if avg_diff < min_avg_diff:
            min_avg_diff = avg_diff
            idx = i
    return idx


def minimum_average_difference(nums: list[int]) -> int:
    def get_avg_diff(idx: int) -> int:
        # 0:i+1
        head = prefix_sum[idx] // (idx + 1)
        # i+2:n
        if idx == n - 1:
            tail = 0
        else:
            tail = (prefix_sum[n - 1] - prefix_sum[idx]) // (n - idx - 1)
        return abs(head - tail)

    n = len(nums)
    prefix_sum = nums[:]
    for i in range(1, n):
        prefix_sum[i] += prefix_sum[i - 1]
    min_avg_diff = inf
    idx = None
    for i in range(n):
        avg_diff = get_avg_diff(i)
        if avg_diff == 0:
            return i
        if avg_diff < min_avg_diff:
            min_avg_diff = avg_diff
            idx = i
    return idx
