from puzzles.three_sum import three_sum


def test_three_sum():
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0]) == []
    assert three_sum([1, 2, -2, -1]) == []
    assert three_sum([]) == []
