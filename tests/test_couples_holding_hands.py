from puzzles.couples_holding_hands import min_swaps_couples


def test_min_swaps_couples():
    assert min_swaps_couples([5, 4, 2, 6, 3, 1, 0, 7]) == 2
    assert min_swaps_couples([0, 2, 1, 3]) == 1
    assert min_swaps_couples([3, 2, 0, 1]) == 0
    assert min_swaps_couples([1, 4, 0, 5, 8, 7, 6, 3, 2, 9]) == 3
