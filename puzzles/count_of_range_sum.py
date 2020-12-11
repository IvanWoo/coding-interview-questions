# https://leetcode.com/problems/count-of-range-sum/
"""
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.

Constraints:
0 <= nums.length <= 10^4
"""
from collections import deque
from typing import List

# TLE: O(n^2)
def count_range_sum(nums: List[int], lower: int, upper: int) -> int:
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    res = 0

    for i in range(n):
        for j in range(i, n):
            if j == i:
                if lower <= nums[j] <= upper:
                    res += 1
            else:
                if lower <= (prefix_sum[j + 1] - prefix_sum[i]) <= upper:
                    res += 1
    return res


# merge sort: O(n*logn)
def count_range_sum(nums: List[int], lower: int, upper: int) -> int:
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    # inclusive
    def mergesort(l, r):
        # [l, r]
        if l == r:
            return 0
        mid = (l + r) >> 1
        count = mergesort(l, mid) + mergesort(mid + 1, r)

        i = j = mid + 1
        for left in prefix_sum[l : mid + 1]:
            while i <= r and prefix_sum[i] - left < lower:
                i += 1
            while j <= r and prefix_sum[j] - left <= upper:
                j += 1
            count += j - i

        prefix_sum[l : r + 1] = sorted(prefix_sum[l : r + 1])
        return count

    return mergesort(0, n)


# merge sort
def count_range_sum(nums: List[int], lower: int, upper: int) -> int:
    n = len(nums)
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    def merge(arr1, arr2):
        ans = deque()
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])
                j += 1

        ans.extend(arr1[i:])
        ans.extend(arr2[j:])
        return list(ans)

    def mergesort(l, r):
        # [l, r)
        mid = (l + r) // 2
        if l == mid:
            return int(lower <= prefix_sum[l] <= upper)
        count = mergesort(l, mid) + mergesort(mid, r)
        i = j = mid
        for left in prefix_sum[l:mid]:
            while i < r and prefix_sum[i] - left < lower:
                i += 1
            while j < r and prefix_sum[j] - left <= upper:
                j += 1
            count += j - i
        # prefix_sum[l:r] = sorted(prefix_sum[l:r])
        prefix_sum[l:r] = merge(prefix_sum[l:mid], prefix_sum[mid:r])
        return count

    return mergesort(0, n)


if __name__ == "__main__":
    count_range_sum([-2, 5, -1], -2, 2)
