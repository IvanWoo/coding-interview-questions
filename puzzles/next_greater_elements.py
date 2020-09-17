# https://leetcode.com/problems/next-greater-element-ii/
"""
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
"""

from typing import List

# brute force: O(n^2)
def next_greater_elements(nums: List[int]) -> List[int]:
    res = [-1] * len(nums)
    for k, v in enumerate(nums):
        stack = -1
        for num in nums[k:] + nums[:k]:
            if num > v:
                stack = num
                break
        res[k] = stack
    return res


# stack: O(n)
def next_greater_elements(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * n
    stack = []
    for i in reversed(range(2 * n)):
        i %= n
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(nums[i])
    return res
