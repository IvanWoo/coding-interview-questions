from puzzles.minimum_time_difference import find_min_difference


def test_find_min_difference():
    assert find_min_difference(["23:59", "00:00"]) == 1
    assert find_min_difference(["23:59", "00:00", "00:00"]) == 0
    assert find_min_difference(["00:00", "04:00", "22:00"]) == 120
