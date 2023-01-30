from puzzles.partition_array_into_three_parts_with_equal_sum import (
    can_three_parts_equal_sum,
)


def test_can_three_parts_equal_sum():
    assert can_three_parts_equal_sum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]) == True
    assert can_three_parts_equal_sum([10, -10, 10, -10, 10, -10, 10, -10]) == True
