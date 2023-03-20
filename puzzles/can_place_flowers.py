# https://leetcode.com/problems/can-place-flowers/description/
"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""


def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    def helper(fb: list[int]) -> int:
        n = len(fb)
        c = 0
        i = 0
        while i < n:
            if fb[i] == 1:
                ...
            elif i - 1 >= 0 and fb[i - 1] == 1:
                ...
            elif i + 1 < n and fb[i + 1] == 1:
                ...
            else:
                fb[i] = 1
                c += 1
            i += 1
        return c

    return helper(flowerbed[:]) >= n
