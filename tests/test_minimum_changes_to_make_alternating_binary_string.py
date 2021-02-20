from puzzles.minimum_changes_to_make_alternating_binary_string import min_operations


def test_min_operations():
    assert min_operations("0100") == 1
    assert min_operations("10") == 0
    assert min_operations("1111") == 2
    assert min_operations("10010100") == 3
