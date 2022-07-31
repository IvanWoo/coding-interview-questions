from puzzles.range_sum_query_mutable import NumArray


def test_NumArray():
    nums = [1, 3, 5]
    numArray = NumArray(nums)
    assert numArray.sumRange(0, 2) == 9
    numArray.update(1, 2)
    assert numArray.sumRange(0, 2) == 8
