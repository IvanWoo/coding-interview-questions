# https://codingbat.com/prob/p189576
"""
Consider the leftmost and righmost appearances of some value in an array. We'll say that the "span" is the number of elements between the two inclusive. A single value has a span of 1. Returns the largest span found in the given array. (Efficiency is not a priority.)


maxSpan([1, 2, 1, 1, 3]) → 4
maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6
"""
from typing import List
import collections


def max_span(nums: List[str]) -> int:
    num_positions = collections.defaultdict(list)
    for index, num in enumerate(nums):
        num_positions[num].append(index)
    return (
        num_positions[max(num_positions.keys())][-1]
        - num_positions[min(num_positions.keys())][0]
    )
