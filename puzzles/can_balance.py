# https://codingbat.com/prob/p158767
"""
Given a non-empty array, return true if there is a place to split the array so that the sum of the numbers on one side is equal to the sum of the numbers on the other side.


canBalance([1, 1, 1, 2, 1]) → true
canBalance([2, 1, 1, 2, 1]) → false
canBalance([10, 10]) → true
"""
from typing import List


def can_balance(nums: List[int]) -> bool:
    for i in range(1, len(nums)):
        if sum(nums[:i]) == sum(nums[i:]):
            return True
        else:
            continue
    return False
