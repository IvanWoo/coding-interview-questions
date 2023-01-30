# https://leetcode.com/problems/sliding-window-maximum/
"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""
from collections import deque
from typing import List


class MonotonicQueue(object):
    def __init__(self):
        self.data = deque()

    def push(self, n):
        while self.data and self.data[-1] < n:
            self.data.pop()
        self.data.append(n)

    def max(self):
        return self.data[0]

    def pop(self, n):
        if self.data and self.data[0] == n:
            self.data.popleft()


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    window = MonotonicQueue()
    res = []
    for i in range(len(nums)):
        if i < k - 1:
            window.push(nums[i])
        else:
            window.push(nums[i])
            res.append(window.max())
            window.pop(nums[i - k + 1])
    return res
