# https://techdevguide.withgoogle.com/paths/advanced/volume-of-water/#!
# https://leetcode.com/problems/trapping-rain-water/

"""
Imagine an island that is in the shape of a bar graph. When it rains, certain areas of the island fill up with rainwater to form lakes. Any excess rainwater the island cannot hold in lakes will run off the island to the west or east and drain into the ocean.

Given an array of positive integers representing 2-D bar heights, design an algorithm (or write a function) that can compute the total volume (capacity) of water that could be held in all lakes on such an island given an array of the heights of the bars. Assume an elevation map where the width of each bar is 1.

Example: Given [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2], return 15 (3 bodies of water with volumes of 1,7,7 yields total volume of 15)
"""
from typing import List

# brute force
def trap(height: List[int]) -> int:
    ans = 0
    for i, h in enumerate(height):
        if i >= 1 and i <= len(height):
            max_left = max(height[: (i + 1)])
            max_right = max(height[i:])
            ans += min(max_left, max_right) - h
    return ans


# dynamic programming
def trap(height: List[int]) -> int:
    if height == []:
        return 0

    max_left, max_right = [0] * len(height), [0] * len(height)

    max_left[0] = height[0]
    for i in range(1, len(height)):
        max_left[i] = max(height[i], max_left[i - 1])

    max_right[len(height) - 1] = height[-1]
    for i in range(len(height) - 2, -1, -1):
        max_right[i] = max(height[i], max_right[i + 1])

    ans = 0
    for k, v in enumerate(height):
        ans += min(max_left[k], max_right[k]) - v
    return ans


# two pointers
def trap(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    l_max, r_max = 0, 0
    ans = 0
    while left <= right:
        l_max = max(l_max, height[left])
        r_max = max(r_max, height[right])
        if l_max < r_max:
            ans += l_max - height[left]
            left += 1
        else:
            ans += r_max - height[right]
            right -= 1
    return ans


if __name__ == "__main__":
    trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
