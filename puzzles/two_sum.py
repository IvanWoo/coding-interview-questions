from typing import List


def two_sum(nums: int, target: int) -> List[int]:
    """
    given an array of integers, return indices of the two numbers such that they add up to a specific target
    assume each input would have exactly one solution, and you may use the same element twice
    :param nums:
    :param target:
    :return:
    """
    hash_table = dict([(v, k) for k, v in enumerate(nums)])
    for i, num in enumerate(nums):
        left = target - num
        if left in hash_table:
            return [i, hash_table[left]]


def two_sum_alt(nums, target):
    """
    given an array of integers, return indices of the two numbers such that they add up to a specific target
    assume each input would have exactly one solution, and you may NOT use the same element twice
    :param nums:
    :param target:
    :return:
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

