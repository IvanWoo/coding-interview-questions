from puzzles.partition_equal_subset_sum import can_partition


def test_can_partition():
    assert can_partition([1, 5, 11, 5]) == True
    assert can_partition([1, 2, 3, 5]) == False
    assert can_partition([1, 2, 5]) == False
