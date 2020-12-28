from puzzles.matchsticks_to_square import makesquare


def test_makesquare():
    assert makesquare([1, 1, 2, 2, 2]) == True
    assert makesquare([3, 3, 3, 3, 4]) == False
    assert makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]) == True
