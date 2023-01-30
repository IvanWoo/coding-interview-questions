# https://leetcode.com/problems/largest-perimeter-triangle/
"""
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Example 1:
Input: nums = [2,1,2]
Output: 5

Example 2:
Input: nums = [1,2,1]
Output: 0

Constraints:
3 <= nums.length <= 104
1 <= nums[i] <= 106
"""


# brute force
def largest_perimeter(nums: list[int]) -> int:
    ans = 0
    n = len(nums)
    for i in range(n):
        for j in range(i):
            for k in range(j):
                ni, nj, nk = nums[i], nums[j], nums[k]
                if ni + nj > nk and ni + nk > nj and nj + nk > ni:
                    ans = max(ans, ni + nj + nk)
    return ans


def largest_perimeter(nums: list[int]) -> int:
    nums.sort(key=lambda x: -x)
    n = len(nums)
    for i in range(n - 2):
        n1, n2, n3 = nums[i : i + 3]
        if n2 + n3 > n1:
            return n1 + n2 + n3
    return 0


if __name__ == "__main__":
    largest_perimeter([2, 1, 2])
