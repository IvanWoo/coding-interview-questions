# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


# O(nlogn), O(n)
def find_unsorted_subarray(nums: list[int]) -> int:
    sorted_nums = sorted(nums)
    start, end = len(nums), 0
    for i in range(len(nums)):
        if sorted_nums[i] != nums[i]:
            start = min(start, i)
            end = max(end, i)
    return max(end - start + 1, 0)


# O(n), O(n)
def find_unsorted_subarray(nums: list[int]) -> int:
    n = len(nums)
    stack = []
    start, end = n, 0
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            start = min(start, stack.pop())
        stack.append(i)

    stack = []
    for i in reversed(range(n)):
        while stack and nums[stack[-1]] < nums[i]:
            end = max(end, stack.pop())
        stack.append(i)
    return max(end - start + 1, 0)


# O(n), O(1)
def find_unsorted_subarray(nums: list[int]) -> int:
    n = len(nums)
    min_val, max_val = float("inf"), float("-inf")
    flag = False
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            flag = True
        if flag:
            min_val = min(min_val, nums[i])

    flag = False
    for i in reversed(range(n - 1)):
        if nums[i] > nums[i + 1]:
            flag = True
        if flag:
            max_val = max(max_val, nums[i])

    l, r = n, 0
    for i in range(n):
        if min_val < nums[i]:
            l = i
            break
    for i in reversed(range(n)):
        if max_val > nums[i]:
            r = i
            break
    return max(r - l + 1, 0)


# O(n), O(1)
def find_unsorted_subarray(nums: list[int]) -> int:
    n = len(nums)
    start, end = n, 0
    prev_hi, prev_lo = n - 1, 0
    for i in range(n):
        if nums[i] < nums[prev_lo]:
            end = i
        else:
            prev_lo = i

    for i in reversed(range(n)):
        if nums[i] > nums[prev_hi]:
            start = i
        else:
            prev_hi = i
    return max(end - start + 1, 0)


if __name__ == "__main__":
    find_unsorted_subarray([2, 6, 4, 8, 10, 9, 15])
