# https://leetcode.com/problems/subarray-product-less-than-k/
"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:
0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""
from typing import List


def num_subarray_product_less_than_k(nums: List[int], k: int) -> int:
    n = len(nums)
    left, prod, count = 0, 1, 0

    for right in range(n):
        prod *= nums[right]

        while prod >= k and left <= right:
            prod /= nums[left]
            left += 1
        # add new subarray ending with right element
        count += right - left + 1
    return count


if __name__ == "__main__":
    num_subarray_product_less_than_k([10, 5, 2, 6], 100)
