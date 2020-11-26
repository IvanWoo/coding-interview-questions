from puzzles.different_ways_to_add_parentheses import diff_ways_to_compute


def test_diff_ways_to_compute():
    assert sorted(diff_ways_to_compute("2-1-1")) == sorted([0, 2])
    assert sorted(diff_ways_to_compute("2*3-4*5")) == sorted([-34, -14, -10, -10, 10])
