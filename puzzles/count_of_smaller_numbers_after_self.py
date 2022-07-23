# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
 
Constraints:

0 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""

from collections import deque
from bisect import bisect_left

from sortedcontainers import SortedList

# brute force: O(n^2)
def count_smaller(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [0] * n
    for i in range(n):
        c = 0
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                c += 1
        ans[i] = c
    return ans


def count_smaller(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [0] * n

    def merge(arr1, arr2):
        ans = deque()
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i][1] > arr2[j][1]:
                ans.append(arr1[i])
                res[arr1[i][0]] += len(arr2) - j
                i += 1
            else:
                ans.append(arr2[j])
                j += 1

        ans.extend(arr1[i:] or arr2[j:])
        return list(ans)

    def sort(nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = sort(nums[:mid])
        right = sort(nums[mid:])

        return merge(left, right)

    sort(list(enumerate(nums)))
    return res


def count_smaller(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [0] * n
    sorted_list = deque()
    for i in reversed(range(n)):
        val = nums[i]
        j = bisect_left(sorted_list, val)
        ans[i] = j
        sorted_list.insert(j, val)
    return ans


def count_smaller(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [0] * n
    sorted_list = SortedList()
    for i in reversed(range(n)):
        val = nums[i]
        j = sorted_list.bisect_left(val)
        ans[i] = j
        sorted_list.add(val)
    return ans


if __name__ == "__main__":
    count_smaller([5, 2, 6, 1])
