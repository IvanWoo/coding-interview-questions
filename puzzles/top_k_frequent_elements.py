# https://leetcode.com/problems/top-k-frequent-elements/
"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from collections import Counter, defaultdict


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counter = defaultdict(int)
    for n in nums:
        counter[n] += 1

    sorted_q = sorted([(val, key) for key, val in counter.items()], reverse=True)
    return [key for _, key in sorted_q[0:k]]


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counter = Counter(nums)
    return [key for key, _ in counter.most_common(k)]
