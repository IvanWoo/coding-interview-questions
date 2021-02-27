from puzzles.ways_to_split_array_into_three_subarrays import ways_to_split


def test_ways_to_split():
    assert ways_to_split([1, 1, 1]) == 1
    assert ways_to_split([0, 3, 3]) == 1
