# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""
from typing import Optional

from puzzles.utils import TreeNode


def sorted_array_to_bst(nums: list[int]) -> Optional[TreeNode]:
    def helper(nums: list[int]):
        if not nums:
            return
        n = len(nums)
        mid = n // 2
        left = helper(nums[:mid])
        right = helper(nums[(mid + 1) :])
        return TreeNode(nums[mid], left, right)

    return helper(nums)


def sorted_array_to_bst(nums: list[int]) -> Optional[TreeNode]:
    def helper(start: int, end: int) -> Optional[TreeNode]:
        if start >= end:
            return
        mid = (start + end) // 2
        left = helper(start, mid)
        right = helper(mid + 1, end)
        return TreeNode(nums[mid], left, right)

    n = len(nums)
    return helper(0, n)
