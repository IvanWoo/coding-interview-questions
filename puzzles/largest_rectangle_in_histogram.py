# https://leetcode.com/problems/largest-rectangle-in-histogram/
"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:
Input: [2,1,5,6,2,3]
Output: 10
"""

from typing import List


# O(n^2)
def largest_rectangle_area(heights: List[int]) -> int:
    ans = 0

    for i, anchor in enumerate(heights):
        for j, boundary in enumerate(heights):
            if j < i:
                continue
            anchor = min(anchor, boundary)
            ans = max(ans, anchor * (j - i + 1))

    return ans


# monotonic stack: O(n)
def largest_rectangle_area(heights: List[int]) -> int:
    heights.append(0)
    n = len(heights)
    stack = [-1]
    ans = 0
    for i in range(n):
        while heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)

    return ans
