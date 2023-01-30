# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
"""
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.

Follow up: Could you do this in O(n) runtime?

Example 1:
Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:
Input: nums = [0]
Output: 0

Example 3:
Input: nums = [2,4]
Output: 6

Example 4:
Input: nums = [8,10,2]
Output: 10

Example 5:
Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127

Constraints:

1 <= nums.length <= 2 * 104
0 <= nums[i] <= 231 - 1
"""

from dataclasses import dataclass
from typing import List


# O(n^2)
def find_maximum_XOR(nums: List[int]) -> int:
    n = len(nums)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans = max(ans, nums[i] ^ nums[j])
    return ans


@dataclass
class TrieNode:
    one = None
    zero = None
    val = None


def find_maximum_XOR(nums: List[int]) -> int:
    # build the trie
    root = TrieNode()
    for num in nums:
        cur = root
        for i in reversed(range(32)):
            mask = 1 << i
            masked_num = mask & num
            if masked_num == 0:
                if not cur.zero:
                    cur.zero = TrieNode()
                cur = cur.zero
            else:
                if not cur.one:
                    cur.one = TrieNode()
                cur = cur.one
        cur.val = num

    ans = 0
    for num in nums:
        cur = root
        for i in reversed(range(32)):
            mask = 1 << i
            masked_num = mask & num
            if masked_num == 0:
                cur = cur.one if cur.one else cur.zero
            else:
                cur = cur.zero if cur.zero else cur.one
        ans = max(ans, num ^ cur.val)
    return ans
