from puzzles.frog_jump import can_cross


def test_can_cross():
    assert can_cross([0, 1, 3, 5, 6, 8, 12, 16, 18]) == False
    assert can_cross([0, 1, 3, 5, 6, 8, 12, 17]) == True
    assert can_cross([0, 1, 2, 3, 4, 8, 9, 11]) == False
    assert can_cross([0, 1, 3, 6, 10, 15, 16, 21]) == True
