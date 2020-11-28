# https://leetcode.com/problems/longest-consecutive-sequence/
"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Follow up: Could you implement the O(n) solution? 

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 104
-109 <= nums[i] <= 109
"""
from typing import List
from puzzles.union_find import UF

# O(nlogn)
def longest_consecutive(nums: List[int]) -> int:
    if not nums:
        return 0
    sorted_nums = sorted(nums)
    res = 1
    count = 1
    for i in range(1, len(nums)):
        if sorted_nums[i] != sorted_nums[i - 1]:
            if sorted_nums[i] - sorted_nums[i - 1] == 1:
                count += 1
            else:
                res = max(res, count)
                count = 1

    return max(res, count)


# O(n)
def longest_consecutive(nums: List[int]) -> int:
    res = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            cur = num
            temp_res = 1

            while cur + 1 in num_set:
                cur += 1
                temp_res += 1

            res = max(res, temp_res)
    return res


# union find
def longest_consecutive(nums: List[int]) -> int:
    uf = UF(len(nums))
    v2i = dict()

    for i, num in enumerate(nums):
        if num in v2i.keys():
            continue
        if num + 1 in v2i.keys():
            uf.union(i, v2i[num + 1])
        if num - 1 in v2i.keys():
            uf.union(i, v2i[num - 1])

        v2i[num] = i

    return max(uf.size) if uf.size else 0


if __name__ == "__main__":
    longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
