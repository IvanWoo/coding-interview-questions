from puzzles.can_i_win import can_i_win


def test_can_i_win():
    assert can_i_win(10, 11) == False
    assert can_i_win(10, 0) == True
    assert can_i_win(10, 1) == True
    assert can_i_win(3, 6) == True
    assert can_i_win(10, 40) == False
