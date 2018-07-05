def two_sum(nums, target):
    """
    given an array of integers, return indices of the two numbers such that they add up to a specific target
    assume each input would have exactly one solution, and you may use the same element twice
    :param nums:
    :param target:
    :return:
    """
    for i in range(len(nums)):
        left = target - nums[i]
        try:
            j = nums.index(left)
            return [i, j]
        except ValueError:
            pass


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


if __name__ == '__main__':
    print(two_sum([1, 2, 7, 11, 15], 9))
    print(two_sum([1, 2, 7, 11, 15], 9) == [1, 2])
